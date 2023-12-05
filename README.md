# Clothize-ML

This is repo for body measurement feature in CLothize app.
This feature is using CNN model to predict keypoints from human image. The output from model is an array with 3k lenght, where k is number of keypoints. The first two is location on x and y and the third is visibility. The output then subracted with corresponding keypoints to get body measurement that used to make clothes.

## About Clothize
Clothize is our product for Product-based capstone project in Bangkit Academy 2023 Batch 2

## Dataset
We use keypoints only part from COCO Dataset, where we copy from from COCO dataset to our kaggle dataset. The keypoint-only dataset is in <a href="https://www.kaggle.com/datasets/asad11914/coco-2017-keypoints/data" taget='_blank'>this kaggle dataset</a>.
If you want to see the original COCO dataset, you can visit <a href='https://cocodataset.org' taget='_blank' >this link</a>
