DURS = input("(square, rectangle, circle, triangle): ")

if DURS == "square":
    tal = float(input("tal:"))
    s = (tal*tal)
    print("%.3f" % s)

elif DURS == "rectangle":
    urt = float(input("urt:"))
    urgun = float(input("urgun:"))
    s = (urt*urgun)
    print("%.3f" % s)

elif DURS == "circle":
    r = float(input("r"))
    s = (3.14*r*r)
    print("%.3f" % s)

elif DURS == "triangle":
    suuri = float(input("suurin urt:"))
    undur = float(input("undur:"))
    s = (0.5*suuri*undur)
    print("%.3f" % s)

