from graphics import *

def main():
    win = GraphWin("My Circle", 300,300)
    c = Circle(Point(100,100), 50)
    c.draw(win)
    win.getMouse() # pause for click in window
    win.close()
    print win.isClosed()
    win.getMouse() # pause for click in window
main()
