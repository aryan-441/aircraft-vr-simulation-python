'''Simple Python Simulation- VR'''
import math 
import matplotlib.pyplot as plt
#constants
g = 9.81
rho = 1.225 

aircraft_data = {  #figures are approximations 
    "Commercial": {

        "A320": {
            "mass": 70000,
            "S": 122,
            "CL": 1.8,
            "CD": 0.03,
            "thrust": 180000,
            "max_headwind": 18,
            "max_tailwind": 7,
            "flaps": {
                0: {"CL_mult": 1.0, "CD_mult": 1.0},
                5: {"CL_mult": 1.1, "CD_mult": 1.3},
                10: {"CL_mult": 1.2, "CD_mult": 1.6},
                15: {"CL_mult": 1.3, "CD_mult": 2.0}
            }
        },

        "B737": {
            "mass": 65000,
            "S": 105,
            "CL": 1.7,
            "CD": 0.03,
            "thrust": 170000,
            "max_headwind": 18,
            "max_tailwind": 7,
            "flaps": {
                1: {"CL_mult": 1.05, "CD_mult": 1.2},
                5: {"CL_mult": 1.15, "CD_mult": 1.5},
                10: {"CL_mult": 1.25, "CD_mult": 1.9},
                15: {"CL_mult": 1.3, "CD_mult": 2.3}
            }
        },

        "B777": {
            "mass": 250000,
            "S": 427,
            "CL": 1.9,
            "CD": 0.035,
            "thrust": 350000,
            "max_headwind": 20,
            "max_tailwind": 10,
            "flaps": {
                5: {"CL_mult": 1.05, "CD_mult": 1.3},
                10: {"CL_mult": 1.1, "CD_mult": 1.6},
                15: {"CL_mult": 1.2, "CD_mult": 2.0},
                20: {"CL_mult": 1.25, "CD_mult": 2.4}
            }
        }
    },

    "General Aviation": {

        "C172": {
            "mass": 1100,
            "S": 16.2,
            "CL": 1.5,
            "CD": 0.04,
            "thrust": 2000,
            "max_headwind": 12,
            "max_tailwind": 4,
            "flaps": {
                0: {"CL_mult": 1.0, "CD_mult": 1.0},
                10: {"CL_mult": 1.1, "CD_mult": 1.2},
                20: {"CL_mult": 1.2, "CD_mult": 1.5},
                30: {"CL_mult": 1.3, "CD_mult": 1.9}
            }
        }
    },

    "Fighters": {

        "F16": {
            "mass": 12000,
            "S": 27.8,
            "CL": 1.6,
            "CD": 0.02,
            "thrust": 160000,
            "max_headwind": 25,
            "max_tailwind": 10,
            "flaps": {
                0: {"CL_mult": 1.0, "CD_mult": 1.0},
                10: {"CL_mult": 1.05, "CD_mult": 1.2}
            }
        },

        "F22 Raptor": {
            "mass": 19700,
            "S": 78.0,
            "CL": 1.7,
            "CD": 0.02,
            "thrust": 350000,
            "max_headwind": 30,
            "max_tailwind": 12,
            "flaps": {
                0: {"CL_mult": 1.0, "CD_mult": 1.0},
                10: {"CL_mult": 1.05, "CD_mult": 1.2}
            }
        },

        "F35 Lightning II": {
            "mass": 22000,
            "S": 42.7,
            "CL": 1.6,
            "CD": 0.025,
            "thrust": 220000,
            "max_headwind": 25,
            "max_tailwind": 10,
            "flaps": {
                0: {"CL_mult": 1.0, "CD_mult": 1.0},
                10: {"CL_mult": 1.05, "CD_mult": 1.2}
            }
        },

        "Su-57": {
            "mass": 25000,
            "S": 78.8,
            "CL": 1.7,
            "CD": 0.025,
            "thrust": 320000,
            "max_headwind": 25,
            "max_tailwind": 10,
            "flaps": {
                0: {"CL_mult": 1.0, "CD_mult": 1.0},
                10: {"CL_mult": 1.05, "CD_mult": 1.2}
            }
        }
    }
}

while True:

    print("Choose input method.\n(1)Select aircraft or (2)Enter data manually.")
    choice = input("Enter your choice (1 or 2)")

    if choice == '1':
        print("\nAircraft categories:\n")
        for category in aircraft_data:
            print(category)

        selected_category = input("Enter category:  ")
        print("\nAircraft\n")
        for aircraft in aircraft_data[selected_category]:
            print(aircraft)

        selected_aircraft = input("Enter aircraft:  ")
        data = aircraft_data[selected_category][selected_aircraft]

        mass = data['mass']
        wing_area = data['S']
        lift_coefficient = data['CL']
        drag_coefficient = data["CD"]
        thrust = data['thrust']
        max_headwind = data["max_headwind"]
        max_tailwind = data["max_tailwind"]
        flaps = data["flaps"]

    else:
        print("Enter aircraft details:   \n")
        model = input("Enter aircraft model:   ")
        mass = float(input("Enter mass:   "))
        wing_area = float(input("Enter wing area:   "))
        lift_coefficient = float(input("Enter the lift coefficient:   "))
        drag_coefficient = float(input("Enter the drag coefficient:   "))
        thrust = float(input("Enter thrust:   "))
        max_headwind = 15
        max_tailwind = 5

        flaps = {
            0: {"CL_mult": 1.0, "CD_mult": 1.0},
            10: {"CL_mult": 1.2, "CD_mult": 1.3},
            20: {"CL_mult": 1.4, "CD_mult": 1.7}
        }

    wind_knots = float(input("Enter wind speed (+ve for headwind, -ve for tailwind) in knots:  "))
    wind = wind_knots * 0.51444

    altitude = float(input("Enter altitude (m):   "))
    rwy_length = float(input("Enter runway length (m):   "))
    rho = 1.225 * (1 - 0.000022 * altitude)

    print(f"Mass: {mass}kg\nWing Area: {wing_area}m^2\nLift Coefficient: {lift_coefficient}\nDrag Coefficient: {drag_coefficient}\nThrust: {thrust}N\nWind: {wind_knots}kt\nAltitude: {altitude}m\nRunway Length: {rwy_length}m\nAir density: ~{rho}kg/m^3\nMax headwind: {max_headwind*1.94384}kt\nMax tailwind: {max_tailwind*1.94384}kt\n\n")

    if wind_knots > max_headwind * 1.94384:
        print("Headwind too strong")
        continue

    if wind_knots < -max_tailwind * 1.94384:
        print("Tailwind too strong")
        continue

    weight = mass * g

    best_distance = float("inf")
    best_flap = None

    for setting in flaps:

        CL_eff = lift_coefficient * flaps[setting]["CL_mult"]
        CD_eff = drag_coefficient * flaps[setting]["CD_mult"]

        v_stall = math.sqrt((2*weight) / (rho * CL_eff * wing_area))
        vr = 1.2 * v_stall

        if vr - wind < 10:
            continue

        v = 0
        x = 0
        t = 0
        dt = 0.1

        velocities = []
        distances = []
        times = []

        while v < vr:
            drag = 0.5 * rho * v**2 * wing_area * CD_eff
            rolling_resistance = 0.02 * mass * g
            
            thrust_eff = thrust * (1 - v / 250)  #thrust isnt constant anymore. eg- if v =100, only 60% thrust will be left
            net_force = thrust_eff - drag - rolling_resistance
            acceleration = net_force/mass
            v += acceleration * dt
            ground_speed = v - wind
            x += ground_speed * dt + 0.5 * acceleration * dt**2
            t += dt

            velocities.append(v)
            distances.append(x)
            times.append(t)

        if x < best_distance:
            best_distance = x
            best_flap = setting
            best_times = times
            best_velocities = velocities
            best_distances = distances
            best_t = t
            best_vr = vr

    print("RESULTS\n")

    print(f"Best flap setting: {best_flap}")
    print(f"Rotation Speed (VR): {best_vr:.2f} m/s")
    print(f"VR: {best_vr*3.6:.2f} km/h")
    print(f"VR: {best_vr*1.94384:.2f} knots")

    print(f"Runway margin: {rwy_length - best_distance:.2f} m")
    print(f"Time to reach VR: {best_t:.2f} seconds.")
    print(f"Distance to reach VR: {best_distance:.2f} metres.")

    if best_distance <= rwy_length:
        print("Takeoff possible")
    else:
        print("Runway too short")

    print(len(best_times), len(best_velocities), len(best_distances),'---Length of lists')

    #Graphs
    plt.figure()

    plt.subplot(2,1,1)
    plt.plot(best_times, best_velocities)
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.title("Velocity vs Time")
    plt.grid()

    plt.subplot(2,1,2)
    plt.plot(best_times, best_distances)
    plt.xlabel("Time (s)")
    plt.ylabel("Distance (m)")
    plt.title("Distance vs Time")
    plt.grid()

    plt.show()