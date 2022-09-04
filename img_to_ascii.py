from PIL import Image
import pywhatkit
Image.open("radhaji.jpeg")
pywhatkit.image_to_ascii_art('radhaji.jpeg','MyArt')
read_file = open("MyArt.txt","r")
print(read_file.read())
