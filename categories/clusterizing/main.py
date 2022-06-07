from dataclasses import dataclass
from typing import List
from typing import Union

import pandas as pd
import vectorizers
from constants import INPUT_FILENAME
from constants import N_CLUSTERS
from constants import RESULT_FILENAME
from loguru import logger
from pandas import DataFrame
from pandas import Series
from preprocessors import normalize_words_in_sentence
from preprocessors import remove_clarification
from preprocessors import remove_digits
from preprocessors import remove_latin
from preprocessors import remove_punctuation
from preprocessors import remove_whitespaces
from sklearn.cluster import KMeans
from utils import get_labelled_cluster
from utils import get_titles_from_file
from utils import save_result_to_csv


@dataclass
class Cluster:
    result: Union[Series, DataFrame]
    method_name: str


def vectorize_words(row_titles: List[str], final_dataset: DataFrame, n_clusters=1000):
    vec_result = vectorizers.vectorize_cv(final_dataset)

    x = vec_result.x

    k_means = KMeans(n_clusters=n_clusters)
    k_means.fit(x)

    matrix = pd.DataFrame(
        x.toarray(), columns=vec_result.vectorizer.get_feature_names_out()
    )

    result = pd.concat([row_titles, matrix], axis=1)
    result['cluster'] = k_means.predict(x)
    return Cluster(result=result, method_name=vec_result.method_name)


def get_final_dataset(row_titles):
    # 2.1 Prepare data
    cleaned_titles = [
        remove_latin(
            remove_whitespaces(
                remove_digits(remove_punctuation(remove_clarification(x)))
            )
        )
        for x in row_titles
    ]

    logger.info(f'Parsed {len(cleaned_titles)} titles')

    # 2.2 Normalize words. Remove some adj (colors, ...)

    return pd.Series([normalize_words_in_sentence(x) for x in cleaned_titles])


if __name__ == '__main__':
    # 1. Read data
    input_filename = INPUT_FILENAME
    row_titles = get_titles_from_file(filename=input_filename)

    logger.info(f'Read {len(row_titles)} titles from {input_filename}')

    # 2. Prepare dataset
    final_dataset = get_final_dataset(row_titles)

    logger.info(f'Normalized {len(final_dataset)} titles')

    # 3. Vectorize and group words
    n_clusters = N_CLUSTERS

    logger.info(f'Start vectorizing and grouping. Number of clusters: {n_clusters}')

    vec_result = vectorize_words(
        row_titles=row_titles, final_dataset=final_dataset, n_clusters=n_clusters
    )

    labelled_cluster = get_labelled_cluster(vec_result.result)

    logger.info(f'Get {len(labelled_cluster)} labelled clusters')

    # 4. Save to result file
    result_filename = RESULT_FILENAME.format(
        method_name=vec_result.method_name, n_clusters=n_clusters
    )
    save_result_to_csv(labelled_cluster, result_filename=result_filename)

    logger.info(f'Result was saved to file {result_filename}')
