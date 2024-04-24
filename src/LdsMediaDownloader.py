import requests
import os
from NfoFile import write_season_nfo, write_episode_nfo 

def handle_season(series_directory, data):
    title = data['title']
    print('  ' + str(title))
    season_directory = series_directory + "/" + title
    mkdir(season_directory)
    img_response = requests.get(data['coverImage']['src'])
    img_path = season_directory + "/" + title + ".jpg"
    if img_response.ok:
        with open(img_path, "wb") as img_file:
            img_file.write(img_response.content)
    nfo_path = season_directory + "/season.nfo"
    write_season_nfo(nfo_path, title)
    episode_listing = get_collection_json(data['id'])
    for index, episode_data in enumerate(episode_listing['items']):
        handle_episode(episode_data, season_directory, index + 1)


def handle_episode(data, season_dir, episode_number):
    title = data['title']
    print('    ' + str(title))
    img_path = season_dir + '/episode' + str(episode_number) + '.jpg'
    img_response = requests.get(data['coverImage']['src'])
    if img_response.ok:
        with open(img_path, "wb") as img_file:
            img_file.write(img_response.content)
    vid_path = season_dir + '/episode' + str(episode_number) + '.mp4'
    vid_response = requests.get(data['downloads'][2]['url'])
    if vid_response.ok:
        with open(vid_path, "wb") as vid_file:
            vid_file.write(vid_response.content)
    nfo_path = season_dir + '/episode' + str(episode_number) + '.nfo'
    #write_episode_nfo(nfo_path, 

def get_collection_json(collection_id):
    response = requests.get('https://www.churchofjesuschrist.org/media/api/v2/asset/collection?lang=eng&context=published&titanId=' + collection_id + '&limit=48&offset=0&childrenOnly=true')
    if response.ok:
        return response.json()
    else:
        raise ConnectionError()


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def handle_series(id, directory):
    mkdir(directory)
    try:
        data = get_collection_json(id)
        print('Downloading LDS content')
        section = data['items']
        for season in section:
            handle_season(directory, season)
    except:
        print("Failed to get the series data")

     
     
