from dataclasses import dataclass
from pathlib import Path
from typing import List

import yaml
from common.paths import FIXTURES_DIR


@dataclass
class Category:
    name: str
    keywords: List[str]


def _load_categories(p: Path):
    with open(p, encoding='utf8') as f:
        result = yaml.safe_load(f)

    category_by_name = {}
    for r in result['categories']:
        if r['name'] in category_by_name:
            raise ValueError('category is duplicated %s', r['name'])

        category_by_name[r['name']] = Category(**r)

    return category_by_name


def get_category(name: str) -> Category:
    if name in _CATEGORIES:
        return _CATEGORIES[name]

    raise ValueError(f'Failed to find category {name}')


_CATEGORIES = _load_categories(FIXTURES_DIR / 'categories.yaml')
