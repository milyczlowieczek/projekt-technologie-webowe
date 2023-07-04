from functools import lru_cache

from .schema import Customer, Product, Order

CustomerStorageType = dict[int, Customer]
ProductStorageType = dict[int, Product]
OrderStorageType = dict[int, Order]

CUSTOMERS: CustomerStorageType = {}
PRODUCTS: ProductStorageType = {
    0: Product(name="Product0", price="100.0", id=0),
    1: Product(name="Product1", price="20.0", id=1)
    }
ORDERS: OrderStorageType = {0: Order(id=0, customerId=0, productId=[0,1])}


@lru_cache(maxsize=1)
def get_customers_storage() -> CustomerStorageType:
    return CUSTOMERS

@lru_cache(maxsize=1)
def get_products_storage() -> ProductStorageType:
    return PRODUCTS

@lru_cache(maxsize=1)
def get_orders_storage() -> OrderStorageType:
    return ORDERS