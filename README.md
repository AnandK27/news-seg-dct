# Newspaper Segmentation using DCT Images

This implementation uses fully convolutional neural network for Newspaper Segmentation in JPEG domain.

* Uses Manually created dataset of newspaper including RGB image and the ground truth masked image for training and validation for classification regions of newspaper on text, picture and background areas. It contains 290 images of English newspapers. There are 4 classes: Article area, picture area, background, Heading .

* Image used in this implementaion is a DCT transformed image for input image and RGB masked image of the dataset.
