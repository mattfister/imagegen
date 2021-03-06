from freezedraw import image
from freezedraw import colors
import random
import colorsys
import copy


class Planet(object):
    def __init__(self, c, r):
        self.c = c
        self.r = r
        self.base_color_hsv = colors.dark_color_hsv()
        self.coloring_func = random.choice([self.color_near, self.color_line_h, self.color_line_v])
        self.color_current = copy.copy(self.base_color_hsv)

    def is_inside(self, p):
        return (p[0] - self.c[0])*(p[0] -self. c[0]) + (p[1] - self.c[1])*(p[1] - self.c[1]) < self.r*self.r

    def color_near(self, x, y):
        return colors.near_hue_hsv(p.base_color_hsv)

    def color_line_h(self, x, y):
        color_current = colors.near_hue_hsv(self.color_current)
        return color_current

    def color_line_v(self, x, y):
        color_current = colors.near_v_hsv(self.color_current)
        return color_current

if __name__ == '__main__':
    w = 880
    h = 440
    ps = []
    planet_ave = w/12
    for i in range(random.randint(1, 3)):
        ps.append(Planet((w/2+random.normalvariate(0, w/4), h/2 + random.normalvariate(0, h/4)),
                         random.normalvariate(planet_ave, planet_ave)))

    c = colors.near_hue_hsv(colors.dark_color_hsv())
    img = image.Image(w, h)
    star_density = random.uniform(0.001, 0.05)
    star_base_color_hsv = colors.dark_color_hsv()

    for y in range(h):
        for x in range(w):
            for p in ps:
                if p.is_inside((x, y)):
                    c = p.coloring_func(x, y)
                    img.set_pixel(x, y, colorsys.hsv_to_rgb(*c))
                    break
            else:
                if random.random() < star_density:
                    img.set_pixel(x, y, colorsys.hsv_to_rgb(*colors.v_up_to(star_base_color_hsv)))
                else:
                    img.set_pixel(x, y, (0, 0, 0))



    img.show()