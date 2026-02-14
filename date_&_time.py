import datetime
date= datetime.date(2026, 1 ,11)
today= datetime.date.today()

time=datetime.time(12, 30 ,0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%y")

target_datatime =datetime.datetime(2026, 1 , 11 , 12 ,30 ,1)
current_datetime=datetime =datetime.datetime.now()

if target_datatime< current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")

print(now)