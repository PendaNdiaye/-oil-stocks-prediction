from model.format_df import format_data

from .format_df import format_data
from .process import process_text
from .params_loader import load_transformers_params

import numpy as np

def predict(data):
    # format data
    df = format_data(data)

    # process data
    features = [process_text(s) for s in df.daily_news.values]

    # load vectorizer
    vectorizer = load_transformers_params(model='vec')

    p_features = vectorizer.fit_transform(features).toarray()

    pca_features = 2500
    p_features = np.hstack([p_features, np.zeros((2, pca_features - 462))])


    # load pca 
    pca = load_transformers_params(model='pca')

    p_features_pca = pca.transform(p_features)

    p_features_pca_reduce = p_features_pca[:, 0:40]

    # load reg log
    lg = load_transformers_params(model='lg')

    return lg.predict(p_features_pca_reduce)




