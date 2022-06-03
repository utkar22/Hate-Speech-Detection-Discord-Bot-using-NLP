'''This python script trains two NLP models, model_hate and model_offensive, on
hate and offensive speech data
The .csv file is read using Pandas. The data contains 3 columns:
hate, offensive, tweet. Hate and Offensive contains score out of 3 on the
hatefulness and offensiveness of the respective tweet. model_hate and
model_offensive are trained on these tweets and scores using a
Stochastic Gradient Descent Pipeline.
'''

import pandas as pd
import pickle
from sklearn.utils import resample
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score


def train_models():
    '''This function trains the models on hate and offensive speech data.'''
    
    datafile = pd.read_csv("hate_speech.csv")

    datafile_majority = datafile[datafile.offensive == 0]
    datafile_minority = datafile[datafile.offensive > 0]

    #Since hatefull and offensive comments are a minority, the offensive tweets
    #are repeated to upsample the amount of offensive tweets, to better train
    #the model
    datafile_minority_upsampled = resample(datafile_minority, replace = True, n_samples = len(datafile_majority), random_state = 123)
    datafile_upsampled = pd.concat([datafile_majority, datafile_minority_upsampled])

    pipeline_sgd = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf',  TfidfTransformer()),
        ('nb', SGDClassifier()),])

    x_train_hate, x_test_hate, y_train_hate, y_test_hate = train_test_split(datafile_upsampled["tweet"], datafile_upsampled["hate"])
    x_train_offensive, x_test_offensive, y_train_offensive, y_test_offensive = train_test_split(datafile_upsampled["tweet"], datafile_upsampled["offensive"])

    model_hate = pipeline_sgd.fit(x_train_hate, y_train_hate)
    model_offensive = pipeline_sgd.fit(x_train_offensive, y_train_offensive)

    return model_hate, model_offensive

def store_models(model_hate, model_offensive):
    '''This function serializes the two models in binary format using the pickle
    library'''
    pickle.dump(model_hate, open("model_hate.sav","wb"))
    pickle.dump(model_offensive, open("model_offensive.sav","wb"))


model_hate, model_offensive = train_models()
store_models(model_hate, model_offensive)





