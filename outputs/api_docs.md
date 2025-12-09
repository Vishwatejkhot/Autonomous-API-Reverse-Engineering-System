# API Documentation
## Introduction
The API is a comprehensive e-commerce platform that allows users to manage products, orders, and transactions.

## Endpoints
### Products
* **GET /products/{product_id}**: Retrieve product details by ID.
* **GET /products**: List all products.

### Users
* **GET /users/{user_id}**: Retrieve user profile by ID.
* **GET /users**: List all users.
* **PUT /users/{user_id}**: Update user profile.

### Orders
* **GET /orders/{order_id}**: Retrieve order details by ID.
* **GET /orders**: List all orders.
* **POST /orders**: Create new order.

### Transactions
* **GET /users/{user_id}/transactions**: Retrieve transaction history for a user.

## Schema Definitions
### Product
 Represents a product with attributes such as product ID, name, description, price, currency, stock, and category.

### User
 Represents a user with attributes such as user ID, name, location, bio, followers, and following.

### Order
 Represents an order with attributes such as order ID, status, and estimated delivery date.

### Transaction
 Represents a transaction with attributes such as transaction ID, amount, currency, and timestamp.