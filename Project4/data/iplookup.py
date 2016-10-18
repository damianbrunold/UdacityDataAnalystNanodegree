import urllib.request
import time
import json

ips = set([])
for line in open("jbead.csv", encoding="utf-8"):
	parts = line.split(",")
	ips.add(parts[1].strip('"'))

batches = []
batch = []
for ip in ips:
	if len(batch) == 100:
		batches.append(batch)
		batch = []
	batch.append(ip)
if batch:
	batches.append(batch)
	
for batch in batches:
	query = '[' + ','.join(['{"query": "' + b + '"}' for b in batch]) + ']'
	print(query)
	with urllib.request.urlopen(urllib.request.Request("http://ip-api.com/batch", query.encode("ascii"))) as response:
		result = response.read()
		print(result.decode("utf-8"))
	time.sleep(1)
