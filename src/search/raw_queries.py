SELECT_PRODUCT_WITH_PAGES_AND_STATES = 'SELECT product.id, product.name, product.description, product.category, ' \
                                       'product.preview_url, COUNT(*) AS marketplaces_count_instock, ' \
                                       'MIN(product_state.price), product_state.price_currency as min_offer FROM ' \
                                       'marketplace_product product JOIN marketplace_productpage product_page on ' \
                                       'product.id = product_page.product_id JOIN marketplace_productstate ' \
                                       'product_state on product_page.id = product_state.product_page_id WHERE ' \
                                       'product.id in (%s) GROUP BY product.id, product.name, product.description,' \
                                       ' product.category, product.preview_url, product_state.price_currency;'
