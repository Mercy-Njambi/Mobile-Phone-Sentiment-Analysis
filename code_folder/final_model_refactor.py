# !pip install contractions
# !pip install transformers
# !pip install nltk
# !pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116

# import nltk

# nltk.download('vader_lexicon', quiet=True)
# nltk.download('all', quiet=True)
# nltk.download('wordnet', quiet=True)
# nltk.download('punkt', quiet=True)
# nltk.download('omw-1.4', quiet=True)
# nltk.download('stopwords', quiet=True)
# nltk.download('tagsets', quiet=True)
# nltk.download('averaged_perceptron_tagger', quiet=True)

# """
# If you don't have the above in your environment, 
# Uncomment them to have them installed/downloaded.
# """

# # Importing relevant libraries
# import pandas as pd
# # import numpy as np

# # from scipy.special import softmax

# # import torch
# import contractions
# # from wordcloud import WordCloud, STOPWORDS


# import re
# # import nltk
# import string
# # import xgboost as xgb
# from nltk import pos_tag
# # from textblob import TextBlob
# # from tqdm.notebook import tqdm
# # from nltk.corpus import stopwords
# # from nltk.probability import FreqDist
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import wordnet
# # from nltk.sentiment import SentimentIntensityAnalyzer
# from nltk.tokenize import word_tokenize #, RegexpTokenizer



# # from transformers import AutoTokenizer
# # from transformers import AutoModelForSequenceClassification



# # from sklearn.model_selection import train_test_split
# from imblearn.over_sampling import SMOTE
# # from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve,accuracy_score
# from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# # from sklearn.naive_bayes import MultinomialNB
# # from sklearn.svm import SVC




# # load our data into the environment
# df = pd.read_csv('./data/Amazon_Combined_Data.csv')

# """"
# from sklearn.preprocessing import FunctionTransformer
# """

# # Data cleaning
# """
# for Deployment purposes
# """
# #   Dropping missing values
# def cleaning_dataset(X):
#     X.dropna(inplace = True)

#     #   Dropping duplicates
#     X.drop_duplicates(inplace = True)

#     # Cleaning Specific columns
#     #Extracting the digits in the Rating column and converting it to an interger type
#     X["Rating"] = X["Rating"].str.extract('(\d+)').astype(int)

#     #Extracting the digits in the price column and converting it to integer
#     X["Price"] = X["Price"].str.extract('(\d+)').astype(int)

#     # Rename the column to brand name
#     X.rename(columns = {"Affiliated Company":"Brand","Brand and Features":"Product_name"},inplace = True)



# # instantiate transformer
# func_transformer_1 = FunctionTransformer(cleaning_dataset)

# # create transformed dataset
# depl_data = func_transformer_1.fit_transform(df)




# """
# for Deployment purposes
# """
# def strip_brand_column(X):
#     word_vocabulary = ['Visit', 'the', 'store', 'Brand:', 'Store']

#     for word in word_vocabulary:
#         X['Brand'] = X['Brand'].str.replace(word, '')

#     # Removing all the white spaces

#     X['Brand'] = X['Brand'].str.strip()

#     # Renaming the amazon renewed with refurbished

#     X['Brand'] = X['Brand'].str.replace('Amazon Renewed','Amazon Refurbished')  


# # instantiate transformer
# func_transformer_2 = FunctionTransformer(strip_brand_column)

# # create transformed dataset
# depl_data = func_transformer_2.fit_transform(depl_data) 



# #removing punctuations from the column
# def feature_engineering(X):
#     X['Product_name'] = X['Product_name'].str.replace(r"\(.*\)","", regex=True)
#     X['Product_name'] = X['Product_name'].str.replace('-',"", regex=True)
#     X['Product_name'] = X['Product_name'].str.replace(',',"", regex=True)
#     X['Product_name'] = X['Product_name'].str.replace('|',"", regex=True)

#     #Splitting the strings in this column into different columns

#     string_cols = X["Product_name"].str.split(" ", n = -1, expand = True)

#     #selecting on the first three words of the string that will form the phone type

#     X["first_word"] = string_cols[8]
#     X["middle_word"] = string_cols[9]
#     X["last_word"] = string_cols[10]

#     #copying the two other columns so as to allow concactination

#     new1 = X["middle_word"].copy()
#     new2 = X["last_word"].copy()
    
#     # concatenating team with name column and overwriting name column

#     X["Model_Type"]= X["first_word"].str.cat(new1, sep =" ")
#     X["Model_Type"]= X["Model_Type"].str.cat(new2, sep =" ")
#     X.drop(["first_word", "middle_word", "last_word"], axis=1, inplace=True)

#     # Removing unnecessary words from the model type column

#     word_vocabulary = ['Smartphone']
#     for word in word_vocabulary:
#         X['Model_Type'] = X['Model_Type'].str.replace(word, '')

