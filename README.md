# magicscan
Introduction and Explaination

There are three steps for generating model(output_labels.txt,output_graph.pb) and labeling testing image (test.jpg):

1.c1_video2frame.py: to write a image and extract a frame from video to .jpg and keep them in folder which named as product_code. This file has some paths to change and dimension of image has to setting in the first place.

2.c2_retrainModel.py: to retrain model(output_labels.txt,output_graph.pb) by using inception_v3 structure. The file input with .jpg files. The file has some paths to change in the bottom of file(see help as guide).

3.c3_label_image.py: for labeling image as any class. It has some path to change in the top of code-line.




