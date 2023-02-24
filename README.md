# FurnitureClassifier

This is a simple Flask API that uses a pre-trained deep learning model to classify images into three categories: "Chair", "Sofa", and "Bed". The model was trained on a custom dataset consisting of images of furniture items and produces an accuracy score of 79%.

To classify an image, send a POST request to http://localhost:5000/predict, with the image file in the request body.
ex: `curl -X POST -F "image=@/path/to/image.jpg" http://localhost:5000/predict`

The API will respond with a JSON object containing the predicted category.

Still in development:
- creating a docker image
- setting up CI/CD pipeline
