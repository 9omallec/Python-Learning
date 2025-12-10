radius = 7
π = 3.14159
circumference = round(2 * π * radius, 5)
area = round((π * radius) ** 2, 5)
diameter = round(2 * π, 5)
volume_sphere = round(4 / 3 * π * radius ** 3, 5)
area_sphere = round(4 * π * radius ** 2, 5)

print("\n===== CIRCLE CALCULATOR =====")
print("Pie:", π)
print("Radius:", radius, "units")
print("Diameter:", diameter, "units")
print("Circumference:", circumference, "units")
print("Area:", area, "square units\n")
print("Sphere -")
print("Volume:", volume_sphere)
print("Area:", area_sphere)
print("=" * 29)