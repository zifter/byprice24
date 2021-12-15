LIST_MATCHES_ELASTIC_FIXTURE = {
    '_scroll_id': 'dajdnasjdadkjn',
    'hits':
        {'total': {'value': 2},
         'hits': [
             {'_source': {
                 'product': {
                     'id': 2,
                     'name': 'Acer Extensa 15 EX215-53G-7014 NX.EGCER.009',
                     'category': 'notebook',
                     'description': '',
                     'preview_url': None},
                 'product_page': {'marketplaces_count_instock': 2,
                                  'min_offer':
                                      {'price': 340.3,
                                       'price_currency': 'BYN'}}}},
             {'_source': {
                 'product': {'id': 3,
                             'name': 'Acer Extensa 15 EX215-52-54D6 NX.EG8ER.00V',
                             'category': 'notebook',
                             'description': '',
                             'preview_url': None},
                 'product_page': {'marketplaces_count_instock': 1,
                                  'min_offer': {'price': 580.3,
                                                'price_currency': 'BYN'}}}}
        ]}}

EXACT_MATCH_ELASTIC_FIXTURE = {
    '_scroll_id': 'dajdnasjdadkjn',
    'hits':
        {'total': {'value': 1},
         'hits': [
             {'_source': {
                 'product': {
                     'id': 2,
                     'name': 'Acer Extensa 15 EX215-53G-7014 NX.EGCER.009',
                     'category': 'notebook',
                     'description': '',
                     'preview_url': None},
                 'product_page': {'marketplaces_count_instock': 2,
                                  'min_offer':
                                      {'price': 340.3,
                                       'price_currency': 'BYN'}}}}
        ]}}

EMPTY_LIST_ELASTIC_FIXTURE = {
    '_scroll_id': 'dajdnasjdadkjn',
    'hits':
        {'total': {'value': 0},
         'hits': []}}

NOT_FULL_SCROLL_FIXTURE = {
    '_scroll_id': 'JDNASJDNAJKDA123',
    'took': 3, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0},
    'hits': {'total': {'value': 54, 'relation': 'eq'}, 'max_score': 2.583145, 'hits': [
        {'_index': 'product', '_type': '_doc', '_id': 'DwD7uH0BUpBsQVTtJaLL', '_score': 2.583145, '_source': {
            'product': {'id': 11, 'name': 'Acer XD1320Wi', 'category': 'Проекторы', 'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/27/5/5240825/yxPcEJ7NtY.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 2390.98, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'fwD_uH0BUpBsQVTtZaL_', '_score': 1.9602306, '_source': {
            'product': {'id': 233, 'name': 'Acer Veriton EZ2740G DQ.VULER.00E', 'category': 'Моноблоки',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/68/2/5370442/uwd6gpljv7.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 2569.82, 'price_currency': 'BYN'}}}},
    ]}}

