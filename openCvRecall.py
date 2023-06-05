import cv2
import numpy as np
# To Upload an image 
image = cv2.imread("opencvrecall.png")
cv2.imshow("Original image ", image)

# 1 . Image Rotation 
# we need height and width forit 

height , width = image.shape[0:2]
rotationMatrix = cv2.getRotationMatrix2D((width/2 , height/2 ), 90 , .5)
rotatedImage = cv2.warpAffine(image ,rotationMatrix , (width , height))
# cv2.imshow("Rotated Image :" , rotatedImage)


# 2 :> Crop an image 
startRow = int(height*.15)
startCol = int(width*.15)
endRow = int(height*.85)
endCol = int(width*.85)

cropedImage = image[startRow:endRow ,startCol:endCol]
# cv2.imshow("Cropped image",cropedImage)


# 3:> Resize an image

resizedImage = cv2.resize(image ,(0,0) , fx=0.50 , fy=0.50)  #fx (width) , fy (height)
# cv2.imshow("Resized Image ", resizedImage)

# 4:>Contrast an image 

contrast_image = cv2.addWeighted(image,3.0,np.zeros(image.shape,image.dtype),0,0)
# cv2.imshow("Contrast Image",contrast_image)

# 5:> Making an image Gussian Blur and median blur

blurImage = cv2.GaussianBlur(image , (9,9),0)
medianBlurImage = cv2.medianBlur(image,7)
# cv2.imshow("Median Blur",medianBlurImage)
# cv2.imshow("Blurr image",blurImage)


# 6:> Detecting Edges 

edgesDected = cv2.Canny(image , 100,200)
# cv2.imshow("Edes Detected  ",edgesDected)

# 6:> cobert image to greyScale (black & white)

greyScaleImage = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
cv2.imshow("B & W iMAGE ", greyScaleImage)

#7:>OCR Extracting text from the imge 
# import  pytesseract
# img = cv2.imread("Life-Quotes-Dolly-680x430.jpg",0)
# stringPart = pytesseract.image_to_string(img)
# print(stringPart)

# 8:> color Detection 

coloredImage = cv2.imread("circles.png")

hsv = cv2.cvtColor(coloredImage , cv2.COLOR_BGR2HSV)
lower_range = np.array([179,100,100],dtype=np.uint8)
upper_range = np.array([189,255,255],dtype=np.uint8)
mask =cv2.inRange(hsv,lower_range ,upper_range)

cv2.imshow("ColoredImge ",coloredImage)
cv2.imshow("HSV",hsv)
cv2.imshow("REd in image",mask)


cv2.waitKey()
cv2.destroyAllWindows()