# Runnable examples

Python 3.10+ standard library only. From repository root:

```bash
python3 examples/run_labs.py --output .local-output/labs
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
python3 scripts/search.py "spring"
```

`motion_math.py`: interpolation, cubic Bézier inversion, arc-length LUT, quaternion slerp, semi-implicit spring, analytic critical spring, RK4, planar FK/IK, time-aware low-pass, premultiplied alpha, spatial grid, A* and stale callback guard. Functions expose explicit subset assumptions.

`run_labs.py` writes 16 experiments and a spring trace. Actual recorded results are in [lab-results.json](../reports/labs/lab-results.json). [Tests](../tests/test_motion_math.py) use independent analytic/geometric fixtures, not mere implementation copies.

`particles.wgsl` illustrates ping-pong compute flow. **NOT_RUN**: shader compile/GPU runtime, browser interactions, media render/decode, sensors, haptics, XR, robots, learned model training and human studies. Python PASS doesn't validate these paths.

Labs are educational references. A* is four-neighbor unit grid; IK is two-link planar without limits/collision; RK4 assumes smooth pure ODE; alpha caller defines color space; arc-length is approximate. Extend fixtures before extending claims.
