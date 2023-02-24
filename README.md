# FurnitureClassifier

This is a simple Flask API that uses transfer learning to build a neural network model on top of a pretrained model to classify images into three categories: "Chair", "Sofa", and "Bed". The model was trained on a custom dataset consisting of images of furniture items and produces an accuracy score of 79%.

files:
- datahandler.py: used to split dataset into train/test/val directories and resizes the images to a smaller format to prevent overfitting.
- trainer.ipynb: performs data augmentation/transformation and builds the neural network model. Evaluations are also present within file.
- deployment/main.py: flask app containing API call

To classify an image, send a POST request to http://localhost:5000/predict, with the image file in the request body.
ex: `curl -X POST -F "image=@/path/to/image.jpg" http://localhost:5000/predict`

The API will respond with a JSON object containing the predicted category.

Still in development:
- creating a docker image
- setting up CI/CD pipeline
