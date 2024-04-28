import os
from .nfo_file import write_series_nfo, write_season_nfo, write_episode_nfo 
from . import download

def season(directory, season):
    print('  ' + str(season.title))
    mkdir(directory)
    img_path = f'{directory}/{season.title}.jpg'
    download.asset(season.image_url, img_path)
    nfo_path = f'{directory}/season.nfo'
    write_season_nfo(nfo_path, season)

def episode(season_dir, episode):
    print('    ' + str(episode.title))
    img_path = f'{season_dir}/episode{episode.entry}.jpg'
    download.asset(episode.image_url, img_path)
    vid_path = f'{season_dir}/episode{episode.entry}.mp4'
    download.asset(episode.video_url, vid_path)
    nfo_path = f'{season_dir}/episode{episode.entry}.nfo'
    write_episode_nfo(nfo_path, episode)

def series(directory, series):
    print(series.title)
    mkdir(directory)
    img_path = f'{directory}/{series.title}.jpg'
    download.asset(series.image_url, img_path)
    nfo_path = f'{directory}/tvshow.nfo'
    write_series_nfo(nfo_path, series)

def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

