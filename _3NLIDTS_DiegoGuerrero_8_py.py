import tkinter as tk
from tkinter import messagebox
import re
import mysql.connector  # Para conectar con MySQL

def insertarRegistro(nombres, apellidos, edad, estatura, telefono, genero):
    try:
        # Conectar con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",              # Usuario de MySQL
            password="",   # Contraseña de MySQL
            database="progavanzada"         # Nombre de la base de datos
        )
        cursor = conexion.cursor()
        # Crear el query SQL para insertar el registro
        query = "INSERT INTO BasePA (Nombre, Apellidos, Edad, Estatura, Telefono, Genero) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nombres, apellidos, edad, estatura, telefono, genero)
        # Ejecutar el query
        cursor.execute(query, valores)
        # Guardar los cambios en la base de datos
        conexion.commit()
        # Cerrar la conexión
        cursor.close()
        conexion.close()
        messagebox.showinfo("Información", "Datos guardados en la base de datos con éxito.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al insertar los datos: {err}")

def EnteroValido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        messagebox.showerror("Error Edad", "Valor de edad equivocado")
        return False

def DecimalValido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def TelefonoValido(valor):
    return valor.isdigit() and len(valor) == 10

def TextoValido(valor):
    # Acepta letras con acento, ñ y ü (ej. "Gómez", "Muñoz", "Güemes")
    return bool(re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\\s]+$", valor))

def borrar():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    rbSeleccionGenero.set(0)

def guardar():
    nombres = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    tel = tbTelefono.get()
    estatura = tbEstatura.get()
    genero = ""
    if rbSeleccionGenero.get() == 1:
        genero = "Masculino"
    elif rbSeleccionGenero.get() == 2:
        genero = "Femenino"
    elif rbSeleccionGenero.get() == 3:
        genero = "Otro"   # La columna Genero de BasePA es varchar(10)
    if (EnteroValido(edad) and DecimalValido(estatura) and TelefonoValido(tel) and TextoValido(nombres) and TextoValido(apellidos)):
        datos = "Nombre : " + nombres + "\n" + "Apellidos : " + apellidos + "\n" + "Edad : " + edad + "\n" + "Telefono : " + tel + "\n" + "Estatura : " + estatura + "\n" + "Genero : " + genero
        with open("3NAgoDic26.txt", "a", encoding="utf-8") as archivo:
            insertarRegistro(nombres, apellidos, edad, estatura, tel, genero)
            archivo.write(datos + "\n\n")
        messagebox.showinfo("Informacion", "Datos guardados correctamente \n" + datos)
    else:
        messagebox.showerror("Error", "Algunos de los campos tienen formato equivocado")

ventana = tk.Tk()
ventana.configure(bg="lavender")
ventana.geometry("800x540")
ventana.resizable(False, False)
ventana.title("Actividad 08 - Insertando registros a la Base de Datos (Formulario Vr3)")
rbSeleccionGenero = tk.IntVar()

fuenteLabel = ("Comic Sans MS", 14, "bold")
fuenteTexto = ("Arial", 14)
fuenteRadio = ("Arial", 12)

tk.Label(ventana, text="Nombre:", font=fuenteLabel, bg="lavender").place(x=107, y=31)
tk.Label(ventana, text="Apellidos:", font=fuenteLabel, bg="lavender").place(x=97, y=77)
tk.Label(ventana, text="Teléfono:", font=fuenteLabel, bg="lavender").place(x=98, y=123)
tk.Label(ventana, text="Estatura:", font=fuenteLabel, bg="lavender").place(x=98, y=170)
tk.Label(ventana, text="Edad:", font=fuenteLabel, bg="lavender").place(x=139, y=214)

tbNombre = tk.Entry(ventana, font=fuenteTexto)
tbNombre.place(x=237, y=29, width=262, height=34)
tbApellidos = tk.Entry(ventana, font=fuenteTexto)
tbApellidos.place(x=237, y=78, width=262, height=34)
tbTelefono = tk.Entry(ventana, font=fuenteTexto)
tbTelefono.place(x=237, y=124, width=262, height=34)
tbEstatura = tk.Entry(ventana, font=fuenteTexto)
tbEstatura.place(x=237, y=171, width=262, height=34)
tbEdad = tk.Entry(ventana, font=fuenteTexto)
tbEdad.place(x=237, y=215, width=262, height=34)

gb = tk.LabelFrame(ventana, text="Género", font=("Comic Sans MS", 12, "bold"), bg="lavender")
gb.place(x=79, y=275, width=580, height=74)
rbFemenino = tk.Radiobutton(gb, text="Femenino", font=fuenteRadio, value=2, variable=rbSeleccionGenero, bg="lavender")
rbFemenino.place(x=51, y=5)
rbMasculino = tk.Radiobutton(gb, text="Masculino", font=fuenteRadio, value=1, variable=rbSeleccionGenero, bg="lavender")
rbMasculino.place(x=249, y=5)
rbOtro = tk.Radiobutton(gb, text="Otro", font=fuenteRadio, value=3, variable=rbSeleccionGenero, bg="lavender")
rbOtro.place(x=468, y=5)

btnGuardar = tk.Button(ventana, text="Guardar", font=fuenteLabel, command=guardar)
btnGuardar.place(x=79, y=427, width=141, height=42)
btnLimpiar = tk.Button(ventana, text="Limpiar", font=fuenteLabel, command=borrar)
btnLimpiar.place(x=502, y=425, width=157, height=44)

ventana.mainloop()
