import requests

file_name = '2015-01-01-15.json.gz'
#This is to ingest data
def ingest_data():
    url = f'https://data.gharchive.org/{file_name}'
    result = requests.get(url).content
    return result
