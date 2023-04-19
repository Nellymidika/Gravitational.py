# Gravity Calculator
# This program calculates the gravitational force between two objects given their masses and distance

G = 6.6743e-11  # Gravitational constant

m1 = float(input("Enter mass of object 1 (kg): "))
m2 = float(input("Enter mass of object 2 (kg): "))
r = float(input("Enter distance between the objects (m): "))

F = G * m1 * m2 / r**2

print("The gravitational force between the two objects is", F, "N.")
