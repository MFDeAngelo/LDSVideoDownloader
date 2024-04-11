import requests
import os

series_directory = "C:\\Users\\iamno\\Videos\\BoM"
series_id = '7415b72b4f0d454a96ed4ccda89194b8'


def handle_season(data):
    title = data['title']
    print('  ' + str(title))
    season_directory = series_directory + "\\" + title
    mkdir(season_directory)
    img_response = requests.get(data['coverImage']['src'])
    img_path = season_directory + "\\" + title + ".jpg"
    if img_response.ok:
        with open(img_path, "wb") as img_file:
            img_file.write(img_response.content)
    nfo_path = season_directory + "\\season.nfo"
    with open(nfo_path, "w") as nfo_file:
        nfo_file.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n');
        nfo_file.write('<tvshow>\n');
        nfo_file.write('  <name>' + title + '</name>\n');
        nfo_file.write('  <genre>Religious</genre>\n');
        nfo_file.write('  <thumb>' + title + '.jpg</thumb>\n');
        nfo_file.write('</tvshow>\n');
    episode_listing = get_collection_json(data['id'])
    for index, episode_data in enumerate(episode_listing['items']):
        handle_episode(episode_data, season_directory, index + 1)


def handle_episode(data, season_dir, episode_number):
    title = data['title']
    print('    ' + str(title))
    img_path = season_dir + '\\episode' + str(episode_number) + '.jpg'
    img_response = requests.get(data['coverImage']['src'])
    if img_response.ok:
        with open(img_path, "wb") as img_file:
            img_file.write(img_response.content)
    vid_path = season_dir + '\\episode' + str(episode_number) + '.mp4'
    vid_response = requests.get(data['downloads'][2]['url'])
    if vid_response.ok:
        with open(vid_path, "wb") as vid_file:
            vid_file.write(vid_response.content)
    nfo_path = season_dir + '\\episode' + str(episode_number) + '.nfo'
    with open(nfo_path, "w") as nfo_file:
        nfo_file.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n');
        nfo_file.write('<episode>\n');
        nfo_file.write('  <name>' + title + '</name>\n');
        nfo_file.write('  <plot>' + data['description'] + '</plot>\n');
        nfo_file.write('  <genre>Religious</genre>\n');
        nfo_file.write('  <thumb>episode' + str(episode_number) + '.jpg</thumb>\n');
        nfo_file.write('</episode>\n');

def get_collection_json(collection_id):
    response = requests.get('https://www.churchofjesuschrist.org/media/api/v2/asset/collection?lang=eng&context=published&titanId=' + collection_id + '&limit=48&offset=0&childrenOnly=true')
    if response.ok:
        return response.json()
    else:
        raise ConnectionError()


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

mkdir(series_directory)
try:
    data = get_collection_json(series_id)
    print('Downloading LDS content')
    section = data['items']
    for season in section:
        handle_season(season)
except:
    print("Failed to get the series data")

 
