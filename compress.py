from PIL import Image

# Open the original image
image = Image.open('/Users/rohanpadhye/Desktop/Projects/smart-doorbell/TestImages/saved_img.jpg')

# Compress the image by reducing the quality
compressed_image = image.copy()
compressed_image.save('compressed_image.jpg', optimize=True, quality=50)
