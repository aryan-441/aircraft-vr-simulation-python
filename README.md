# JTS Simple Python Simulator VR

**Project date: 22 March 2026. Updated: 28 May 2026.**

This interactive Python program estimates aircraft takeoff performance. Despite “VR” in the filename, it does not implement virtual reality; it models an aircraft’s ground roll and plots the results.

## What it calculates

Choose a built-in aircraft profile or enter aircraft parameters, then provide wind, altitude, and runway length. The program estimates stall and rotation speed, evaluates available flap settings, simulates acceleration and ground distance, and reports the shortest computed takeoff distance. Matplotlib plots velocity and distance over time.

## Technologies and setup

Python 3 and Matplotlib. Install Matplotlib with `python -m pip install matplotlib`, then run the script from a terminal. The script uses interactive console input and opens Matplotlib plots.

## Limitations

Aircraft values and the model are approximations. The calculation is an educational programming and physics exercise, not operational aviation guidance. Input validation and physics-model verification are needed.
