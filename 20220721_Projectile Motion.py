# Projectile Motion
# https://www.codewars.com/kata/5af96cea3e9715ec670001dd/train/python

# 나의 풀이
import math
class Projectile:
    def __init__(self, h0, v0, a):
        self.h0 = h0
        self.v0 = v0
        self.a = a
        self.b = self.v0 * math.sin(math.pi * self.a / 180.0)
        self.c = self.v0 * math.cos(math.pi * self.a / 180.0)

    def height_eq(self):
        if self.h0 == 0:
            return f"h(t) = -16.0t^2 + {round(self.b, 3)}t"
        else:
            return f"h(t) = -16.0t^2 + {round(self.b, 3)}t + {self.h0:0.1f}"

    def horiz_eq(self):
        return f"x(t) = {round(self.c, 3)}t"

    def height(self, t):
        return round(-16 * t * t + self.b * t + self.h0, 3)

    def horiz(self, t):
        return round(self.c * t, 3)

    def landing(self):
        t = (self.b + (self.b ** 2 + 64 * self.h0) ** 0.5) / 32
        h = self.c * t
        return [round(h, 3), 0, round(t, 3)]

p = Projectile(5, 2, 45)
print(p.height_eq(), "h(t) = -16.0t^2 + 1.414t + 5.0")
print(p.horiz_eq(), "x(t) = 1.414t")
print(p.height(0.2), 4.643)
print(p.horiz(0.2), 0.283)
print(p.landing(), [0.856, 0, 0.605])

p = Projectile(0, 5, 45)
print(p.height_eq(), "h(t) = -16.0t^2 + 3.536t")
print(p.horiz_eq(), "x(t) = 3.536t")
print(p.height(0.2), 0.067)
print(p.horiz(0.2), 0.707)
print(p.landing(), [0.781, 0, 0.221])

p = Projectile(15, 12, 80)
print(p.height_eq(), "h(t) = -16.0t^2 + 11.818t + 15.0")
print(p.horiz_eq(), "x(t) = 2.084t")
print(p.height(0), 15)
print(p.horiz(0), 0)
print(p.height(1), 10.818)
print(p.horiz(1), 2.084)
print(p.landing(), [2.929, 0, 1.406])