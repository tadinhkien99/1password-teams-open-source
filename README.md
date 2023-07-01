# Alopecia Classification

## 0. Overview
Alopecia classification involves the categorization and differentiation of conditions that cause hair loss from those that do not. This classification is crucial for accurate diagnosis, treatment planning, and management of individuals experiencing hair-related issues. Here is an overview of the classification of alopecia and non-alopecia conditions:

Alopecia Conditions:
 - Androgenetic Alopecia: Also known as pattern hair loss, this condition is characterized by progressive, non-scarring hair loss that primarily affects the scalp. It is the most common form of alopecia and is influenced by genetic and hormonal factors.
 - Alopecia Areata: An autoimmune disorder causing patchy hair loss due to the immune system attacking the hair follicles. It can occur on the scalp or other body areas and may progress to total or universal hair loss.
 - Traction Alopecia: Hair loss caused by repetitive tension or pulling on the hair, often due to tight hairstyles like braids, ponytails, or extensions.
 - Telogen Effluvium: A temporary form of hair loss caused by a disturbance in the hair growth cycle, resulting in excessive shedding. It can be triggered by various factors such as stress, hormonal changes, medications, or nutritional deficiencies.
 - Cicatricial (Scarring) Alopecia: Hair loss characterized by the destruction and replacement of hair follicles with scar tissue. It can result from autoimmune diseases, infections, trauma, or certain medications.
 - Other Types of Alopecia: There are additional less common types of alopecia, including alopecia mucinosa, trichotillomania (hair pulling disorder), anagen effluvium (hair loss during the growth phase), and congenital alopecia (present from birth).

Non-Alopecia Conditions:
 - Normal Hair Shedding: It is normal for individuals to experience some hair shedding as part of the natural hair growth cycle. This shedding is not considered pathological and should not cause significant hair loss or thinning.
 - Temporary Hair Loss: Various factors like illness, surgery, certain medications, or hormonal changes can lead to temporary hair loss that resolves once the underlying cause is addressed.
 - Structural Hair Disorders: Some individuals may have hair abnormalities due to structural or genetic factors, but without significant hair loss. Examples include conditions like trichorrhexis nodosa or pili torti.
 - Hair Breakage: Hair breakage refers to the snapping or breaking of hair strands, often due to excessive heat styling, chemical treatments, or mechanical trauma. While it can result in thinner-looking hair, it is not a form of true alopecia.


- [Alopecia Classification](#project-title)
    - [0. Overview](#0-overview)
    - [1. Dataset](#1-dataset)
    - [2. Run code](#2-run-code)
    - [3. Feature Processed](#4-feature-processed)
    - [4. Models](#5-models)
    - [5. Evaluate](#6-evaluate)
    - [6. License](#8-license)

## 1. Dataset

We use 2 classes images Alopecia and Non Alopecia.
| Parameter      | Type     |
|:---------------|:---------|
| `Alopecia`     | `Image`  |
| `Non Alopecia` | `Image` |

## 2. Run code

Clone the project

```bash

  git clone https://github.com/tadinhkien99/health-app-ward.git
```

Go to the project directory

```bash
  cd health-app-ward
```

Install libraries

```bash
  pip install -r requirements.txt
```

Run web app

```bash
  python app.py
```

## 3. Feature Processed
- Aumentation
- Pretrained model

## 4. Models

- [InceptionV3](https://www.tensorflow.org/api_docs/python/tf/keras/applications/inception_v3/InceptionV3)

  The InceptionV3 model is a deep learning architecture designed for image classification, known for its efficient use of computation and strong accuracy. It has been widely used for tasks such as object recognition, transfer learning, and feature extraction in computer vision applications.

- [MobileNet](https://www.tensorflow.org/api_docs/python/tf/keras/applications/mobilenet/MobileNet)

  The MobileNet model is a lightweight deep learning architecture specifically designed for mobile and embedded devices, offering a good trade-off between model size and accuracy. It achieves efficiency by employing depthwise separable convolutions, making it well-suited for real-time image classification and other resource-constrained applications.

- [ResNet50](https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet50/ResNet50)

  The ResNet50 model is a deep learning architecture that consists of 50 layers, known for its exceptional performance in image classification and other computer vision tasks. It introduces the concept of residual connections, allowing for deeper networks to be trained effectively and achieving state-of-the-art accuracy on large-scale datasets.

- [VGG16](https://www.tensorflow.org/api_docs/python/tf/keras/applications/vgg16/VGG16)
 
  VGG16 is a deep convolutional neural network architecture known for its simplicity and effectiveness in image classification tasks. With 16 layers of trainable parameters, it has achieved competitive performance on various benchmark datasets.

## 5. Evaluate

- Accuracy score
- Confusion matrix
- Classification report
- ROC curve
- Precision-recall curve
- F1 score

## 6. License

[MIT](https://choosealicense.com/licenses/mit/)

## 🚀 About Me

- [Kien Kuro](https://github.com/tadinhkien99)

## Support

For support, email tadinhkien99@gmail.com
