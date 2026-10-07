import unittest, math, random, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'examples'))
from motion_math import *


class InterpolationTests(unittest.TestCase):
    def test_lerp_inverse_extrapolation(self):
        for u in (-1,0,.3,1,2):
            self.assertAlmostEqual(inverse_lerp(2,7,lerp(2,7,u)),u)
    def test_degenerate_range(self):
        with self.assertRaises(ValueError):inverse_lerp(1,1,1)
    def test_smoothstep_derivatives(self):
        h=1e-5
        self.assertEqual(smoothstep(-1),0)
        self.assertEqual(smoothstep(2),1)
        self.assertLess(abs((smoothstep(h)-smoothstep(0))/h),4e-5)
    def test_bezier_linear_identity(self):
        for u in (.001,.1,.5,.9,.999):
            self.assertAlmostEqual(bezier_easing(u,.2,.2,.8,.8),u,places=11)
    def test_bezier_known_midpoint(self):
        self.assertAlmostEqual(bezier_easing(.5,.42,0,.58,1),.5)
    def test_bezier_inverts_x(self):
        # Independent s=.5 fixture: x=.875, y=.5 for controls (1,0),(1,1).
        self.assertAlmostEqual(bezier_easing(.875,1,0,1,1),.5)
    def test_bezier_invalid(self):
        with self.assertRaises(ValueError):bezier_easing(.5,-1,0,.5,1)
    def test_arclength_line(self):
        table=arc_length_table(((0,0),(1,0),(2,0),(3,0)),32)
        self.assertAlmostEqual(table[-1][1],3)
        self.assertAlmostEqual(parameter_at_distance(table,1.5),.5)
    def test_arclength_curved_refinement(self):
        points=((0,0),(0,1),(1,1),(1,0))
        errors=[abs(arc_length_table(points,n)[-1][1]-2) for n in (16,32,64)]
        # This symmetric cubic has exact length 2, derived by integrating speed.
        self.assertGreater(errors[0],errors[1]);self.assertGreater(errors[1],errors[2])
    def test_arclength_degenerate(self):
        self.assertEqual(parameter_at_distance(arc_length_table(((1,1),)*4),10),0)
    def test_slerp_antipodal(self):
        self.assertEqual(slerp((1,0,0,0),(-1,0,0,0),.5),(1.,0.,0.,0.))
    def test_slerp_known_rotation(self):
        q=slerp((1,0,0,0),(0,0,0,1),.5)
        self.assertAlmostEqual(q[0],math.sqrt(.5));self.assertAlmostEqual(q[3],math.sqrt(.5))
    def test_zero_quaternion(self):
        with self.assertRaises(ValueError):slerp((0,0,0,0),(1,0,0,0),.5)


class SolverTests(unittest.TestCase):
    def test_critical_initial_conditions(self):
        self.assertEqual(critical_spring(2,3,1,4,0),(2.,3.))
    def test_critical_derivative(self):
        x,v=critical_spring(1,.7,0,5,.2);h=1e-6
        numeric=(critical_spring(1,.7,0,5,.2+h)[0]-critical_spring(1,.7,0,5,.2-h)[0])/(2*h)
        self.assertAlmostEqual(v,numeric,places=7)
    def test_semiimplicit_convergence(self):
        reference=critical_spring(1,0,0,10,.5)[0];errors=[]
        for n in (100,200,400):
            x,v=1.,0.;h=.5/n
            for _ in range(n):x,v=spring_step(x,v,0,1,100,20,h)
            errors.append(abs(x-reference))
        self.assertGreater(errors[0],errors[1]);self.assertGreater(errors[1],errors[2])
    def test_rk4_independent_decay_oracle(self):
        errors=[]
        for n in (5,10,20):
            y=(1.,)
            for i in range(n):y=rk4_step(lambda t,s:(-s[0],),y,i/n,1/n)
            errors.append(abs(y[0]-math.exp(-1)))
        self.assertGreater(errors[0]/errors[1],12)
        self.assertGreater(errors[1]/errors[2],12)
    def test_rk4_coupled_oscillator(self):
        y=(1.,0.);h=.01
        for i in range(100):y=rk4_step(lambda t,s:(s[1],-s[0]),y,i*h,h)
        self.assertAlmostEqual(y[0],math.cos(1),places=8)
        self.assertAlmostEqual(y[1],-math.sin(1),places=8)
    def test_invalid_parameters(self):
        for mass,dt in ((0,.1),(1,-.1)):
            with self.assertRaises(ValueError):spring_step(1,0,0,mass,100,20,dt)
    def test_nonfinite(self):
        with self.assertRaises(ValueError):lerp(0,float('nan'),.5)
    def test_derivative_dimensions(self):
        with self.assertRaises(ValueError):rk4_step(lambda t,s:(1,2),(1,),0,.1)


