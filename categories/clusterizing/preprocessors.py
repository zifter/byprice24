import re
import string

import pymorphy2
import webcolors
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from ru_stopwords import RU_STOPWORDS

stemmer = SnowballStemmer('russian')
morph = pymorphy2.MorphAnalyzer()


def remove_punctuation(table):
    # TODO: Fix problem with hyphen
    return table.translate(str.maketrans('', '', string.punctuation))


def remove_digits(table):
    return table.translate(str.maketrans('', '', string.digits))


def remove_whitespaces(title):
    return ' '.join([word.strip() for word in title.split()])


def remove_clarification(title):
    return re.sub(r'([\(\[]).*?([\)\]])', r'\g<1>\g<2>', title)


def remove_latin(table):
    # TODO: Fix problem with some words like 'DVD', 'USB', 'SSD'
    return table.translate(
        str.maketrans('', '', string.ascii_lowercase + string.ascii_uppercase)
    )


def remove_colors(steamed_food_names):
    colors = webcolors.CSS3_NAMES_TO_HEX.keys()

    result = []
    for sentence in steamed_food_names:
        words = sentence.split(' ')
        filtered = filter(lambda word: word not in colors, words)
        result.append(' '.join([word for word in filtered]))

    return result


def normalize_words_in_sentence(sentence):
    # TODO: add colors and measure units to RU_STOPWORDS
    token_words = word_tokenize(sentence)

    steamed_sentence = []
    for word in token_words:
        meta = morph.parse(word)[0]
        normal_form = meta.normal_form
        if (normal_form in RU_STOPWORDS) or ('UNKN' in meta.tag):
            continue

        steamed_sentence.append(normal_form)

    return ' '.join(steamed_sentence)
