"""Small educational references, not production physics/robotics engines.

Units: seconds, radians, consistent spatial units. All algorithms document
their subset assumptions; tests use independent analytic/geometric fixtures.
"""
import math
import heapq
from bisect import bisect_left


def finite(*values):
    if not all(math.isfinite(v) for v in values):
        raise ValueError('finite values required')


def lerp(a, b, u):
    finite(a, b, u)
    return a + (b - a) * u


def inverse_lerp(a, b, value):
    finite(a, b, value)
    if a == b:
        raise ValueError('degenerate range')
    return (value - a) / (b - a)


def smoothstep(u):
    finite(u)
    u = min(1.0, max(0.0, u))
    return u * u * (3 - 2 * u)


def cubic_bezier(points, u):
    """Four equal-dimension points, normalized curve parameter u."""
    if len(points) != 4 or not points[0]:
        raise ValueError('four nonempty points required')
    if any(len(p) != len(points[0]) for p in points):
        raise ValueError('dimension mismatch')
    finite(u, *(x for p in points for x in p))
    v = 1 - u
    w = (v**3, 3*v*v*u, 3*v*u*u, u**3)
    return tuple(sum(wi*p[j] for wi, p in zip(w, points))
                 for j in range(len(points[0])))


def bezier_easing(u, x1, y1, x2, y2):
    """Bisection of monotonic CSS-style x(s), then y(s); u in [0,1]."""
    finite(u, x1, y1, x2, y2)
    if not (0 <= u <= 1 and 0 <= x1 <= 1 and 0 <= x2 <= 1):
        raise ValueError('u and x control points must be in [0,1]')
    if u in (0, 1):
        return float(u)
    points = ((0., 0.), (x1, y1), (x2, y2), (1., 1.))
    lo, hi = 0., 1.
    for _ in range(60):
        mid = (lo + hi) / 2
        if cubic_bezier(points, mid)[0] < u:
            lo = mid
        else:
            hi = mid
    return cubic_bezier(points, (lo+hi)/2)[1]


def arc_length_table(points, count=256):
    """Polyline approximation; count segments, NOT an exact integral."""
    if not isinstance(count, int) or count < 1:
        raise ValueError('positive integer segment count required')
    table = [(0., 0.)]
    previous = cubic_bezier(points, 0.)
    distance = 0.
    for i in range(1, count+1):
        u = i/count
        current = cubic_bezier(points, u)
        distance += math.dist(current, previous)
        table.append((u, distance))
        previous = current
    return table


def parameter_at_distance(table, distance):
    finite(distance)
    total = table[-1][1]
    if total == 0:
        return 0.
    distance = min(total, max(0., distance))
    i = bisect_left([row[1] for row in table], distance)
    if i == 0:
        return table[0][0]
    a, b = table[i-1], table[i]
    if b[1] == a[1]:
        return b[0]
    return lerp(a[0], b[0], (distance-a[1])/(b[1]-a[1]))


def quaternion_normalize(q):
    if len(q) != 4:
        raise ValueError('quaternion uses four components (w,x,y,z)')
    finite(*q)
    n = math.sqrt(sum(x*x for x in q))
    if n == 0:
        raise ValueError('zero quaternion')
    return tuple(x/n for x in q)


def slerp(q0, q1, u):
    finite(u)
    a, b = quaternion_normalize(q0), quaternion_normalize(q1)
    dot = sum(x*y for x, y in zip(a, b))
    if dot < 0:
        b = tuple(-v for v in b)
        dot = -dot
    dot = min(1., max(-1., dot))
    if dot > 0.9995:
        return quaternion_normalize(tuple(lerp(x,y,u) for x,y in zip(a,b)))
    theta = math.acos(dot)
    w0 = math.sin((1-u)*theta)/math.sin(theta)
    w1 = math.sin(u*theta)/math.sin(theta)
    return quaternion_normalize(tuple(w0*x+w1*y for x,y in zip(a,b)))


def spring_step(x, v, target, mass, stiffness, damping, dt):
    """Semi-implicit Euler for linear 1D spring; stability not guaranteed."""
    finite(x, v, target, mass, stiffness, damping, dt)
    if mass <= 0 or stiffness < 0 or damping < 0 or dt < 0:
        raise ValueError('invalid spring parameters')
    a = (-stiffness*(x-target)-damping*v)/mass
    v = v + a*dt
    return x + v*dt, v


def critical_spring(x0, v0, target, omega, time):
    """Exact fixed-target critical spring, omega>0, t>=0."""
    finite(x0, v0, target, omega, time)
    if omega <= 0 or time < 0:
        raise ValueError('omega positive, time nonnegative')
    y0 = x0-target
    b = v0+omega*y0
    e = math.exp(-omega*time)
    return target+(y0+b*time)*e, (v0-omega*b*time)*e


