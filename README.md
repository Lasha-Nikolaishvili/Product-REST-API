# Django DRF REST API for Product Data Manipulation

This Django project provides a RESTful API for managing product and category data. It includes endpoints for retrieving, listing, creating, updating, and deleting products, as well as categories.

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

Endpoint: `rest-api/products/<product_id>/`

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
        1
    ]
  }
  ```

### Product List

Endpoint: `rest-api/products/`

- Method: GET
- Description: Retrieves a list of all products (name, price) with pagination.
- Example Response:
  ```json
  {
    "count": 3,
    "next": "http://127.0.0.1:8000/rest-api/products/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Black T-Shirt",
            "price": "25.50"
        },
        {
            "id": 2,
            "name": "Smart T-Shirt",
            "price": "250.99"
        }
    ]
  }
  ```

### Create Product

Endpoint: `rest-api/products/`

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

Endpoint: `rest-api/products/<product_id>/`

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

Endpoint: `rest-api/products/<product_id>/`

- Method: DELETE
- Description: Deletes an existing product.
- Parameters:
  - `product_id`: The unique identifier of the product to be deleted.

### Category Detail

Endpoint: `rest-api/categories/<category_id>/`

- Method: GET
- Description: Retrieves full details of a specific category.
- Parameters:
  - `category_id`: The unique identifier of the category.
- Example Response:
  ```json
  {
    "id": 1,
    "name": "Books"
  }
  ```

### Category List

Endpoint: `rest-api/categories/`

- Method: GET
- Description: Retrieves a list of all categories.
- Example Response:
  ```json
  [
    {
        "id": 1,
        "name": "Books"
    },
    {
        "id": 2,
        "name": "Electronics"
    }
  ]
  ```

### Create Category

Endpoint: `rest-api/categories/`

- Method: POST
- Description: Creates a new category.
- Body Parameters:
  - `name` (string): The name of the category.
- Example Request Body:
  ```json
  {
    "name": "New Category"
  }
  ```

### Update Category

Endpoint: `rest-api/categories/<category_id>/`

- Method: PUT
- Description: Updates an existing category.
- Parameters:
  - `category_id`: The unique identifier of the category to be updated.
  - `name` (string): The updated name of the category.
- Example Request Body:
  ```json
  {
    "name": "Updated Category"
  }
  ```

### Delete Category

Endpoint: `rest-api/categories/<category_id>/`

- Method: DELETE
- Description: Deletes an existing category.
- Parameters:
  - `category_id`: The unique identifier of the category to be deleted.

## Admin User Credentials

- Username: admin
- Password: admin
- Email: admin@mail.com

## Technologies Used

- Django
- Django REST Framework
- markdown
- Swagger UI

## Authors

- [Lasha-Nikolaishvili](https://github.com/Lasha-Nikolaishvili)
