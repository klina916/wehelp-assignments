import urllib.request as request
import json
import re
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)

poiList=data["result"]["results"]
with open("data.csv", "w", encoding="utf-8") as file:
    for poi in poiList:
        region=poi["address"].split('  ', 1)[1]
        pattern=r".*區"
        region = re.search(pattern, region)
        imageUrl=poi["file"].lower().split('jpg')[0]
        imageUrl=imageUrl+"jpg"

        file.write(poi["stitle"]+","+region.group(0)+","+poi["longitude"]+","+poi["latitude"]+','+imageUrl+"\n")
