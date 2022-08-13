from PIL import Image
import sys
import os 

folder = sys.argv[1]
count = 0 
for file_name in os.listdir(folder):
    colorImage  = Image.open(folder+file_name)
    transposed  = colorImage.transpose(Image.ROTATE_90)
    rotated     = colorImage.rotate(45)
    transposed2  = colorImage.transpose(Image.ROTATE_270)
    transposed.save(folder+str(count)+"_90.jpg")
    rotated.save(folder+str(count)+"_45.jpg")
    transposed2.save(folder+str(count)+"_270.jpg")
    count += 1 
