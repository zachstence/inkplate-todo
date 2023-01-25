from inkplate6_COLOR import Inkplate

from server import Server

if __name__ == "__main__":
    server = Server()

    inkplate = Inkplate()
    inkplate.begin()

    inkplate.display()
