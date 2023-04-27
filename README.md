# Skin-Disease-Image-Classifier-for-Accurate-and-Accessible-Diagnosis

![1](https://user-images.githubusercontent.com/98489395/235007226-76b8aec2-796f-42b1-a0dd-6880e78322a1.png)


## Prerequisites

1. Python: 3.11.2
2. Deep Learning Frameworks: TensorFlow or PyTorch
3. Data Scrapping: Selenium
4. Data Preprocessing: data cleaning, data augmentation and data normalization
5. GPU(optonal)
6. Development Environment: conda 23.3.3
7. Dataset: [DermNet NZ Image Library](https://github.com/FridahKimathi) and [DermNet NZ Image Library](https://github.com/FridahKimathi)
8. Access to Cloud Computing Services: Google colab

## Introduction:

This project aims to develop a skin disease image classifier using machine learning algorithms to accurately diagnose and classify skin diseases. The objective is to provide a user-friendly platform that improves accessibility and affordability of dermatological care, while also aiding dermatologists in their clinical decision-making process and reducing the time it takes to diagnose skin diseases.

## Data Sources:

The dataset used for this project will be sourced from two primary websites - [DermNet NZ Image Library](https://github.com/FridahKimathi) and [DermNet NZ Image Library](https://github.com/FridahKimathi). DermNet NZ Image Library contains a vast collection of clinical images of various skin conditions, while the ISIC 2019 Challenge dataset focuses on the detection of melanoma and benign skin lesions. The combination of these datasets will provide a diverse range of skin conditions for the image classifier to learn from.

## Focus Diseases
1. Acne
2. Atopic dermatitis(Eczema)
3. Actinic keratosis
4. Benign Keratosis-like Lesions
5. Melanoma
6. Psoriasis
7. Basal cell carcinoma
8. Tinea


## Data Preprocessing:

The collected data will be preprocessed to ensure that it is suitable for the machine learning model. The images will be resized to a standard size to reduce the computational load and ensure consistency across the dataset. Additionally, the images will be labelled with the corresponding skin disease to facilitate supervised learning.

## Model Architecture:

The model architecture will be based on Convolutional Neural Networks (CNNs), a deep learning technique widely used for image classification tasks. Transfer Learning will be employed to utilise pre-trained models such as VGG-19, InceptionV3, and ResNet50 to fine-tune the model and improve its performance.

## Model Evaluation:

The model will be evaluated based on the accuracy. The accuracy will indicate the proportion of correctly classified skin diseases.

## Web Application:

The image classifier will be integrated into a web application that allows users to upload images of their skin diseases and receive a diagnosis. The application will be built using Flask, a Python-based web framework, and deployed on a cloud platform such as AWS or Heroku.

<img width="949" alt="frontpage_website" src="https://user-images.githubusercontent.com/98489395/235007469-93d33cf4-d514-4ffe-a751-5fe49ccb2d5c.png">

!(https://skin-disease-project-384422.uc.r.appspot.com/)


## Demo

Insert gif or link to demo

## Authors

- [@Fridah Kimathi](https://github.com/FridahKimathi)
- [@Anthony Nene](https://github.com/AnthonyNene-Kiarie)
- [@Scholar Chepkirui](https://github.com/Scholarchep)
- [@Amos Kibet](https://github.com/AmosMaru)
- [@Eugene Kuloba](https://github.com/eugenekuloba)
- [@Beth Mithamor](https://github.com/Mythamor)
