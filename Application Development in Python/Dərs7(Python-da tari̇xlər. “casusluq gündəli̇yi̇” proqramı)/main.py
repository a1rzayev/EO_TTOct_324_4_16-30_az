import datetime

date_time = datetime.datetime(2021, 9, 30, 13, 53, 23, 583)

print(f"object datetime - {date_time}")
print(f"type - {type(date_time)}")

date1 = datetime.date(2025, 4, 20)
time1 = datetime.time(12, 15, 15)

print(f"date - {date1}, typedate - {type(date1)}")
print(f"time - {time1}, typetime - {type(time1)}")

date_now = datetime.datetime.now()
date_today = datetime.datetime.today()
date_date = datetime.date.today()

print(f"date now - {date_now}")
print(f"date today - {date_today}")
print(f"date date - {date_date}")

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekdays_us = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(f"weekday - {weekdays[date_now.weekday()]}")
print(f"isoweekday - {weekdays_us[date_now.isoweekday()]}")

print(f"datetime to str - {date_now.strftime('%d.%m.%Y %H:%M:%S')}")
str_to_datetime = datetime.datetime.strptime("2026/11/13 19:12:35", "%Y/%m/%d %H:%M:%S")
print(str_to_datetime)


ferq = datetime.timedelta(seconds=0, minutes=0, hours=1)

print(date_now - ferq)