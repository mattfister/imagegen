import colorsys
from freezedraw import colors
from freezedraw import image
from freezedraw import normalizer
from noise import perlin
import math

simp1 = perlin.SimplexNoise()
simp1.randomize()
simp2 = perlin.SimplexNoise()
simp2.randomize()
simp3 = perlin.SimplexNoise()
simp3.randomize()


def height(x, y):
    result = simp1.noise2(x, y) + 0.5*simp2.noise2(x*2, y*2) + 0.25*simp3.noise2(x*3, y*3)
    min = -1.75
    max = 1.75
    scale = max - min
    result = (result-min)/scale
    return result

def water_value(x, y, height, max_height):
    result = height + 0.5*math.fabs(simp1.noise2(x*50, y*50))
    result = result / (max_height + 0.5)
    return result

if __name__ == '__main__':
    w = 880
    h = 440
    img = image.Image(w, h)
    land_c = colors.bright_color_hsv()
    water_c = colors.near_hue_hsv(colorsys.rgb_to_hsv(105/255.0, 216/255.0, 255/255.0))

    simp = perlin.SimplexNoise()

    simp.randomize()
    ssimp = perlin.SimplexNoise()
    ssimp.randomize()

    for y in range(h):
        for x in range(w):
            v = normalizer.normalize(height(x/w,y/h), 0.0, 1.0)

            if v < 0.4:
                img.set_pixel(x, y, colorsys.hsv_to_rgb(water_c[0], water_c[1], water_value(x/w, y/h, v, 0.4)))
            else:
                img.set_pixel(x, y, colorsys.hsv_to_rgb(land_c[0], land_c[1], v))
    img.show()