from argparse import ArgumentParser
from typing import Dict
from typing import List
from typing import Optional

import yaml
from bs4 import BeautifulSoup
from shared import BACKEND_FIXTURES_DIR
from shared import DATA_DIR
from transliterate import translit

SERVICE_WORDS = {'и', 'под', 'над', 'на', 'для', 'по', 'к', 'за'}


def get_context():
    parser = ArgumentParser()
    parser.add_argument('--source-file', default=DATA_DIR / 'onliner-25-01-2022.html')
    parser.add_argument('--output-file', default=BACKEND_FIXTURES_DIR / 'categories.yaml')
    return parser.parse_args()


def merge_categories(result, prev_result):
    return result


class CategoryExtractor:
    @staticmethod
    def get_top_category_id(tag):
        if not tag.has_attr('data-id'):
            return None

        category_id = tag.attrs['data-id']
        if not category_id.isnumeric():
            return None

        return category_id

    @staticmethod
    def get_name(raw, title):
        if 'url' in raw:
            return raw['url'].split('/')[-1].split('?')[0]

        return translit(title, 'ru', reversed=True).replace('\'', '').replace(' ', '-').replace(',', '').lower()

    @staticmethod
    def get_keywords(title):
        base = title.lower()
        keywords = [base]
        words = set(base.replace(',', ' ').replace('-', ' ').replace('(', '').replace(')', '').split()) - SERVICE_WORDS
        keywords.extend(words)
        return sorted(list(set(keywords)))

    @staticmethod
    def create_category(raw, parent):
        title = raw['title'].replace('\xa0', ' ')
        return {
            'name': CategoryExtractor.get_name(raw, title),
            'ru': title,
            'parent': parent['name'] if parent else None,
            'keywords': CategoryExtractor.get_keywords(title),
        }

    @staticmethod
    def to_category_fixtures(raw_categories: List[Dict], parent: Optional[Dict] = None, deep=0) -> List[Dict]:
        result: List[Dict] = []
        # raw_categories.sort(key=lambda c: c['title'])
        for raw in raw_categories:
            print(deep * '  ' + raw['title'] + ' ' + str(raw.get('url')))

            parent = CategoryExtractor.create_category(raw, parent)
            child = CategoryExtractor.to_category_fixtures(raw.get('child', []), parent, deep + 1)
            if child:
                parent['child'] = child
            result.append(parent)

        return result

    def parse(self, source_file) -> List[Dict]:
        cache: Dict[str, Dict] = {}

        with open(source_file) as f:
            data = f.read()
            soup = BeautifulSoup(data)

            top_categories = soup.findAll('li', class_='catalog-navigation-classifier__item')
            for category in top_categories:
                top_category_id = CategoryExtractor.get_top_category_id(category)
                if not top_category_id:
                    continue

                category_title = category.find_all('span', class_='catalog-navigation-classifier__item-title-wrapper')

                cache[top_category_id] = {'data-id': top_category_id, 'title': category_title[0].get_text(strip=True)}

            top_categories = soup.findAll('div', class_='catalog-navigation-list__category')
            for top_category in top_categories:
                top_category_id = CategoryExtractor.get_top_category_id(top_category)
                if not top_category_id:
                    continue

                result_categories = []
                categories = top_category.find_all('div', class_='catalog-navigation-list__aside-item')
                for category in categories:
                    category_title = category.find_all('div', class_='catalog-navigation-list__aside-title')

                    sub_categories = category.find_all('a', class_='catalog-navigation-list__dropdown-item')

                    result_sub_categories = []
                    for sub_category in sub_categories:
                        href = sub_category.attrs['href']
                        title = sub_category.find('span', class_='catalog-navigation-list__dropdown-title').get_text(
                            strip=True)
                        result_sub_categories.append({
                            'url': href,
                            'title': title,
                        })

                    result = {'title': category_title[0].get_text(strip=True), 'child': result_sub_categories}

                    result_categories.append(result)

                cache[top_category_id]['child'] = result_categories

        return CategoryExtractor.to_category_fixtures(list(cache.values()))


class CategoryTransform:
    def __init__(self, categories: List[Dict]):
        self._cs = categories

    def transform(self) -> Dict:
        filtered = []
        for c in self._cs:
            if c['ru'] in ('Еда',):
                continue

            filtered.append(c)

        filtered.append({
            'name': 'books',
            'ru': 'Книги',
            'keywords': [
                'книга',
            ]
        })

        return {
            'categories': self.categories(filtered),
            'group': self.group(filtered),
        }

    def categories(self, cs):
        category_by_name = {}
        # deduplication
        for r in self.leaf(cs):
            if r['name'] in category_by_name:
                category_by_name[r['name']]['keywords'] = sorted(list(set(category_by_name[r['name']]['keywords']).union(set(r['keywords']))))
            else:
                category_by_name[r['name']] = r

        return list(category_by_name.values())

    def leaf(self, categories: List[Dict]) -> List[Dict]:
        result = []
        for c in categories:
            if 'child' in c:
                result.extend(self.leaf(c['child']))
            else:
                result.append({
                    'name': c['name'],
                    'keywords': c['keywords'],
                })

        return result

    def group(self, cs: List[Dict]):
        result = []
        for c in cs:
            r = {
                'name': c['name'],
                'ru': c['ru'],
            }

            if 'child' in c:
                r['child'] = self.group(c['child'])

            result.append(r)

        return result

    @staticmethod
    def to_plain(categories: List[Dict]) -> List[Dict]:
        result = categories
        for c in categories:
            result.extend(CategoryTransform.to_plain(c.get('child', [])))

        return result

    @staticmethod
    def validate(categories: List[Dict]):
        categories = CategoryTransform.to_plain(categories)

        category_by_name = {}
        for r in categories:
            category_by_name.setdefault(r['name'], []).append(r)

        for name, l in category_by_name.items():
            if len(l) > 1:
                print(f'{name} - {len(l)}')


def main(context):
    extractor = CategoryExtractor()
    result = extractor.parse(context.source_file)

    prev_result = {}
    with open(context.output_file, encoding='utf8') as f:
        prev_result = yaml.safe_load(f)
    result = merge_categories(result, prev_result)

    new_result = CategoryTransform(result).transform()

    with open(context.output_file, 'w', encoding='utf8') as f:
        yaml.dump(new_result, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


if __name__ == '__main__':
    main(get_context())
