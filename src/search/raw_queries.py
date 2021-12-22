SELECT_PRODUCT_WITH_PAGES_AND_STATES = """
SELECT p.id, p.name, p.description, p.category,  p.description, p.preview_url,
marketplaces_instock.count as marketplaces_count_instock, MIN(ps.price) as min_offer,
 ps.price_currency as min_offer_currency from marketplace_product p
JOIN marketplace_productpage pp on p.id = pp.product_id
JOIN marketplace_productstate ps on pp.id = ps.product_page_id

    JOIN (SELECT p.id, count(DISTINCT pp.marketplace_id) AS count  from marketplace_product p
     JOIN marketplace_productpage pp on p.id = pp.product_id
     GROUP BY p.id) AS marketplaces_instock on marketplaces_instock.id = p.id

    JOIN (SELECT pp.id, MAX(ps.created) as created from marketplace_productpage pp
    JOIN marketplace_productstate ps on pp.id = ps.product_page_id
    GROUP BY pp.id) AS latest_state on  pp.id = latest_state.id AND ps.created = latest_state.created

WHERE p.id IN (%s)
GROUP BY p.id, p.name, p.description, p.category, p.description, p.preview_url,
ps.price_currency, marketplaces_instock.count;"""
