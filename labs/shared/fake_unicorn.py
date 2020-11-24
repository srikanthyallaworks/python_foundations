""" Fake Unicorn HAT HD library.

Interface borrowed from:
   https://raw.githubusercontent.com/pimoroni/unicorn-hat-hd/master/library/unicornhathd/__init__.py

"""

import colorsys
import time
import pyglet
import sys

try:
    import numpy
except ImportError:
    raise ImportError('This library requires the numpy module\nInstall with: sudo pip install numpy')


__version__ = '0.0.4'

_SOF = 0x72
_DELAY = 1.0 / 120

WIDTH = 16
HEIGHT = 16

PHAT = None
HAT = None
PHAT_VERTICAL = None
AUTO = None
PANEL_SHAPE = (16, 16)


_rotation = 0
_brightness = 0.5
_buffer_width = 16
_buffer_height = 16
_addressing_enabled = False
_buf = numpy.zeros((_buffer_width, _buffer_height, 3), dtype=int)

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




is_setup = False


def setup():
    """Initialize Unicorn HAT HD."""
    global _buf, is_setup

    if is_setup:
        return

    #pyglet.app.run()
    is_setup = True


def enable_addressing(enabled=True):
    """Enable multi-panel addressing support (for Ubercorn)."""
    global _addressing_enabled
    _addressing_enabled = enabled


def setup_buffer(width, height):
    """Set up the internal pixel buffer.

    :param width: width of buffer, ideally in multiples of 16
    :param height: height of buffer, ideally in multiples of 16

    """
    global _buffer_width, _buffer_height, _buf

    _buffer_width = width
    _buffer_height = height
    _buf = numpy.zeros((_buffer_width, _buffer_height, 3), dtype=int)


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
    global _brightness

    _brightness = b


def set_rotation(r):
    """Set the display rotation in degrees.

    Actual rotation will be snapped to the nearest 90 degrees.

    """
    global _rotation

    _rotation = int(round(r / 90.0))


def get_rotation():
    """Return the display rotation in degrees."""
    return _rotation * 90


def set_layout(pixel_map=None):
    """Do nothing, for library compatibility with Unicorn HAT."""
    pass


def set_all(r, g, b):
    """Set all pixels to RGB colour.

    :param r: Amount of red from 0 to 255
    :param g: Amount of green from 0 to 255
    :param b: Amount of blue from 0 to 255

    """
    _buf[:] = r, g, b


def set_pixel(x, y, r, g=None, b=None):
    """Set a single pixel to RGB colour.

    :param x: Horizontal position from 0 to 15
    :param y: Veritcal position from 0 to 15
    :param r: Amount of red from 0 to 255
    :param g: Amount of green from 0 to 255
    :param b: Amount of blue from 0 to 255

    """
    if type(r) is tuple:
        r, g, b = r

    elif type(r) is str:
        try:
            r, g, b = COLORS[r.lower()]

        except KeyError:
            raise ValueError('Invalid color!')

    _buf[int(x)][int(y)] = r, g, b


def set_pixel_hsv(x, y, h, s=1.0, v=1.0):
    """Set a single pixel to a colour using HSV.

    :param x: Horizontal position from 0 to 15
    :param y: Veritcal position from 0 to 15
    :param h: Hue from 0.0 to 1.0 ( IE: degrees around hue wheel/360.0 )
    :param s: Saturation from 0.0 to 1.0
    :param v: Value (also known as brightness) from 0.0 to 1.0

    """
    r, g, b = [int(n * 255) for n in colorsys.hsv_to_rgb(h, s, v)]
    set_pixel(x, y, r, g, b)


def get_pixel(x, y):
    """Get pixel colour in RGB as a tuple.

    :param x: Horizontal position from 0 to 15
    :param y: Veritcal position from 0 to 15

    """
    return tuple(_buf[int(x)][int(y)])


def shade_pixels(shader):
    """Set all pixels to a colour determined by a shader function.

    :param shader: function that accepts x/y position and returns an r,g,b tuple.

    """
    for x in range(WIDTH):
        for y in range(HEIGHT):
            r, g, b = shader(x, y)
            set_pixel(x, y, r, g, b)


def get_pixels():
    """Return entire buffer."""
    return _buf


def get_shape():
    """Return the shape (width, height) of the display."""
    return _buffer_width, _buffer_height


def clear():
    """Clear the buffer."""
    _buf.fill(0)


def off():
    """Clear the buffer and immediately update Unicorn HAT HD.

    Turns off all pixels.

    """
    clear()
    show()


window = pyglet.window.Window(600, 600, resizable=False)
event_loop = pyglet.app.EventLoop()

cell_width = window.width/16
box_width = cell_width*.5


def get_box(bx,by):
    return pyglet.shapes.Rectangle(x=cell_width * bx, y=cell_width * by, width=box_width, height=box_width)

@window.event
def on_draw():
    window.clear()
    pyglet.shapes\
          .Rectangle(x=0, y=0, width=window.width,height=window.height, color=(10, 10, 10))\
          .draw()    
    buf = numpy.rot90(_buf, _rotation)
    for row in range(HEIGHT):
        for column in range(WIDTH):
            box = get_box(row,column)
            box.color=buf[int(row)][int(column)]
            box.draw()


@window.event
def on_close():
    event_loop.exit()
    window.close()
    sys.exit()
    return pyglet.event.EVENT_HANDLED


def show():
    """Output the contents of the buffer to Unicorn HAT HD."""
    setup()
    pyglet.clock.tick()
    for window in pyglet.app.windows:
        window.switch_to()
        window.dispatch_events()
        window.dispatch_event('on_draw')
        window.flip()



rotation = set_rotation
brightness = set_brightness
