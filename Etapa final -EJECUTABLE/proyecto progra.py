from mysql.connector import cursor
import tbl_usuario
import tbl_prestamo
import tbl_deposito
import tbl_ahorro

from tkinter import ttk
from PIL import ImageTk
from PIL import Image
import random
import PIL.Image
from tkinter import*
from tkinter import messagebox
import sys
import os


window = Tk()
window.geometry("370x400")
window.resizable(False, False)
frame_app = Frame(window, width=1200, height=600 )
window.title('Registro | TransferCloud')
my_table = ttk.Treeview(window)
frame_app.pack()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

path=resource_path("JAJA.ico")
window.iconbitmap(path)

# Inicializando las variables para almacenar lo que escriba el usuario en las cajas de Texto (Entry)
cuenta = IntVar()
nombre = StringVar()
contrasena = IntVar()

def cancelar():
    entry_nombre.delete(0 , END)
    entry_edad.delete(0 , END)
    entry_apellido.delete(0 , END)

def quit():
    window.destroy()


def crear_registro():
    
    
# Creando función "agregar_sala()", función que se ejecuta la dar clic en el botón "Agregar"
# Obteniendo los valores de los widgets Entry mediante la función "GET()" 
    # y almacenandolos en las variables previamente inicializadas
    cuenta = entry_nombre.get()
    nombre = entry_edad.get()
    contrasena = entry_apellido.get()
    
    
    # creando un objeto de la Base de datos "MyDatabase", para acceder a la función "insert_db"
    db_demo = tbl_usuario.MyDatabase()
    # ejecutando la función "insert_db" y enviando las variables como parámetros
    db_demo.insert_db(cuenta, nombre, contrasena)

    

#-------Demás Ventanas------------------------------


    v1 = Toplevel()
    v1.resizable(False,False)
    v1.title("Seleción bancos")
    v1.geometry("370x400")
    
    path=resource_path("JAJA.ico")
    v1.iconbitmap(path)
    
    frame_fondo=Frame(v1, width="360", height="390", bg="#0384fc")
    frame_fondo.place(x=5, y=5)
    L1=Label(frame_fondo,text="Elija su banco de \n preferencia",fg="white",bg="#0384fc",font=("Calibri", "25"), justify="center")
    L1.place(x=45,y=0)

    path=resource_path("banpais.jpg")
    my_image1 = PIL.Image.open(path)
    photo1 = ImageTk.PhotoImage(my_image1)
    path=resource_path("atlantida1png.jpg")
    my_image2 = PIL.Image.open(path)
    photo2 = ImageTk.PhotoImage(my_image2)
    path=resource_path("occidente1.jpg")
    my_image3 = PIL.Image.open(path)
    photo3 = ImageTk.PhotoImage(my_image3)
    
    
    button1 = Button(frame_fondo, bg="#0041a8", text="BANPAÍS",fg="white",font=("Arial", "10", "bold"), command=banco ,image=photo1, width=100, height=120, border=5, cursor="hand2")
    button1.place(x=20, y=110)
    button1.config(activebackground="#0041a8")
    button1.config(activeforeground="#0041a8")
    button1.config(compound="top")
    button2 = Button(frame_fondo, bg="#0041a8",text="ATLÁNTIDA", fg="white", font=("Arial", "10", "bold"), command=banco, image=photo2, width=100, height=120, border=5, cursor="hand2")
    button2.place(x=230, y=110)
    button2.config(activebackground="#0041a8")
    button2.config(activeforeground="#0041a8")
    button2.config(compound="top")
    button3 = Button(frame_fondo,bg="#0041a8", text="OCCIDENTE", fg="white", font=("Arial", "10", "bold"), command=banco, image=photo3, width=100, height=120, border=5, cursor="hand2")
    button3.place(x=120, y=250)
    button3.config(activebackground="#0041a8")
    button3.config(activeforeground="#0041a8")
    button3.config(compound="top")



    
    v1.mainloop()



