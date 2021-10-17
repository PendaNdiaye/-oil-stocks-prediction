from model.format_df import format_data

from .format_df import format_data
from .process import process_text
from .params_loader import load_transformers_params

import numpy as np

def predict(data): #transforme les données, 
    # format data
    df = format_data(data)

    # process data #processing
    features = [process_text(s) for s in df.daily_news.values]

    # load vectorizer 
    vectorizer = load_transformers_params(model='vec')

    p_features = vectorizer.fit_transform(features).toarray()
    print(p_features.shape)

    

    p_features_cols = p_features.shape[1]
    #max_features_output = p_features.shape[1]
    max_features_output = 2500


    p_features = np.hstack([p_features, np.zeros((p_features.shape[0], max_features_output - p_features_cols))])


    # load pca 
    pca = load_transformers_params(model='pca')

    p_features_pca = pca.transform(p_features)

    p_features_pca_reduce = p_features_pca[:, 0:40]

    # load reg log
    lg = load_transformers_params(model='lg')

    return lg.predict(p_features_pca_reduce)




