from PIL import Image, ImageFilter
def toGray():
    img = Image.open("images/beijing.jpg")
    
    grayscale_img = img.convert("L")
    grayscale_img.save("images/output.jpg")
    
    blur=img.filter(ImageFilter.BoxBlur(30))
    blur.show()
    
def flip():
    img=Image.open("images/beijing.jpg")
    converted=img.transpose(Image.FLIP_TOP_BOTTOM)
    converted.show()

if __name__ == "__main__":
    #toGray()
    flip()