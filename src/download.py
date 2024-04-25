import requests


def asset(url, file_path):
    response = requests.get(url)
    if response.ok:
        with open(file_path, "wb") as file:
            file.write(response.content)
    else:
        raise ConnectionError()

def json(url):
    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        raise ConnectionError()

def collection_json(collection_id):
    return json('https://www.churchofjesuschrist.org/media/api/v2/asset/collection?lang=eng&context=published&titanId=' + collection_id + '&limit=48&offset=0&childrenOnly=true')
