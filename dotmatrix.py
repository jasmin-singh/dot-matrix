#created with the help of Trevor Barron
import numpy as np
import turtle
import turtle as t
from PIL import Image
from math import pi,sin,cos,floor

#function to get raster image data values from any image
def get_pixel_data(image_path):
    #pixel data from image
    #image path = file path to image
    img = Image.open(image_path).convert('L')
    pixels = img.load()
    width, height = img.size

    imagePixelData = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(img.getpixel((x,y)))
        imagePixelData.append(row)
    return imagePixelData

#usage
image_path = "file.jpg"
imagePixelData = get_pixel_data(image_path)
#print(imagePixelData) #debug

#insert image to bitmap data
#function to make a sublist of values from each block of pixels.  
#blocksize = number of rows and number of columns that form a "block" of pixel values
  #insert image to bitmap data
def block_values(blockSize, row, col):
    blockSubList = []
    for subRow in range(blockSize):
        for subCol in range(blockSize):
            blockSubList.append(imagePixelData[row*blockSize + subRow][col*blockSize + subCol])  
    #print(blockSubList)
    return(blockSubList)

#function to calculate the average pixel value from the block sublist
def average_pixel_value(blockSubList):
    pixelSum = 0
    numPixels = len(blockSubList)^2 
    for item in blockSubList:
        pixelSum = item + pixelSum
    pixelAverage = pixelSum // numPixels
    #print(pixelAverage) #debug
    return(pixelAverage)

#function to convert the average pixel value to circle radius
#draw the circle with center at the center of the current block
def draw_circle(pixelAverage, row, col, bmpWidth, bmpHeight, blockSize):
    #convert average pixel value to a circle radius
    # divide by half because diameter of circle is equal to blocksize.  Radius is 1/2 of blocksize
    circle_radius = (0.5*blockSize*(255-pixelAverage)/255)
    #print(circle_radius) #debug
    #0,0 is center of turtle canvas.  need to translate current row,col in imagePixelData list to turtle coordinates
    x = 0 - bmpWidth//2 + col * blockSize
    y = 0 + bmpHeight//2 - row * blockSize - blockSize//2  # turtle starts circle at left edge
    #print(x,y, row, col, pixelAverage)  #debug
    turtle.goto(x,y)
    turtle.color("white")
    turtle.pencolor("white")
    turtle.fillcolor("black")
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(circle_radius)
    turtle.end_fill()
    turtle.penup()
    #turtle.update() # update the screen
    return()

#function to convert the average pixel value to a circle with radius = blocksize and fill with pseudo_color value
#draw the circle with center at the center of the current block
def draw_pseudo_color_circle(pixelAverage,row,col,bmpWidth,bmpHeight,blockSize):
    #0,0 is center of turtle canvas.  need to translate current row,col in imagePixelData list to turtle coordinates
    x = 0 - (bmpWidth//2) + (col * blockSize)
    y = 0 + (bmpHeight//2) - (row * blockSize - (blockSize//2))  # turtle starts circle at left edge
    turtle.goto(x,y)
    # convert from pixel average to RGB values to fill the circle drawn
    # red channel is -127*sin(2*pi*grayscale/255) + 127
    # green channel is -127 * cos(2*pi*grayscale/255) + 127
    # blue channel is 127sin(2*pi*grayscale/255) + 127

    R = int(-127*sin(2*pi*pixelAverage/255) + 128)
    G = int(-127*cos(2*pi*pixelAverage/255) + 128)
    B = int( 127*sin(2*pi*pixelAverage/255) + 128)
    
    turtle.color("white") # dont want to see the turtle pen line
    turtle.fillcolor(R,G,B)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(blockSize//2)
    turtle.end_fill()
    turtle.penup()
    turtle.update() # update the screen
    return()

#function to convert the average pixel value to a circle with radius = blocksize and fill with grayscale value
#draw the circle with center at the center of the current block
def draw_grayscale_circle(pixelAverage, row, col, bmpWidth, bmpHeight, blockSize):
    #0,0 is center of turtle canvas.  need to translate current row,col in imagePixelData list to turtle coordinates
    x = 0 - bmpWidth//2 + col * blockSize
    #turtle starts circle at left edge
    y = 0 + bmpHeight//2 - row * blockSize - blockSize//2
    turtle.goto(x,y)

    #make R=G=B = average pixel value to get a grayscale image
    turtle.color("white") # dont want to see the turtle pen line
    turtle.fillcolor(pixelAverage,pixelAverage,pixelAverage)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(blockSize//2)
    turtle.end_fill()
    turtle.penup()
    #turtle.update() # update the screen
    return()

### main program starts here ###
turtle.hideturtle()
turtle.penup()
#turtle.speed(0)
turtle.tracer(0,0)
#avoids bad color sequence error
turtle.colormode(255)

# ask the user for the blocksize desired
blockSize = 3
while (blockSize % 2 != 0):
  blockSize = int(input("Enter the block size in pixels (multiple of 2)\n(recommend 4, 8, or 16 for small images): "))

#ask the user for the processing to perform
imageMode = 0
while (imageMode == 0):
    imageMode = int(input("\nEnter the image render mode (1, 2, or 3). \n(1) uses black circles of varying radius, \n(2) circles filled with pseudo color\n(3) fills circles with grayscale: "))

#print(blockSize) #debug
#print(imageMode) #debug

#get the pixel data - just grabs the data from the function that holds it.
imagePixelData = get_pixel_data(image_path)

# get the width and height of the image from the list imagePixelData
bmpWidth = len(imagePixelData[0]) 
# the image width in pixels is the number of entries in each row of the pixel data list
bmpHeight = len(imagePixelData) 
# the image height in pixels is the number of sublists that are in the pixel data list

# truncate width and height to a multiple of the block size
bmpWidth = blockSize * (bmpWidth//blockSize) 
bmpHeight = blockSize * (bmpHeight//blockSize)

#print(bmpHeight) #debug
#print(bmpWidth) #debug

#scan thru the image data block by block
for row in range ((bmpHeight//blockSize)):
    for col in range ((bmpWidth//blockSize)):
        
        # make a sublist of image data for the current block
        # this is a list that contains the pixel data from a "block" of the image
        blockSubList = block_values(blockSize, row, col)   

        #calculate the average pixel value for the current block
        # this average represents the average grayscale value for the current block in the image
        pixelAverage = average_pixel_value(blockSubList)

        if (imageMode == 1):
            #draw a circle to represent the current block.  radius is proportional to gray level
            #smaller radius corresponds to lighter average value , larger radius corresponds to darker average value
            draw_circle(pixelAverage, row, col, bmpWidth, bmpHeight, blockSize)

        elif (imageMode == 2):
            #draw a circle to represent the current block.
            #radius = blocksize.  fill value is equal to average pixel value
            draw_pseudo_color_circle(pixelAverage, row, col, bmpWidth, bmpHeight, blockSize)

        else: #image mode 3
        #draw a circle to represent the current block.  radius = blocksize.  fill value is equal to average pixel value
            draw_grayscale_circle(pixelAverage, row, col, bmpWidth, bmpHeight, blockSize)

turtle.update()
turtle.mainloop()
