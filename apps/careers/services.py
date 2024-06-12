from json import JSONDecodeError

import requests
from django.conf import settings

# TOKEN = settings.HURMA_API_KEY
#
# def get_hurma_vacations():
#     url = 'https://crassula.hurma.work/api/v1/vacancy'
#     head = {'token': TOKEN}
#     try:
#         response = requests.get(url, headers=head)
#         vacancies = response.json()['result']['data']
#         return vacancies
#     except (KeyError, TypeError, JSONDecodeError) as e:
#         print(e)
