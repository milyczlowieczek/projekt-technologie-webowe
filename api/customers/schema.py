from enum import Enum

from pydantic import BaseModel

class CustomerCreateSchema(BaseModel):
    name: str
    surname: str
    email: str
    phoneNumber: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Jan",
                "surname": "Kowalski",
                "email": "jan.kowalski@example.com",
                "phoneNumber": "000-000-000",
            }
        }


class CustomerUpdateSchema(BaseModel):
    name: str | None
    surname: str | None
    email: str | None
    phoneNumber: str | None

    class Config:
        schema_extra = {
            "example": {
                "name": "Janek",
                "surname": "Kowalczyk"
            }
        }


class Customer(CustomerCreateSchema):
    id: int


class ProductCreateSchema(BaseModel):
    name: str
    price: float

    class Config:
        schema_extra = {
            "example": {
                "name": "Product",
                "price": "100.0"
            }
        }

class Product(ProductCreateSchema):
    id: int

class ProductUpdateSchema(BaseModel):
    name: str | None
    price: float | None

    class Config:
        schema_extra = {
            "example": {
                "name": "Product2",
            }
        }


class OrderCreateSchema(BaseModel):
    productId: list[int]
    customerId: int

    class Config:
        schema_extra = {
            "example": {
                "productId": [0, 1],
                "customerId": 0
            }
        }

class Order(OrderCreateSchema):
    id: int

class OrderUpdateSchema(BaseModel):
    productId: list[int] | None
    customerId: int | None

    class Config:
        schema_extra = {
            "example": {
                "productId": [0]
            }
        }







# class StudentCreateSchema(BaseModel):
#     first_name: str
#     last_name: str

#     class Config:
#         schema_extra = {
#             "example": {
#                 "first_name": "Zbyszek",
#                 "last_name": "Kieliszek",
#             }
#         }


# class StudentUpdateSchema(BaseModel):
#     first_name: str | None
#     last_name: str | None

#     class Config:
#         schema_extra = {
#             "example": {
#                 "first_name": "Zbysiu",
#             }
#         }


# class Student(StudentCreateSchema):
#     id: int


# class Mark(float, Enum):
#     BARDZO_DOBRY = 5.0
#     DOBRY_PLUS = 4.5
#     DOBRY = 4.0
#     DOSTATECZNY_PLUS = 3.5
#     DOSTATECZNY = 3.0
#     NIEDOSTATECZNY = 2.0