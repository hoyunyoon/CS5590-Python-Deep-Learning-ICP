# ICP-10

#### Complete the following:
```
Name: Hoyun Yoon
Email: hynkz@umsystem.edu 
```
---
```
Partner Name: Martin Yap  
Partner Email: may2fn@umsystem.edu
Partner ICP-Link: https://github.com/UMKC-APL-PythonDeepLearing/icp_10-may2fn
```

```
Video Link:  https://youtu.be/nCOvijgRbcc
```
### SUBMIT PYTHON NOTEBOOK FILE (ipynb files)
<br/>
 
# Write brief explanation here:  
For this ICP, we are implementing image classification with Convolutional Neural Network (CNN). Before doing the tasks for the ICP, we had to load the cifar10 dataset and preprocess the training and testing datasets for the model. The first task had us create a sequential model using a given layer layout that uses convolutional, dropout, max pooling, dense, and flatten layers. The sequential model was fitted with the training dataset and evaluated using the testing dataset. A functional API model was then created using the same layout and evaluated to see if there were any performance changes between the models. Comparing the performances of the two models, we found that they produced similar results with the functional model having a slightly higher accuracy and lower loss. These models were then saved so that we did not need to refit the models because compiling and fitting the models took roughly 2 hours each.
<br/><br/>
Next, we had to apply specified callbacks to the model. The callbacks were saved to different variables and stored in a list. This list was then used with the callbacks parameter in the fit method for the model we chose to continue using for the rest of the ICP. After fitting the model with the callbacks, the model was saved as a h5 file. We then had to predict the first four images of the test data and print their actual labels. The predicted classes were found using the predict and argmax methods. By printing out the variable that is holding the result of the argmax method, we can see the predictions of the model. Printing out the images and their labels, we found that the model was able to correctly predict all the classes of the images.
<br/><br/>
Finally, we had to create our own dataset with images we found on the internet. For our dataset, we chose to find images of transportation vehicles people would use. The dataset has ten different classes. The google drive folder holding these images is split into train and test folders in a way for the validation split to be equal to 20 percent. After preprocessing the datasets, the model was compiled and fit with the training dataset. The training and validation accuracy were then plotted on a graph to see how they change as epoch increases. The training accuracy increased as epoch increased and eventually started to plateau when reaching 1.0. The validation accuracy remained stagnant at a low accuracy and did not show much change as epoch increased. We then saved the model and used it to predict images in the test dataset. Due to the model not being accurate with the test dataset, majority of its predictions were wrong. We were able to identify that the model was able to predict a few correct classes, but the training and testing datasets should be increased for better results.
