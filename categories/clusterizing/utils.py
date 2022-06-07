from typing import List

import numpy as np
import pandas as pd


def get_titles_from_file(filename='onliner.csv') -> List[str]:
    df = pd.read_csv(filename, delimiter=',')
    return df['title']


def get_matrix(row_titles, X, vectorizer):
    return pd.concat(
        [
            row_titles,
            pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out()),
        ],
        axis=1,
    )


def get_labelled_cluster(result):
    clusters = result['cluster'].unique()
    labels = []
    for i in range(len(clusters)):
        subset = result[result['cluster'] == clusters[i]]
        words = ' '.join(
            [
                x
                for x in np.where(subset.all() != 0, subset.columns, None)
                if x and x != 'title' and x != 'cluster' and len(x.split()) == 1
            ]
        )
        labels.append(words)
    labels_table = pd.DataFrame(zip(clusters, labels), columns=['cluster', 'label'])
    return pd.merge(result, labels_table, on='cluster', how='left')


def save_result_to_csv(labelled_cluster, result_filename='out.csv'):
    df = pd.DataFrame(labelled_cluster[['title', 'label']])

    out_filename = f'results/{result_filename}'

    df.to_csv(path_or_buf=out_filename, index=False)
