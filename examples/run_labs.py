"""Run scoped, headless numerical experiments with analytic/geometric oracles."""
import argparse, json, math, random, sys, platform, hashlib, csv
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from motion_math import *


def run(output):
    output.mkdir(parents=True,exist_ok=True)
    labs=[]
    def record(name,domains,actual,expected,error,limit,note):
        passed=math.isfinite(error) and error<=limit
        labs.append(dict(name=name,domains=domains,actual=actual,expected=expected,
                         absolute_error=error,allowed_error=limit,status='PASS' if passed else 'FAIL',scope=note))
    record('01-lerp','D01 D06',lerp(2,8,.25),3.5,abs(lerp(2,8,.25)-3.5),1e-12,'Scalar known value')
    e=bezier_easing(.875,1,0,1,1)
    record('02-easing-inversion','D06',e,.5,abs(e-.5),1e-12,'Independent parametric s=.5 fixture')
    points=((0,0),(0,1),(1,1),(1,0))
    length=arc_length_table(points,256)[-1][1]
    record('03-arclength','D02',length,2.,abs(length-2),2e-5,'Polyline approximation to exact symmetric cubic length')
    q=slerp((1,0,0,0),(0,0,0,1),.5)
    record('04-rotation','D02 D06',q,[math.sqrt(.5),0,0,math.sqrt(.5)],max(abs(q[0]-math.sqrt(.5)),abs(q[3]-math.sqrt(.5))),1e-12,'90 degree halfway orientation')
    x,v=critical_spring(1,0,0,10,.5)
    record('05-critical-oracle','D08',x,6*math.exp(-5),abs(x-6*math.exp(-5)),1e-12,'Fixed target, mass=1,k=100,c=20')
    errors=[];trace=[]
    for n in (100,200,400):
        xx,vv=1.,0.;h=.5/n
        for i in range(n):
            xx,vv=spring_step(xx,vv,0,1,100,20,h)
            if n==400:trace.append((i+1,(i+1)*h,xx,vv,critical_spring(1,0,0,10,(i+1)*h)[0]))
        errors.append(abs(xx-x))
    ratio=errors[0]/errors[1]
    record('06-spring-convergence','D09 D10',errors,'decreasing error on refinement',0 if errors[0]>errors[1]>errors[2] else 1,0,'Only this linear critical spring and selected timesteps')
    with (output/'spring-trace.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['sample','time_s','x_numerical','velocity','x_analytic']);w.writerows(trace)
    y=(1.,)
    for i in range(20):y=rk4_step(lambda t,s:(-s[0],),y,i*.05,.05)
    record('07-rk4-decay','D10',y[0],math.exp(-1),abs(y[0]-math.exp(-1)),3e-8,'Smooth ODE xprime=-x')
    angles=ik2(1,1,1,1);end=fk2(1,1,*angles)
    record('08-fk-ik','D07 D17',end,[1,1],math.dist(end,(1,1)),1e-12,'Planar two-link; no joint limits/collision')
    vals=[]
    for hz in (30,60,120):
        value=0.
        for _ in range(hz):value=lowpass(value,1,1/hz,.4)
        vals.append(value)
    record('09-filter-rate','D03 D04',vals,1-math.exp(-2.5),max(abs(t-(1-math.exp(-2.5))) for t in vals),1e-12,'Held unit step over one second')
    rng=random.Random(8);cloud=[(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(80)]
    oracle={(i,j) for i in range(len(cloud)) for j in range(i+1,len(cloud)) if math.dist(cloud[i],cloud[j])<=.2}
    result=grid_neighbors(cloud,.2)
    record('10-neighbor-grid','D05 D14',len(result),len(oracle),len(result.symmetric_difference(oracle)),0,'Exact pair set versus independent brute force')
    route=astar_grid(5,5,{(2,0),(2,1),(2,2),(2,3)},(0,0),(4,0))
    record('11-planning','D13',len(route)-1,12,abs(len(route)-1-12),0,'Four-neighbor unit grid with known required detour')
    color=alpha_over((.5,0,0,.5),(0,0,1,1))
    record('12-alpha','D24 D28',color,[.5,0,.5,1],max(abs(a-b) for a,b in zip(color,(.5,0,.5,1))),1e-12,'Premultiplied example; working color space caller-owned')
    owner=TransitionOwner();a=owner.request('opening');b=owner.request('closing')
    accepted=owner.complete(a,'open');owner.complete(b,'closed')
    record('13-interruption','D20 D22',dict(stale_accepted=accepted,state=owner.state),'reject stale, closed',0 if not accepted and owner.state=='closed' else 1,0,'Logical ownership only, no browser execution')
    timestamps=[Fraction(n*1001,30000) for n in range(300)]
    interval=timestamps[-1]-timestamps[-2]
    record('14-rational-cadence','D03 D40',str(interval),'1001/30000',0 if interval==Fraction(1001,30000) else 1,0,'No encoder/display measurement')
    r1=random.Random(45);r2=random.Random(45)
    seq1=[r1.random() for _ in range(20)];seq2=[r2.random() for _ in range(20)]
    record('15-seed-replay','D14 D36',seq1[:3],seq2[:3],max(abs(a-b) for a,b in zip(seq1,seq2)),0,'Same Python generator/version and call order')
    a=[math.sin(2*math.pi*10*n/60) for n in range(60)]
    b=[math.sin(2*math.pi*70*n/60) for n in range(60)]
    record('16-aliasing','D04 D27',max(abs(x-y) for x,y in zip(a,b)),0.,max(abs(x-y) for x,y in zip(a,b)),2e-13,'Ideal sample equivalence; no human perception claim')
    report=dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),python=platform.python_version(),
                source_sha256=hashlib.sha256(Path(__file__).with_name('motion_math.py').read_bytes()).hexdigest(),
                labs=labs,summary=dict(total=len(labs),passed=sum(l['status']=='PASS' for l in labs)),
                limitation='Headless Python fixtures only. No GPU, browser, media decode, sensor, hardware or human study verification.')
    (output/'lab-results.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(report['summary']))
    return 0 if report['summary']['passed']==len(labs) else 1


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path('.local-output/labs'))
    sys.exit(run(parser.parse_args().output))