def banco():        
                    banco = Toplevel()
                    banco.resizable(False,False)
                    banco.title("Transaccion a Realizar")
                    banco.geometry("370x400")
                    
                    path=resource_path("JAJA.ico")
                    banco.iconbitmap(path)

                    path=resource_path("hombre.png")
                    my_image1 = PIL.Image.open(path)
                    photo1 = ImageTk.PhotoImage(my_image1)

                    path=resource_path("Tarjetas.png")
                    my_image2 = PIL.Image.open(path)
                    photo2 = ImageTk.PhotoImage(my_image2)

                    path=resource_path("Depo.png")
                    my_image3 = PIL.Image.open(path)
                    photo3 = ImageTk.PhotoImage(my_image3)
                    frame_fondo=Frame(banco, width="360", height="390", bg="#0384fc")
                    frame_fondo.place(x=5, y=5)

                    L1=Label(frame_fondo,text="Elija un tipo de",fg="white",bg="#0384fc",font=("Calibri", "20"))
                    L1.place(x=95,y=10)
                    L2=Label(frame_fondo,text="transacción a realizar.",fg="white",bg="#0384fc",font=("Calibri", "20"))
                    L2.place(x=65,y=45)


                    button_prestamo = Button(frame_fondo, image=photo1,bg="black", width=160, height=60,cursor="hand2", command=prestamo)
                    button_prestamo.place(x=100, y=140)
                    button_depo = Button(frame_fondo,image=photo3,bg="black", width=160, height=60,cursor="hand2", command=deposito)
                    button_depo.place(x=100, y=230)
                    button_debito = Button(frame_fondo, image=photo2,bg="black",width=160,height=65,cursor="hand2", command=ahorro)
                    button_debito.place(x=100, y=310)

                    



                    banco.mainloop()



        
#Subcomands-----------------------------------------

def prestamo():     
                    window2 = Toplevel()
                    window2.geometry("370x400")
                    window2.resizable(False, False)
                    frame_app = Frame(window2, width=1200, height=600, )
                    window2.title('TransferCloud | Préstamo')
                    my_table = ttk.Treeview(window)
                    frame_app.pack()

                    path=resource_path("JAJA.ico")
                    window2.iconbitmap(path)


# Inicializando las variables para almacenar lo que escriba el usuario en las cajas de Texto (Entry)
                    cuenta = IntVar()
                    nombre = StringVar()
                    monto = IntVar()

                    def cancelar():
                        entry_nombre.delete(0 , END)
                        entry_edad.delete(0 , END)
                        entry_apellido.delete(0 , END)

                    def quit():
                        window2.destroy()


                    def crear_registro():
# Creando función "agregar_sala()", función que se ejecuta la dar clic en el botón "Agregar"
# Obteniendo los valores de los widgets Entry mediante la función "GET()" 
    # y almacenandolos en las variables previamente inicializadas
                        cuenta = entry_nombre.get()
                        nombre = entry_edad.get()
                        monto = entry_apellido.get()

    
                        entry_nombre.delete(0 , END)
                        entry_edad.delete(0 , END)
                        entry_apellido.delete(0 , END)

                        messagebox.showinfo(message="Su transacción se ha realizado con éxito.", title="Transacción") 
    
    # creando un objeto de la Base de datos "MyDatabase", para acceder a la función "insert_db"
                        db_demo = tbl_prestamo.MyDatabase()
    # ejecutando la función "insert_db" y enviando las variables como parámetros
                        db_demo.insert_db(cuenta, nombre, monto)




                    import mysql.connector
                    connection =mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="db_demo")

                    cursor = connection.cursor()
                    cursor.execute("SELECT CUENTA ,NOMBRE, MONTO  FROM TBL_PRESTAMO")


     
    
    
                    my_table = ttk.Treeview(window)
    

                    registro=0
                    for fila in cursor:
                        registro=registro+1
                        print(str(registro) + "-"+str(fila))
      
                        cuenta = fila[0]
                        nombre = fila[1]
                        monto = fila[2]
    
                        my_table.insert(parent="", index="end", iid=registro, text=str(registro),
                            values=(cuenta, nombre, monto))
                    connection.close() 


        # Define Our Columns 
                    my_table['columns'] = ('CUENTA', 'NOMBRE', 'MONTO')







