import ssl
import certifi
ssl._create_default_https_context = ssl.create_default_context(cafile=certifi.where())

import requests
import os
import zipfile
from io import BytesIO  # Correct for Python 3
import glob
import shapefile
import tempfile
import json

def point_inside_polygon(x, y, poly):
    n = len(poly)
    inside = False
    p1x, p1y = poly[0]
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def download_shapefiles():
    comm_area_url = ("https://data.cityofchicago.org/download/"
                     "9wp7-iasj/application/zip")
    os.makedirs("data", exist_ok=True)

    r = requests.get(comm_area_url)
    f = BytesIO(r.content)  # Use BytesIO in Python 3
    with zipfile.ZipFile(f, 'r') as zipf:
        zipf.extractall("data")

def get_community_area_coords():
    shapefiles = list(glob.glob("data/*.shp"))
    if len(shapefiles) != 1:
        raise ValueError("More than one shapefile found")
    shapefile_name = shapefiles[0]

    sf = shapefile.Reader(shapefile_name)
    shapes = sf.shapes()
    recs = sf.records()

    results = {}
    for i, (shape, rec) in enumerate(zip(shapes, recs)):
        _, temp_out_filename = tempfile.mkstemp()
        _, temp_in_filename = tempfile.mkstemp()

        with open(temp_out_filename, "w") as f:
            for coords in shape.points:
                f.write("%f %f\n" % (coords[0], coords[1]))

        os.system("gdaltransform -s_srs '+proj=tmerc +lat_0=36.66666666666666 "
                  "+lon_0=-88.33333333333333 +k=0.9999749999999999 "
                  "+x_0=300000.0000000001 +y_0=0 +ellps=GRS80 "
                  "+towgs84=0,0,0,0,0,0,0 +units=us-ft +no_defs' "
                  " -t_srs epsg:4326 < "+temp_out_filename+" > "+
                  temp_in_filename)

        with open(temp_in_filename, "r") as f:
            coords = []
            for latlng in f:
                lat, lng, _ = latlng.split()
                coords.append((float(lat), float(lng)))
        results[rec[0]] = coords
    return results

def get_neighborhood_for_point(lat, lng, commareas):
    for commarea, commdata in commareas.items():  # Python 3: use items()
        if point_inside_polygon(lng, lat, commdata):
            return commarea
    return None

if __name__ == "__main__":
    download_shapefiles()
    areas = get_community_area_coords()
    json.dump(areas, open("community_areas.json", "w"), indent=2)
