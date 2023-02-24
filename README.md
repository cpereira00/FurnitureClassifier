# FurnitureClassifier

This is a simple Flask API that uses transfer learning to build a neural network model on top of a pretrained model to classify images into three categories: "Chair", "Sofa", and "Bed". The model was trained on a custom dataset consisting of images of furniture items and produces an accuracy score of 82%.

Model details:

![image](https://user-images.githubusercontent.com/62851785/221097662-28094d4b-d346-4b4c-bdf2-844c3add3489.png)

Model Classification report:

![image](https://user-images.githubusercontent.com/62851785/221097694-060e4968-c5d0-4f09-949f-596bd94cc063.png)

files:
- datahandler.py: used to split dataset into train/test/val directories and resizes the images to a smaller format to prevent overfitting.
- trainer.ipynb: performs data augmentation/transformation and builds the neural network model. Evaluations are also present within file.
- deployment/main.py: flask app containing API call

To run the app:
1. Clone the repository
2. Run the flask app

Additional steps to explore the model
3. download the dataset, unzip it and place in root of directory
4. Run the dataHandler.py script
5. Run the trainer.ipynb script
 
To classify an image, send a POST request to http://localhost:5000/predict, with the image file in the request body.
ex: `curl -X POST -F "image=@/path/to/image.jpg" http://localhost:5000/predict`

The API will respond with a JSON object containing the predicted category.

Still in development:
- creating a docker image
- setting up CI/CD pipeline
