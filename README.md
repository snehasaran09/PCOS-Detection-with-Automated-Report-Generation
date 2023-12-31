# PCOS-Detection-with-Automated-Report-Generation
This project employs a probabilistic approach to detecting Polycystic Ovary Syndrome (PCOS) through the analysis of ovarian ultrasound images.

This project begins with the augmentation of acquired ovarian ultrasound datasets. From 100 infected images and 1300 normal ovary images, we have created a dataset of roughly 7500 infected and 7500 normal ovary images. The images were segmented using a watershed algorithm and three models were employed. The Bayesian CNN + XGBoost model gave us the highest accuracy which was used in automating the report generation process by providing a numerical value of the probability of each image being PCOS infected and the histogram for the same. 
