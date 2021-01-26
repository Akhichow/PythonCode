import pytz
import datetime

localtime = datetime.datetime.now()
utctime = datetime.datetime.utcnow()

print("Naive local time is {}".format(localtime))
print("Naive utc is {}".format(utctime))

aware_localtime = pytz.utc.localize(localtime).astimezone()
aware_utctime = pytz.utc.localize(utctime)

print("Aware local time is {}, timezone {}".format(aware_localtime, aware_localtime.tzinfo))
print("Aware utc is {}, timezone {}".format(aware_utctime, aware_utctime.tzinfo))
