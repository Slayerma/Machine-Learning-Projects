

from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# Text to be rendered
txt = """Python is an interpreted high-level general-purpose programming
Its design philosophy emphasizes code readability with its use of signi"""

# Create a new image with a white background
width, height = 800, 600
image = Image.new('RGB', (width, height), color=(255, 255, 255))

# Create a drawing object
draw = ImageDraw.Draw(image)

# Use a built-in font provided by PIL
# font = ImageFont.truetype(font_path, 24)
font = ImageFont.truetype('wg_goodbye_font.ttf', 24)  # Replace 'Arial.ttf' with any built-in font name

# Split the text into lines based on a maximum line width
max_line_width = 50
lines = textwrap.wrap(txt, max_line_width)

# Draw the lines of text onto the image
y = 10
for line in lines:
    draw.text((10, y), line, font=font, fill=(0, 0, 138))
    y += font.size + 10

# Save the image
image.save("handwritten_text.png")
print("END")