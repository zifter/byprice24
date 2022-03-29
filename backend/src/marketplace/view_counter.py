from django_redis import get_redis_connection


class ViewCounterRedis:
    REDIS_CLIENT = get_redis_connection('default')
    STORAGE_NAME = 'storage:product_view_counts'

    def __init__(self, product_id: int = None, number_of_products: int = None):
        self.product_id = product_id
        self.number_of_products = number_of_products

    def get_most_popular_products_id(self):
        product_ids = self.REDIS_CLIENT.zrange(self.STORAGE_NAME, -self.product_id, -1)[::-1]
        return [int(product_id) for product_id in product_ids]

    def increment_product_views(self):
        product_views = self.get_product_views(self.product_id)
        if not product_views:
            self.create_initial_product_views(self.product_id)

        self.REDIS_CLIENT.zincrby(self.STORAGE_NAME, 1, self.product_id)

    def get_product_views(self, product_id):
        return self.REDIS_CLIENT.zscore(self.STORAGE_NAME, product_id)

    def create_initial_product_views(self, product_id):
        self.REDIS_CLIENT.zadd(self.STORAGE_NAME, {product_id: 0})
