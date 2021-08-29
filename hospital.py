import datetime as dt


def format_time(x):
        time_list = x.split(":")
        hora = dt.time(int(time_list[0]), int(time_list[1]))
        return hora
    
#Input Nombre edad sexo y hora de ingreso
class Paciente():

    def __init__(self, nombre, edad, sexo, hora_ingreso, hora_egreso = False, covid = False):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.hora_ingreso = hora_ingreso
        self.hora_egreso = hora_egreso
        self.covid = covid
    
    def covid_positive(self): #Si sale positivo de covid hacer esto
        self.covid = True
    
    def egreso(self): 
        self.hora_ingreso = format_time(self.hora_ingreso)
        self.egreso = format_time(self.egreso)
    
    
    
