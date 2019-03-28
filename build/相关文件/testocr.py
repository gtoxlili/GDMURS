from PIL import Image
import os
import sys

if not os.path.exists(sys.argv[1]+"/试卷"):        
		os.makedirs(sys.argv[1]+"/试卷")           
else:
        None


# 加载原始图片
img = Image.open(sys.argv[1]+"/test_1.jpg").resize((2400, 1750))
# 从左上角开始 剪切 200*200的图片
x=200
y=750
img2 = img.crop((x, y,900+x,386+y )).resize((630, 270))
img2.save(sys.argv[1]+"/试卷/test_1.jpg")
y=1050
img2 = img.crop((x, y,900+x,386+y )).resize((630, 270))
img2.save(sys.argv[1]+"/试卷/test_2.jpg")
img = Image.open(sys.argv[1]+"/test_2.jpg").resize((2400, 1750))
# 从左上角开始 剪切 200*200的图片
x=1350
y=350
img2 = img.crop((x, y,900+x,386+y )).resize((630, 270))
img2.save(sys.argv[1]+"/试卷/test_3.jpg")
y+=250
img2 = img.crop((x, y,900+x,386+y )).resize((630, 270))
img2.save(sys.argv[1]+"/试卷/test_4.jpg")
y+=250
img2 = img.crop((x, y,900+x,386+y )).resize((630, 270))
img2.save(sys.argv[1]+"/试卷/test_5.jpg")
y+=250
img2 = img.crop((x, y,900+x,386+y )).resize((630, 270))
img2.save(sys.argv[1]+"/试卷/test_6.jpg")

print("i am ok")