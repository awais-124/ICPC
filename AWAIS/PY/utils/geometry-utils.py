from math import sqrt

# ---------- POINT ----------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# ---------- BASIC ----------
def dist(a, b):
    return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def cross(a, b, c):
    return (b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x)

def orientation(a, b, c):
    val = cross(a, b, c)
    if val > 0: return 1  # CCW
    if val < 0: return -1 # CW
    return 0

# ---------- CONVEX HULL ----------
def convex_hull(points):
    points = sorted(points, key=lambda p: (p.x, p.y))

    if len(points) < 2:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]
