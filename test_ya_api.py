import pytest
from ya_api import create_folder
import requests
from token_ya import token

class TestYAPI:
	def setup(self):
		print('setup')

	def teardown(self):
		print('teardown')

	@pytest.fixture()
	def connection(self):
		headers = {
			'Accept': 'application/json',
			'Authorization': f'OAuth {token}'
		}

		name = 'aaa'

		params = {
			'path': f'{name}',
		}

		url = f'https://cloud-api.yandex.net/v1/disk/resources/'
		result = requests.get(url, params=params, headers=headers)

		return result

	def test_create_folder(self, connection):
		assert create_folder('aaa') == connection