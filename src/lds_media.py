from parsers import parse_episode, parse_season, parse_series
import download
import handle

def start(directory, id):
    print('Downloading LDS content')
    collection_json = download.collection_json('4da6a5e612768eada390a3e0f6c0e386a015447a')
    series_json = next(s for s in collection_json['items'] if s['id'] == id)
    series = parse_series(series_json)
    series_directory = f'{directory}/{series.title}'
    handle.series(series_directory, series)
    for season in enumerate_seasons_from(series):
        season_directory = f'{series_directory}/{season.title}'
        handle.season(season_directory, season)
        for episode in enumerate_episodes_from(season):
            handle.episode(season_directory, episode)

def enumerate_seasons_from(series):
    series_json = download.collection_json(series.id)
    for season_json in series_json['items']:
        yield parse_season(season_json)

def enumerate_episodes_from(season):
    season_json = download.collection_json(season.id)
    for index, episode_json in enumerate(season_json['items']):
        episode = parse_episode(episode_json)
        episode.entry = index + 1
        yield episode
