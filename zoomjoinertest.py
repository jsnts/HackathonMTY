import pyautogui as pyg 
import webbrowser as wb 
import datetime 
import time
import tamez_lib as t
import csv
from operator import methodcaller
from time import sleep

#This is the start of my user friendly Auto Zoom Joiner
'''
Objectives for my Auto Zoom Joiner:
1- Once you start your program it will run indefinitely until you type in 'stop'
3- It will be user friendly and easy to understand 
4- In terminal it will show how much time is left for the next class 
    * Optional * - The user can customize whether the program shows this at all, or at what intervals 
5- * Optional * - Send a notification to users phone
6- At the end of the zoom class, it quits the zoom class
7- Prendo mi compu y se activa
8- Switch
9- Que aunque este durante clase entre a la clase
'''

week_days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo" ]
today = f"{datetime.date.today()}" #Turns the datetime object into a string
today = today.split("-") #Turns into a list
today = list(map(int, today)) #Turns all strings into an integer
week_num = datetime.date(today[0], today[1], today[2]).weekday() #This gives out what day number of the week it is
day = week_days[week_num] #Finds what day of the week it is

def format_date(x): #This function will check if today you have the class and if not will return None
    if type(x) == type(datetime.date.today()):
        return x
    day_list = x.strip().split(', ')
    if day in day_list: #Checks if today is the class 
        return datetime.date.today()
    else: 
        return None
def format_time(x, nu=1): #This functions accepts example: 9:00-10:00 and returns 9:00 as a datetime object
    time_list = x.split('-')
    time_split = list(map(methodcaller("split", ":"), time_list))
    if nu == 1:
        zoomtime = datetime.time(int(time_split[0][0]), int(time_split[0][1]))
        return zoomtime
    elif nu == 2:
        zoomtime = datetime.time(int(time_split[1][0]), int(time_split[1][1]))
        return zoomtime
def given_datetime(given_date, given_time): #Combines today and the hour of the class to create a complete datetime object
    # YY, MM, DD, HH, MM
    if given_date == None:
        return None
    mydatetime = datetime.datetime.combine(given_date, given_time)
    return mydatetime
def asin_check(x):
    if x == None:
        return False
    if day in x:
        return True
    else:
        return False


class Zoom:
    def __init__(self, name, hour, zoom_link, asin=None, date=datetime.date.today(), teacher=None):
        self.name = name
        self.date = format_date(date)
        self.hour = format_time(hour, 1)
        self.end_hour = format_time(hour, 2)
        self.time = hour
        self.teacher = teacher
        self.asin = asin_check(asin)
        self.zoom_link = str(zoom_link)
        self.compDate = given_datetime(self.date, self.hour)
    def start_class(self):
        sleep(2)
        #This checks if its free time
        if self.zoom_link == "None":
            print("Tienes horas libres" )
            return
        #This checks how much time is let until class starts
        if self.date != None: #This code checks how much time is left till class starts and if the class already finished then zoom class is over
            self.wait_time_sec = (self.compDate - datetime.datetime.now().replace(microsecond=0)).total_seconds()
        else:
            self.wait_time_sec = -1
        if self.wait_time_sec < 0:
            print (f"Ya se acabo la clase de {self.name}")
            return
        print(f"{self.name} empieza en: + {str(self.compDate - datetime.datetime.now())}")
        time.sleep(self.wait_time_sec)

        # zoom app related 
        wb.get(using='chrome').open(self.zoom_link, new=2) #open zoom link in a new window
        time.sleep(5) # given time for the link to show app top-up window
        pyg.click(x=944, y=255, clicks=1, interval=0, button='left') # click on open zoom.app option
        time.sleep(15) # wait for 15 sec
        pyg.click(x=800, y=666, clicks=1, interval=0, button='left') # Enter zoom with turned off camera
        

        
        
class_dict={}

with open('/Users/Alberto/Desktop/PYTHON GENERAL/python  bin  txt files/HorarioPython - Hoja 1.csv', 'r', newline='') as f: #This loop finds all the classes in the file and make them into objects and put them in a dictionary
    reader = enumerate(csv.reader(f))
    for i, row in reader:
        if i > 0:
            class_dict[f'Clase {i}'] = Zoom(row[0], row[2], row[4], row[5], row[1], row[3])            

listadehoy = []

for key, value in class_dict.items(): #This loop finds what clases you have today and puts them in a list
    if datetime.date.today() == value.date:
        listadehoy.append(value)

listadehoy.sort(key=lambda x: x.hour, reverse=False) #This function sorts the list from first class to last class of the day

#Output
print(f'''{t.Color.bold}
¡Hola Alberto!{t.Color.End}
{t.Color.Red}
Bienvenido a tu programa: {t.Color.Red} Auto {t.Color.Cyan} Zoom {t.Color.Red} Joiner
{t.Color.End}''')




asin = ''
alt = 1
def horario():
    global alt
    global asin
    print(f'''

Este es tu horario del dia de hoy: {datetime.date.today(): }
Hoy tienes {len(listadehoy)} materias

{'       Horario': <24}|                Materia
===================================================================''')
    for i in listadehoy:
        if alt % 2 == 0:
            print(f'''{t.Color.bg_White}{t.Color.Black}[Clase {alt}]{i.time: <15}| {i.name}{t.Color.End}
===================================================================''')
        else:
            print(f'''{t.Color.bg_Black}{t.Color.White}[Clase {alt}]{i.time: <15}| {i.name}{t.Color.End}
===================================================================''')
        if i.asin == True:
            asin = asin + f'[Clase {alt}] {i.name}, ' #Añade a la string de asin para decir que asin tinenes
        alt += 1


horario()

if asin == '':
    asin = 'Ninguno'

print(f"\nHoy tienes clase Asincronica de:\n{asin}\n")

progmclase = input("¿Deseas programar otra clase para hoy? ")
   
 
if "s" in progmclase or "S" in progmclase:
    new_class_number = input("¿Cuantas clases nuevas deseas programar para hoy? ")
    if new_class_number == "None" or new_class_number =="none":
        horario()
    else:
        new_class_number = int(new_class_number)
        while True:
            for i in range(new_class_number):
                new_class_list = []
                new_class_list.append(f"{datetime.date.today()}")
                input_list = ["el nombre de la clase", "el horario (ex. 12:00-13:00)", "Link de zoom (escribe 'None' si no hay)"]
                print(f"{t.Color.Cyan}¡Perfecto!{t.Color.End}")
                for i in input_list:
                    new_class_list.append(input(f"Porfavor ingrese {i}\n---> "))
                listadehoy.append(Zoom(new_class_list[1], new_class_list[2], new_class_list[3]))
            listadehoy.sort(key=lambda x: x.hour, reverse=False)
            break
        horario()
else:
    horario()



# with open('/Users/Alberto/Desktop/Reuniones Añadidas - Hoja 1.csv', 'a', newline = '') as f:
#     for i in new_class_list:
#         f.write(i)


    
if len(listadehoy) == 0:
    print("¡Perfecto! Hoy no tienes ninguna clase, mejor checa eso mi pana") 
else: 
    print("Perfecto! Empecemos con tu siguiente clase")   
    for i in listadehoy:
        i.start_class()
        
        
format_time("18:00-19:00")