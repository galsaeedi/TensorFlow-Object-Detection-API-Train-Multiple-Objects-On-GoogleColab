# training-data-python-scripts-for-tensorflow-object-detection-API
<br>

<h3 align="center">copied repository from [EdjeElectronics] (https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10). and added my own python script </h3>
My added scripts are: txt_to_csv.py and Object_detection_image.py

</br>After gathering images just run the following script to convert txt labels files to csv:
```bash
python txt_to_csv.py
``` 
This will generate .csv file in proper format for custom object detection with [Tensorflow detector](https://github.com/tensorflow/models).



<h3 align="center"> ~Description~ </h3>
the repository contains the images, annotation data, .csv files, and TFRecords needed to train the detector. It also contains Python scripts that are used to generate the training data. It has scripts to test out the object detection classifier on images, videos, or a webcam feed (**NOTE**: here i'm just using object detection classifier on images).  

used to generate my own training data. If you want to practice training your own **electricity meter detector**, you can leave all the files as they are. 
**otherwise**, After clone my repo > follow this part (3. Gather and Label Pictures) from EdjeElectronics tutorial to train your own object detector.
