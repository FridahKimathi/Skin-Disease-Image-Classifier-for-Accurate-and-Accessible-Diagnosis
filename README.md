# Skin-Disease-Image-Classifier-for-Accurate-and-Accessible-Diagnosis

1. Prerequisites
2. Python Programming Language
3. Deep Learning Frameworks
4. Data Scrapping Skills
5. Data Preprocessing Skills
6. GPU
7. Development Environment
8. Dataset
9. Access to Cloud Computing Services

## Introduction:
This project aims to develop a skin disease image classifier using machine learning algorithms to accurately diagnose and classify skin diseases. The objective is to provide a user-friendly platform that improves accessibility and affordability of dermatological care, while also aiding dermatologists in their clinical decision-making process and reducing the time it takes to diagnose skin diseases.

## Data Sources:
The dataset used for this project will be sourced from two primary websites - DermNet NZ Image Library and ISIC 2019 Challenge. DermNet NZ Image Library contains a vast collection of clinical images of various skin conditions, while the ISIC 2019 Challenge dataset focuses on the detection of melanoma and benign skin lesions. The combination of these datasets will provide a diverse range of skin conditions for the image classifier to learn from.

## Data Preprocessing:
The collected data will be preprocessed to ensure that it is suitable for the machine learning model. The images will be resized to a standard size to reduce the computational load and ensure consistency across the dataset. Additionally, the images will be labelled with the corresponding skin disease to facilitate supervised learning.

## Model Architecture:
The model architecture will be based on Convolutional Neural Networks (CNNs), a deep learning technique widely used for image classification tasks. Transfer Learning will be employed to utilise pre-trained models such as VGG-19, InceptionV3, and ResNet50 to fine-tune the model and improve its performance.

## Model Evaluation:
The model will be evaluated based on the accuracy. The accuracy will indicate the proportion of correctly classified skin diseases.

## Web Application:
The image classifier will be integrated into a web application that allows users to upload images of their skin diseases and receive a diagnosis. The application will also provide additional information on the specific skin disease, including symptoms, causes, and treatment options. The application will be built using Flask, a Python-based web framework, and deployed on a cloud platform such as AWS or Heroku.
