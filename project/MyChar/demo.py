from PIL import Image 
import argparse

parse = argparse.ArgumentParser()

#定义参数
parse.add_argument('file') 
parse.add_argument('-o','--out') 
parse.add_argument('--width',type=int,default=60)
parse.add_argument('--height',type=int,default=60)

args = parse.parse_args()

img = args.file
outfile = args.out
Width = args.width
Height = args.height

print(Width,'*',Height)

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r,g,b,alpha=256):
    if(alpha==0):
        return ' '

    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    length = len(ascii_char)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open(img)
    im = im.resize((Width,Height), Image.NEAREST)

    txt=''

    for i in range(Height):
        for j in range(Width):
            txt+=get_char(*im.getpixel((j,i)))
        txt+='\n'
    
    print(txt)


    if outfile:
        with open(outfile,'w') as f:
            f.write(txt)
    else:
        with open("output3.txt",'w') as f:
                f.write(txt)










