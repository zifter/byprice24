SELECT_PRODUCT_WITH_MIN_PRICE_BY_IDS = """
select r.id,
  r.name,
  r.category_id,
  mc.ru as category_tr,
  r.preview_url,
  r.price,
  r.price_currency AS price_currency
from (
    SELECT p.id,
      p.NAME,
      p.category_id,
      p.preview_url,
      Min(ps.price) AS price,
      ps.price_currency AS price_currency
    FROM marketplace_product p
      join (
      select unnest, ordinality
      from unnest(%s) with ordinality
        ) as x (id, ordering) on p.id = x.id
      JOIN marketplace_productpage pp ON p.id = pp.product_id
      JOIN marketplace_productstate ps ON pp.id = ps.product_page_id
      JOIN (
        SELECT pp.id,
          Max(ps.created) AS created
        FROM marketplace_productpage pp
          JOIN marketplace_productstate ps ON pp.id = ps.product_page_id
        GROUP BY pp.id
      ) AS latest_state ON pp.id = latest_state.id
      AND ps.created = latest_state.created
    WHERE p.id IN %s
    GROUP BY p.id,
      p.NAME,
      p.category_id,
      p.preview_url,
      ps.price_currency,
      x.ordering
    ORDER BY x.ordering
) as r
LEFT JOIN marketplace_categorygroup mc ON r.category_id = mc.category_id
"""
