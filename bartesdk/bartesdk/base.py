import requests

class BaseAPI:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def create(self, **kwargs):
        headers = {
            'X-Token-Api': self.api_key,
            'Content-Type': 'application/json',
            'accept': 'application/json'
        }
        payload = kwargs
        response = requests.post(self.base_url, headers=headers, json=payload)
        return response.status_code, response.json() if response.ok else response.text

    def get(self, **params):
        headers = {
            'X-Token-Api': self.api_key,
            'Content-Type': 'application/json',
            'accept': 'application/json'
        }
        response = requests.get(self.base_url, headers=headers, params=params)
        return response.json()

    def getByUuid(self, uuid):
        headers = {
            'X-Token-Api': self.api_key
        }
        url = f"{self.base_url}/{uuid}"
        response = requests.get(url, headers=headers)
        return response.json()

    def update(self, uuid, **kwargs):
        headers = {
            'X-Token-Api': self.api_key,
            'Content-Type': 'application/json',
            'accept': '*/*'
        }
        url = f"{self.base_url}/{uuid}"
        payload = kwargs
        response = requests.put(url, headers=headers, json=payload)
        try:
            response_data = response.json() if response.ok else response.text
        except ValueError:
            response_data = response.text
        return response.status_code, response_data

    def cancel(self, uuid):
        headers = {
            'X-Token-Api': self.api_key,
            'accept': '*/*'
        }
        url = f"{self.base_url}/{uuid}"
        response = requests.delete(url, headers=headers)
        return response.status_code, response.ok