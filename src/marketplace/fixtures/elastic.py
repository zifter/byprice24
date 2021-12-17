LIST_MATCHES_ELASTIC_FIXTURE = {'count': 2,
                                'next_page': 2,
                                'previous_page': 0,
                                'objects': [
                                    {'_source': {
                                        'product': {'id': 1,
                                                    'name': 'Acer Extensa 15 EX215-53G-7014 NX.EGCER.009',
                                                    'category': 'notebook',
                                                    'description': '',
                                                    'preview_url': None},
                                        'product_page': {'marketplaces_count_instock': 1,
                                                         'min_offer': {'price': '340.30',
                                                                       'price_currency': 'BYN'}}}},
                                    {'_source': {
                                        'product': {'id': 2,
                                                    'name': 'Acer Extensa 15 EX215-52-54D6 NX.EG8ER.00V',
                                                    'category': 'notebook',
                                                    'description': '',
                                                    'preview_url': None},
                                        'product_page': {'marketplaces_count_instock': 1,
                                                         'min_offer': {'price': '580.30',
                                                                       'price_currency': 'BYN'}}}}]}

NOT_FULL_PAGINATION_ELASTIC_FIXTURE = {'count': 2,
                                       'next_page': 3,
                                       'previous_page': 1,
                                       'objects': [
                                           {'_source': {
                                               'product': {'id': 1,
                                                           'name': 'Acer Extensa 15 EX215-53G-7014 NX.EGCER.009',
                                                           'category': 'notebook',
                                                           'description': '',
                                                           'preview_url': None},
                                               'product_page': {'marketplaces_count_instock': 1,
                                                                'min_offer': {'price': '340.30',
                                                                              'price_currency': 'BYN'}}}}
                                       ]}

EMPTY_LIST_ELASTIC_FIXTURE = {'count': 0,
                              'next_page': 2,
                              'previous_page': 0,
                              'objects': []}
