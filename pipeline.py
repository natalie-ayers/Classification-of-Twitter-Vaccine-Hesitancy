import pandas as pd
import gensim
import ast
import gensim.corpora as corpora
from gensim.models import CoherenceModel
from gensim.models.ldamodel import LdaModel
from gensim.models.wrappers import LdaMallet
import matplotlib.pyplot as plt 
import time
import datetime

MALLET_PATH = '/usr/lib/mallet-2.0.8/bin/mallet'

def fit_lda_model(corpus, dict, model, params):
    """

    """

    if model == 'LdaModel':
        lda_model = LdaModel(corpus=corpus,
                        id2word=dict,
                        num_topics=params['num_topics'], 
                        random_state=params['random_state'],
                        update_every=1,
                        chunksize=params['chunksize'],
                        passes=10,
                        alpha=params['alpha'],
                        eta=params['eta'],
                        per_word_topics=True)

    elif model == 'LdaMallet':
        lda_model = LdaMallet(mallet_path=MALLET_PATH,
                        corpus=corpus,
                        id2word=dict,
                        num_topics=params['num_topics'],
                        alpha=params['alpha'],
                        random_seed=params['random_seed']
                        )

    return lda_model
    

def build_corpus_dict(doc_lst, filter_extremes=True, \
    filter_params=(400, 0.8, 1000000)):
    """
    """
    
    b, a, k = filter_params    
    
    id2word_dict = corpora.Dictionary(doc_lst)
    if filter_extremes:
        id2word_dict.filter_extremes(no_below=b, no_above=a, keep_n=k)

    lda_corpus = [id2word_dict.doc2bow(doc) for doc in doc_lst]

    return id2word_dict, lda_corpus

def lda_eval(fitted_model, doc_lst, lda_corpus, id2word_dict, model):
    """
    """

    # Perplexity (lower is better)
    if model == 'LdaModel':
        perplexity_lda = fitted_model.log_perplexity(lda_corpus)
    else:
        perplexity_lda = 'N/A' 

    # Compute Coherence Score (higher is better)
    coherence_model_lda = CoherenceModel(model=fitted_model, texts=doc_lst, \
        dictionary=id2word_dict, coherence='c_v')
    coherence_lda = coherence_model_lda.get_coherence()

    return coherence_lda, perplexity_lda
    
def choose_lda_models(doc_field, n_grams=1,verbose=True):
    """
    Perform manual Grid Search of specified LDA models and parameters and
        store results in dataframe to evaluate
    Inputs:
        doc_field (Series): Pandas Series containing all docs to classify
    Returns (df): a DataFrame containing the results of each model evaluated,
        including LDA Model Type, the Parameters tested, the Time to Train,
        the Coherence, and the Perplexity
    """

    # Config: Dictionaries of models and hyperparameters
    MODELS = {
        'GensimLDA': 'LdaModel'
        , 
        'MalletLDA': 'LdaMallet'
    }

    GRID = {
        'GensimLDA': [{'chunksize': x, 'num_topics': y, \
                        'alpha': a, 'eta': b,'random_state': 100} 
                            for x in (2000) \
                            for y in (5, 10, 15) \
                            for a in (0.1, 0.3, 0.6, 'symmetric') \
                            for b in (0.3, 0.6, 0.8, 1)
                            ]
                            ,
        'MalletLDA': [{'num_topics': y, 'alpha': a, \
                        'random_seed': 100} 
                            for y in (3, 5, 10) \
                            for a in (0.1, 0.3, 0.6, 'symmetric') \
                                ]
    }

    # Initialize results data frame 
    results = pd.DataFrame(columns=['LDA Model', 'Params', \
        'Time Elapsed', 'Coherence', 'Perplexity', 'Topics'])

    # Create list of docs
    if n_grams == 1:
        doc_lst = []
        for doc in doc_field:
            doc_lst.append(ast.literal_eval(doc))
        #print('Created doc_lst', doc_lst[0:8])

    elif n_grams > 1:
        doc_lst = []
        for doc in doc_field:
            doc_lst.append(doc)
    
    # Create dictionary and corpus 
    id2word_dict, lda_corpus = build_corpus_dict(doc_lst)
    #print('dict:',id2word_dict.token2id)
    #print()
    #print('corpus first 5:',lda_corpus[0:5])
    try:
        # Loop over models 
        for model_key in MODELS.keys(): 
            
            # Loop over parameters 
            for params in GRID[model_key]: 
                print("Training model:", model_key, "|", params)
                
                # Begin timer 
                start = datetime.datetime.now()

                # Create model 
                model = MODELS[model_key]
                
                # Fit model on training set 
                fitted = fit_lda_model(lda_corpus, id2word_dict, model, params)
                
                # Show topics 
                topics = fitted.print_topics()
                
                # Evaluate predictions 
                coherence, perplexity = lda_eval(fitted, doc_lst, \
                    lda_corpus, id2word_dict, model)
                
                # End timer
                stop = datetime.datetime.now()
                time_elapsed = stop - start
                print("Time Elapsed:", time_elapsed) 
                #print('Coherence',coherence)
                # Store results in your results data frame 
                results = results.append({'LDA Model': model_key, 
                    'Params': params, 'Time Elapsed': time_elapsed, 
                    'Coherence': coherence, 'Perplexity': perplexity,\
                    'Topics': topics}, \
                        ignore_index=True)
    except:
        return results
    
    return results
