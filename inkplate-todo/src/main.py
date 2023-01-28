from inkplate6_COLOR import Inkplate

from fonts import fonts


if __name__ == "__main__":
    display = Inkplate()
    display.begin()

    start_x = 10
    start_y = 10
    text_height = 24

    text = "abcdefghijklmnopqrstuvwxyz\nABCDEFGHIJKLMNOPQRSTUVWXYZ\n0123456789-=\n`[]\\;',./\n~\{\}|:\"<>?"

    for l, line in enumerate(text.splitlines()):
        line_y = start_y + l * text_height
        grid = fonts.to_pixels("arial24", line)
        for r, row in enumerate(grid):
            for c, pixel in enumerate(row):
                if pixel:
                    display.writePixel(start_x + c, line_y + r, Inkplate.RED)

    display.display()
