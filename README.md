# northwestern_research

 **Steps**
 - 1) Build Container: ```docker build -t ubuntu-python-java . ```
 - 2) Run Container: ```docker run -v %cd%:/usr/src/app -it ubuntu-python-java``` USING Command Prompt not PowerShell 
 - 3) Now once in Docker Container navigate to correct directory: ```cd /usr/src/app/```
 - 4) Run application: ```python3 VideoToPose.py```

 docker cp <container_id>:/usr/src/app/annotated_image.jpg ./annotated_image.jpg
docker cp <container_id>:/usr/src/app/segmentation_mask.jpg ./segmentation_mask.jpg
