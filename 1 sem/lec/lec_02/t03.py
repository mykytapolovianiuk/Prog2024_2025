# Визначити у якій координатній чверті лежить введена з клавіатури точка x, y

x, y = [float(n) for n in input("input (x, y): ").split()]

if x > 0 and y > 0:
    print(f"Tочка ({x}, {y}) належить до 1ї координатної четверті")
elif x < 0 and y > 0:
    print(f"Tочка ({x}, {y}) належить до 2ї координатної четверті")
elif x < 0 and y < 0:
    print(f"Tочка ({x}, {y}) належить до 3ї координатної четверті")
elif x > 0 and y < 0:
    print(f"Tочка ({x}, {y}) належить до 4ї координатної четверті")
else:
    print(f"Tочка ({x}, {y}) лежить на одній з координатних осей")
