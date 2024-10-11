import regex
import warnings

from datasets import load_dataset

def get_datasets():
    ds_corpus = load_dataset("clarin-knext/fiqa-pl", "corpus")
    ds_queries = load_dataset("clarin-knext/fiqa-pl", "queries")
    return ds_corpus, ds_queries

def main(): 
    warnings.filterwarnings("ignore")

    ds_corpus, ds_queries = get_datasets()

if __name__ == "__main__":
    main()