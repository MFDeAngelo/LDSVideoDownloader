import argparse
from src.LdsMediaDownloader import handle_series

# series_directory = "C:/Users/iamno/Videos/BoM"
# series_id = '7415b72b4f0d454a96ed4ccda89194b8'

parser = argparse.ArgumentParser(
        prog="LDS Media Downloader",
        description="Automatically downloads collections of LDS videos and formats them for JellyFin",
        epilog="Author: Matthew F DeAngelo")

parser.add_argument("--directory", required=True)
parser.add_argument("--collection-id")

args = parser.parse_args()

handle_series(args.directory, args.collection_id)
