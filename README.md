# Clothize-ML

This is repo for body measurement feature in CLothize app.
This feature is using CNN model to predict keypoints from human image. The output from model is an array with 3k lenght, where k is number of keypoints. The first two is location on x and y and the third is visibility. The output then subracted with corresponding keypoints to get body measurement that used to make clothes.

## About Clothize
Clothize is our product for Product-based capstone project in Bangkit Academy 2023 Batch 2

## Dataset
We use fixed clothing size prediction dataset. The edited dataset is in csv file in. The original dataset is in <a href="https://www.kaggle.com/datasets/tourist55/clothessizeprediction" taget='blank'>this kaggle dataset</a>.