# Widgets dentro del contender OPTIONS
                    frame_form = Frame(window2, width=350, height=380, bg="#0384fc")
                    frame_form.place(x=10, y=10)
                    label_nombre = Label(frame_form, 
                    text="N° DE CUENTA:",
                    font=("Century Gothic", "20", "bold"),
                      fg="white",
                      bg="#0384fc")
                    label_nombre.place(x=30, y=30)
                    entry_nombre = Entry(frame_form, justify=LEFT, width=25, 
                     font=("Century Gothic", "14"))
                    entry_nombre.place(x=30, y=70)

                    label_edad = Label(frame_form, 
                      text="NOMBRE:",
                      font=("Century Gothic", "20", "bold"),
                      fg="white",
                      bg="#0384fc")
                    label_edad.place(x=30, y=100)
                    entry_edad = Entry(frame_form, justify=LEFT, width=25, 
                        font=("Century Gothic", "14"))
                    entry_edad.place(x=30, y=140)

                    label_apellido = Label(frame_form, 
                      text="MONTO A INGRESAR:",
                      font=("Century Gothic", "20", "bold"),
                      fg="white",
                      bg="#0384fc")
                    label_apellido.place(x=30, y=170)
                    entry_apellido = Entry(frame_form, justify=LEFT, width=25, 
                        font=("Century Gothic", "14"))
                    entry_apellido.place(x=30, y=210)


                    button_agregar = Button(frame_form, text="REGISTRAR", 
                        font=("Century Gothic", "14", "bold"),
                        command=crear_registro)
                    button_agregar.place(x=110, y=250)

                    button_cancelar = Button(frame_form, text="CANCELAR", 
                        font=("Century Gothic", "14", "bold"),
                         command=cancelar)
                        
                    button_cancelar.place(x=30, y=300)

                    button_salir = Button(frame_form, text="   SALIR    ", 
                        font=("Century Gothic", "14", "bold"),
                        command=quit)
                        
                    button_salir.place(x=210, y=300)
                    window2.mainloop()




def deposito():     
                    window2 = Toplevel()
                    window2.geometry("370x400")
                    window2.resizable(False, False)
                    frame_app = Frame(window2, width=1200, height=600, )
                    window2.title('TransferCloud | Depósito')
                    my_table = ttk.Treeview(window)
                    frame_app.pack()

                    path=resource_path("JAJA.ico")
                    window2.iconbitmap(path)


# Inicializando las variables para almacenar lo que escriba el usuario en las cajas de Texto (Entry)
                    cuenta = IntVar()
                    nombre = StringVar()
                    monto = IntVar()

                    def cancelar():
                        entry_nombre.delete(0 , END)
                        entry_edad.delete(0 , END)
                        entry_apellido.delete(0 , END)

                    def quit():
                        window2.destroy()


                    def crear_registro():
# Creando función "agregar_sala()", función que se ejecuta la dar clic en el botón "Agregar"
# Obteniendo los valores de los widgets Entry mediante la función "GET()" 
    # y almacenandolos en las variables previamente inicializadas
                        cuenta = entry_nombre.get()
                        nombre = entry_edad.get()
                        monto = entry_apellido.get()

    
                        entry_nombre.delete(0 , END)
                        entry_edad.delete(0 , END)
                        entry_apellido.delete(0 , END)

                        messagebox.showinfo(message="Su transacción se ha realizado con éxito.", title="Transacción") 
    
    # creando un objeto de la Base de datos "MyDatabase", para acceder a la función "insert_db"
                        db_demo = tbl_deposito.MyDatabase()
    # ejecutando la función "insert_db" y enviando las variables como parámetros
                        db_demo.insert_db(cuenta, nombre, monto)




                    import mysql.connector
                    connection =mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="db_demo")

                    cursor = connection.cursor()
                    cursor.execute("SELECT CUENTA ,NOMBRE, MONTO  FROM TBL_DEPOSITO")


     
    
    
                    my_table = ttk.Treeview(window)
    

                    registro=0
                    for fila in cursor:
                        registro=registro+1
                        print(str(registro) + "-"+str(fila))
      
                        cuenta = fila[0]
                        nombre = fila[1]
                        monto = fila[2]
    
                        my_table.insert(parent="", index="end", iid=registro, text=str(registro),
                            values=(cuenta, nombre, monto))
                    connection.close() 


        # Define Our Columns 
                    my_table['columns'] = ('CUENTA', 'NOMBRE', 'MONTO')







