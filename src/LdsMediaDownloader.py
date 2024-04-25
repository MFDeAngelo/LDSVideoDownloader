import os
from nfo_file import write_season_nfo, write_episode_nfo 
from parsers import parse_episode, parse_season
import download

def handle_season(series_directory, data):
    season = parse_season(data)
    print('  ' + str(season.title))
    season_directory = series_directory + "/" + season.title
    mkdir(season_directory)
    img_path = season_directory + "/" + season.title + ".jpg"
    download.asset(season.image_url, img_path)
    nfo_path = season_directory + "/season.nfo"
    write_season_nfo(nfo_path, season.title)
    episode_listing = download.collection_json(season.id)
    for index, episode_data in enumerate(episode_listing['items']):
        handle_episode(episode_data, season_directory, index + 1)


def handle_episode(data, season_dir, episode_number):
    episode = parse_episode(data)
    episode.entry = episode_number
    print('    ' + str(episode.title))
    img_path = season_dir + '/episode' + str(episode.entry) + '.jpg'
    download.asset(episode.image_url, img_path)
    vid_path = season_dir + '/episode' + str(episode.entry) + '.mp4'
    download.asset(episode.video_url, vid_path)
    nfo_path = season_dir + '/episode' + str(episode.entry) + '.nfo'
    write_episode_nfo(nfo_path, episode)



def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def handle_series(id, directory):
    mkdir(directory)
    try:
        data = download.collection_json(id)
        print('Downloading LDS content')
        section = data['items']
        for season in section:
            handle_season(directory, season)
    except:
        print("Failed to get the series data")

     
     
