import yaml
import requests

def read_config():
	import requests
	import yaml

	url = 'https://raw.githubusercontent.com/hady-awayda/fullstack-repo/main/config.yaml'

	response = requests.get(url)

	if response.status_code == 200:
		config = yaml.safe_load(response.content)
		
		variable = config.get('is_anagram')
		if variable is True:
			print("It is indeed an anagram!")
		else:
			print("Not actually an anagram...")

if __name__ == '__main__':
	read_config()