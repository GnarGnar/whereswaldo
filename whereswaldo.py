import numpy as np
from PIL import Image, ImageDraw

waldo1 = Image.open("swamp_waldo.png")
waldo2 = Image.open("waldo_dinosaurs.png")
waldo3 = Image.open("waldo_toys.png")
waldo4 = Image.open("waldo_spain.png")
waldo5 = Image.open("waldo_space.png")
waldo6 = Image.open("waldo_troy.png")

waldo1.load()
waldo2.load()
waldo3.load()
waldo4.load()
waldo5.load()
waldo6.load()

def waldo1func():

	draw = ImageDraw.Draw(waldo1)
	draw.line((450,490) + (481,490), fill = (0,255,0), width = 5)
	draw.line((450,515) + (481,515), fill = (0,255,0), width =5)
	draw.line((450,490) + (450,515), fill = (0,255,0),width = 5)
	draw.line((481,490) + (481,515), fill =(0,255,0),width =5)
	del draw
	waldo1.show()
	width, height = waldo1.size
	print (width)
	print (height)
	
	
	
def waldo2func():
	waldo2.show()
	
def waldo3func():
	waldo3.show()
	
def waldo4func():
	waldo4.show()
	
def waldo5func():
	waldo5.show()
	
waldo1func()

