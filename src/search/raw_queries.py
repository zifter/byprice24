SELECT_PRODUCT_WITH_PAGES_AND_STATES = """
SELECT   p.id,
         p.NAME,
         p.description,
         p.category,
         p.description,
         p.preview_url,
         marketplaces_instock.count AS marketplaces_count_instock,
         Min(ps.price)              AS price,
         ps.price_currency          AS price_currency
FROM     marketplace_product p
JOIN     marketplace_productpage pp
ON       p.id = pp.product_id
JOIN     marketplace_productstate ps
ON       pp.id = ps.product_page_id
JOIN
         (
                  SELECT   p.id,
                           Count(DISTINCT pp.marketplace_id) AS count
                  FROM     marketplace_product p
                  JOIN     marketplace_productpage pp
                  ON       p.id = pp.product_id
                  GROUP BY p.id) AS marketplaces_instock
ON       marketplaces_instock.id = p.id
JOIN
         (
                  SELECT   pp.id,
                           Max(ps.created) AS created
                  FROM     marketplace_productpage pp
                  JOIN     marketplace_productstate ps
                  ON       pp.id = ps.product_page_id
                  GROUP BY pp.id) AS latest_state
ON       pp.id = latest_state.id
AND      ps.created = latest_state.created
WHERE    p.id IN %s
GROUP BY p.id,
         p.NAME,
         p.description,
         p.category,
         p.description,
         p.preview_url,
         ps.price_currency,
         marketplaces_instock.count
"""

SELECT_PRODUCT_WITH_PAGES_AND_STATES_ORDER_BY_PRICE_DESC = """
SELECT   p.id,
         p.NAME,
         p.description,
         p.category,
         p.description,
         p.preview_url,
         marketplaces_instock.count AS marketplaces_count_instock,
         Min(ps.price)              AS price,
         ps.price_currency          AS price_currency
FROM     marketplace_product p
JOIN     marketplace_productpage pp
ON       p.id = pp.product_id
JOIN     marketplace_productstate ps
ON       pp.id = ps.product_page_id
JOIN
         (
                  SELECT   p.id,
                           Count(DISTINCT pp.marketplace_id) AS count
                  FROM     marketplace_product p
                  JOIN     marketplace_productpage pp
                  ON       p.id = pp.product_id
                  GROUP BY p.id) AS marketplaces_instock
ON       marketplaces_instock.id = p.id
JOIN
         (
                  SELECT   pp.id,
                           Max(ps.created) AS created
                  FROM     marketplace_productpage pp
                  JOIN     marketplace_productstate ps
                  ON       pp.id = ps.product_page_id
                  GROUP BY pp.id) AS latest_state
ON       pp.id = latest_state.id
AND      ps.created = latest_state.created
WHERE    p.id IN %s
GROUP BY p.id,
         p.NAME,
         p.description,
         p.category,
         p.description,
         p.preview_url,
         ps.price_currency,
         marketplaces_instock.count
ORDER BY MIN(ps.price) DESC;
"""

SELECT_PRODUCT_WITH_PAGES_AND_STATES_ORDER_BY_PRICE_ASC = """
SELECT   p.id,
         p.NAME,
         p.description,
         p.category,
         p.description,
         p.preview_url,
         marketplaces_instock.count AS marketplaces_count_instock,
         Min(ps.price)              AS price,
         ps.price_currency          AS price_currency
FROM     marketplace_product p
JOIN     marketplace_productpage pp
ON       p.id = pp.product_id
JOIN     marketplace_productstate ps
ON       pp.id = ps.product_page_id
JOIN
         (
                  SELECT   p.id,
                           Count(DISTINCT pp.marketplace_id) AS count
                  FROM     marketplace_product p
                  JOIN     marketplace_productpage pp
                  ON       p.id = pp.product_id
                  GROUP BY p.id) AS marketplaces_instock
ON       marketplaces_instock.id = p.id
JOIN
         (
                  SELECT   pp.id,
                           Max(ps.created) AS created
                  FROM     marketplace_productpage pp
                  JOIN     marketplace_productstate ps
                  ON       pp.id = ps.product_page_id
                  GROUP BY pp.id) AS latest_state
ON       pp.id = latest_state.id
AND      ps.created = latest_state.created
WHERE    p.id IN %s
GROUP BY p.id,
         p.NAME,
         p.description,
         p.category,
         p.description,
         p.preview_url,
         ps.price_currency,
         marketplaces_instock.count
ORDER BY MIN(ps.price) ASC;
"""
