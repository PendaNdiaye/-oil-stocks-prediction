import pickle as pickle
import os


REPO_DIR = os.path.dirname(os.path.abspath(''))

MODELS_PARAMS_DIR = os.path.join(REPO_DIR, "model/params")

def load_transformers_params(model='lg'):
    
    if model == 'vec':
            
        # nlp vectorizer
        vectorizer = pickle.load(
            open(
                os.path.join(MODELS_PARAMS_DIR, 'vectorizer.pk'),
                'rb'
                )
            )
        param = vectorizer
  

    elif model == 'pca':

        # pca params
        pca = pickle.load(
            open(
                os.path.join(MODELS_PARAMS_DIR, 'pca.pk'),
                'rb'
                )
            )
        param = pca


    elif model == 'lg':
        # logistic params
        lg = pickle.load(
            open(
                os.path.join(MODELS_PARAMS_DIR, 'lg.pk'),
                'rb'
                )
            )
        param = lg

    else:
        raise NotImplemented('please check your string param')


    return param

