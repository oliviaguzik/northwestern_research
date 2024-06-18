# northwestern_research

 **Steps**
 1) Build Container: ```docker build -t ubuntu-python-java . ```
 2) Run Container: ```docker run -v %cd%:/usr/src/app -it ubuntu-python-java``` USING Command Prompt not PowerShell 
 3) Now once in Docker Container navigate to correct directory: ```cd /usr/src/app/```
 4) Run application: ```python3 VideoToPose.py```

 docker cp <container_id>:/usr/src/app/annotated_image.jpg ./annotated_image.jpg
docker cp <container_id>:/usr/src/app/segmentation_mask.jpg ./segmentation_mask.jpg


**Computational Tasks**
1) Opening and reading the video file using OpenCV
2) Reading each frame from the video 
3) Converting the frame color space from BGR to RGB (OpenCV uses BGR and MediaPipe uses RGB)
4) Calculating the timestamp for each frame 
5) Copying the image, looping through landmarks, and drawing landmarks on the image using OpenCV and MediaPipe
6) Converting the annotated frame back to BGR for saving 
7) Saving the annotated frame withe the timestamp in the filename 

**ML Tasks**
1) Detecting pose landmarks in each frame using the MediaPipe PoseLandmarker model
