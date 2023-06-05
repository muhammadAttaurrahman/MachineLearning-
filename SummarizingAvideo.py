import cv2
import numpy as np 

# importing video and getting height and width of the video 
video = cv2.VideoCapture("originolVideo.mp4") 
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))

threshold= 20.0

# Now we have to write our summarized video
writer =cv2.VideoWriter("summarizedVideo.mp4", cv2.VideoWriter_fourcc(*'DIVX'),25, (width, height))
# ret is a boolean varaible that will return either True or Flase and here we are saving the first frame of our video
ret, frame1 = video.read() 
# Here we are assigning first frame to the prevoius frame
previous_frame = frame1 

unique_frames= 0
common_frames = 0 
all_frames = 0 


while True :
    ret, frame = video.read()
    if ret is True :
        # Here below function is very important 
        # We are subtracting new frame from the prevous frame and summing it as well 
        # and then dividing that by the size of the current frame 
        # Now if the difference between both frames is larger than fixed threshold it will be cosidered a unique frame 
        # If the difference is smaller it will be considered similar frame
        if(((np.sum(np.absolute(frame-previous_frame))/np.size(frame)) > threshold)):
            writer.write(frame)
        else:
            previous_frame=frame 
            common_frames+=1
        
        cv2.imshow("Frame", frame)
        all_frames +=1 
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("All frames :" ,all_frames)
print("Unique frames :", unique_frames)
print("Common frames :",common_frames)

# releasing the video and writer
video.release()
writer.release()
cv2.destroyAllWindows()
