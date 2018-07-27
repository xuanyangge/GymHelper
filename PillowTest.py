from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('./push-ups/test1.jpeg').convert('RGBA')

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a drawing context
d = ImageDraw.Draw(txt)

r = 20

d.ellipse((10, 10, 10+r, 10+r), fill=(255,0,0,128))

# draw text, half opacity
d.text((10,10), "Hello", fill=(255,255,255,128))
# draw text, full opacity
d.text((10,60), "World", fill=(255,255,255,255))

d.point
out = Image.alpha_composite(base, txt)

out.show()