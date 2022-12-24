# Retinal Disease Recognition and Localisation through Convolutional Neural Networks
Corso di Elaborazione di Bioimmagini A.A. 2022/2023  
Ravelli Fabrizio - mat. 177085

## Dataset
The dataset used (**Retinal OCT Images)** was obtained from the kaggle website (https://www.kaggle.com/datasets/paultimothymooney/kermany2018).

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
The activation maps for each convolutional layer of each model are contained in the activation_maps folder and were obtained with the script in the same folder.  
The image in the activation_maps/images folder (DRUSEN.jpeg) was used to generate them.
