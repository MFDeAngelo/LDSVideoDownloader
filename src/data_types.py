from dataclasses import dataclass

@dataclass
class Episode:
    title: str
    description: str
    entry: int
    image_url: str
    video_url: str

    def __init__(self, title:str, description:str, image_url:str, video_url:str):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.video_url = video_url


@dataclass
class Season:
    id: str
    title: str
    image_url: str

    def __init__(self, id:str, title:str, image_url:str):
        self.id = id 
        self.title = title
        self.image_url = image_url

@dataclass
class Series:
    id: str
    title: str
    image_url: str

    def __init__(self, id:str, title:str, image_url:str):
        self.id = id
        self.title = title
        self.image_url = image_url
