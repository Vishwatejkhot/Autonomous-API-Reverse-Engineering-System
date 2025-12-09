import requests

class ECommerceAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_product(self, product_id):
        url = f"{self.base_url}/products/{product_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_products(self):
        url = f"{self.base_url}/products"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_user(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_users(self):
        url = f"{self.base_url}/users"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def update_user(self, user_id, data):
        url = f"{self.base_url}/users/{user_id}"
        response = requests.put(url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_order(self, order_id):
        url = f"{self.base_url}/orders/{order_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_orders(self):
        url = f"{self.base_url}/orders"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def create_order(self, data):
        url = f"{self.base_url}/orders"
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return response.json()
        else:
            return None

    def get_transactions(self, user_id):
        url = f"{self.base_url}/users/{user_id}/transactions"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None