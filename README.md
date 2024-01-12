# Trimap-Driven-Bayesian-Matting-with-CNN
Bayesian Matting for Image Transparency Estimation with Trimaps with and without CNN

Orchard-Bouman clustering is not typically associated with Bayesian methods. It's possible there's some confusion in your question. Orchard-Bouman clustering is a method used in image processing for color quantization. On the other hand, Bayesian methods are a broad class of statistical techniques based on Bayes' theorem, used in a wide range of fields, including machine learning, data analysis, and decision making. If you have a specific context or application in mind where Orchard-Bouman clustering and Bayesian methods are used together, please provide more details so I can give a more accurate answer.

# Bayesian matting without CNN

The provided code [Bayesian_matting.ipynb] performs Bayesian matting, a method used to enhance the quality of image cutouts by refining the transition between foreground and background. It takes an input image and a trimap (defining likely foreground, background, and uncertain regions) and iteratively calculates alpha values (pixel transparencies) using a weighted clustering approach. The algorithm refines these alpha values until convergence, resulting in an improved matte that accurately separates foreground and background elements. This is particularly useful for tasks like photo editing, where precise object extraction is essential.

# Bayesian matting with CNN

The provided code [Bayesian_matting_with_CNN.ipynb] implements a Bayesian Matting Convolutional Neural Network (CNN) using PyTorch for image matting. The BayesianMattingCNN class defines a simple neural network architecture with convolutional layers. The preprocess_input function prepares the input image and trimap for the network, and train_bayesian_matting_cnn trains the model using Mean Squared Error (MSE) loss and the Adam optimizer.

In the main function, an image and trimap are loaded, and a Bayesian matting alpha matte is obtained using the previously defined bayesian_matte function (which seems to be missing in the provided code, and you might need to add it or provide a suitable alternative). The input is then preprocessed, and a BayesianMattingCNN model is created, trained, and saved. The trained model is loaded, and a prediction is made on the input. The resulting alpha matte is displayed alongside the original image and trimap.

In this notebook run the below block which has bayesian_matte function which is used in the CNN model. 

# Trimap generation

A sample mimic of trimap generation is in trimap_generate.py 
The trimap is a binary image where pixels are labeled as fully foreground, fully background, or unknown, denoted by pixel values 255, 0, and values in between (e.g., 128) respectively.

# results

# Bayesian matting without CNN
![image](https://github.com/RakhilML/Trimap-Driven-Bayesian-Matting-with-CNN/assets/106943173/e5c9c79b-3506-41cf-8a4b-3010a017d911)

# Bayesian matting with CNN
![image](https://github.com/RakhilML/Trimap-Driven-Bayesian-Matting-with-CNN/assets/106943173/aeee9cd3-c03f-4b12-b052-a852f98d9f15)