FULL_PAGINATION_FIXTURE = {
    '_scroll_id': 'JDNASJDNAJKDA123',
    'took': 3, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0},
    'hits': {'total': {'value': 20, 'relation': 'eq'}, 'max_score': 2.583145, 'hits': [
        {'_index': 'product', '_type': '_doc', '_id': 'DwD7uH0BUpBsQVTtJaLL', '_score': 2.583145, '_source': {
            'product': {'id': 11, 'name': 'Acer XD1320Wi', 'category': 'Проекторы', 'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/27/5/5240825/yxPcEJ7NtY.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 2390.98, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'fwD_uH0BUpBsQVTtZaL_', '_score': 1.9602306, '_source': {
            'product': {'id': 233, 'name': 'Acer Veriton EZ2740G DQ.VULER.00E', 'category': 'Моноблоки',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/68/2/5370442/uwd6gpljv7.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 2569.82, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'gQD_uH0BUpBsQVTtbaKB', '_score': 1.9602306, '_source': {
            'product': {'id': 235, 'name': 'Acer Veriton Z4870G DQ.VTQER.006', 'category': 'Моноблоки',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/68/9/5172369/3h17ncyrtY.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 1784.23, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'iAD_uH0BUpBsQVTttKLQ', '_score': 1.9602306, '_source': {
            'product': {'id': 250, 'name': 'Acer Veriton EZ2740G DQ.VULER.00C', 'category': 'Моноблоки',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/68/1/5370441/7T1SQUS1mi.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 2662.62, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'iQD_uH0BUpBsQVTtvqK2', '_score': 1.9602306, '_source': {
            'product': {'id': 252, 'name': 'Acer Veriton Z4870G DQ.VTQER.01Y', 'category': 'Моноблоки',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/68/1/5172371/xrjXmB20Mw.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 2269.54, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'uAABuX0BUpBsQVTtYqLx', '_score': 1.8143868, '_source': {
            'product': {'id': 337, 'name': 'Acer Aspire C24-1650 DQ.BFTER.006', 'category': 'Моноблоки',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/68/2/5230462/qBYfC51iWU.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 1874.84, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'YYMBuX0BxEljMe8yuEAe', '_score': 1.8143868, '_source': {
            'product': {'id': 354, 'name': 'Acer Aspire C24-1650 DQ.BFSER.00D', 'category': 'Моноблоки',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/68/9/5230459/QZNQJ6ISbq.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 2662.4, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'YoMBuX0BxEljMe8yvUAD', '_score': 1.8143868, '_source': {
            'product': {'id': 355, 'name': 'Acer Aspire C24-1650 DQ.BFSER.009', 'category': 'Моноблоки',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/68/0/5230460/UR3fEcwTuH.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 2134.5, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'wQABuX0BUpBsQVTtwqIX', '_score': 1.8143868, '_source': {
            'product': {'id': 356, 'name': 'Acer Aspire C24-1650 DQ.BFTER.004', 'category': 'Моноблоки',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/68/4/5230464/vxWKkEbnV3.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 1980.95, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'wwABuX0BUpBsQVTt0KK_', '_score': 1.8143868, '_source': {
            'product': {'id': 359, 'name': 'Acer Aspire C24-1650 DQ.BFSER.005', 'category': 'Моноблоки',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/68/3/5230463/ikOBHAlzQ7.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 2272.7, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'GwD7uH0BUpBsQVTtvqKW', '_score': 1.5793719, '_source': {
            'product': {'id': 35, 'name': 'Acer Extensa 15 EX215-52-54D6 NX.EG8ER.00V', 'category': 'notebook',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/64/6/4368196/G7jEd2ooK6.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 1864.33, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'IwD8uH0BUpBsQVTtKaJH', '_score': 1.5793719, '_source': {
            'product': {'id': 59, 'name': 'Acer Extensa 15 EX215-52-57XA NX.EG8EU.00H', 'category': 'notebook',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/64/8/4533248/kdCEUdVIou.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 1764.74, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'uoP7uH0BxEljMe8yDz_z', '_score': 1.5793719, '_source': {
            'product': {'id': 3, 'name': 'Acer Swift 3 SF314-42-R420 NX.HSEER.00D', 'category': 'notebook',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/64/9/2688119/gD9WcOtj7u.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 1700.0, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'FAD7uH0BUpBsQVTta6LY', '_score': 1.5793719, '_source': {
            'product': {'id': 21, 'name': 'Acer Extensa 15 EX215-52-368N NX.EG8ER.01C', 'category': 'notebook',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/64/4/4368194/pmrqtg5Qie.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 1443.0, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'zIP7uH0BxEljMe8yzT-I', '_score': 1.5793719, '_source': {
            'product': {'id': 39, 'name': 'Acer Extensa 15 EX215-52-38YG NX.EG8ER.01Q', 'category': 'notebook',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/64/0/4368190/ETtmbb8ABi.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 1521.34, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'HAD7uH0BUpBsQVTt06I5', '_score': 1.5793719, '_source': {
            'product': {'id': 40, 'name': 'Acer Extensa 15 EX215-52-38SC NX.EG8ER.004', 'category': 'notebook',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/64/8/4379578/LSw5L4LRAy.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 1256.16, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'zYP7uH0BxEljMe8y1T_z', '_score': 1.5793719, '_source': {
            'product': {'id': 41, 'name': 'Acer Extensa 15 EX215-52-36UB NX.EG8ER.005', 'category': 'notebook',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/64/7/4379577/dUwt6WVAVy.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 1338.59, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'zoP7uH0BxEljMe8y2T-F', '_score': 1.5793719, '_source': {
            'product': {'id': 42, 'name': 'Acer Extensa 15 EX215-52-34U4 NX.EG8ER.014', 'category': 'notebook',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/64/4/4379574/u9M58WZlvS.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 1343.21, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': '0IP7uH0BxEljMe8y6z-G', '_score': 1.5793719, '_source': {
            'product': {'id': 46, 'name': 'Acer Extensa 15 EX215-22-R091 NX.EG9ER.00H', 'category': 'notebook',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/64/5/4368135/1wEiaPi3ba.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 1179.25, 'price_currency': 'BYN'}}}},
        {'_index': 'product', '_type': '_doc', '_id': 'IgD8uH0BUpBsQVTtIaKY', '_score': 1.5793719, '_source': {
            'product': {'id': 57, 'name': 'Acer Extensa 15 EX215-52-30D1 NX.EG8EU.00J', 'category': 'notebook',
                        'description': '',
                        'preview_url': 'https://cdn.dataimgstore.com/preview/64/9/4533249/vCb17DrzWt.jpeg'},
            'product_page': {'marketplaces_count_instock': 1,
                             'min_offer': {'price': 1430.92, 'price_currency': 'BYN'}}}}]}}
