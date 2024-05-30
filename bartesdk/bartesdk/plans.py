import requests

class plansAPI:
    def __init__(self, api_key, env="prd", api_version="v2"):
        self.api_key = api_key
        self.base_url = self._get_base_url(env, api_version)

    def _get_base_url(self, env, api_version):
        if env == "prd":
            return f'https://api.barte.com/{api_version}/plans'
        elif env == "sandbox":
            return f'https://sandbox-api.barte.com/{api_version}/plans'
        else:
            raise ValueError("Invalid environment specified")

    def getByUuid(self, uuid):
        headers = {
            'X-Token-Api': self.api_key,
            'accept': 'application/json'
        }
        url = f"{self.base_url}/{uuid}"
        response = requests.get(url, headers=headers)
        return response.status_code, response.json() if response.ok else response.text

    def get(self):
        headers = {
            'X-Token-Api': self.api_key,
            'accept': 'application/json'
        }
        response = requests.get(self.base_url, headers=headers)
        return response.status_code, response.json() if response.ok else response.text

    def create(self, **kwargs):
        headers = {
            'X-Token-Api': self.api_key,
            'Content-Type': 'application/json',
            'accept': 'application/json'
        }
        payload = kwargs
        response = requests.post(self.base_url, headers=headers, json=payload)
        return response.status_code, response.json() if response.ok else response.text
        
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

