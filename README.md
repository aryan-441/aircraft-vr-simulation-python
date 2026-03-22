# aircraft-vr-simulation-python
A basic simulation which calculates the VR (rotation speed) of an aircraft based on several factors including mass, wing area, wind speed, etc. It models keys forces including thrust, lift and drag. It also includes environmental factors such as wind speed (headwind/tailwind), altitude (affecting air density), and runway length. 
At each step, forces are calculated, net acceleration is determined and velocity and the position of the aircraft are updated. The loop continues until rotation speed is reached.
The key concept is that takeoff isn't governed by a single equation, but rather the interaction of different factors such as lift, drag and thrust.
Inputs: Aircraft type (either predefined figures or custom inputs), wind speed, altitude and runway length.
Outputs: VR speed, distance covered, graphs of motion (velocity vs time, distance vs time), and time to takeoff.
22-03-2026
