from redis.client import Redis


class CounterViewsRedis:
    STORAGE_NAME = 'storage:product_view_counts'

    def __init__(self, redis_client: Redis):
        self.redis_client = redis_client

    def get_most_popular_products_id(self, number_of_products: int) -> list[int]:
        product_ids = self.redis_client.zrange(self.STORAGE_NAME, -number_of_products, -1)[::-1]
        return [int(product_id) for product_id in product_ids]

    def increment_product_views(self, product_id: int):
        product_views = self.get_product_views(product_id)
        if not product_views:
            self.create_initial_product_views(product_id)

        self.redis_client.zincrby(self.STORAGE_NAME, 1, product_id)

    def get_product_views(self, product_id: int) -> int:
        number_of_views = self.redis_client.zscore(self.STORAGE_NAME, product_id)
        if not number_of_views:
            return 0
        return int(number_of_views)

    def create_initial_product_views(self, product_id: int):
        self.redis_client.zadd(self.STORAGE_NAME, {product_id: 0})