# # instantiate transformer
# func_transformer_3 = FunctionTransformer(feature_engineering)

# # create transformed dataset
# depl_data = func_transformer_3.fit_transform(depl_data) 


# # Extract the review dates from the Location and Date of Review Column
# def cleaning_location_and_date_of_review_column(X):
#     X['Location and Date of Review'] = X['Location and Date of Review']\
#     .str.replace('Reviewed in the United States on ', '')


#     # Rename the column to Review Date

#     X.rename(columns = {'Location and Date of Review': 'Review Date'}, inplace = True)

#     # Convert the column into datetime format

#     X['Review Date'] = pd.to_datetime(X['Review Date'], errors = 'coerce')

# # instantiate transformer
# func_transformer_4 = FunctionTransformer(feature_engineering)

# # create transformed dataset
# depl_data = func_transformer_3.fit_transform(depl_data) 


# # Drop rows not in English
# def review_title_and_review(df):
    
#     df = df[df['Review Title'].map(lambda x: x.isascii())]
#     df = df[df['Review'].map(lambda x: x.isascii())]



# def reorder_columns_in_dataframe(df):
#     df = df.reindex(columns=['Product_name', 'Model_Type', 'Brand', 'Price', 'Review Date', 
#                          'Rating', 'Review Title', 'Review'])

#     # removing /n from the texts
#     df['Review Title'] = df['Review Title'].str.strip()
#     df['Review'] = df['Review'].str.strip()

#     # Dropping  unnecessary columns
#     df.drop('Product_name', axis=1, inplace=True)



# def creating_labels_based_on_ratings(rating):

#     if rating <= 2:
#       return 'Negative'
#     elif rating == 3:
#       return 'Neutral'
#     else: 
#       return 'Positive'



# # PREPROCESSING
# # fixing contractions
# def text_contraction(text):
  
#   # creating an empty list
#   expanded_words = []

#   for word in text.split():
#     # using contractions.fix to expand the shortened words
#     expanded_words.append(contractions.fix(word))  
    
#   expanded_text = ' '.join(expanded_words)

#   return expanded_text



# # tokenization
# def tokenize_words(text):
#   # grab all the punctuations
#   punctuation = string.punctuation

#   # lower case our string
#   # text = str([word.lower() for word in t
#   # remove the digits
#   text = re.sub('\d', '', text)

#   # cretae our word tokens
#   tokens = word_tokenize(text)

#   # grab the stop words from stopwords.words('english)
#   # stopwords_list = stopwords.words('english')
#   # stopwords_list += punctuation
#   # stopwords_list = stopwords.words('english') + list(string.punctuation)
#   # stopwords_list += ["''", '""', '...', '``', '..', '....']
#   punctuation_list = list(string.punctuation)
#   punctuation_list += ["''", '""', '...', '``', '..', '....']

#   # remove the stop words
#   clean_list = [word.lower() for word in tokens if word.lower() not in punctuation_list]
  
#   # return a clean tokenized set
#   return clean_list



# # create a function that takes in the nltk POS tags
# # and transforms them to wordnet tags
# def wordnet_pos(word_tag):
#     '''
#     Translate nltk POS to wordnet tags
#     '''
#     if word_tag.startswith('J'):
#         return wordnet.ADJ
#     elif word_tag.startswith('V'):
#         return wordnet.VERB
#     elif word_tag.startswith('N'):
#         return wordnet.NOUN
#     elif word_tag.startswith('R'):
#         return wordnet.ADV
#     else:
#         return wordnet.NOUN



# def word_lemma(text):
#     '''
#     Translate the text POS tags to Word net tags then pass it to the lemmatizer
    
#     '''
#     # inastantiate the lemmatizer
#     lemmatizer = WordNetLemmatizer() 

#     # get the pos tags for the text
#     word_pos_tags = pos_tag(text)
    
#     # translate the pos tags to word net tags
#     word_net_tag = [(text[0], wordnet_pos(text[1])) for text in word_pos_tags]
    
#     # Pass the text with the wordnet tags to the lemmatizer
#     lemma_word = [lemmatizer.lemmatize(text[0], text[1]) for text in word_net_tag]
    
#     return lemma_word



# def tf_vectorization(X_train, X_val):
#     # instaniate the vectorizer
#     tf_vectorizer = TfidfVectorizer(ngram_range=(1,2), max_df = 3000, min_df=2, max_features= 4000)

#     # fit and transform X_train
#     X_train_tf = tf_vectorizer.fit_transform(X_train)

#     # transform the X_val
#     X_val_tf = tf_vectorizer.transform(X_val)

#     return (X_train_tf, X_val_tf)



# def smote_resampling(X_train_tf, y_train):
#     # oversampling
#     smote = SMOTE(random_state=42)

#     # fit smote on the train dataset
#     X_train_resampled, y_train_resampled = smote.fit_resample(X_train_tf, y_train)






