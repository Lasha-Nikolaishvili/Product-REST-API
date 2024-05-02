# Django DRF REST API for Product Data Manipulation

This Django project provides a RESTful API for managing product data. It includes endpoints for retrieving, listing, creating, updating, and deleting products.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Lasha-Nikolaishvili/Product-REST-API
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Start the development server:

    ```bash
    python manage.py runserver
    ```

## Endpoints

### Product Detail

Endpoint: `rest-api/products/<product_id>`

- Method: GET
- Description: Retrieves full details of a specific product.
- Parameters:
  - `product_id`: The unique identifier of the product.
- Example Response:
  ```json
  {
    "id": 50,
    "name": "I. Robot",
    "price": "19.95",
    "stock": 12,
    "categories": [
        "Books"
    ]
  }
  ```

### Product List

Endpoint: `rest-api/products`

- Method: GET
- Description: Retrieves a list of all products (name, price) with pagination.
- Example Response:
  ```json
  {
    "count": 5,
    "next": "http://localhost:8000/rest-api/products/?page=2",
    "previous": null,
    "results": [
        {
            "name": "Neuromancer",
            "price": "14.99"
        },
        {
            "name": "Didostatis Marjvena",
            "price": "30.50"
        }
    ]
  }
  ```

### Create Product

Endpoint: `rest-api/products/create`

- Method: POST
- Description: Creates a new product.
- Body Parameters:
  - `name` (string): The name of the product.
  - `price` (float): The price of the product.
  - `stock` (integer): The stock quantity of the product.
  - `categories` (list): The categories of the product.
- Example Request Body:
  ```json
  {
    "id": 1,
    "name": "New Product",
    "price": 20.99,
    "stock": 75,
    "categories": [1, 2, 3]
  }
  ```

### Update Product

Endpoint: `rest-api/products/<product_id>/update`

- Method: PUT
- Description: Updates an existing product.
- Parameters:
  - `product_id`: The unique identifier of the product to be updated.
- Body Parameters:
  - `stock` (integer): The updated stock quantity of the product.
- Example Request Body:
  ```json
  {
    "stock": 50
  }
  ```

### Delete Product

Endpoint: `rest-api/products/<product_id>/delete`

- Method: DELETE
- Description: Deletes an existing product.
- Parameters:
  - `product_id`: The unique identifier of the product to be deleted.

## Technologies Used

- Django
- Django REST Framework
- markdown

## Authors

- [Lasha-Nikolaishvili](https://github.com/Lasha-Nikolaishvili)
