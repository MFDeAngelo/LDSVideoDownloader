from data_types import Episode


def parse_episode(json):
    return Episode(
            title = json['title'],
            description = json['description'],
            image_url = json['coverImage']['src'],
            video_url = json['downloads'][2]['url']
            )


def parse_season(json):
    pass
