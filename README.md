# Retinal Disease Recognition and Localisation through Convolutional Neural Networks
Corso di Elaborazione di Bioimmagini A.A. 2022/2023  
Ravelli Fabrizio - mat. 177085

## Dataset
The dataset used for the work can be found at https://www.kaggle.com/datasets/fabrizioravelli/retinal-oct-images-splitted  

This collection of retinal images (76607) obtained by OCT (Optical Coherence Tomography) was made available by the authors of Identifying Medical Diagnoses and Treatable Diseases by Image-Based Deep Learning [Kermany et al. 2018].  
However, the original dataset available at the link https://www.kaggle.com/datasets/paultimothymooney/kermany2018 has duplicate images in the training test and data leakage between the training and testing folders.  
The duplicate images, and removed, were identified using the SHA-256 key.  

## Architectures
The architectures used in training and testing are:
- FCNNplus (proposed architecture)
- STANDARD_CNN from https://github.com/Djack1010/tami
- VGG16
- VGG19
- EfficientNetB0
- InceptionV3
- Xception

## GradCAM
In the GradCAM folder there is a selection of 10 heatmaps per class for each model.  
The CATIA2 tool was used to generate the heatmaps. (https://github.com/reFraw/CATIA2)

## Activation maps
The activation maps for each convolutional layer of the FCNNplus network are contained in the activation_maps folder and were obtained with the script in the same folder.  
The image in the activation_maps/images folder (DRUSEN.jpeg) was used to generate them.
