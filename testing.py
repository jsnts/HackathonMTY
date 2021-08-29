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

def format_time(x):
        time_list = x.split(":")
        hora = dt.time(int(time_list[0]), int(time_list[1]))
        return hora
    
class Paciente:

    def __init__(self, nombre, edad, sexo, hora_ingreso, ala, hora_egreso = False, fecha = dt.date.today(), covid = False):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.hora_ingreso = hora_ingreso
        self.ala = ala
        self.hora_egreso = hora_egreso
        self.covid = covid
        #esto hace que la fecha de todos los objetos sean Datetime, ya sea una fecha de antes o una fecha actual
        if type(fecha) != type(dt.date.today()):
            date = fecha
            date = date.split("-")
            date = list(map(int, date))
            self.fecha = dt.date(date[0], date[1], date[2])
        else:
            self.fecha = fecha
    
    def covid_positive(self): #Si sale positivo de covid hacer esto
        self.covid = True
        #pacientas_expuestos.append(self)
            
    
    def salida(self): 
        self.hora_ingreso = format_time(self.hora_ingreso)
        self.egreso = format_time(self.egreso)
        
obj = Paciente("Javier", 18, "Masculino", "18:03", 2)


with open('/Users/Alberto/Desktop/HACKATHON/HackathonMTY/Hospital In-Out Excel - Hoja 1.csv', mode='a') as file_:
    file_.write(f"\n{obj.nombre}, {obj.edad}, {obj.sexo}, {obj.hora_ingreso}, {obj.ala}, {obj.hora_egreso},{obj.fecha}, {obj.covid}")
    
    
