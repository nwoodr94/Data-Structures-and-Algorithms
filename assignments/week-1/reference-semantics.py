def main():
    
    p = Point(11, 22)

    print(p)

    n = 5
    mystery(p, n)
    print(p)

    p.x = p.y
    mystery(p, n)
    print(p)

    p2 = Point(100, 200)
    p = p2
    mystery(p2, n)
    print(str(p) + " :: " + str(p2))


def mystery(p, n):
    n = 0
    p.x = p.x+33

    print(str(p.x) + ", " + str(p.y) + " " + str(n))

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


main()

# (11, 22)
# 44, 22 0
# (44, 22)
# 55, 22 0
# (55, 22)
# 133, 200 0
# (133, 200) :: (133, 200)