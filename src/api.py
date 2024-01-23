import json
import os

import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Api:
    def __init__(self):
        self.url = 'https://api.wikimedia.org/core/v1/wikipedia/'
        self.endpoint = '/search/page'

    def get_results(self, search_text: json):
        language_code = 'en'
        number_of_results = 1
        headers = {
            # 'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
            'User-Agent': 'GPT (CITS)'
        }
        url = self.url + language_code + self.endpoint
        parameters = {'q': search_text, 'limit': number_of_results}
        response = requests.get(url, headers=headers, params=parameters)
        return json.dumps(response.json())


if __name__ == '__main__':
    api = Api()
    results = api.get_results("gpt")
    print(results)
