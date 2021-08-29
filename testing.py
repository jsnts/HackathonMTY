import datetime as dt
let = "9:00"

def time(x):
    time_list = let.split(":")
    hora = dt.time(int(time_list[0]), int(time_list[1]))
    return hora


date = f"{dt.date.today()}"
date = date.split("-")
date = list(map(int, date))
date_object = dt.date(date[0], date[1], date[2])

print(date_object, type(date_object))