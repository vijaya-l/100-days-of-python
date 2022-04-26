from turtle import *
import tkinter as tk

color("red", "yellow")
begin_fill()
while True:
    forward(300)
    left(190)
    if abs(pos()) < 1:
        break
end_fill()
done()
