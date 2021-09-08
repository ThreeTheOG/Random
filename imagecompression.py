from PIL import Image

# The file you want to compress.
fileName = 'Screenshot.png'

# Opens the file with pillow.
picture = Image.open(fileName)

# Prefix for Compressed Version(Not Required)
prefix = 'comp_'

# Gets the current(Beofre Compression) image Resolution.
res = picture.size

# Prints the Current resolution of the image.
print(f'Current image resoultion is: {res}')

# Compresses the file, and sets the quality to 65 (In reasearch it shows that 65 is the magic number for compression to quality ratio)
picture.save(prefix + fileName, optimize=True, quality = 65)

# No extra comment version
from PIL import Image

fileName = 'Screenshot.png'
prefix = 'comp_'
picture = Image.open(fileName)
res = picture.size

print(f'Current image resoultion is: {res}')
picture.save(prefix + fileName, optimize=True, quality = 65)

# If you need this for your PC, it wont do much, but when uploading from a server(Saving bandwidth), or storing images on a server, can make cost and performance much better, and it only costs a small amount of image quality.  

