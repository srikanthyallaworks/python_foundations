import unicornhathd
import time
import math
import itertools

rows,columns=unicornhathd.get_shape()

def getPosition(n):
    """Takes an integer, figures out the row/column

    Args:
        n (int): some number

    Returns:
        int,int: row,column tuple
    """
    return 0


def toColor(n):
    """Figures out what color the index is supposed to be

    Args:
        n (int): some number

    Returns:
        (int,int,int): RGB color. Will be white,red,blue,or green
    """
    return (255,255,255)


def main():
  unicornhathd.brightness(1)
  unicornhathd.set_all(0,0,255)

  for i in itertools.count():
    row,column = getPosition(i)
    r,g,b = toColor(i)
    unicornhathd.set_all(0,0,0)
    unicornhathd.set_pixel(row,column,r,g,b)
    unicornhathd.show()
    time.sleep(.5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        unicornhathd.clear()
        unicornhathd.off()
