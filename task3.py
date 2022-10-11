x = float(input("Please input X coordinate: "))
y = float(input("Please input Y coordinate: "))

if x == 0 and y == 0:
    print("Not defined")
elif x > 0 and y == 0:
    print("On X axe, positive dir.")
elif x > 0 and y > 0:
    print("I quadrant")
elif x == 0 and y > 0:
    print("On Y axe, positive dir.")
elif x < 0 and y > 0:
    print("II quadrant")
elif x < 0 and y == 0:
    print("On X axe, negative dir.")
elif x < 0 and y < 0:
    print("III quadrant")
elif x == 0 and y < 0:
    print("On Y axe, negative dir.")
elif x > 0 and y < 0:
    print("IV quadrant")