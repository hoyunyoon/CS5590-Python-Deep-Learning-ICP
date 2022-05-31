# ICP-6

#### Complete the following:
```
Name: Hoyun Yoon
Email: hynkz@umsystem.edu
```
---
```
Partner Name: Martin Yap
Partner Email: may2fn@umsystem.edu
Partner ICP-Link: https://github.com/UMKC-APL-PythonDeepLearing/icp_6-may2fn
```

```
Video Link: (if not submitting in class)   https://youtu.be/B1fTDmMYmL4
```
### SUBMIT PYTHON NOTEBOOK FILE (ipynb files)

<br/>
 
# Write brief explanation here:
<br/>
For the first question, we had to analyze the house_dataset.csv. We first had to identify and delete the outlier data in the GarageArea field by making a scatter plot and then dropping the outlier data. Next, we created a regression model with the SalePrice and OverallQual features and plotted their regression line. We then found the top five most correlated features to SalePrice and built a regression model with those features. Afterwards, we applied PCA on the same dataset and made a new regression model using the PCA result. The models were then evaluated using MAE, MSE, RMSE, and R2 score.
<br/> <br/>
In the second question, we analyzed the credit_card.csv. For preprocessing, we had to remove all the null values with the mean of that column. The elbow method was then used to identify a good k value to used for the KMeans algorithm. Once the KMeans model was made, we calculated the silhouette score for the model. Feature scaling was then done on the dataset and a new KMeans model was built using the scaled dataset. The silhouette score was calculated for the model and compared to the original value to see if there was any improvement. Finally, PCA was applied to the original dataset and that result was used to make another KMeans model. The model's silhouette score was then calculated and compared to see if there was any improvement.
