from PIL import Image
def toGray():
    img = Image.open("images/beijing.jpg")
    
    grayscale_img = img.convert("L")
    
    grayscale_img.save("images/output.jpg")
    
if __name__ == "__main__":
    toGray()