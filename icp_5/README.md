# ICP-5

#### Complete the following:
```
Name: Hoyun Yoon 
Email: hynkz@umsystem.edu
```
---
```
Partner Name:  Martin Yap
Partner Email: may2fn@umsystem.edu
Partner ICP-Link: https://github.com/UMKC-APL-PythonDeepLearing/icp_5-may2fn

```
### SUBMIT PYTHON NOTEBOOK FILE (ipynb files)

```
Video Link: (if not submitting in class)   https://www.youtube.com/watch?v=VqfunYbi5WE
```
<br/>
 
Write brief explanation here:
<br/>
In the first question, we had to analyze the Titanic dataset. We first checked the data for any NaN values and checked the correlation between the survived and sex columns, which showed a high correlation between the two data columns. Some of the data was then visualized and removed if found to be unnecessary for training and testing the model. The remaining column data was then encoded and NaN values were replaced with the column's mean value. The final training and testing data sets for x and y were then formed and used to fit the svm, naive bayes, and knn models. Their predictions on the x test data set were then compared to the actual y test data set to find the accuracy score of each model. Once we had the accuracy scores, we printed out the confusion matrix for each model using the y test data and the y prediction data of the respective model.
<br/>
For the second question, we were tasked with analyzing the handwritten digits data set. Once the models and data set were initalized, we visualized some of the images in the data set, as well as analyze some of the details in the data set like the shape and target names. The training and testing datasets were then made using the train_test_split method with a test size of 0.5. The training sets and the x test set were then used to find the y prediction data set for the svm, knn, and naive bayes models. The y prediction data set was then used to find the accuracy score and the classification report of the model using the y test data set for each of the models. Next, we evaluated an image by flattening the image 9 and had all the models predict what class it belonged to. Once we saw their predictions, we visualized what the actual number was to see which models were able to correctly identify the number. Finally, we had to identify the best k value for the knn model. To do this, we went through a range from 1 to 49 for the n_neighbors variable in the KNN classifieer and found each k value's accuracy score. The accuracy scores were then plotted on a graph to help identify the best k value.
