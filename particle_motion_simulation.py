import matplotlib.pyplot as plt

# Mass input
while True:
    try:
        mass = float(input("Enter mass of the particle (kg): "))
        if mass <= 0:
            print("Mass must be a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Force input
while True:
    try:
        force = float(input("Enter force applied on the particle (N): "))
        if force <= 0:
            print("Force must be a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Calculate acceleration
acceleration = force / mass
print(f"Acceleration of the particle is {acceleration:.2f} m/s²")

# Total simulation time
while True:
    try:
        total_time = int(input("Enter total simulation time (seconds): "))
        if total_time <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Initial velocity and position
velocity = 0.0
position_value = 0.0
time_interval = 1

# Lists for storing values for a graph
times = []
positions = []
velocities = []

# Simulation loop
print("\nTime (s)\tPosition (m)\tVelocity (m/s)")
for t in range(1, total_time + 1):
    velocity += acceleration * time_interval
    position_value += velocity * time_interval

    times.append(t)
    positions.append(position_value)
    velocities.append(velocity)

    print(f"{t}\t\t{position_value:.2f}\t\t{velocity:.2f}")

# Plotting the motion
plt.figure(figsize=(10,5))
plt.plot(times, positions, label="Position (m)")
plt.plot(times, velocities, label="Velocity (m/s)")
plt.title("Particle Motion under Constant Force")
plt.xlabel("Time (s)")
plt.ylabel("Position (m) / Velocity (m/s)")
plt.legend()
plt.grid(True)

# Option to save plot
save_plot = input("Do you want to save plot as an image? (yes/no): ").lower()
if save_plot == "yes":
    plt.savefig("particle_motion.png")
    print("Plot saved as particle_motion.png")

plt.show()


