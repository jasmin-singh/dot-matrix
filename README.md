# dot-matrix
A Python3/Python Turtle program that takes raster image data values from any image and renders the image in black-and-white, pseudocolor, and grayscale dots.

# How Does It Work?
This program first uses a function to get raster values from any image. Then, it takes that data and makes a sublist of values from each block of pixels by separating the blocks into rows and columns. The average pixel value is calculated from the block sublist. The average pixel value is then converted to a circle radius by dividing the block size in half. The program scans through the image data block by block and represents each with a circle depending on render style. 

## Input
&emsp; &emsp; &emsp; &emsp; &emsp; &nbsp; &nbsp; ![Example image file that depicts a flower of orange and yellow shades against greenery comprised of cool colors.](https://github.com/user-attachments/assets/843ec35d-8b95-4ac3-ad30-d03bec91c530)

The example image (`file.png`) is uploaded as a test image for the program (Credit: University of South Florida). <br />Upload your own file by replacing `image_path = "file.jpg"` with the file path to your image.


## Output
### Black-and-White Render
![The image file is rendered in black-and-white with four different blocksize dimensions.](https://github.com/user-attachments/assets/43ebb64f-aa4c-4ea8-8e80-4a7d165f7044)

### Pseudocolor Render
![The image file is rendered in pseudocolor with four different blocksize dimensions.](https://github.com/user-attachments/assets/c793d4e0-75dc-4c3d-a1cb-4ed67e08875b)

### Grayscale Render
![The image file is rendered in grayscale with four different blocksize dimensions.](https://github.com/user-attachments/assets/12f5c3a9-a578-47d1-912b-0954d62c9650)

# Purpose and Applications
I made this as an experimental tool to render important image information with the least amount of detail. It's fascinating to see what information our eyes and brain need to understand what an image is trying to convey. 
The grayscale mode reveals the depth of the image. Seeing an image in pseudocolor can help with understanding lighting, especially within low-light images (think of a heat signature). Black-and-white rendering can help with identifying silhouettes. Different rendering sizes help with interpreting how much detail is needed to see information in an image. <br />

This is also important to learn when creating art. I aim to improve this program to become a tool (a helping eye) for artists — since it reduces the image to barebones information, this program can help artists understand what information is important when they look at reference images.
