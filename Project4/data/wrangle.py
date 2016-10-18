import re
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'en_US')
print(",".join(["date", "time", "weekday", "week", "ip", "version", "locale", "java", "os", "osversion", "arch"]))
for line in open("lograw.txt", encoding="utf-8"):
	m = re.match(r"^([^ ]+) ([^ ]+ [^ ]+) jbead ([0-9.]+) ([^ ]+), java ([^ ]+)[^,]*, (.*) ([^ ]+) ([^ ]+)\n$", line)
	if m:
		ip = m.group(1)
		date = m.group(2)
		version = m.group(3)
		loc = m.group(4)
		java = m.group(5)
		os = m.group(6)
		osversion = m.group(7)
		arch = m.group(8)
		dt = datetime.datetime.strptime(date, "%d/%b/%Y:%H:%M:%S %z")
		date = dt.strftime("%Y-%m-%d")
		time = dt.strftime("%H:%M:%S")
		weekday = dt.strftime("%A")
		week = dt.strftime("%W")
		# TODO do geoip lookup?
		print(",".join([date, time, weekday, week, ip, version, loc, java, os, osversion, arch]))
