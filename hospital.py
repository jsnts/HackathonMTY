import datetime as dt
import csv


pacientas_expuestos = {}

def format_time(x):
        time_list = x.split(":")
        hora = dt.time(int(time_list[0]), int(time_list[1]))
        return hora
    
#Input Nombre edad sexo y hora de ingreso
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
            date = date.split("/")
            date = list(map(int, date))
            self.fecha = dt.date(date[2], date[1], date[0])
        else:
            self.fecha = fecha
    
    def covid_positive(self): #Si sale positivo de covid hacer esto
        self.covid = True
        #pacientas_expuestos.append(self)
            
    
    def salida(self): 
        self.hora_ingreso = format_time(self.hora_ingreso)
        self.egreso = format_time(self.egreso)
        
    

lista_pacientes_anteriores = []
#checa los pacientes anteriores
with open('/Users/Alberto/Desktop/HACKATHON/HackathonMTY/Hospital In-Out Excel - Hoja 1.csv', 'r', newline='') as f:
    reader = enumerate(csv.reader(f))
    for i, row in reader:
        if i > 0:
            lista_pacientes_anteriores.append(Paciente(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
            

lista_pacientes = []

with open('/Users/Omen/Desktop/github/HackMTY/HackathonMTY/Hospital In-Out Excel - Hoja 1.csv', "w+", newline="") as f:
    myFile = csv.writer(f)
    myFile.writerow(["Nombre", "Edad", "Sexo", "Hora de Ingreso", "ala", "Hora de Egreso", "Fecha", "Covid"])
    noOfpatients = int(input("Cuantos pacientes va a ingresar: "))
    for i in range(noOfpatients):
        nombre = input("Paciente " + str(i + 1) + "Por favor ingresa tu nombre: ")
        edad = input("Paciente " + str(i + 1) + "Por favor ingresa tu edad: ")
        sexo = input("Paciente " + str(i + 1) + "Por favor ingresa tu sexo: ")
        hora_ing = input("Paciente " + str(i + 1) + "Por favor ingresa la hora a la que entro: ")
        ala = input("Paciente " + str(i + 1) + "Por favor ingresa el ala en la que estaba: ")
        hora_egr = input("Paciente " + str(i + 1) + "Por favor ingresa tu hora de salida: ")
        fecha = input("Paciente " + str(i + 1) + "Por favor ingresa la fecha (dd/mm/AAAA): ")
        covid = input("Paciente " + str(i + 1) + "Por favor ingresa si tiene covid: ")
        myFile.writerow ([nombre, edad, sexo, hora_ing, ala, hora_egr, fecha, covid])
    

with open('/Users/Omen/Desktop/github/HackMTY/HackathonMTY/Hospital In-Out Excel - Hoja 1.csv', 'r', newline='') as f:
    reader = enumerate(csv.reader(f))
    for i, row in reader:
        if i > 0:
            lista_pacientes.append(Paciente(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))


print(lista_pacientes)


lista_pacientes_hoy = []
