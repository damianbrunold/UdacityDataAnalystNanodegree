import json

"""
[
   {"as":"AS31272 WildPark Co",
	"city":"Nikolayev",
	"country":"Ukraine",
	"countryCode":"UA",
	"isp":"WildPark Co",
	"lat":46.968,
	"lon":31.9787,
	"org":"ISP NEON",
	"query":"217.77.215.159",
	"region":"",
	"regionName":"Mykolaivs\\'ka oblast",
	"status":"success",
	"timezone":"Europe/Kiev",
	"zip":""},
   ...
]
"""

print("ip,timezone,lat,lon,zip,country,countryCode,city,regionName")
for line in open("iplist.json", encoding="utf-8"):
	if line.startswith('[{"query"'): continue
	datasets = json.loads(line)
	for data in datasets:
		if data["status"] == "success":
			print("\"" + data["query"] + "\"," +
				  "\"" + data["timezone"] + "\"," +
				  str(data["lat"]) + "," +
				  str(data["lon"]) + "," +
				  "\"" + data["zip"] + "\"," + 
				  "\"" + data["country"] + "\"," + 
				  "\"" + data["countryCode"] + "\"," + 
				  "\"" + data["city"] + "\"," + 
				  "\"" + data["regionName"] + "\"")
