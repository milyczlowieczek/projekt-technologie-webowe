from fastapi import APIRouter, HTTPException, Query

from .storage import get_customers_storage, get_orders_storage, get_products_storage
from .schema import (CustomerCreateSchema, CustomerUpdateSchema, Customer, Order, Product, OrderCreateSchema, ProductCreateSchema, OrderUpdateSchema, ProductUpdateSchema)

router = APIRouter()


CUSTOMERS_STORAGE = get_customers_storage()
ORDERS_STORAGE = get_orders_storage()
PRODUCTS_STORAGE = get_products_storage()

@router.get("/customers")
async def get_customers() -> list[Customer]:
    return list(get_customers_storage().values())


@router.get("/customers/{customer_id}")
async def get_customer(customer_id: int) -> Customer:
    try:
        return CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )


@router.patch("/customers/{customer_id}")
async def update_customer(
    customer_id: int, updated_customer: CustomerUpdateSchema
) -> Customer:
    existing_customer = None
    try:
        existing_customer = CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )
    if not updated_customer.name and not updated_customer.surname and not updated_customer.email and not updated_customer.phoneNumber:
        raise HTTPException(
            status_code=422, detail="Must contain at least one non-empty field."
        )
    if updated_customer.name:
        existing_customer.name = updated_customer.name

    if updated_customer.surname:
        existing_customer.surname = updated_customer.surname
    
    if updated_customer.email:
        existing_customer.email = updated_customer.email
    
    if updated_customer.phoneNumber:
        existing_customer.phoneNumber = updated_customer.phoneNumber

    return existing_customer


@router.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int) -> None:
    try:
        del CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )


@router.post("/customers")
async def create_customer(customer: CustomerCreateSchema) -> Customer:
    id = len(CUSTOMERS_STORAGE) + 1
    new_customer = Customer(**customer.dict(), id=id)
    CUSTOMERS_STORAGE[id] = new_customer
    return new_customer


@router.get("/orders")
async def get_orders() -> list[Order]:
    return list(get_orders_storage().values())

@router.get("/orders/{order_id}")
async def get_order(order_id: int) -> Order:
    try:
        return CUSTOMERS_STORAGE[order_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Order with ID={order_id} does not exist."
        )

@router.patch("/orders/{order_id}")
async def update_order(
    order_id: int, updated_order: OrderUpdateSchema
) -> Customer:
    existing_order = None
    try:
        existing_order = ORDERS_STORAGE[order_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Order with ID={order_id} does not exist."
        )
    if not updated_order.customerId and not updated_order.productId:
        raise HTTPException(
            status_code=422, detail="Must contain at least one non-empty field."
        )
    if updated_order.customerId:
        existing_order.customerId  = updated_order.customerId

    if updated_order.productId:
        existing_order.productId  = updated_order.productId
    
    return existing_order


@router.delete("/orders/{order_id}")
async def delete_order(order_id: int) -> None:
    try:
        del ORDERS_STORAGE[order_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Order with ID={order_id} does not exist."
        )


@router.post("/orders")
async def create_order(order: OrderCreateSchema) -> Order:
    id = len(ORDERS_STORAGE) + 1
    new_order = Order(**order.dict(), id=id)
    ORDERS_STORAGE[id] = new_order
    return new_order


@router.get("/products")
async def get_products() -> list[Product]:
    return list(get_products_storage().values())

@router.get("/products/{product_id}")
async def get_product(product_id: int) -> Product:
    try:
        return PRODUCTS_STORAGE[product_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Product with ID={product_id} does not exist."
        )

@router.patch("/products/{product_id}")
async def update_product(
    product_id: int, updated_product: ProductUpdateSchema
) -> Product:
    existing_product = None
    try:
        existing_product = PRODUCTS_STORAGE[product_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Product with ID={product_id} does not exist."
        )
    if not updated_product.name and not updated_product.price:
        raise HTTPException(
            status_code=422, detail="Must contain at least one non-empty field."
        )
    if updated_product.name:
        existing_product.name = updated_product.name

    if updated_product.price:
        existing_product.price = updated_product.price
    
    return existing_product


@router.delete("/products/{product_id}")
async def delete_product(product_id: int) -> None:
    try:
        del PRODUCTS_STORAGE[product_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Product with ID={product_id} does not exist."
        )

@router.post("/products")
async def create_product(product: ProductCreateSchema) -> Product:
    id = len(PRODUCTS_STORAGE) + 1
    new_product = Product(**product.dict(), id=id)
    PRODUCTS_STORAGE[id] = new_product
    return new_product