# Widgets dentro del contender OPTIONS
                    frame_form = Frame(window2, width=350, height=380, bg="#0384fc")
                    frame_form.place(x=10, y=10)
                    label_nombre = Label(frame_form, 
                    text="N° DE CUENTA:",
                    font=("Century Gothic", "20", "bold"),
                      fg="white",
                      bg="#0384fc")
                    label_nombre.place(x=30, y=30)
                    entry_nombre = Entry(frame_form, justify=LEFT, width=25, 
                     font=("Century Gothic", "14"))
                    entry_nombre.place(x=30, y=70)

                    label_edad = Label(frame_form, 
                      text="NOMBRE:",
                      font=("Century Gothic", "20", "bold"),
                      fg="white",
                      bg="#0384fc")
                    label_edad.place(x=30, y=100)
                    entry_edad = Entry(frame_form, justify=LEFT, width=25, 
                        font=("Century Gothic", "14"))
                    entry_edad.place(x=30, y=140)

                    label_apellido = Label(frame_form, 
                      text="MONTO A INGRESAR:",
                      font=("Century Gothic", "20", "bold"),
                      fg="white",
                      bg="#0384fc")
                    label_apellido.place(x=30, y=170)
                    entry_apellido = Entry(frame_form, justify=LEFT, width=25, 
                        font=("Century Gothic", "14"))
                    entry_apellido.place(x=30, y=210)


                    button_agregar = Button(frame_form, text="REGISTRAR", 
                        font=("Century Gothic", "14", "bold"),
                        command=crear_registro)
                    button_agregar.place(x=110, y=250)

                    button_cancelar = Button(frame_form, text="CANCELAR", 
                        font=("Century Gothic", "14", "bold"),
                         command=cancelar)
                        
                    button_cancelar.place(x=30, y=300)

                    button_salir = Button(frame_form, text="   SALIR    ", 
                        font=("Century Gothic", "14", "bold"),
                        command=quit)
                        
                    button_salir.place(x=210, y=300)
                    window2.mainloop()


    

def ahorro():     
                    window2 = Toplevel()
                    window2.geometry("370x400")
                    window2.resizable(False, False)
                    frame_app = Frame(window2, width=1200, height=600, )
                    window2.title('TransferCloud | Ahorro')
                    my_table = ttk.Treeview(window)
                    frame_app.pack()

                    path=resource_path("JAJA.ico")
                    window2.iconbitmap(path)


# Inicializando las variables para almacenar lo que escriba el usuario en las cajas de Texto (Entry)
                    cuenta = IntVar()
                    nombre = StringVar()
                    monto = IntVar()

                    def cancelar():
                        entry_nombre.delete(0 , END)
                        entry_edad.delete(0 , END)
                        entry_apellido.delete(0 , END)

                    def quit():
                        window2.destroy()


                    def crear_registro():
# Creando función "agregar_sala()", función que se ejecuta la dar clic en el botón "Agregar"
# Obteniendo los valores de los widgets Entry mediante la función "GET()" 
    # y almacenandolos en las variables previamente inicializadas
                        cuenta = entry_nombre.get()
                        nombre = entry_edad.get()
                        monto = entry_apellido.get()

    
                        entry_nombre.delete(0 , END)
                        entry_edad.delete(0 , END)
                        entry_apellido.delete(0 , END)

                        messagebox.showinfo(message="Su transacción se ha realizado con éxito.", title="Transacción") 
    
    # creando un objeto de la Base de datos "MyDatabase", para acceder a la función "insert_db"
                        db_demo = tbl_ahorro.MyDatabase()
    # ejecutando la función "insert_db" y enviando las variables como parámetros
                        db_demo.insert_db(cuenta, nombre, monto)




                    import mysql.connector
                    connection =mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="db_demo")

                    cursor = connection.cursor()
                    cursor.execute("SELECT CUENTA ,NOMBRE, MONTO  FROM TBL_AHORRO")


     
    
    
                    my_table = ttk.Treeview(window)
    

                    registro=0
                    for fila in cursor:
                        registro=registro+1
                        print(str(registro) + "-"+str(fila))
      
                        cuenta = fila[0]
                        nombre = fila[1]
                        monto = fila[2]
    
                        my_table.insert(parent="", index="end", iid=registro, text=str(registro),
                            values=(cuenta, nombre, monto))
                    connection.close() 


        # Define Our Columns 
                    my_table['columns'] = ('CUENTA', 'NOMBRE', 'MONTO')







