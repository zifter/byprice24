from dataclasses import dataclass
from typing import Optional

import pandas as pd
from fuzzywuzzy import fuzz
from sklearn.base import BaseEstimator
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


@dataclass
class VectorizationResult:
    x: 'Sparse matrix of (n_samples, n_features)'  # noqa: F722
    method_name: str
    vectorizer: Optional[BaseEstimator]


def vectorize_cv(final_dataset: pd.DataFrame):
    vectorizer_cv = CountVectorizer(analyzer='word')
    x = vectorizer_cv.fit_transform(final_dataset)
    return VectorizationResult(x=x, vectorizer=vectorizer_cv, method_name='cv')


def vectorize_wtf(final_dataset: pd.DataFrame):
    vectorizer_wtf = TfidfVectorizer(analyzer='word')
    x = vectorizer_wtf.fit_transform(final_dataset)
    return VectorizationResult(x=x, vectorizer=vectorizer_wtf, method_name='wtf')


def vectorize_ntf(final_dataset: pd.DataFrame):
    vectorizer_ntf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2))
    x = vectorizer_ntf.fit_transform(final_dataset)
    return VectorizationResult(x=x, vectorizer=vectorizer_ntf, method_name='ntf')


def vectorize_fuzzywuzzy(final_dataset: pd.DataFrame):
    # TODO: integrate fuzzywuzzy
    x = pd.crosstab(
        [list(range(len(final_dataset))), final_dataset], final_dataset
    ).apply(
        lambda col: [
            fuzz.token_sort_ratio(col.name, x) for x in col.index.get_level_values(1)
        ]
    )
    return VectorizationResult(x=x, vectorizer=None, method_name='fuzzywuzzy')
