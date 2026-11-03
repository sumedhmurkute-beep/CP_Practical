import math


# Part A: Euler simulation for a first-order reaction
c0 = 2.5
k = 0.04
dt = 1.0
total_time = 12

concentration = c0
print("Part A: Euler simulation")
print(f"{'Time (min)':>10} {'Concentration (mol/L)':>24} {'Conversion (%)':>18}")

for time in range(total_time + 1):
    conversion = (c0 - concentration) / c0 * 100
    print(f"{time:10d} {concentration:24.4f} {conversion:18.2f}")
    if time < total_time:
        concentration = concentration - k * concentration * dt

euler_concentration = concentration
exact_concentration = c0 * math.exp(-k * total_time)
absolute_error = abs(euler_concentration - exact_concentration)
print(f"\nEuler concentration at {total_time} min: {euler_concentration:.4f} mol/L")
print(f"Exact concentration at {total_time} min: {exact_concentration:.4f} mol/L")
print(f"Absolute error: {absolute_error:.6f} mol/L")

# Continue with Euler steps until conversion reaches 40% or time reaches 100 min.
concentration = c0
time = 0
conversion = 0.0

while conversion < 40.0 and time < 100:
    concentration = concentration - k * concentration * dt
    time += 1
    conversion = (c0 - concentration) / c0 * 100

print("\nPart A: 40% conversion stopping condition")
print(f"Time needed: {time} min")
print(f"Final concentration: {concentration:.4f} mol/L")


# Part B: Count and sum the digits in a sample code.
code = input("\nPart B: Enter a sample code: ")

if code == "":
    print("The code is empty.")
else:
    digit_count = 0
    digit_sum = 0

    for character in code:
        if character.isdigit():
            digit_count += 1
            digit_sum += int(character)

    if digit_count == 0:
        print("The code contains no digits.")
    else:
        print(f"Number of digits: {digit_count}")
        print(f"Sum of digits: {digit_sum}")
