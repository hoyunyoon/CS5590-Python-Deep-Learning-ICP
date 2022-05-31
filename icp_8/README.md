# ICP-8

#### Complete the following:
```
Name: Hoyun Yoon 
Email: hynkz@umsystem.edu
```
---
```
Partner Name: Martin Yap
Partner Email:  may2fn@umsystem.edu
Partner ICP-Link:  https://github.com/UMKC-APL-PythonDeepLearing/icp_8-may2fn
```

```
Video Link: 

```
### SUBMIT PYTHON NOTEBOOK FILE (ipynb files)
<br/>
 
# Write brief explanation here:

<br/>
For the first part of this ICP, we had to analyze the diabetes csv file using a Keras model. The given code showed the initial steps needed to import and preprocess the data as well as how the keras model is used. The given model was then used as a baseline to see how changing parts of the model or data affect the model's accuracy and loss. The first step was to add more dense layers to the model and compare how the accuracy and loss change. We added four more dense layers with different numbers of neurons in each layer. The model was then fitted with the training data and evaluated using the testing data to provide us with its accuracy and loss scores. We found that adding more layers increased the accuracy and decreased the loss, but also noted that increasing the number of layers too high may lead to overfitting. Next, we had to pass the validation data using the fit method. The fitted model was then saved to a new variable. This fitted model was then used to plot the accuracy and loss for the training and validation data. In the plot for accuracy, we saw that the accuracy for both followed a similar trend as epoch increased. The major differences being that testing had lower accuracy and testing had more prominent min max spikes. For the loss plot, the training and testing loss followed similar trends as epoch increased. The major difference between the two being that training had lower loss and testing had bigger min max spikes. Finally, we had to normalize the testing and training data to see how it would affect accuracy. The x datasets were transformed using the standard scaler and saved to new variables. A new model was used and fitted with the scaled data. We then evaluated model with the scaled testing data and compared the loss and accuracy scores. What we found was that scaling the data increased the accuracy and maintained a similar loss value to the original model.  
<br/>
In the second part of this ICP, we had to analyze the Breast Cancer csv file using a Keras model. For this dataset, we followed a similar pattern to how the first part was conducted, however, the dataset needed to be preprocessed first. We first extracted the features from the dataset and placed them into X and y datasets. The y dataset was then sent through a label encoder to transform the B and M values to 0 and 1 values so that the program would be able to read the data. Training and testing datasets were then made using the train_test_split method and a keras model was generated. The model was fitted with the training data and then evaluated to find the accuracy and loss scores to act as a baseline for this part of the ICP. We then added more dense layers to a new model to see how the accuracy and loss would change. In this new model, we add two dense layers with different values for the neurons in the layers. The model was then fitted and evaluated to find the model's accuracy and loss scores. What we found was that accuracy increased and loss decreased when adding more dense layers. However, like as we said in part 1, we must be careful not to overfit the data with the model. Next, we had to add the validation data to the fit method. The model was fitted with the training and validation data and saved to a new variable. This variable was then used to plot the accuracies and losses of the training and testing data. In the accuracy graph, we saw that they both followed similar trends as epoch increased. The major difference between them was that testing had larger min max spikes as epoch increased. For the loss graph, testing and training followed a similar trend as epoch increased. Like the accuracy graph, the testing loss showed more prominent min max spikes as epoch increased. Finally, the data was normalized using the standard scaler and saved to new variables. A new model was then made and fitted with the scaled data. The model was then evaluated with the scaled testing data to get the accuracy and loss scores. What we found was that the scaled model had a lower loss and higher accuracy.

