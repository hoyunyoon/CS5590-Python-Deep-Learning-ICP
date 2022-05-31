# ICP-7

#### Complete the following:
```
Name: Hoyun Yoon 
Email: hynkz@umsystem.edu 
```
---
```
Partner Name: Martin Yap
Partner Email: may2fn@umsystem.edu
Partner ICP-Link: https://github.com/UMKC-APL-PythonDeepLearing/icp_7-may2fn
```

```
Video Link: https://youtu.be/IGQORFfjc1w
```
### SUBMIT PYTHON NOTEBOOK FILE (ipynb files)
<br/>
 
# Write brief explanation here:
<br/>
For the first part of the assignment, we had to use the given text classification notebook to learn more about the different classification models and how basic NLP techniques can be applied to them. The Multinomial Naive Bayes classifier was already made in the notebook file given, and we had to apply the support vector machine (SVM) and k nearest neighbor (KNN) classifiers. For the SVM and KNN classifiers, we fit the classifiers with the tfidf X training dataset and the twenty train dataset from the fetch 20 news groups dataset. The classifiers were then used to predict the results for the tfidf X test dataset. Using the accuracy score method, the accuracies for the classifiers were found using the predictions and the test data from the fetch 20 news groups dataset. Classification reports for each classifier were printed out and used to compare how each classifier performed. To test the bigram and stop words parts of the tfidf vectorizer, we decided to use the Multinomial Naive Bayes classifier since it had a high accuracy and did not take long to fit the model. Using the ngram_range(2, 2) to get the bigrams, we were able to get new X training and X testing datasets to fit the model. Similarly, setting stop_words equal to english, we were able to get new X training and testing datasets. These new datasets were then used on the Multinomial Naive Bayes classifier. The accuracy scores were found and compared to the original to see how it changed.
<br/>
In the second part of the assignment, we had to apply nltk algorithms to a given story that was extracted using the BeautifulSoup library. The text for the story about the fox and the crow was extracted using the given url and the BeautifulSoup library. A list of parameters was used to get the necessary tags to extract from the soup object. Also, the spaces from the beginning and end of text units were removed from the text. With all the preprocessing done, we first tokenized the text into their sentences and words using the sent_tokenize and word_tokenize methods. Next, we cleaned the words dataset to remove all the non-letter elements. The dataset was then tokenized again and then we applied PoS tagging to the new text dataset. We then applied stemming using the porter, snowball, and lancaster stemmers. For each stemmer, we used a for loop to go through each word in the text and printed the stem of the word out to the user. For lemmatization, we looped through all words in the text and sent each of them to the wordnet lemmatizer. The lemma for each word was then displayed to the user. To display the trigrams, we used the ngrams method from the nltk library and sent it the text dataset and the value 3. The trigrams and the number of times each trigram appeared were then shown to the user. We then had to apply named entity recognition to the text. This was done using the ne_chunk, pos_tag, and wordpunct_tokenize methods from the nltk library. The named entities were then shown to the user using a for loop. Finally, we had to plot the word frequencies after removing the stop words from the words dataset. We first removed all the punctuation and the stop words from the words dataset. Then we used the FreqDist method on the dataset and displayed the top ten most common words and the frequency distribution plot for the top ten words.

