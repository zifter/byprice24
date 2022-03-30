class CounterViewsRedis:
    STORAGE_NAME = 'storage:product_view_counts'

    def __init__(self, redis_client, product_id: int = None, number_of_products: int = None):
        self.redis_client = redis_client
        self.product_id = product_id
        self.number_of_products = number_of_products

    def get_most_popular_products_id(self) -> list:
        product_ids = self.redis_client.zrange(self.STORAGE_NAME, -self.product_id, -1)[::-1]
        return [int(product_id) for product_id in product_ids]

    def increment_product_views(self):
        product_views = self.get_product_views()
        if not product_views:
            self.create_initial_product_views()

        self.redis_client.zincrby(self.STORAGE_NAME, 1, self.product_id)

    def get_product_views(self) -> int:
        number_of_views = self.redis_client.zscore(self.STORAGE_NAME, self.product_id)
        if not number_of_views:
            return 0
        return int(number_of_views)

    def create_initial_product_views(self):
        self.redis_client.zadd(self.STORAGE_NAME, {self.product_id: 0})
