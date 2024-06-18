# northwestern_research

 **Commands**
 - Build Container: ```docker build -t ubuntu-python-java . ```
 - Run Container: ```docker run -v .:/~ -d -it ubuntu-python-java```

 docker cp <container_id>:/usr/src/app/annotated_image.jpg ./annotated_image.jpg
docker cp <container_id>:/usr/src/app/segmentation_mask.jpg ./segmentation_mask.jpg
