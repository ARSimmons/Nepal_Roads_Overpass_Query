__author__ = 'Ari'

import json
from urllib2 import urlopen
import datetime
import sys
sys.setrecursionlimit(5000)


def get_overpass_json_data(url):
    """Receive the content of ``url``, parse it as JSON and return the
       object.
    """
    response = urlopen(url)
    data = str(response.read())
    return json.loads(data)

def query_out_timestamp(json_data):
    """ query from each json (way item only) the timestamp
    """


    json_timestamp = json_data['timestamp']

    return json_timestamp



def classify_time(json_timestamp):
    """ compare the local time to the timestamp in the JSON file. Return a
    string which says either
    "two days after quake", "one week after quake", "over a week to 16 days after quake" or "before quake"
    """

    # ex: 2015-05-03 20:55:15.790000
    current_time = datetime.datetime.now()

    # json formatted
    # timestamp looks like this
    # u'2013-08-17T22:41:18Z'
    parsed_json_year = datetime.datetime.strptime(json_timestamp, "%Y-%m-%dT%H:%M:%SZ")

    day_of_quake = datetime.datetime(2015,04,25,hour=06,minute=11,second=26)


    delta = (parsed_json_year - day_of_quake).days


    if delta >= 0 and delta <= 2:
        return "two days after quake"
    elif delta > 2 and delta <= 7:
        return "one week after quake"
    elif delta > 7 and delta <= 16:
        return "over a week to 16 days after quake"
    elif delta > 16 and delta <= 18:
        return "17 or 18 days after quake - day of and day after 7.3 magnitude aftershock"
    elif delta < 0:
        return "before quake"

def assign_stroke_color(classified_time):
    """assign color to display based on classified_time"""

    # neon green if "two days after quake"
    if classified_time == "two days after quake":
        return "#39FF14"

    # yellow if "one week"
    elif classified_time == "one week after quake":
        return "#FFFF00"

    # orange if "16 days"
    elif classified_time == "over a week to 16 days after quake":
        return "#FF9900"

    # red if 17 days - aftershock day
    elif classified_time == "17 or 18 days after quake - day of and day after 7.3 magnitude aftershock":
        return "#FF0000"

    #gray if "over a year ago"
    elif classified_time == "before quake":
        return "#808080"


def write_to_linestring(source, source_coords, classified_time, stroke_color):
    """ write the json into geojson
        takes all the items from one way ("lat", "lon", "id", "user", "tags", "timestamp")
        writes all the items with new tags "last_updated","stroke","stroke-width"
        returns a dict
    """

    coords = []
    # create the coordinates for each way
    for node in source['nodes']:
        # if the item is being edited you will sometimes get a KeyError -
        # no key for the feature yet
        coords.append(source_coords[node])

    if source['type'] == "way":
        ln = {
            "type": "Feature",
            "geometry": {
                "type": 'LineString',
                "coordinates": coords
                },
            "properties": {
                "user": source['user'],
                "id": source['id'],
                "version": source['version'],
                "timestamp": source['timestamp'],
                "road type": source['tags']['highway'],
                "last_updated": classified_time,
                "stroke": stroke_color,
                "stroke-width": 2
                }
            }

    return ln


def extract_coords_from_nodes(source_dict):
    """ write the coords of all .json nodes into a
        dict with the id as the key
    """

    coords = {}
    for element in source_dict['elements']:
        if element['type'] == 'node':
            coords[element['id']] = [float(element['lon']), float(element['lat'])]
    return coords


def __main__():

    # query by nepal name
    nepal_lines ="http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3Barea%5B%22name%22%3D%22%E0%A4%A8%E0%A5%87%E0%A4%AA%E0%A4%BE%E0%A4%B2%22%5D%3B%28way%5B%22highway%22~%22motorway%7Ctrunk%7Cprimary%7Cmotorway_link%7Ctrunk_link%7Cprimary_link%7Cunclassified%7Ctertiary%7Csecondary%7Ctrack%7Cpath%7Cresidential%7Cservice%7Csecondary_link%7Ctertiary_link%22%5D%28area%29%3B%29%3Bout%20meta%3B%3E%3Bout%20skel%20qt%3B%0A"

    # gorkha lines
    gorkha_all = "http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3B%28way%5B%22highway%22~%22motorway%7Ctrunk%7Cprimary%7Cmotorway_link%7Ctrunk_link%7Cprimary_link%7Cunclassified%7Ctertiary%7Csecondary%7Ctrack%7Cpath%22%5D%2827%2E892190893968916%2C84%2E50340270996094%2C28%2E07894754104761%2C84%2E76089477539062%29%3B%29%3Bout%20meta%3B%3E%3Bout%20skel%20qt%3B%0A"

    # shake zone lines
    line_all = "http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3B%28way%5B%22highway%22~%22motorway%7Ctrunk%7Cprimary%7Cmotorway_link%7Ctrunk_link%7Cprimary_link%7Cunclassified%7Ctertiary%7Csecondary%7Ctrack%7Cpath%22%5D%2827%2E610538528074823%2C84%2E38873291015625%2C28%2E357567857801694%2C85%2E418701171875%29%3B%29%3Bout%20meta%3B%3E%3Bout%20skel%20qt%3B%0A"

    # two linestrings
    line_url2 = "http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3Bway%28around%3A50%2C55%2E693309807744484%2C21%2E151986122131348%29%5B%22highway%22~%22secondary%22%5D%3Bout%20meta%20center%3B%3E%3Bout%20skel%20qt%3B%0A"

    outfile = r'C:\Users\Ari\Documents\GitHub\Nepal_Roads_OverpassQuery\nepal_wide_road_data.geojson'

    geojson = { "type": "FeatureCollection", "features": [] }

    all_data_dict = get_overpass_json_data(nepal_lines)


    with open(outfile, 'w') as geojson_file:

        coords_dict = extract_coords_from_nodes(all_data_dict)

        for element in all_data_dict['elements']:

            if element['type'] == "way":
                data_item_timestamp = query_out_timestamp(element)
                data_w_update = classify_time(data_item_timestamp)
                data_item_color = assign_stroke_color(data_w_update)
                line_dict = write_to_linestring(element, coords_dict, data_w_update, data_item_color)
                geojson['features'].append(line_dict)
        json.dump(geojson, geojson_file)


