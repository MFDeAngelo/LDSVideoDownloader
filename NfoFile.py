

def write_season_nfo(nfo_path, title):
    with open(nfo_path, "w") as nfo_file:
        nfo_file.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n');
        nfo_file.write('<tvshow>\n');
        nfo_file.write('  <name>' + title + '</name>\n');
        nfo_file.write('  <genre>Religious</genre>\n');
        nfo_file.write('  <thumb>' + title + '.jpg</thumb>\n');
        nfo_file.write('</tvshow>\n');

def write_episode_nfo(nfo_path, episode):
    with open(nfo_path, "w") as nfo_file:
        nfo_file.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n');
        nfo_file.write('<episode>\n');
        nfo_file.write('  <name>' + episode.title + '</name>\n');
        nfo_file.write('  <plot>' + episode.description + '</plot>\n');
        nfo_file.write('  <genre>Religious</genre>\n');
        nfo_file.write('  <thumb>episode' + str(episode.entry) + '.jpg</thumb>\n');
        nfo_file.write('</episode>\n');
