# K Nearest Neighbor
Challenge: Got some anonymised data and need to classify it based on last column of data set. The data file is included in this folder. This was part of the Udemy course i am taking to get better at data analysis. Why? Because of creating intelligent robots eventually :smile: :robot:

So i went ahead and looked at the given data through some plotting. Found out that the range of the data is quite big so i had to scale it down for inorder to make the job of the modelling algorithm a bit easier. I used Sklearn libraries on this and StandardScaler was the library in question.

Why we have to scale? From sklearn:

Standardization of datasets is a common requirement for many machine learning estimators implemented in scikit-learn; they might behave badly if the individual features do not more or less look like standard normally distributed data: Gaussian with zero mean and unit variance.

So we Standardize data because of the way the libraries work :smile: The key word here is Gaussian.

Anyway after pre processing the data (standardization) i trained the knn model with a low k value (1). This did not give me good results and led to making a for loop to determine which k value would be good for higher accuracy rates on my model predictions. This graph is what popped out :laughing:

![The data file itself](https://github.com/viltsu123/basic_python_practice/blob/master/data_analysis_learning/KNeighborLearning/error_rate_diff_k.png)

This tells me that the higher i would go with my K value, the lower the errors would get. Actually this bottoms out around K=20 as there is not more variance anymore beyond that point in errors.

So of i went and trained my knn model again and got better results for classification accuracy. The accuracy increased around 10 points so this did the trick.

Learned about this K Nearest Neighbor classification strategy and data preprocessing with python and sklearn libraries :smile:
