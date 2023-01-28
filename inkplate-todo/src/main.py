from inkplate6_COLOR import Inkplate

from lib import clickup

TEXT_SIZE = 1
TEXT_HEIGHT = TEXT_SIZE * 10

if __name__ == "__main__":
    display = Inkplate()
    display.begin()

    tasks = clickup.get_tasks()

    display.setTextSize(TEXT_SIZE)
    
    for i, task in enumerate(tasks):
        x = 100
        y = 100 + i * TEXT_HEIGHT
        display.printText(x, y, str(task))
    
    display.display()
