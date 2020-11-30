from unicorn_hat_sim import UnicornHatSim
import pygame

WIDTH = 16
HEIGHT = 16

PHAT = None
HAT = None
PHAT_VERTICAL = None
AUTO = None
PANEL_SHAPE = (16, 16)


class BigUnicornHatSim(UnicornHatSim):
    def __init__(self, width, height, rotation_offset=0):

        # Set some defaults
        self.rotation_offset = rotation_offset
        self.rotation(0)
        self.pixels = [(0, 0, 0)] * width * height
        self.pixel_size = 35
        self.width = width
        self.height = height
        self.window_width = width * self.pixel_size
        self.window_height = height * self.pixel_size

        # Init pygame and off we go
        pygame.init()
        pygame.display.set_caption("Unicorn HAT simulator")
        self.screen = pygame.display.set_mode(
            [self.window_width, self.window_height])
        self.clear()


_unicornhathd = BigUnicornHatSim(16, 16, 0)




COLORS = {
    'red': (255, 0, 0),
    'lime': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'magenta': (255, 0, 255),
    'cyan': (0, 255, 255),
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'gray': (127, 127, 127),
    'grey': (127, 127, 127),
    'silver': (192, 192, 192),
    'maroon': (128, 0, 0),
    'olive': (128, 128, 0),
    'green': (0, 128, 0),
    'purple': (128, 0, 128),
    'teal': (0, 128, 128),
    'navy': (0, 0, 128),
    'orange': (255, 165, 0),
    'gold': (255, 215, 0),
    'purple': (128, 0, 128),
    'indigo': (75, 0, 130)
}






def setup():
    """Initialize Unicorn HAT HD."""
    pass


def enable_addressing(enabled=True):
    """Enable multi-panel addressing support (for Ubercorn)."""
    pass


def setup_buffer(width, height):
    """Set up the internal pixel buffer.

    :param width: width of buffer, ideally in multiples of 16
    :param height: height of buffer, ideally in multiples of 16

    """
    pass


def enable_display(address, enabled=True):
    """Enable a single display in the chain.

    :param address: address of the display from 0 to 7
    :param enabled: True/False to indicate display is enabled

    """
    pass


def setup_display(address, x, y, rotation):
    """Configure a single display in the chain.

    :param x: x offset of display portion in buffer
    :param y: y offset of display portion in buffer
    :param rotation: rotation of display

    """
    pass


def set_brightness(b):
    """Set the display brightness between 0.0 and 1.0.

    :param b: Brightness from 0.0 to 1.0 (default 0.5)

    """    
    _unicornhathd.brightness(b)


def set_rotation(r):
    """Set the display rotation in degrees.

    Actual rotation will be snapped to the nearest 90 degrees.

    """
    _unicornhathd.rotation(r)


def get_rotation():
    """Return the display rotation in degrees."""
    return _unicornhathd._rotation


def set_layout(pixel_map=None):
    """Do nothing, for library compatibility with Unicorn HAT."""
    _unicornhathd.set_layout(pixel_map)


def set_all(r, g, b):
    """Set all pixels to RGB colour.
    :param r: Amount of red from 0 to 255
    :param g: Amount of green from 0 to 255
    :param b: Amount of blue from 0 to 255
    """
    for row in range(_unicornhathd.height):
        for column in range(_unicornhathd.width):
            _unicornhathd.set_pixel(row,column,r,g,b)  


def set_pixel(x, y, r, g=None, b=None):
    """Set a single pixel to RGB colour.

    :param x: Horizontal position from 0 to 15
    :param y: Veritcal position from 0 to 15
    :param r: Amount of red from 0 to 255
    :param g: Amount of green from 0 to 255
    :param b: Amount of blue from 0 to 255

    """
    _unicornhathd.set_pixel(int(x),int(y),r,g,b)


def set_pixel_hsv(x, y, h, s=1.0, v=1.0):
    """Set a single pixel to a colour using HSV.

    :param x: Horizontal position from 0 to 15
    :param y: Veritcal position from 0 to 15
    :param h: Hue from 0.0 to 1.0 ( IE: degrees around hue wheel/360.0 )
    :param s: Saturation from 0.0 to 1.0
    :param v: Value (also known as brightness) from 0.0 to 1.0

    """
    _unicornhathd.set_pixel_hsv(x,y,h,s,v)


def get_pixel(x, y):
    """Get pixel colour in RGB as a tuple.

    :param x: Horizontal position from 0 to 15
    :param y: Veritcal position from 0 to 15

    """
    i = (x * _unicornhathd.width) + y
    return _unicornhathd.pixels[i]


def shade_pixels(shader):
    """Set all pixels to a colour determined by a shader function.

    :param shader: function that accepts x/y position and returns an r,g,b tuple.

    """
    for x in range(_unicornhathd.width):
        for y in range(_unicornhathd.height):
            r, g, b = shader(x, y)
            set_pixel(x, y, r, g, b)


def get_pixels():
    """Return entire buffer."""
    pass


def get_shape():
    """Return the shape (width, height) of the display."""
    return _unicornhathd.width,_unicornhathd.height


def clear():
    """Clear the buffer."""
    _unicornhathd.clear()


def off():
    """Clear the buffer and immediately update Unicorn HAT HD.

    Turns off all pixels.

    """
    _unicornhathd.off()



def show():
    """Output the contents of the buffer to Unicorn HAT HD."""
    _unicornhathd.show()



rotation = set_rotation
brightness = set_brightness