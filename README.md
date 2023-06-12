# Garbage-Classifier
## Introduction:
The Garbage Classifier is a machine learning model and accompanying code that aims to classify images into various categories of garbage. This project provides a solution to automatically classify garbage images, helping to promote proper waste management and recycling practices.

## Installation:
To use the Garbage Classifier, please follow the steps below:

### 1. Clone the repository from GitHub:
git clone https://github.com/anubhav-97/Garbage-Classifier.git
### 2. Install the required dependencies. It is recommended to use a virtual environment to avoid conflicts with other Python packages.
cd Garbage-Classifier
pip install -r requirements.txt
### 3. Download the pre-trained model weights:
### You will need to download the pre-trained model weights file from the following link and place it in the weights directory:
### Download Model Weights
### 4. Run the application:
python classify.py
## Usage:
Once the application is running, you can use it to classify garbage images. Here are the steps to follow:
Place the image file you want to classify in the images directory.
In the terminal or command prompt, execute the following command:
python classify.py
The application will process the image and display the predicted category of the garbage in the console.
## Customization:
If you want to train the model on your own dataset or modify the existing code, you can follow the steps below:

Prepare your dataset:

Create a new directory named dataset.
Inside the dataset directory, create subdirectories for each category of garbage you want to classify. For example, dataset/plastic, dataset/paper, dataset/metal, etc.
Place the corresponding images in their respective directories.
Train the model:

Open the train.py file and modify the configuration parameters according to your needs.
Run the training script:
Copy code
python train.py
Use the trained model:

After training, the model weights will be saved in the weights directory.
You can use the trained model by following the instructions in the "Usage" section above.
Contributing:
Contributions to the Garbage Classifier project are welcome. If you want to contribute, please follow these steps:

Fork the repository on GitHub.

Create a new branch with a descriptive name for your feature or bug fix.

Make the necessary changes in your branch.

Commit your changes and push them to your forked repository.

Submit a pull request, clearly describing the changes you made and their purpose.
