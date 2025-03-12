DURS = input("(square, rectangle, circle, triangle): ")

if DURS == "square":
    a = float(input())
    s = (a*a)
    print("%.3f" % s)

elif DURS == "rectangle":
    a = float(input())
    b = float(input())
    s = (a*b)
    print("%.3f" % s)

elif DURS == "circle":
    r = float(input("r"))
    s = (3.14*r*r)
    print("%.3f" % s)

elif DURS == "triangle":
    L = float(input())
    h = float(input())
    s = (0.5*L*h)
    print("%.3f" % s)

