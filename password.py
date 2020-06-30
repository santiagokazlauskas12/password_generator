import string
import random 


def generate_pass(x,y):
    password_letters=[]
    password_numbers=[]
    
    while len(password_letters)< x:
        password_letters.append(string.ascii_letters[(random.randrange(len(string.ascii_letters)))])

    while len(password_numbers)< y:    
        password_numbers.append(string.digits[(random.randrange(len(string.digits)))])
    
    print("".join(password_numbers + password_letters))

def ingreso():
    x=input("Ingresa en formato numerico, cuantas letras quieres que contenga tu password :  ")

    y=input("Ingresa en formato numerico, cuantos numeros quieres que contenga tu password :  ")
    return x,y


#---------------------------------------------------------------------------------------    

x,y=ingreso()

try:
     x=int(x)
     y=int(y)
    
except:
    print( "Solo puedes ingresar numeros, Ej: 1,3,6")
    ingreso()


generate_pass(x,y)