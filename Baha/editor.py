from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os
print(os.listdir('.'))
for k in os.listdir('.'):
    if k.endswith('.jpg') or k.endswith('.png'):
        i = Image.open(k)
        fn, flext = os.path.splitext(k)

        res = i.convert('L')
        res1 = res.filter(ImageFilter.BLUR)
        res2 = res1.resize((1080, 1080))
        width, height = res2.size

        draw = ImageDraw.Draw(res2)
        text = "baha3035"
        title = "white"
        font = ImageFont.truetype("arial.ttf", 80)
        textwidth, textheight = draw.textsize(text, font)

        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        draw.text((x, y), text, title, font=font)

        # Here are files with separate Images changes and the result
        res2.save('final_images/{}{}'.format(fn, flext))