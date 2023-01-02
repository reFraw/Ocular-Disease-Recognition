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

## Visual Explainability
To verify the correct learning of patterns by the network, visual explainability will be provided to the model.  
This will be achieved by using the ScoreCAM algorithm for heatmap generation and intermediate activations analysis.  
### Class Activation Mapping
The ScoreCAM algorithm was used to generate the heatmaps as opposed to the more classical GradCAM algorithm.  
For each class, five images were randomly selected from the test folder and the heatmaps obtained are in the ScoreCAM/FCNNplus_ScoreCAM.zip folder.  
