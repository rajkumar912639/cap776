
from PIL import Image

img = Image.open("example.jpg")

print(img.format, img.size, img.mode)
img.show()
