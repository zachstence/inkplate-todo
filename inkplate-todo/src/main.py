from inkplate6_COLOR import Inkplate

from fonts import fonts

TEXT_SIZE = 1
TEXT_HEIGHT = TEXT_SIZE * 10

if __name__ == "__main__":
    display = Inkplate()
    display.begin()

    x = 100
    y = 100

    grid = fonts.to_pixels("arial24", "Testing")
    for r, row in enumerate(grid):
        for c, pixel in enumerate(row):
            if pixel:
                display.writePixel(100 + c, 100 + r, Inkplate.BLACK)

    display.display()
