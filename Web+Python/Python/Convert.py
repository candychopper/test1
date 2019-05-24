import os, sys, pythonFile, re, shutil, random, Convert, Data
from PIL import Image
ImagePath = os.listdir("Pic")

def ConvertImages():
	os.system("clear")	
	print(ImagePath)	

	#im = Image.open('Pic/Buttonpic4.jpg')
	#new_im = im.convert('RGBA')
	#new_im.save('Pic/test4.png', 'PNG', quality=100)
	
	# JPG to PNG
	im = Image.open('Pic/Buttonpic4.jpg')
	im.save("Pic/TestKuva.png")
	# PNG to JPG
	from glob import glob                                                           
	import cv2 
	pngs = glob('Pic/*.png')

	for j in pngs:
		img = cv2.imread(j)
		cv2.imwrite(j[:-3] + 'jpg', img)
		print(img)

if __name__ == "__main__":
	ConvertImages()
