from dataclasses import dataclass

@dataclass
class Episode:
    title: str
    description: str
    entry: int
    image_url: str
    video_url: str
