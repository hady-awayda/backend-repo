import yaml
import requests

def read_config():
	import requests
	import yaml

	# URL of the raw config.yaml file in the remote repository
	url = 'https://raw.githubusercontent.com/username/repo/branch/path/to/config.yaml'

	# Fetch the file
	response = requests.get(url)

	if response.status_code == 200:
		# Parse the YAML content
		config = yaml.safe_load(response.content)
		
		# Access the desired variable
		variable = config.get('your_variable_name')
		print(variable)
	else:
		print(f"Failed to fetch the file. Status code: {response.status_code}")
