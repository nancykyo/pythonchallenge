import urllib
from PIL import Image

if __name__ == '__main__':
	oxygen = Image.open("samples/oxygen.png")
	print oxygen.size, oxygen.mode
	rgb_im = oxygen.convert('RGB')
	for x in xrange(0,629,7):
		r, g, b = rgb_im.getpixel((x, 46))
		if r==g and g==b:
			print chr(r),