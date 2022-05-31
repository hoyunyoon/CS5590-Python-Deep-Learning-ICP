# ICP-12

#### Complete the following:
```
Name: Hoyun Yoon 
Email:hynkz@umsystem.edu
```
---
```
Partner Name:  Martin Yap
Partner Email: may2fn@umsystem.edu
Partner ICP-Link: https://github.com/UMKC-APL-PythonDeepLearing/icp_12-may2fn
```

```
Video Link: https://youtu.be/f3vRmuvBAFc
```
### SUBMIT PYTHON NOTEBOOK FILE (ipynb files)
<br/>
 
# Write brief explanation here:

<br/>
For this ICP, we are implementing sentiment analysis and transfer learning. With sentiment analysis, we are using two dataset files called Sentiment.csv and spam.csv. We first used the Sentiment.csv to understand how the dataset should be preprocessed before creating the training and testing datasets. To preprocess the dataset, we kept only the necessary columns, converted all the text to lowercase, removed all non-alphanumeric characters, removed the rt at the start of all the texts, and removed all the stop words. From there, we could tokenize the text and turn the text into sequences. A keras model was then built using an embedding layer as the input layer, an LSTM layer, and a dense layer for the output layer. The model was compiled with categorical cross entropy as the loss method, adam as the optimizer, and accuracy as our metric.
<br/><br/>
The sentiment column from the dataset was encoded and then one-hot encoded to form our y values. Using the train_test_split method with the text sequences and one-hot encoded labels, we formed the training and testing datasets with a test size of 0.33. The model was then fitted with the training data over seven epochs. Once the model was fitted with the data, it was evaluated using the testing data and we found the model had an accuracy of about 65% and a loss value of 1.00. This high loss value indicates a high summation of error with the model.
<br/><br/>
The model was then saved and reloaded into a new model variable. New text was then implemented and processed in a similar manner to the Sentiment.csv dataset. The reloaded model's predict method was then used to identify which sentiment the model thought best fit the text. Looking at how the model categorized the sentiment labels, we were able to identify that the model predicted that the text had a positive sentiment label.
<br/><br/>
The spam dataset was then loaded into the notebook using latin-1 encoding and preprocessed the same way the sentiment dataset was preprocessed. The text data was then tokenized, converted into sequences, and padded to the same length. A model using the same layout as the sentiment model was made and compiled. The labels for the text data were encoded and then one-hot encoded. Training and testing datasets were made with the train_test_split using the sequences and labels. The model was fitted with the training data and then evaluated using the testing data. The accuracy and loss scores of the model were then displayed to show it had an accuracy of 98% and loss of 8%. This indicates that the model is very accurate and has little errors.  
<br/><br/>
For the transfer learning portion of the ICP, we brought in the model and dataset we used in ICP 10. The image dataset was preprocessed to get the training and testing datasets that would be implemented with the model. The model with the callbacks from ICP 10 was implemented and remodeled a bit to adjust the output of the model. The model layers were then frozen to allow the model to be implemented to the new model. Using the old model as the input layer, a new model was made that implemented more dense and dropout layers. After compiling the model, it was fitted with the training data. The model was then used to predict the first five images, and the prediction was displayed along with the actual labels. Looking at the prediction and actual labels, we could see that the model was not very accurate and was mislabeling the images as the wrong classes.
<br/><br/>
The model from ICP 10 had a couple layers unfrozen and was then used to form another model. The layer layout for the new model was the same as the layout used for when the ICP 10 model had all its layers frozen. After compiling the model, the model was fitted with the training data and used to identify the first five images in the testing dataset. The prediction and actual labels were then displayed to show how accurate the prediction was. Based on the prediction of the first five images, we saw that the model was not very accurate and would only be correct sometimes for the images.
