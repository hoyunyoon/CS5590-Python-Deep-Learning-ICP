# ICP-11

##### [Dataset Link](https://umkc.app.box.com/s/znrabf69ksd4hkkpvj3r8ibo06lwuwlg)

#### Complete the following:
```
Name: Hoyun Yoon 
Email: hynkz@umsystem.edu 
```
---
```
Partner Name: Martin Yap
Partner Email: may2fn@umsystem.edu
Partner ICP-Link:  https://github.com/UMKC-APL-PythonDeepLearing/icp_11-may2fn
```

```
Video Link:  https://youtu.be/oSXKIi8iyOg
```
### SUBMIT PYTHON NOTEBOOK FILE (ipynb files)
<br/>
 
# Write brief explanation here:

In this ICP, we are learning more about sequential keras models and using the embedding layer. The first task of the ICP was to identify mistakes in the model code given in the PowerPoint slides and explaining why they need to be corrected. We were able to identify four mistakes within the given code. One mistake was not defining the input_dim variable. This needs to be corrected since it is being used to define the input dimensions of the model. Another mistake was the number of neurons used in the last layer of the model since the model would be making classifications that may not be applicable to the dataset. The next mistake was the activation function used for the output layer. Softmax is used when more than two classes are present in the classification, but the dataset we are working with only has the neg and pos classifications. The last mistake in the code we found was the loss method being used. Sparse categorical crossentropy needs to be changed since the labels we are using are one-hot encoded and we are only identifying if the review is negative or positive. After identifying these mistakes, we created a model that we believe resembled a corrected version of the model code.
<br/><br/>
The next task of the ICP was to remove the "unsup" labeled reviews from the dataset. We used the loc method to identify and save all the reviews that were not labeled with "unsup." The unique method was then used to identify that the only labels in the dataset were neg and pos. We then had to filter the dataset by removing the punctuation characters, turning all the reviews to lowercase, and stemming all the words to their roots. For filtering punctuation characters, we accessed the reviews column and removed all the punctuation characters by replacing them with blank spaces. With the casing, we accessed the reviews column and used the lower method for the text to make the reviews all in lowercase. To reduce the words to their root, we word tokenized the reviews and then used the porter stemmer to stem all the words in the reviews.  
<br/><br/>
The fourth part of the ICP had us add the embedding layer to the model and compare how it performed against the original. Before making the new model, we had to preprocess the dataset into new training and testing sets since we cleaned and filtered it in the previous problems. During the preprocessing of the data, we also defined the variables needed for the embedding layer. After we created the new training and testing sets, we added the embedding layer to the model code. With the embedding layer, we used the vocab size and the max review length we identified while creating the new training and testing sets for the input dimension and length, respectively. A flatten layer was then added after the embedding layer and we adjusted the number of neurons in the dense layer to ensure that the embedding and dense layers would be compatible with each other. A copy of the original model was also made to work with the new training and testing sets. After fitting and evaluating the models, we found that adding the embedding layer did not really help improve accuracy. There were some runs of the code where the model with the embedding layer did improve the accuracy and was experiencing overfitting, but it was infrequent, and we saw it having lower accuracy and underfitting more. The next part of the ICP had us identify if the model was experiencing underfitting or overfitting. For both the original and embedding models, we found that they both experienced underfitting since they both performed poorly in the fitting and evaluating processes. When the embedding model did achieve higher accuracies, it was experiencing overfitting since it achieved high accuracies during the fitting process, but a lower accuracy during the evaluating process. We later explain in part six of the ICP that overfitting can be prevented by using the early stopping callback or the shuffle parameter to help prevent the model from just memorizing the data.
<br/><br/>
With part six of the ICP, we had to apply the code to the 20_newsgroup dataset. When importing the dataset, we chose to use only two of the categories, which were the alt.atheism and soc.religion.christian categories. We also defined the variables we would be using for the embedding layer to process this new data. The dataset was then preprocessed in a similar manner as to how the previous dataset was processed to obtain the new training and testing sets. A new model was also made to use the variables we defined earlier and to be able to use the training and testing sets for the 20_newsgroup dataset. After fitting and evaluating the model, we found that the model was experiencing overfitting since the model was achieving high accuracies in the fitting process and obtained a lower accuracy in the evaluating process. Part seven of the ICP had us predict over one sample of the data and check if its prediction was correct or not. For this, we used the sample at index 3 of the 20_newsgroup testing set. We had to reshape the sample to be able to have the model predict its class. After identifying the model's prediction, we compared it to the actual label found in the y test set and saw that the model was able to correctly guess the class.
<br/><br/>
The extra credit for this ICP wanted us to add a convolution and max pooling layer to the model. In this portion, we used the Conv1D and MaxPooling1D layers and they were added between the embedding layer and the flatten layer. The model was then trained and evaluated to ensure the model would be able to work with these two new layers added to the model. After evaluating the model, we found that the model was experiencing overfitting since the model achieved a lower accuracy during evaluation compared to the accuracies it was achieving in the fitting process.
```

```
