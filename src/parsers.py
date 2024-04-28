#from data_types import Episode
import data_types

def parse_episode(json):
    return data_types.Episode(
            title = json['title'],
            description = json['description'],
            image_url = json['coverImage']['src'],
            video_url = json['downloads'][2]['url']
            )

def parse_season(json):
    return data_types.Season(
            id = json['id'],
            title = json['title'],
            image_url = json['coverImage']['src']
            )

def parse_series(json):
    return data_types.Series(
            id = json['id'],
            title = json['title'],
            image_url = json['coverImage']['src']
            )
