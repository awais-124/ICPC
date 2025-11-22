import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

def cross_product(a, b):
    return a.x * b.y - a.y * b.x

def dot_product(a, b):
    return a.x * b.x + a.y * b.y

def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0  # collinear
    return 1 if val > 0 else 2  # clock or counterclock wise

def on_segment(p, q, r):
    return (min(p.x, r.x) <= q.x <= max(p.x, r.x) and
            min(p.y, r.y) <= q.y <= max(p.y, r.y))

def segments_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if (o1 == 0 and on_segment(p1, p2, q1)) or \
       (o2 == 0 and on_segment(p1, q2, q1)) or \
       (o3 == 0 and on_segment(p2, p1, q2)) or \
       (o4 == 0 and on_segment(p2, q1, q2)):
        return True

    return False

def convex_hull(points):
    if len(points) < 3:
        return points

    points = sorted(points, key=lambda p: (p.x, p.y))

    def build_hull(points):
        hull = []
        for p in points:
            while len(hull) >= 2 and orientation(hull[-2], hull[-1], p) != 2:
                hull.pop()
            hull.append(p)
        return hull

    lower = build_hull(points)
    upper = build_hull(reversed(points))
    return lower[:-1] + upper[:-1]
