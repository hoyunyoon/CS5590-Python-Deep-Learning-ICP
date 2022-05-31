# ICP-9

#### Complete the following:
```
Name: Hoyun Yoon 
Email: hynkz@umsystem.edu 
```
---
```
Partner Name: Martin Yap 
Partner Email: may2fn@umsystem.edu
Partner ICP-Link:  https://github.com/UMKC-APL-PythonDeepLearing/icp_9-may2fn
```

```
Video Link: https://youtu.be/yRARFX616mw

```
### SUBMIT PYTHON NOTEBOOK FILE (ipynb files)
<br/>
 
# Write brief explanation here:
<br/>
For this ICP, we learned more about the sequential and functional API models using the MNIST dataset. The first task we had to complete was changing the number of hidden layers and the activation function of the original sequential model. In the new sequential model, we changed the activation method from relu to tanh and added 3 more hidden layers to the model with different neuron counts. When we fitted and evaluated the model, we found that the model had a lower accuracy and lower loss compared to the original. We then had to plot the loss and accuracy for the training and testing data of the history object. When we plotted the accuracy and loss, we saw that the training data had smooth curves and easy to distinguish plateaus; while the testing data showed similar behavior in the beginning for both accuracy and loss but was more scattered and showed prominent min and max points. The next task was to run a model without scaling the images to see how the accuracy would be affected. This was achieved by saving the reshaped data to new variables and using those variables in the place of the scaled data. When we ran the model, we found that the model had a lower accuracy and a higher loss compared to the original. Next, we had to convert the sequential model to a functional API model. To make the functional API model, we made the input layer, the two hidden layers, and the output layer and used the keras Model method to form the model. The model was then fitted and evaluated to find its accuracy and loss. What we found was that the functional model had a similar accuracy and a slightly lower loss compared to the original sequential model. Finally, we had to plot an image from the test data and do inferencing to check the model's prediction on the image. For this task, we displayed the image we were using and then used the predict method and the numpy argmax method to identify the model's prediction. The predict_classes method was not working when we were running the code, so we opted to use the predict and argmax methods to get the model's prediction.
<br/><br/>
In the extra credit portion of this ICP, we first had to use the sparce categorical cross entropy loss method and identify why we were receiving an error as well as how to overcome this error. When we ran the code, we saw that it produced an invalid argument error. We identified that this was due to the one-hot encoding labels not fitting the criteria for the sparse categorical cross entropy method since it is expecting integers and the one-hot encoding labels are floats. To overcome this error, we used the test_train_split method to get our labels rather than using the to_categorical method. We also had to add a flatten layer to the model since the input shape for the images was 28 by 28. From there, the model was able to be fit and evaluated to obtain the loss and accuracy. For the second part of the extra credit, we had to use a method from the numpy library to print the correct class from the model prediction. To print the correct class from the model's prediction, we have to use the numpy's argmax method. The prediction of the model is sent to the argmax method to identify the maximum value of the prediction array, which identifies the class the model believes the image is depicting.