# Widgets dentro del contender OPTIONS
                    frame_form = Frame(window2, width=350, height=380, bg="#0384fc")
                    frame_form.place(x=10, y=10)
                    label_nombre = Label(frame_form, 
                    text="N° DE CUENTA:",
                    font=("Century Gothic", "20", "bold"),
                      fg="white",
                      bg="#0384fc")
                    label_nombre.place(x=30, y=30)
                    entry_nombre = Entry(frame_form, justify=LEFT, width=25, 
                     font=("Century Gothic", "14"))
                    entry_nombre.place(x=30, y=70)

                    label_edad = Label(frame_form, 
                      text="NOMBRE:",
                      font=("Century Gothic", "20", "bold"),
                      fg="white",
                      bg="#0384fc")
                    label_edad.place(x=30, y=100)
                    entry_edad = Entry(frame_form, justify=LEFT, width=25, 
                        font=("Century Gothic", "14"))
                    entry_edad.place(x=30, y=140)

                    label_apellido = Label(frame_form, 
                      text="MONTO A INGRESAR:",
                      font=("Century Gothic", "20", "bold"),
                      fg="white",
                      bg="#0384fc")
                    label_apellido.place(x=30, y=170)
                    entry_apellido = Entry(frame_form, justify=LEFT, width=25, 
                        font=("Century Gothic", "14"))
                    entry_apellido.place(x=30, y=210)


                    button_agregar = Button(frame_form, text="REGISTRAR", 
                        font=("Century Gothic", "14", "bold"),
                        command=crear_registro)
                    button_agregar.place(x=110, y=250)

                    button_cancelar = Button(frame_form, text="CANCELAR", 
                        font=("Century Gothic", "14", "bold"),
                         command=cancelar)
                        
                    button_cancelar.place(x=30, y=300)

                    button_salir = Button(frame_form, text="   SALIR    ", 
                        font=("Century Gothic", "14", "bold"),
                        command=quit)
                        
                    button_salir.place(x=210, y=300)
                    window2.mainloop()




#Intocableeeeeee!!!----------------------------------------------------



import mysql.connector
connection =mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="db_demo")

cursor = connection.cursor()
cursor.execute("SELECT CUENTA ,NOMBRE, CONTRASENA  FROM TBL_USUARIOS")


     
    
    
my_table = ttk.Treeview(window)
    

registro=0
for fila in cursor:
    registro=registro+1
    print(str(registro) + "-"+str(fila))
      
    cuenta = fila[0]
    nombre = fila[1]
    contrasena = fila[2]
    
    my_table.insert(parent="", index="end", iid=registro, text=str(registro),
        values=(cuenta, nombre, contrasena))
connection.close() 










# Widgets dentro del contender OPTIONS
frame_form = Frame(window, width=350, height=380, bg="#0384fc")
frame_form.place(x=10, y=10)
label_nombre = Label(frame_form, 
              text="N° de cuenta:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#0384fc")
label_nombre.place(x=30, y=30)
entry_nombre = Entry(frame_form, justify=LEFT, width=25, 
             font=("Century Gothic", "14"))
entry_nombre.place(x=30, y=70)

label_edad = Label(frame_form, 
              text="Nombre:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#0384fc")
label_edad.place(x=30, y=100)
entry_edad = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_edad.place(x=30, y=140)

label_apellido = Label(frame_form, 
              text="Contraseña:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#0384fc")
label_apellido.place(x=30, y=170)
entry_apellido = Entry(frame_form, justify=LEFT, width=25, show="*", 
                font=("Century Gothic", "14"))
entry_apellido.place(x=30, y=210)


button_agregar = Button(frame_form, text="Registrar", 
                        font=("Century Gothic", "14", "bold"),
                        command=crear_registro)
button_agregar.place(x=110, y=250)

button_cancelar = Button(frame_form, text="Cancelar", 
                        font=("Century Gothic", "14", "bold"),
                         command=cancelar)
                        
button_cancelar.place(x=30, y=300)

button_salir = Button(frame_form, text="   Salir    ", 
                        font=("Century Gothic", "14", "bold"),
                        command=quit)
                        
button_salir.place(x=210, y=300)
window.mainloop()
#Intocableeeee----------------------------------------