class KinematicSignalTests(unittest.TestCase):
    def test_fk_independent_pose(self):
        x,y=fk2(1,1,0,math.pi/2)
        self.assertAlmostEqual(x,1);self.assertAlmostEqual(y,1)
    def test_ik_both_branches(self):
        for elbow in (-1,1):
            q=ik2(1,1,1,1,elbow)
            self.assertLess(math.dist(fk2(1,1,*q),(1,1)),1e-12)
            self.assertEqual(1 if q[1]>0 else -1,elbow)
    def test_unreachable_and_underdetermined(self):
        for x,y in ((3,0),(0,0)):
            with self.assertRaises(ValueError):ik2(1,1,x,y)
    def test_inner_unreachable(self):
        with self.assertRaises(ValueError):ik2(2,1,.1,0)
    def test_filter_time_constant_independent_oracle(self):
        expected=1-math.exp(-1/.4)
        for n in (20,60,120):
            y=0.
            for _ in range(n):y=lowpass(y,1,1/n,.4)
            self.assertAlmostEqual(y,expected,places=12)
    def test_filter_irregular_time(self):
        dts=(.1,.05,.2,.15,.5);y=0.
        for dt in dts:y=lowpass(y,1,dt,.4)
        self.assertAlmostEqual(y,1-math.exp(-sum(dts)/.4),places=12)
    def test_filter_invalid(self):
        with self.assertRaises(ValueError):lowpass(0,1,.1,0)
    def test_alpha_known_result(self):
        self.assertEqual(alpha_over((.5,0,0,.5),(0,0,1,1)),(.5,0,.5,1.))
    def test_alpha_identity(self):
        b=(.2,.1,.3,.5)
        self.assertEqual(alpha_over((0,0,0,0),b),b)


class ArchitectureTests(unittest.TestCase):
    def test_grid_vs_bruteforce_negative_boundaries(self):
        rng=random.Random(17)
        points=[(rng.uniform(-2,2),rng.uniform(-2,2)) for _ in range(100)]
        points.extend([(-.5,0),(0,0),(.5,0)])
        r=.5
        oracle={(i,j) for i in range(len(points)) for j in range(i+1,len(points)) if math.dist(points[i],points[j])<=r}
        self.assertEqual(grid_neighbors(points,r),oracle)
    def test_astar_optimal_path(self):
        path=astar_grid(5,5,{(2,0),(2,1),(2,2),(2,3)},(0,0),(4,0))
        self.assertEqual(len(path)-1,12)
        self.assertEqual(path[0],(0,0));self.assertEqual(path[-1],(4,0))
    def test_astar_disconnected(self):
        self.assertIsNone(astar_grid(3,3,{(1,0),(1,1),(1,2)},(0,0),(2,0)))
    def test_astar_same_endpoint(self):
        self.assertEqual(astar_grid(2,2,set(),(0,0),(0,0)),[(0,0)])
    def test_stale_callback(self):
        owner=TransitionOwner();old=owner.request('opening');new=owner.request('closing')
        self.assertFalse(owner.complete(old,'open'));self.assertEqual(owner.state,'closing')
        self.assertTrue(owner.complete(new,'closed'));self.assertEqual(owner.state,'closed')


if __name__=='__main__':unittest.main()