def rk4_step(f, state, time, dt):
    """Pure smooth ODE derivative f(t, tuple); no event/collision solving."""
    finite(time, dt, *state)
    if dt < 0:
        raise ValueError('nonnegative dt required')
    def derivative(t, y):
        result = tuple(f(t, y))
        if len(result) != len(state):
            raise ValueError('derivative dimension mismatch')
        finite(*result)
        return result
    def shifted(k, factor):
        return tuple(y+dt*factor*ki for y,ki in zip(state,k))
    k1 = derivative(time,state)
    k2 = derivative(time+dt/2,shifted(k1,.5))
    k3 = derivative(time+dt/2,shifted(k2,.5))
    k4 = derivative(time+dt,shifted(k3,1.))
    return tuple(y+dt*(a+2*b+2*c+d)/6 for y,a,b,c,d in zip(state,k1,k2,k3,k4))


def fk2(length1, length2, q1, q2):
    finite(length1,length2,q1,q2)
    if min(length1,length2) <= 0:
        raise ValueError('positive link lengths required')
    return (length1*math.cos(q1)+length2*math.cos(q1+q2),
            length1*math.sin(q1)+length2*math.sin(q1+q2))


def ik2(length1, length2, x, y, elbow=1):
    """Planar unconstrained two-link IK; no joint limits or obstacles."""
    finite(length1,length2,x,y)
    if min(length1,length2) <= 0 or elbow not in (-1,1):
        raise ValueError('positive lengths and elbow +/-1 required')
    radius = math.hypot(x,y)
    if radius == 0 and length1 == length2:
        raise ValueError('origin has underdetermined first joint')
    if radius > length1+length2+1e-12 or radius < abs(length1-length2)-1e-12:
        raise ValueError('unreachable target')
    c = (x*x+y*y-length1**2-length2**2)/(2*length1*length2)
    q2 = elbow*math.acos(min(1.,max(-1.,c)))
    q1 = math.atan2(y,x)-math.atan2(length2*math.sin(q2),length1+length2*math.cos(q2))
    return q1,q2


def lowpass(previous, sample, dt, tau):
    """Causal exponential response to held sample; time-aware alpha."""
    finite(previous,sample,dt,tau)
    if dt < 0 or tau <= 0:
        raise ValueError('dt>=0 and tau>0 required')
    alpha = -math.expm1(-dt/tau)
    return lerp(previous,sample,alpha)


def alpha_over(a, b):
    """Premultiplied RGBA; caller defines working color space."""
    if len(a)!=4 or len(b)!=4:
        raise ValueError('RGBA required')
    finite(*a,*b)
    if not (0<=a[3]<=1 and 0<=b[3]<=1):
        raise ValueError('alpha out of range')
    return tuple(a[i]+b[i]*(1-a[3]) for i in range(4))


def grid_neighbors(points, radius):
    """Undirected Euclidean radius pairs in 2D; exact narrow phase."""
    finite(radius,*(x for p in points for x in p))
    if radius <= 0 or any(len(p)!=2 for p in points):
        raise ValueError('positive radius and 2D points required')
    cells={}
    for i,(x,y) in enumerate(points):
        key=(math.floor(x/radius),math.floor(y/radius))
        cells.setdefault(key,[]).append(i)
    pairs=set()
    for i,(x,y) in enumerate(points):
        cx,cy=math.floor(x/radius),math.floor(y/radius)
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                for j in cells.get((cx+dx,cy+dy),[]):
                    if i<j and math.dist(points[i],points[j])<=radius:
                        pairs.add((i,j))
    return pairs


def astar_grid(width,height,blocked,start,goal):
    """Four-neighbor unit-cost grid; returns optimal path or None."""
    if width<1 or height<1:
        raise ValueError('positive dimensions')
    def valid(p):
        return 0<=p[0]<width and 0<=p[1]<height and p not in blocked
    if not valid(start) or not valid(goal):
        raise ValueError('invalid endpoint')
    heuristic=lambda p:abs(p[0]-goal[0])+abs(p[1]-goal[1])
    heap=[(heuristic(start),0,start)]
    best={start:0};parent={}
    while heap:
        _,cost,current=heapq.heappop(heap)
        if cost!=best.get(current):
            continue
        if current==goal:
            path=[current]
            while current in parent:
                current=parent[current];path.append(current)
            return list(reversed(path))
        x,y=current
        for p in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            new=cost+1
            if valid(p) and new<best.get(p,math.inf):
                best[p]=new;parent[p]=current
                heapq.heappush(heap,(new+heuristic(p),new,p))
    return None


class TransitionOwner:
    """Minimal stale-completion guard; not a full reactive framework."""
    def __init__(self):
        self.generation=0
        self.state='closed'

    def request(self,state):
        self.generation+=1
        self.state=state
        return self.generation

    def complete(self,token,state):
        if token!=self.generation:
            return False
        self.state=state
        return True
