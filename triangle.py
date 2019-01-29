import re
def classify_triangle(a, b, c):
    if str(a).isdigit() and str(b).isdigit() and str(c).isdigit() and a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                return("Equilateral triangle")
            elif a == b or a == c or b == c:
                return("Isoceles triangle")
            elif a * a + b * b == c * c or a * a + c * c == b * b or c * c + b * b == a * a:
                return("Right triangle")
            else:
                return("Scalene triangle")
        else:
            return("Not a Triangle")
    else:
        return("InvalidInput")


