<div align="center">

# Sentiment Analysis

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Enraged%20Face.png" alt="Enraged Face" width="10%" height="10%" />
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Angry%20Face.png" alt="Angry Face" width="10%" height="10%" />
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Neutral%20Face.png" alt="Neutral Face" width="10%" height="10%" />
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Grinning%20Face%20with%20Smiling%20Eyes.png" alt="Grinning Face with Smiling Eyes" width="10%" height="10%" />
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Beaming%20Face%20with%20Smiling%20Eyes.png" alt="Beaming Face with Smiling Eyes" width="10%" height="10%" />
</div>

> [!CAUTION]
This repository will not actively maintaned but any contribution will be accepted

## Data Mining
The data is collected using the crawling technique from Nitter, an alternative front end to Twitter (X) that can bypass limitations when searching for tweets, and a Python module named ntscraper.

## Data Labeling
Data labeling was done automatically using a collection of sentiment-analysis transformers based on the Indonesian model RoBERTa, which categorizes sentiment into positive and negative groups. Positive groups are data sets that include terms that convey praise, motivation, and encouragement. Meanwhile, negative group is a term that conveys rejection, aggression, and humiliation.

## Data Pre-processing

- Case Folding
  
  To make data more useful, case folding is the process of equating characters into little letters.
  
  Using the lower() function, the code transforms the text data into the same shape.

- Cleaning
  
  After a case folding procedure to generate quality data is completed, the cleaning process will eliminate any unneeded data such as URL links, usernames, empty characters, hashtags, reading marks, and numerals.
  
  The code uses the re library's regular expression to remove superfluous data. The codes (www\.[^\s]+) and (https?://[^ \s] +) are used to remove links starting with https, then there is the code @[^\ s]+ used to delete the username mentioned on a tweet, the code [\s)+ for deleting empty characters, the codes #([^\s]+) for removing hashtag, the rt code for delete retweet marks, and the code \d used to eliminate numbers. Newly cleansed data is saved in the Cleaned table.

- Tokenizing
  
  After removing unnecessary data, a tokenizing process is performed, which breaks sentences into chunks of words by separating them with space characters.
  
  The code uses the word_tokenize library of nltk to divide words based on spacing characters, which are subsequently placed in the tokenized table.

- Normalization
  
  Normalization is the process of correcting terms that do not conform to KBBI (Kamus Besar Bahasa Indonesia). This phase is required since data from Twitter shows that there is still a lot of slang words, necessitating a normalizing technique in order to produce the best results.
  
  The code refers to words from the Colloquial Indonesian Lexicon lexicon, which contains slang words. This code will be repeated for each data point to guarantee that each word is already in accordance with the Great Dictionary of Indonesia. New data with the default word is saved in the Normalized table.

- Stopword Removal
  
  The next phase is stopword removal, which is the process of identifying key words by eliminating words that appear frequently but have no significant significance, such as verbs and particles.
  
  The code removes irrelevant words based on the nltk library's stopword list. This code will be repeated on each data point to ensure that no more stopwords are used, and then the new data is saved in the Stopword table.

- Stemming
  
  After going through the stopword removal phase, the data will proceed to the stemming phase. Stemming is the process of reducing words to their most basic forms in order to improve information accuracy.
  
  To remove existing backups, the code calls the Literary library's StemmerFactory() and StopwordRemoverFactory() functions. The new data containing the base word is saved in the Stemmed table.

- Filtering
  
  Filtering is the process of removing words that are either too short or too long in order to eliminate meaningless terms.
  
  The code will cycle through the input and then eliminate words that are too short or too complex, resulting in terms with more than three letters but fewer than 26.

## Sentiment Analysis
The data is classified using support vector machine modeling. During this stage, the data will be divided using the sklearn library's train_test_split() function.

The SVC is used to access the SVM module and involves the argument kernel as random_state in its operation. The fit() method will be used to store the results of the training data modeling in the classifier, and then the predict() function will be used to predict the testing data using the y_pred label.
