from inkplate6_COLOR import Inkplate

import os

inkplate = Inkplate()

if __name__ == "__main__":
    print(os.listdir())

    inkplate.begin()

    inkplate.drawRect(50, 50, 75, 75, inkplate.GREEN)
    inkplate.display()
