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
	draw = ImageDraw.Draw(waldo2)
	draw.line((1545,262) + (1564,262), fill = (0,255,0), width = 5)
	draw.line((1564,262) + (1566,275), fill = (0,255,0), width =5)
	draw.line((1566,275) + (1552,276), fill = (0,255,0),width = 5)
	draw.line((1552,276) + (1545,262), fill =(0,255,0),width =5)
	del draw
	waldo2.show()
	width, height = waldo2.size
	print (width)
	print (height)
	
def waldo3func():
	draw = ImageDraw.Draw(waldo3)
	draw.line((931,1532) + (1003,1532), fill = (0,255,0), width = 5)
	draw.line((1003,1532) + (995,1590), fill = (0,255,0), width =5)
	draw.line((995,1590) + (945,1586), fill = (0,255,0),width = 5)
	draw.line((945,1586) + (931,1532), fill =(0,255,0),width =5)
	del draw
	waldo3.show()
	width, height = waldo3.size
	print (width)
	print (height)
	
def waldo4func():
	draw = ImageDraw.Draw(waldo4)
	draw.line((160,1909) + (300,1909), fill = (0,255,0), width = 5)
	draw.line((300,1909) + (300,2074), fill = (0,255,0), width =5)
	draw.line((300,2074) + (195,2074), fill = (0,255,0),width = 5)
	draw.line((195,2074) + (160,1909), fill =(0,255,0),width =5)
	del draw
	waldo4.show()
	width, height = waldo4.size
	print (width)
	print (height)
	
def waldo5func():
	draw = ImageDraw.Draw(waldo5)
	draw.line((1095,1142) + (1214,1142), fill = (0,255,0), width = 5)
	draw.line((1214,1142) + (1206,1214), fill = (0,255,0), width =5)
	draw.line((1206,1214) + (1112,1209), fill = (0,255,0),width = 5)
	draw.line((1112,1209) + (1095,1142), fill =(0,255,0),width =5)
	del draw
	waldo5.show()
	width, height = waldo5.size
	print (width)
	print (height)

def waldo6func():
	draw = ImageDraw.Draw(waldo6)
	draw.line((430,1535) + (520,1535), fill = (0,255,0), width = 5)
	draw.line((520,1535) + (519,1570), fill = (0,255,0), width =5)
	draw.line((519,1570) + (445,1567), fill = (0,255,0),width = 5)
	draw.line((445,1567) + (430,1535), fill =(0,255,0),width =5)
	del draw
	waldo6.show()
	width, height = waldo6.size
	print (width)
	print (height)
	
	
waldo1func()
waldo2func()
waldo3func()
waldo4func()
waldo5func()
waldo6func()

