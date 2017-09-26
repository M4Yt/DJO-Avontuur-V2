import json

def load(path):
	with open(path,encoding='utf-8') as data:
		return json.load(data)
