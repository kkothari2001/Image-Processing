## Image Processing Tasks given by SRA (Society of Robotics and automation) VJTI

The following tasks have ben performed by me, without the use of image processing libraries like opencv and only the mathematical manupilation of the image arrays using numpy was permitted.

---

### 1. Image Rotation

The given image had to be rotated by various angles.
I acheived this by calculating the new and y cordinates of each pixel with the help of a rotation matrix.

<img width="640" height="450" src="https://github.com/SRA-VJTI/practice-assignments/blob/master/Image-Processing/assets/rotate.png">

**Output**
|<img width="640" height="450" src="https://github.com/SRA-VJTI/practice-assignments/blob/master/Image-Processing/assets/rotate-no-bound.png">|<img width="640" height="450" src="https://github.com/SRA-VJTI/practice-assignments/blob/master/Image-Processing/assets/rotate-bound.png">|
|:---:|:---:|
|No Bound|Bound|

### 2. Applying Kernels

We found out how to apply certain kernels like blurring and sharpening to various images that had been provided to us. This was done with the help of convolutions of a kernel over the image.

| <img width="640" height="450" src="https://github.com/SRA-VJTI/practice-assignments/blob/master/Image-Processing/assets/blur.jpeg"> | <img width="640" height="450" src="https://github.com/SRA-VJTI/practice-assignments/blob/master/Image-Processing/assets/filter.png"> |
| :---------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------: |


**Output**
|<img width="640" height="450" src="https://github.com/SRA-VJTI/practice-assignments/blob/master/Image-Processing/assets/box-blur-out.png">|<img width="640" height="450" src="https://github.com/SRA-VJTI/practice-assignments/blob/master/Image-Processing/assets/gaussian-blur-out.png">|<img width="640" height="450" src="https://github.com/SRA-VJTI/practice-assignments/blob/master/Image-Processing/assets/sharpen-out.png">|
|:---:|:---:|:---:|
|Median Filter|Gaussian Filter|Sharpen|

### 3. Edge Detection

I carried out edge detection using convolutions of various filters/kernels over the image that had been converted to Black and white.

1. Vertical edge detection
2. Horizontal edge detection
3. Sobel edge detection (right, left, top, bottom)
   <img width="450" height="450" src="https://github.com/SRA-VJTI/practice-assignments/blob/master/Image-Processing/assets/edge-detection.png">|<img width="450" height="450" src="https://github.com/SRA-VJTI/practice-assignments/blob/master/Image-Processing/assets/edge-detection2.jpg">

### 4. Morphological Transformation

I found out about the various morphological kernels like erosion and dilation and their corresponding kernels and used the code of edge detection to do the same.

   <img width="640" height="450" src="https://github.com/SRA-VJTI/practice-assignments/blob/master/Image-Processing/assets/morphological.png">

### 5. Masking

Using the image as an HSV file I was successfully able mask and isolate purely the blue ball in the given image.

<img width="640" height="450" src="https://github.com/SRA-VJTI/practice-assignments/blob/master/Image-Processing/assets/mask.jpg">

### 6. ROI

I used bitwiseXOR operation in numpy to differentiate the 2 images. This created a mask which was used to isolate the ball!

|                                                             Figure 1                                                              |                                                              Figure 2                                                              |
| :-------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------: |
| <img width="640" height="450" src="https://github.com/SRA-VJTI/practice-assignments/blob/master/Image-Processing/assets/roi.jpg"> | <img width="640" height="450" src="https://github.com/SRA-VJTI/practice-assignments/blob/master/Image-Processing/assets/ROI2.jpg"> |
