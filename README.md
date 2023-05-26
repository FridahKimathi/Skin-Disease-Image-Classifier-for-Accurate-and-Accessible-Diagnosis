
# **Derma AI: Skin Disease Image Classifier for Accurate and Accessible Diagnosis**

<img src="Images\Readme_pictures\1.png" alt="Derma AI logo" width="949" height="400">

#### **Authors**: [Fridah Kimathi](https://github.com/FridahKimathi), [Scholar Chepkirui](https://github.com/Scholarchep), [Amos Kibet](https://github.com/AmosMaru), [Anthony Nene](https://github.com/AnthonyNene-Kiarie), [Eugene Kuloba](https://github.com/eugenekuloba) and [Beth Mithamor](https://github.com/Mythamor)


Table of Contents
========

 * [Prerequisites](#Prerequisites)
 * [Overview](#Overview)
 * [Data Sources](#Data-Sources)
 * [Focus Diseases](#Focus-Diseases)
 * [Data Preprocessing](#Data-Preprocessing)
 * [Model Architecture](#Model-Architecture)
 * [Model Evaluation](#Model-Evaluation)
 * [Web Application](#Web-Application)
 * [Demo](#Demo)
 * [For More Information](#For-More-Information)
 * [Repository Structure](#Repository-Structure)

## Prerequisites
***

1. Python: 3.11.2 or above 
2. Deep Learning Frameworks such TensorFlow 
3. Data Scrapping libraries such as Selenium
4. Data Preprocessing knowledge, including data cleaning, data augmentation, and data normalization techniques.
5. GPU(optional)
6. Development Environment such as anaconda 23.3.3
7. Dataset: [`DermNet NZ Image Library`](https://dermnetnz.org/image-library) and [`ISIC 2019 Challenge`](https://challenge.isic-archive.com/data/#2019)
8. Access to Cloud Computing Services such as Google Colab

## Overview:
***
Skin diseases can have a significant impact on a person's health and wellbeing. Early diagnosis and treatment are essential for preventing complications, scarring, disfigurement, and even life-threatening conditions such as skin cancer. This project aims to develop an image classifier that can accurately identify common skin diseases in images uploaded by users.

## Data Sources:
***
The data used for this project was sourced from two primary websites - [`DermNet NZ Image Library`](https://dermnetnz.org/image-library) and [`ISIC 2019 Challenge`](https://challenge.isic-archive.com/data/#2019). The combination of these datasets provides a diverse range of skin conditions for the image classifier to learn from.

## Focus Diseases:
***
The image classifier was trained to identify eight focus diseases: `Acne`, `Atopic Dermatitis (Eczema)`, `Actinic Keratosis`, `Benign Keratosis-like Lesions`, `Melanoma`, `Psoriasis`, `Basal Cell Carcinoma`, and `Tinea (Ringworm)`. These diseases were selected based on their prevalence and the potential impact they can have on a person's health.

## Data Preprocessing:
***

Before training the model, the collected data is preprocessed to ensure its suitability. The images are resized to a standard size to reduce computational load and ensure consistency across the dataset. Additionally, the images are labelled with the corresponding skin disease to facilitate supervised learning.

## Model Architecture:
***
Derma AI's model architecture is based on Convolutional Neural Networks (CNNs), a deep learning technique widely used for image classification tasks. Transfer learning is employed to utilise pre-trained models such as `VGG-19` and `EfficientNet` to fine-tune the model and improve its performance.

## Model Evaluation:
***

The model's accuracy, indicating the proportion of correctly classified skin diseases, is used to evaluate its performance. 

         Training and Validation Accuracy and Loss
<img src="Images\Readme_pictures\loss_acc.png" alt="Loss and accuracy" width="949">

## Web Application:
***

To make the skin disease image classifier easily accessible to users, it was integrated into a user-friendly web application. Users can upload images of their skin diseases, and the application provides an accurate diagnosis of the skin condition. The application only accepts images that contain human skin and gives an error message if the uploaded image is not a valid image file or if the skin disease is not in our database yet.

The skin disease image classifier web application is powered by Flask, a popular Python-based web framework, and is hosted on the Google Cloud platform, ensuring reliability and scalability.

[`Derma AI website`](https://skin-disease-project-384422.uc.r.appspot.com/)

<img src="https://user-images.githubusercontent.com/98489395/235007469-93d33cf4-d514-4ffe-a751-5fe49ccb2d5c.png" alt="frontpage_website" width="949" >

## Demo:
***

Insert gif or link to demo

## Conclusion:
***

The skin disease classifier model has shown promising results in accurately identifying various skin diseases with an 88% accuracy rate on the test set. The integration of this model into a website will provides an accessible and efficient platform for users to upload photos of their skin diseases and receive accurate diagnoses. However, the model is not without its limitations, including the potential for bias in the training dataset and variability in image quality uploaded by users. Future work includes expanding the dataset and improving the model's ability to identify other skin conditions, as well as conducting real-world validation studies and integrating the model with telemedicine technologies. Despite these limitations, the model represents a significant step forward in the field of dermatology and has the potential to improve access to healthcare for individuals with skin conditions.

## Limitations:
***

* **Limited dataset:** The model was trained on a limited dataset, which may not be representative of all skin disease and skin types. 
* **Lack of diversity:** Skin diseases can present differently in different people based on factors such as age, skin type, and ethnicity.Potential bias in the dataset used for training the model, which may lead to inaccurate predictions for certain demographics or skin types.
* **Dependence on image quality:** The model's perfomance may vary depending on the quality of images uploaded by users. Images that are blurry, poorly lit, or not centered properly may not be accurately classified by the model.
* **Human error:** The accuracy of the model may also be affected by human error, such as mislabeling or misdiagnosing the skin disease images in the dataset.

## Recommendations:
***
* Collect more diverse and high-quality  skin disease images from different populations and sources to improve the model's ability to generalize to new data.
* Incorporate expert knowledge  from dermatologists or other medical professionals to verify and help label and diagnose the skin disease images in the dataset.

* Incorporate additional metrics such as precision, recall, and F1 score to evaluate the model's performance.

* Investigate the potential of incorporating additional data sources such as patient history and clinical data to improve the accuracy of the diagnosis.

## Future Work:
***

* **Real-world validation:** Real-world validation studies can be conducted to evaluate the model's performance in clinical settings and to assess its impact on patient outcomes.
* **Expand dataset:** Expanding the dataset with more diverse skin types, demographics, and skin conditions can improve the model's generalizability and reduce potential biases.
* **Expand to other skin conditions:** The model can be further developed to identify a broader range of skin conditions beyond the current scope of skin diseases, such as wounds. This would increase the versatility and usefulness of the model for both patients and healthcare professionals.
* **Explainable AI:** Implementing explainable AI techniques can help clinicians and patients understand the model's decision-making process, increasing trust and transparency in the model's predictions.
* **Integrate model with telemedicine technologies:** The model can also be integrated with telemedicine technologies to enable remote diagnosis and treatment of skin diseases.


## For More Information
***
We appreciate your decision to use our skin disease image classifier, and we hope that it will contribute to your overall skin health and well-being. Should you have any queries or apprehensions, please do not hesitate to reach out to us. Additionally, you can refer to the [`Jupyter Notebook`](https://github.com/FridahKimathi/Skin-Disease-Image-Classifier-for-Accurate-and-Accessible-Diagnosis/blob/main/DermaAI.ipynb) for a comprehensive analysis or review the [`presentation`](https://github.com/FridahKimathi/Skin-Disease-Image-Classifier-for-Accurate-and-Accessible-Diagnosis/blob/main/Skin_Image_Classifier_Presentation.pdf) for further information.

## Repository Structure

```
├── Data
├── Images
├── Notebooks
├── website
├── DermaAI.ipynb
├── README.md
├── Skin_Image_Classifier_Presentation.pdf
```# Derma-AI-Skin-Disease-Image-Classifier-for-Accurate-and-Accessible-Diagnosis
