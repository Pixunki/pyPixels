import time
import board
import neopixel


pixel_pin = board.D18

WIDTH = 16
HEIGHT = 8
NUM_PIXELS = WIDTH*HEIGHT

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, NUM_PIXELS, brightness=0.02, auto_write=False, pixel_order=ORDER)
pixels.fill((0,0,0))
pixels.show()

pixels[0] = (255,255,255)
pixels[8] = (255,255,255)
pixels[64] = (255,255,255)
pixels.show()
