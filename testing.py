import datetime as dt
let = "9:00"

def time(x):
    time_list = let.split(":")
    hora = dt.time(int(time_list[0]), int(time_list[1]))
    return hora


date = f"{dt.date.today()}"

date_object = dt.datetime.(date, "%Y-%m-%d")

print(date_object, type(date_object))