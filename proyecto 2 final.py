import tkinter as tk #Import de la libreria tkinter y se nombra como tk
from tkinter import ttk  #Import de las funciones ttk desde la libreria tkinter
import sys #import de la libreria sys
from tkinter import messagebox#import de la función messagebox de la libreria tkinter
import random#import de la libreria random

#######################################
rutaEmpresas = "empresas.txt"
rutaTransportes = "transportes.txt"
rutaViajes = "viajes.txt"
root = tk.Tk()
############################################3

def volverPrin():
    global root
    root.destroy()
    root = tk.Tk()
    root.geometry("500x500")
    menuPrincipal()

##############################################

def menuPrincipal():#Función para la cración de la ventana para el menú principal
    global root
    root.destroy
    root.geometry("700x500")
    root.title("Menú principal")
    root.resizable(False,False)
    root.config(bg="white")

    tk.Label(root, text="         MENÚ PRINCIPAL      ", font=("arial", 15),bg="peachpuff" , fg="Black").pack(fill=tk.X)
    tk.Label(root, text="Seleccione una opción" , font=("arial",15),bg="white",fg="gray10").place(x=250,y=40)



    botonMP1= tk.Button(root, text="Opciones administrativas", width=25, font=("Arial",12), bg="peachpuff",fg="black", command=ventanaClave).place(x=250,y=110)
    botonMP2= tk.Button(root, text="Opciones de usuario normal", width=25,font=("Arial",12), bg="peachpuff",fg="black", command=opcionesUsuario).place(x=250,y=170)
    botonMP3= tk.Button(root, text="Salir",width=25, font=("Arial",12), bg="peachpuff",fg="black", command=Salir).place(x=250,y=230)
############################################################################################


def ventanaClave():
    global root
    root.destroy()
    root = tk.Tk()
    root.geometry("700x400")
    root.title("accesando a opciones administrativas")
    root.config(bg=("white"))
    root.resizable(False,False)

    tk.Label(root, text="        Ingresando a opciones administrativas      ", font=("arial", 15),bg="peachpuff" , fg="Black").pack(fill=tk.X)
    


    labelClave = tk.Label(root, bg="white",text="Ingrese la clave de acceso:",font=("arial",15)).place(x=25, y=100)
    clave = tk.StringVar()
    claveEntry=tk.Entry(root,textvariable=clave,width=50).place(x=210, y=150)

    botonIngresando =  tk.Button(root, text="ingresar", font=("Arial",12), bg="peachpuff",fg="black", command=lambda:VerificarClave(clave.get())).place(x=400,y=290)                             
    botonVolver =  tk.Button(root, text="Volver", font=("Arial",12), bg="peachpuff",fg="black", command=volverPrin).place(x=500,y=290)


    root.mainloop

def VerificarClave(clave):
    with open ("clave.txt", "r") as archivo:
        texto = archivo.readlines()
    if texto[0] == clave:
        return opcionesAdmin()
    else:
        tk.messagebox.showerror("Clave incorrecta", "La clave ingresada es incorrecta")
            

#############################################################################################
def opcionesAdmin():
    global root
    root.destroy()
    root = tk.Tk()
    root.geometry("700x500")
    root.title("Opciones administrativas")
    root.config(bg=("white"), cursor="arrow")
    root.resizable(False,False)

    tk.Label(root, text="         Opciones administrativas      ", font=("arial", 15),bg="peachpuff" , fg="Black").pack(fill=tk.X)
    tk.Label(root, text="Seleccione una opción" , font=("arial",15),bg="white",fg="gray10").place(x=250,y=40)

    botonOA1= tk.Button(root, text="Gestión de empresas", width=28, font=("Arial",12), bg="peachpuff",fg="black", command=gestionEmpresas).place(x=225,y=110)
    botonOA2= tk.Button(root, text="Gestión de transporte por empresa", width=28,font=("Arial",12), bg="peachpuff",fg="black", command=gestionTransportes).place(x=225,y=170)
    botonOA3= tk.Button(root, text="Gestión de viaje",width=28, font=("Arial",12), bg="peachpuff",fg="black", command=gestionViaje).place(x=225,y=230)
    botonOA4= tk.Button(root, text="Consultar historial de reservaciones", width=28, font=("Arial",12), bg="peachpuff",fg="black", command=historialReservaciones).place(x=225,y=290)
    botonOA5= tk.Button(root, text="Estadísticas de viaje", width=28, font=("Arial",12), bg="peachpuff",fg="black", command=estadisticas).place(x=225,y=350)
    botonOA6= tk.Button(root, text="Volver", width=28, font=("Arial",12), bg="peachpuff",fg="black", command=volverPrin).place(x=225,y=410)
########################################################################################################
"""
Gestion de empresas
"""
########################################################################################################    
def gestionEmpresas():
    global root
    root.destroy()
    root = tk.Tk()
    root.geometry("700x400")
    root.title("Opciones administrativas")
    root.config(bg=("white"), cursor="arrow")
    root.resizable(False,False)

    tk.Label(root, text="         Gestión de empresas      ", font=("arial", 15),bg="peachpuff" , fg="Black").pack(fill=tk.X)
    tk.Label(root, text="Seleccione una opción" , font=("arial",15),bg="white",fg="gray10").place(x=250,y=40)

    botonGE1= tk.Button(root, text="Agregar empresa", width=28, font=("Arial",12), bg="peachpuff",fg="black", command=VentanaAgregarEmpresas).place(x=250,y=110)
    botonGE2= tk.Button(root, text="Eliminar empresa", width=28,font=("Arial",12), bg="peachpuff",fg="black", command=VentanaEliminarEmpresas).place(x=250,y=170)
    botonGE3= tk.Button(root, text="Modificar empresa",width=28, font=("Arial",12), bg="peachpuff",fg="black", command=VentanaModificarEmpresa).place(x=250,y=230)
    botonGE4= tk.Button(root, text="Mostrar empresas", width=28, font=("Arial",12), bg="peachpuff",fg="black", command=crearVentanaMostrarEmpresas).place(x=250,y=290)
    botonGE5= tk.Button(root, text="Volver", width=28, font=("Arial",12), bg="peachpuff",fg="black", command=opcionesAdmin).place(x=250,y=350)
########################################################################################################    
def VentanaAgregarEmpresas():
    global root
    root.destroy()
    root = tk.Tk()
    root.geometry("700x400")
    root.title("Agregando empresa")
    root.config(bg=("white"))
    root.resizable(False,False)

    tk.Label(root, text="        Agregando empresa      ", font=("arial", 15),bg="peachpuff" , fg="Black").pack(fill=tk.X)
    tk.Label(root, text="Ingrese la informacion de la empresa a guardar" , font=("arial",15),bg="white",fg="gray10").place(x=150,y=40)




    labelCedula = tk.Label(root, bg="white",text="Ingrese la cédula jurídica:",font=("arial",10)).place(x=25, y=100)
    cedula = tk.StringVar()
    cedulaEntry=tk.Entry(root,textvariable=cedula,width=50).place(x=190, y=100)

    labelNombre = tk.Label(root, bg="white",text="Ingrese el nombre de la empresa:",font=("arial",10)).place(x=25, y=150)
    nombre = tk.StringVar()
    nombreEntry=tk.Entry(root,textvariable=nombre,width=50).place(x=225, y=150)


    labelDireccion = tk.Label(root, bg="white",text="Ingrese la direccion de la empresa:",font=("arial",10)).place(x=25, y=200)
    direccion = tk.StringVar()
    direccionEntry=tk.Entry(root,textvariable=direccion,width=50).place(x=230, y=200)


    LabelProvincia = tk.Label(root, text="Provincia:",bg="white",font=("arial",10)).place(x=25, y=250)
    provincia = tk.StringVar()
    comboProvincia=ttk.Combobox(root,textvariable=provincia, values=("San Jose", "Heredia","Limon","Cartago","Puntarenas","Guanacaste","Alajuela")).place(x=100, y=250)

    botonGuardaE = (tk.Button(root, text="Agregar empresa", font=("Arial",12), bg="peachpuff",fg="black",
                              command=lambda:guardarEmpresa(cedula.get(),nombre.get(),direccion.get(),provincia.get())).place(x=300,y=290))
                             
    botonVolver =  tk.Button(root, text="Volver", font=("Arial",12), bg="peachpuff",fg="black", command=gestionEmpresas).place(x=500,y=290)

    
    root.mainloop
    
def existeEmpresa(lista, cedula):#Función que ve si empresa ya existe
    if lista != []:
        empresa = lista[0]
        if empresa[0].lower() == cedula.lower():
            return True
        else:
            return existeEmpresa(lista[1:], cedula)
    else:
        return 0    

def guardarEmpresaMOD(cedula, nombre, direccion,provincia):
    if cedula !="" and nombre != "" and direccion != "" and provincia != "" :
                archivo = open(rutaEmpresas,"a")
                archivo.write(str(cedula))
                archivo.write(",")
                archivo.write(str(nombre))
                archivo.write(",")
                archivo.write(str(direccion))
                archivo.write(",")
                archivo.write(str(provincia))
                archivo.write("\n")
                archivo.close
                tk.messagebox.showinfo("Empresa modificada", ("La empresa " +nombre+" ha sido modificada con exito"))

             
def guardarEmpresa(cedula, nombre, direccion,provincia):
    try:
        contenido = retornaContenidoArchivo(rutaEmpresas)
        if existeEmpresa(contenido,cedula) == True:
            tk.messagebox.showerror("Error ", "Ya existe una emprea registrada con esa cédula ")
        else:
            if largo(int(cedula)) == 10 and cedula!=int:
                if cedula !="" and nombre != "" and direccion != "" and provincia != "" :
                    archivo = open(rutaEmpresas,"a")
                    archivo.write(str(cedula))
                    archivo.write(",")
                    archivo.write(str(nombre))
                    archivo.write(",")
                    archivo.write(str(direccion))
                    archivo.write(",")
                    archivo.write(str(provincia))
                    archivo.write("\n")
                    archivo.close
                    tk.messagebox.showinfo("Empresa agregada", ("La empresa"+" " +nombre+" " "ha sido agregada con exito"))
                else:
                    tk.messagebox.showerror("Error en los datos", "No deben de haber espacios vacios")
            else:
                tk.messagebox.showerror("Error ", "La cédula debe tener 10 digitos numericos ")
    except ValueError:
        tk.messagebox.showerror("Error en la cédula", "La cédula debe tener 10 digitos numericos")        

def largo(num):
    cont = 0
    while num>0:
        cont += 1
        num = num//10
    return cont

def largoL(lista):
    cont=0
    for i in lista:
        cont +=1
    return cont    


##########################################################################################################################################

def VentanaEliminarEmpresas():
    global root
    root.destroy
    root.destroy()
    root = tk.Tk()
    root.geometry("700x400")
    root.title("Eliminando empresa")
    root.config(bg=("white"))
    root.resizable(False,False)

    tk.Label(root, text="        Eliminando empresa      ", font=("arial", 15),bg="peachpuff" , fg="Black").pack(fill=tk.X)
    tk.Label(root, text="Ingrese la informacion de la empresa a eliminar" , font=("arial",15),bg="white",fg="gray10").place(x=150,y=40)




    labelCedula = tk.Label(root, bg="white",text="Ingrese la cédula jurídica de la empresa a eliminar:",font=("arial",15)).place(x=25, y=100)
    cedula1 = tk.StringVar()
    cedulaEntry=tk.Entry(root,textvariable=cedula1,width=50).place(x=210, y=150)

                     
    botonEliminar =  tk.Button(root, text="Eliminar", font=("Arial",12), bg="peachpuff",fg="black", command=lambda:eliminarEmpresa(cedula1.get())).place(x=300,y=290)                             

    botonVolver =  tk.Button(root, text="Volver", font=("Arial",12), bg="peachpuff",fg="black", command=gestionEmpresas).place(x=500,y=290)


    root.mainloop





def retornaContenidoArchivo(rutaEmpresas): #Función que retorna contenido de empresa
    with open(rutaEmpresas, "r") as archivo:
        todoTexto=archivo.read()
    convertirTextoALista = todoTexto.split("\n")
    return convierteALista(convertirTextoALista)



def convierteALista(lista):
    if lista == []:
        return []
    elif lista[0] != "":
        return [lista[0].split(",")] + convierteALista(lista[1:])
    else:
        return convierteALista(lista[1:])



def guardarItems(lista):
    with open (rutaEmpresas, "w") as archivo:
        while lista !=[]:
            linea = ",".join(lista[0])+"\n"
            archivo.write(linea)
            lista = lista[1:]
    
def eliminarEmpresa(cedula):
    empresas = retornaContenidoArchivo(rutaEmpresas)
    nuevaL = []
    elimina = False
    for empre in empresas:
        if cedula != empre[0]:
            nuevaL += [empre]
        else:
            elimina = True
    if(elimina):
        guardarItems(nuevaL)
        tk.messagebox.showinfo("Empresa eliminada", ("La empresa cedula: " +cedula+ " ha sido elminada con exito"))
    else:
        tk.messagebox.showerror("Error en la cedula", "La empresa: "+cedula+" no existe")

##################################################################################################################
def VentanaModificarEmpresa():
    global root
    root.destroy()
    root = tk.Tk()
    root.geometry("700x400")
    root.title("Modificando empresa")
    root.config(bg=("white"))
    root.resizable(False,False)

    tk.Label(root, text="        modificando empresa      ", font=("arial", 15),bg="peachpuff" , fg="Black").pack(fill=tk.X)
    tk.Label(root, text="Ingrese la informacion de la empresa a modificar" , font=("arial",15),bg="white",fg="gray10").place(x=150,y=40)




    labelCedulaM = tk.Label(root, bg="white",text="Ingrese la cédula jurídica:",font=("arial",10)).place(x=25, y=100)
    cedulaM = tk.StringVar()
    cedulaEntry=tk.Entry(root,textvariable=cedulaM,width=50).place(x=190, y=100)

    labelNombreM = tk.Label(root, bg="white",text="Ingrese el nuevo nombre de la empresa:",font=("arial",10)).place(x=25, y=150)
    nombreM = tk.StringVar()
    nombreEntry=tk.Entry(root,textvariable=nombreM,width=50).place(x=278, y=150)


    labelDireccionM = tk.Label(root, bg="white",text="Ingrese la nueva direccion de la empresa:",font=("arial",10)).place(x=25, y=200)
    direccionM = tk.StringVar()
    direccionEntry=tk.Entry(root,textvariable=direccionM,width=50).place(x=278, y=200)


    LabelProvinciaM = tk.Label(root, text="Provincia:",bg="white",font=("arial",10)).place(x=25, y=250)
    provinciaM = tk.StringVar()
    comboProvincia=ttk.Combobox(root,textvariable=provinciaM, values=("San Jose", "Heredia","Limon","Cartago","Puntarenas","Guanacaste","Alajuela")).place(x=100, y=250)

    botonGuardaE = (tk.Button(root, text="Modificar empresa", font=("Arial",12), bg="peachpuff",fg="black",
                              command=lambda:modicarEmpresa(cedulaM.get(),nombreM.get(),direccionM.get(),provinciaM.get())).place(x=300,y=290))
                             
    botonVolver =  tk.Button(root, text="Volver", font=("Arial",12), bg="peachpuff",fg="black", command=gestionEmpresas).place(x=500,y=290)

    
    root.mainloop
    

def modicarEmpresa(cedula, nombreNuevo,direccionNueva,provinciaNueva):
    empresas=retornaContenidoArchivo(rutaEmpresas)
    with open(rutaEmpresas,"w") as archivo:
        archivo.write
    modificarEmpresaAux(empresas,cedula,nombreNuevo,direccionNueva,provinciaNueva)
        
def modificarEmpresaAux(empresas,cedula,nombre,direccion,provincia):
    if empresas != []:
        if largoL(empresas[0]) == 4:
            empresa = empresas[0]
            if empresa[0] == cedula:
                empresa[1] = nombre
                empresa[2] = direccion
                empresa[3] = provincia
            guardarEmpresaMOD(empresa[0], empresa[1], empresa[2],empresa[3])
        modificarEmpresaAux(empresas[1:],cedula,nombre,direccion,provincia)

            

#########################################################################################################################    
def crearVentanaMostrarEmpresas():

    ventanaMostrar = tk.Toplevel(root)
    ventanaMostrar.title("Empresas")
    ventanaMostrar.resizable(False,False)
    frame = tk.Frame(master=ventanaMostrar, width=800, height=800, bg="white")


    labelMensajeLista = tk.Label(frame,text="Lista de empresas",font= ("arial",20), bg="peachpuff")
    labelMensajeLista.grid(row=1, column=0)

    mostrarEmpresas(frame, 3)

    frame.pack()
    


def mostrarEmpresas(frameParam,contadorGrid):
    archivo= open(rutaEmpresas, "r")
    contenido = archivo.read()
    lineas = contenido.split("\n")
    listaRetorno=[]
    for linea in lineas:
        partes = linea.split(",")
        listaRetorno += [partes]
        if largoL(partes) == 4:
            texto = "Cedula: "+partes[0]+" Empresa: "+partes[1]+" Ubicacion: "+partes[2]+" Provincia: "+partes[3]
            labelMensajeTemp=tk.Label(frameParam, text=texto, bg="white", fg="black")
            labelMensajeTemp.grid(row=contadorGrid, column=0)
            contadorGrid += 1
######################################################################################################################
"""
Gestion de transportes
"""
#######################################################################################################################
def gestionTransportes():
    global root
    root.destroy()
    root = tk.Tk()
    root.geometry("700x400")
    root.title("Opciones Gestión de transportes")
    root.config(bg=("white"), cursor="arrow")
    root.resizable(False,False)

    tk.Label(root, text="         Gestión de transportes      ", font=("arial", 15),bg="peachpuff" , fg="Black").pack(fill=tk.X)
    tk.Label(root, text="Seleccione una opción" , font=("arial",15),bg="white",fg="gray10").place(x=250,y=40)

    botonGT1= (tk.Button(root, text="Agregar transporte", width=28, font=("Arial",12),
                         bg="peachpuff",fg="black", command=VentanaAgregarTransporte).place(x=250,y=110))
    botonGT2= (tk.Button(root, text="Eliminar transporte", width=28,font=("Arial",12),
                         bg="peachpuff",fg="black", command=VentanaEliminarTransporte).place(x=250,y=170))
    botonGT3= (tk.Button(root, text="Modificar transporte",width=28, font=("Arial",12),
                         bg="peachpuff",fg="black", command=VentanamodificarTransporte).place(x=250,y=230))
    botonGT4= (tk.Button(root, text="Mostrar transporte", width=28, font=("Arial",12),
                         bg="peachpuff",fg="black", command=crearVentanaMostrarTransporte).place(x=250,y=290))
    botonGT5= (tk.Button(root, text="Volver", width=28, font=("Arial",12),
                         bg="peachpuff",fg="black", command=opcionesAdmin).place(x=250,y=350))

def VentanaAgregarTransporte():
    global root
    root.destroy()
    root = tk.Tk()
    root.geometry("700x400")
    root.title("Agregando empresa")
    root.config(bg=("white"))
    root.resizable(False,False)

    tk.Label(root, text="        Agregando transporte      ", font=("arial", 15),bg="peachpuff" , fg="Black").pack(fill=tk.X)
    tk.Label(root, text="Ingrese la informacion del transporte a guardar" , font=("arial",15),bg="white",fg="gray10").place(x=150,y=40)


    labelPlaca = tk.Label(root, bg="white",text="Ingrese la placa del transporte:",font=("arial",10)).place(x=25, y=70)
    placa = tk.StringVar()
    placaEntry=tk.Entry(root,textvariable=placa,width=50).place(x=225, y=70)

    labelMarca = tk.Label(root, bg="white",text="Ingrese la marca del transporte:",font=("arial",10)).place(x=25, y=100)
    marca = tk.StringVar()
    MarcaEntry=tk.Entry(root,textvariable=marca,width=50).place(x=225, y=100)


    labelModelo = tk.Label(root, bg="white",text="Ingrese el modelo del transporte:",font=("arial",10)).place(x=25, y=130)
    modelo = tk.StringVar()
    modeloEntry=tk.Entry(root,textvariable=modelo,width=50).place(x=225, y=130)


    Labelanno = tk.Label(root, text="Ingrese el año del transporte:",bg="white",font=("arial",10)).place(x=25, y=170)
    anno = tk.StringVar()
    annoEntry= tk.Entry(root,textvariable=anno,width=50).place(x=225, y=170)

    labelEmpresa = tk.Label(root, bg="white",text="Ingrese la empresa del transporte:",font=("arial",10)).place(x=25, y=200)
    empresa = tk.StringVar()
    empresaEntry=tk.Entry(root,textvariable=empresa,width=50).place(x=225, y=200)


    labelCantidadDeAsientosEco= tk.Label(root, bg="white",text="Ingrese la cantidad de asientos economicos :",font=("arial",10)).place(x=25, y=230)
    cantEco = tk.StringVar()
    ecoEntry=tk.Entry(root,textvariable=cantEco,width=20).place(x=295, y=230)

    labelCantidadDeAsientosNor= tk.Label(root, bg="white",text="Ingrese la cantidad de asientos normales :",font=("arial",10)).place(x=25, y=260)
    cantNor = tk.StringVar()
    NorEntry=tk.Entry(root,textvariable=cantNor,width=20).place(x=295, y=260)

    labelCantidadDeAsientosvip= tk.Label(root, bg="white",text="Ingrese la cantidad de asientos vip :",font=("arial",10)).place(x=25, y=290)
    cantVip = tk.StringVar()
    NorEntry=tk.Entry(root,textvariable=cantVip,width=20).place(x=295, y=290)


    botonGuardaT = (tk.Button(root, text="Agregar transporte", font=("Arial",12), bg="peachpuff",fg="black",
                              command=lambda:agregarTransporte(placa.get(),marca.get(),modelo.get(),anno.get(),cantEco.get(),cantNor.get(),cantVip.get())).place(x=300,y=320))
                             
    botonVolver =  tk.Button(root, text="Volver", font=("Arial",12), bg="peachpuff",fg="black", command=gestionTransportes).place(x=500,y=320)

    
    root.mainloop
##################################################################################################################################

def agregarTransporte(placa, marca,modelo,anno,cantEco,cantNor,cantVip):
    try:
        contenido = retornaContenidoArchivo(rutaTransportes)
        if existeEmpresa(contenido,placa) == True:
            tk.messagebox.showerror("Error", "Ya eiste un transporte registrado con ese numero de placa")
        else:
            if placa !="" and marca != "" and modelo != "" and anno != "" and cantEco !="" and cantNor != "" and cantVip !="":
                archivo = open(rutaTransportes,"a")
                archivo.write(str(placa))
                archivo.write(",")
                archivo.write(str(marca))
                archivo.write(",")
                archivo.write(str(modelo))
                archivo.write(",")
                archivo.write(str(anno))
                archivo.write(",")
                archivo.write(str(cantEco))
                archivo.write(",")
                archivo.write(str(cantNor))
                archivo.write(",")
                archivo.write(str(cantVip))
                archivo.write("\n")
                archivo.close
                tk.messagebox.showinfo("Transporte agregado", ("El transporte placa "+placa+ " ha sido agregada con exito"))
            else:
                tk.messagebox.showerror("Error en los datos", "No deben de haber espacios vacios")
                
    except ValueError:
        tk.messagebox.showerror("Error en los datos", "Ingrese los datos de forma correcta")
        
            

def VentanaEliminarTransporte():
    global root
    root.destroy
    root.destroy()
    root = tk.Tk()
    root.geometry("700x400")
    root.title("Eliminando transporte")
    root.config(bg=("white"))
    root.resizable(False,False)

    tk.Label(root, text="        Eliminando transporte      ", font=("arial", 15),bg="peachpuff" , fg="Black").pack(fill=tk.X)
    tk.Label(root, text="Ingrese la informacion del transporte a eliminar" , font=("arial",15),bg="white",fg="gray10").place(x=150,y=40)




    labelplaca = tk.Label(root, bg="white",text="Ingrese la placa del transporte a eliminar:",font=("arial",15)).place(x=25, y=100)
    placa1 = tk.StringVar()
    placaEntry=tk.Entry(root,textvariable=placa1,width=50).place(x=210, y=150)

                     
    botonEliminar =  tk.Button(root, text="Eliminar", font=("Arial",12), bg="peachpuff",fg="black", command=lambda:eliminarTransporte(placa1.get())).place(x=300,y=290)                             

    botonVolver =  tk.Button(root, text="Volver", font=("Arial",12), bg="peachpuff",fg="black", command=gestionTransportes).place(x=500,y=290)


    root.mainloop

def guardarItems(lista):
    with open (rutaTransportes, "w") as archivo:
        while lista !=[]:
            linea = ",".join(lista[0])+"\n"
            archivo.write(linea)
            lista = lista[1:]
    
def eliminarTransporte(placa):
    transportes = retornaContenidoArchivo(rutaTransportes)
    nuevaLT = []
    elimina = False
    for tran in transportes:
        if placa != tran[0]:
            nuevaLT += [tran]
        else:
            elimina = True
    if(elimina):
        guardarItems(nuevaLT)
        tk.messagebox.showinfo("Transporte eliminado", ("El transporte placa: " +placa+ " ha sido elminado con exito"))
    else:
        tk.messagebox.showerror("Error en la placa", "El transporte: "+placa+" no existe")    
###################################################################
def VentanamodificarTransporte():
    global root
    root.destroy()
    root = tk.Tk()
    root.geometry("700x400")
    root.title("Agregando empresa")
    root.config(bg=("white"))
    root.resizable(False,False)

    tk.Label(root, text="        modificando transporte      ", font=("arial", 15),bg="peachpuff" , fg="Black").pack(fill=tk.X)
    tk.Label(root, text="Ingrese la informacion del transporte a guardar" , font=("arial",15),bg="white",fg="gray10").place(x=150,y=40)


    labelPlaca = tk.Label(root, bg="white",text="Ingrese la placa del transporte:",font=("arial",10)).place(x=25, y=70)
    placaM = tk.StringVar()
    placaMEntry=tk.Entry(root,textvariable=placaM,width=50).place(x=225, y=70)

    labelMarca = tk.Label(root, bg="white",text="Ingrese la marca del transporte:",font=("arial",10)).place(x=25, y=100)
    marcaM = tk.StringVar()
    MarcaMEntry=tk.Entry(root,textvariable=marcaM,width=50).place(x=225, y=100)


    labelModelo = tk.Label(root, bg="white",text="Ingrese el modelo del transporte:",font=("arial",10)).place(x=25, y=130)
    modeloM = tk.StringVar()
    modeloMEntry=tk.Entry(root,textvariable=modeloM,width=50).place(x=225, y=130)


    Labelanno = tk.Label(root, text="Ingrese el año del transporte:",bg="white",font=("arial",10)).place(x=25, y=170)
    annoM = tk.StringVar()
    annoMEntry= tk.Entry(root,textvariable=annoM,width=50).place(x=225, y=170)

    labelEmpresa = tk.Label(root, bg="white",text="Ingrese la empresa del transporte:",font=("arial",10)).place(x=25, y=200)
    empresaM = tk.StringVar()
    empresaMEntry=tk.Entry(root,textvariable=empresaM,width=50).place(x=225, y=200)


    labelCantidadDeAsientosEco= tk.Label(root, bg="white",text="Ingrese la cantidad de asientos economicos :",font=("arial",10)).place(x=25, y=230)
    cantEcoM = tk.StringVar()
    ecoMEntry=tk.Entry(root,textvariable=cantEcoM,width=20).place(x=295, y=230)

    labelCantidadDeAsientosNor= tk.Label(root, bg="white",text="Ingrese la cantidad de asientos normales :",font=("arial",10)).place(x=25, y=260)
    cantNorM = tk.StringVar()
    NorMEntry=tk.Entry(root,textvariable=cantNorM,width=20).place(x=295, y=260)

    labelCantidadDeAsientosvip= tk.Label(root, bg="white",text="Ingrese la cantidad de asientos vip :",font=("arial",10)).place(x=25, y=290)
    cantVipM = tk.StringVar()
    VipMEntry=tk.Entry(root,textvariable=cantVipM,width=20).place(x=295, y=290)


    botonGuardaT = (tk.Button(root, text="Agregar transporte", font=("Arial",12), bg="peachpuff",fg="black",
                              command=lambda:modificarTransporte(placaM.get(),marcaM.get(),modeloM.get(),annoM.get(),cantEcoM.get(),cantNorM.get(),cantVipM.get())).place(x=300,y=320))
                             
    botonVolver =  tk.Button(root, text="Volver", font=("Arial",12), bg="peachpuff",fg="black", command=gestionTransportes).place(x=500,y=320)

    
    root.mainloop

def modificarTransporte(placa, marcaNueva,modeloNuevo,annoNuevo,cantEcoNuevo,cantNorNuevo,cantVipNuevo):
    transportes=retornaContenidoArchivo(rutaTransportes)
    with open(rutaTransportes,"w") as archivo:
        archivo.write
    modificarTransporteAux(transportes,placa,marcaNueva,modeloNuevo,annoNuevo,cantEcoNuevo,cantNorNuevo,cantVipNuevo)
        
def modificarTransporteAux(transportes,placa,marca,modelo,anno,cantEco,cantNor,cantVip):
    if transportes != []:
        if largoL(trnasportes[0]) == 7:
            transporte = transportes[0]
            if transporte[0] == placa:
                transporte[1] = marca
                transporte[2] = modelo
                transporte[3] = anno
                transporte[4] = cantEco
                transporte[5] = cantNor
                transporte[6] = cantVip
            guardarTransporteMOD(transporte[0], transporte[1], transporte[2],transporte[3],transporte[4],transporte[5],transporte[6])
        modificarEmpresaAux(transportes[1:],placa,marca,modelo,anno,cantEco,cantNor,cantVip)
       
                
def guardarTransporteMOD(placa,marca,modelo,anno,cantEco,cantNor,cantVip):
    try:
        if placa !="" and marca != "" and modelo != "" and anno != "" and cantEco !="" and cantNor != "" and cantVip !="":
                archivo = open(rutaTransportes,"a")
                archivo.write(str(placa))
                archivo.write(",")
                archivo.write(str(marca))
                archivo.write(",")
                archivo.write(str(modelo))
                archivo.write(",")
                archivo.write(str(anno))
                archivo.write(",")
                archivo.write(str(cantEco))
                archivo.write(",")
                archivo.write(str(cantNor))
                archivo.write(",")
                archivo.write(str(cantVip))
                archivo.write("\n")
                archivo.close
                tk.messagebox.showinfo("Transporte modificado", ("El transporte placa "+placa+ " ha sido modificado con exito"))
        else:
            tk.messagebox.showerror("Error en los datos", "No deben de haber espacios vacios")
    except ValueError:
        tk.messagebox.showerror("Error en los datos", "Error al modificar el transporte")


    
###################################################################
def crearVentanaMostrarTransporte():

    ventanaMostrarT = tk.Toplevel(root)
    ventanaMostrarT.title("Transportes")
    ventanaMostrarT.resizable(False,False)
    frame = tk.Frame(master=ventanaMostrarT, width=800, height=800, bg="white")


    labelMensajeLista = tk.Label(frame,text="Lista de transportes",font=("arial",20), bg="peachpuff")
    labelMensajeLista.grid(row=1, column=0)

    mostrarTransportes(frame, 5)

    frame.pack()

def mostrarTransportes(frameParam,contadorGrid):
    archivo= open(rutaTransportes, "r")
    contenido = archivo.read()
    lineas = contenido.split("\n")
    listaRetorno=[]
    for linea in lineas:
        partes = linea.split(",")
        listaRetorno += [partes]
        if largoL(partes) == 7:
            texto = ("Placa: "+partes[0]+" Marca: "+partes[1]+" Modelo: "+partes[2]+" Año: "+partes[3]+" Cantidad asientos clase económica: "+partes[4]+
                     " Cantidad asientos clase normal: "+partes[5]+" Cantidad asientos clase vip: "+partes[6])
            labelMensajeTemp=tk.Label(frameParam, text=texto, bg="white", fg="black")
            labelMensajeTemp.grid(row=contadorGrid, column=0)
            contadorGrid += 1
######################################################################################################################################

def gestionViaje():
    global root
    root.destroy()
    root = tk.Tk()
    root.geometry("700x400")
    root.title("Opciones gestion de viaje")
    root.config(bg=("white"), cursor="arrow")
    root.resizable(False,False)

    tk.Label(root, text="         Gestión de viajes      ", font=("arial", 15),bg="peachpuff" , fg="Black").pack(fill=tk.X)
    tk.Label(root, text="Seleccione una opción" , font=("arial",15),bg="white",fg="gray10").place(x=250,y=40)

    botonGE1= tk.Button(root, text="Agregar viaje", width=28, font=("Arial",12), bg="peachpuff",fg="black", command=VentanaAgregarViaje).place(x=250,y=110)
    botonGE2= tk.Button(root, text="Eliminar viaje", width=28,font=("Arial",12), bg="peachpuff",fg="black", command=VentanaEliminarViaje).place(x=250,y=170)
    botonGE3= tk.Button(root, text="Modificar viaje",width=28, font=("Arial",12), bg="peachpuff",fg="black", command=VentanamodificarViaje).place(x=250,y=230)
    botonGE4= tk.Button(root, text="Mostrar viaje", width=28, font=("Arial",12), bg="peachpuff",fg="black", command=crearVentanaMostrarViajes).place(x=250,y=290)
    botonGE5= tk.Button(root, text="Volver", width=28, font=("Arial",12), bg="peachpuff",fg="black", command=opcionesAdmin).place(x=250,y=350)
    
def VentanaAgregarViaje():
    global root
    root.destroy()
    root = tk.Tk()
    root.geometry("700x400")
    root.title("Agregando viaje")
    root.config(bg=("white"))
    root.resizable(False,False)

    tk.Label(root, text="        Agregando viaje      ", font=("arial", 15),bg="peachpuff" , fg="Black").pack(fill=tk.X)
    tk.Label(root, text="Ingrese la informacion del viaje a guardar" , font=("arial",15),bg="white",fg="gray10").place(x=150,y=40)


    labelPaisSal = tk.Label(root, bg="white",text="Ingrese el pais y ciudad de salida:",font=("arial",10)).place(x=25, y=70)
    PaisSal = tk.StringVar()
    PaisSalEntry=tk.Entry(root,textvariable=PaisSal,width=50).place(x=225, y=70)

    labellabel = tk.Label(root, bg="white",text="Ingrese la fecha y hora de salida:",font=("arial",10)).place(x=25, y=100)
    fechaSal = tk.StringVar()
    fechaSalEntry=tk.Entry(root,textvariable=fechaSal,width=50).place(x=225, y=100)

    labelPaisLLe = tk.Label(root, bg="white",text="Ingrese el pais y ciudad de llegada:",font=("arial",10)).place(x=25, y=130)
    PaisLLe = tk.StringVar()
    PaisLLeEntry=tk.Entry(root,textvariable=PaisLLe,width=50).place(x=235, y=130)


    labelfechaLLe = tk.Label(root, bg="white",text="ingresa la fecha y hora de llegada:",font=("arial",10)).place(x=25, y=160)
    fechaLLe = tk.StringVar()
    fechaLLeEntry=tk.Entry(root,textvariable=fechaLLe,width=50).place(x=235, y=160)
    


    LabelempresaYtransporte = tk.Label(root, text="Ingrese la empresa y transporte:",bg="white",font=("arial",10)).place(x=25, y=190)
    empresaYtransporte = tk.StringVar()
    empresaYtransporteEntry= tk.Entry(root,textvariable=empresaYtransporte,width=50).place(x=220, y=190)

    
    labelMontEco= tk.Label(root, bg="white",text="Ingrese el monto de la clase economica :",font=("arial",10)).place(x=25, y=220)
    MontEco = tk.StringVar()
    MontEcoEntry=tk.Entry(root,textvariable=MontEco,width=20).place(x=295, y=220)

    labelMontNor= tk.Label(root, bg="white",text="Ingrese el monto de la clase normal :",font=("arial",10)).place(x=25, y=250)
    MontNor = tk.StringVar()
    NorEntry=tk.Entry(root,textvariable=MontNor,width=20).place(x=295, y=250)

    labelMontVip= tk.Label(root, bg="white",text="Ingrese ingrese el monto de la clase vip :",font=("arial",10)).place(x=25, y=290)
    MontVip = tk.StringVar()
    MontVipEntry=tk.Entry(root,textvariable=MontVip,width=20).place(x=295, y=290)


    botonGuardaT = (tk.Button(root, text="Agregar transporte", font=("Arial",12), bg="peachpuff",fg="black",
                              command=lambda:guardarViaje(PaisSal.get(),fechaSal.get(),PaisLLe.get(),fechaLLe.get(),empresaYtransporte.get(),MontEco.get(),MontNor.get(),MontVip.get())).place(x=300,y=320))
                             
    botonVolver =  tk.Button(root, text="Volver", font=("Arial",12), bg="peachpuff",fg="black", command=gestionViaje).place(x=500,y=320)
#########################################################################
def numeroViaje():
    numeroViaje= random.randint(1,9999)
    print(numeroViaje)


def guardarViaje(PaisSal,fechaSal,PaisLLe,fechaLLe,empresaYtransporte,MontEco,MontNor,MontVip):
    try:
        if PaisSal !="" and fechaSal != "" and PaisLLe != "" and fechaLLe != "" and empresaYtransporte !="" and MontEco != "" and MontNor !="" and MontVip !="":
                    numero = random.randint(1,9999)  
                    archivo = open(rutaViajes,"a")
                    archivo.write(str(numero))
                    archivo.write(",")              
                    archivo.write(str(PaisSal))
                    archivo.write(",")
                    archivo.write(str(fechaSal))
                    archivo.write(",")
                    archivo.write(str(PaisLLe))
                    archivo.write(",")
                    archivo.write(str(fechaLLe))
                    archivo.write(",")
                    archivo.write(str(empresaYtransporte))
                    archivo.write(",")
                    archivo.write(str(MontEco))
                    archivo.write(",")
                    archivo.write(str(MontNor))
                    archivo.write(",")
                    archivo.write(str(MontVip))
                    archivo.write("\n")
                    archivo.close
                    tk.messagebox.showinfo("Viaje agregado", ("El viaje numero " +str(numero)+  "ha sido agregada con exito"))
        
        else:
            tk.messagebox.showerror("Error en los datos", "No deben de haber espacios vacios")
            
    except ValueError:
        tk.messagebox.showerror("Error en los datos", "Ingrese los datos de forma correcta")


    
def VentanaEliminarViaje():
    global root
    root.destroy
    root.destroy()
    root = tk.Tk()
    root.geometry("700x400")
    root.title("Eliminando viaje")
    root.config(bg=("white"))
    root.resizable(False,False)

    tk.Label(root, text="        Eliminando viaje      ", font=("arial", 15),bg="peachpuff" , fg="Black").pack(fill=tk.X)
    tk.Label(root, text="Ingrese la informacion del viaje a eliminar" , font=("arial",15),bg="white",fg="gray10").place(x=150,y=40)




    labelCedula = tk.Label(root, bg="white",text="Ingrese el número de viaje  a eliminar:",font=("arial",15)).place(x=25, y=100)
    viaje1 = tk.StringVar()
    viajeEntry=tk.Entry(root,textvariable=viaje1,width=50).place(x=210, y=150)

                     
    botonEliminarV =  tk.Button(root, text="Eliminar", font=("Arial",12), bg="peachpuff",fg="black", command=lambda:eliminarViaje(viaje1.get())).place(x=300,y=290)                             

    botonVolver =  tk.Button(root, text="Volver", font=("Arial",12), bg="peachpuff",fg="black", command=gestionViaje).place(x=500,y=290)


    root.mainloop

def guardarItems(lista):
    with open (rutaViajes, "w") as archivo:
        while lista !=[]:
            linea = ",".join(lista[0])+"\n"
            archivo.write(linea)
            lista = lista[1:]
    
def eliminarViaje(viaje):
    viajes = retornaContenidoArchivo(rutaViajes)
    nuevaLV = []
    elimina = False
    for via in viajes:
        if viaje != via[0]:
            nuevaLV += [via]
        else:
            elimina = True
    if(elimina):
        guardarItems(nuevaLV)
        tk.messagebox.showinfo("Viaje eliminado", ("El viaje numero: " +viaje+ " ha sido elminado con exito"))
    else:
        tk.messagebox.showerror("Error en el viaje", "El viaje numero: "+viaje+" no existe")    




def VentanamodificarViaje():
    pass

def crearVentanaMostrarViajes():

    ventanaMostrarV = tk.Toplevel(root)
    ventanaMostrarV.title("Viajes")
    ventanaMostrarV.resizable(False,False)
    frame = tk.Frame(master=ventanaMostrarV, width=800, height=800, bg="white")


    labelMensajeLista = tk.Label(frame,text="Lista de viajes",font=("arial",20), bg="peachpuff")
    labelMensajeLista.grid(row=1, column=0)

    mostrarViajes(frame, 8)

    frame.pack()

def mostrarViajes(frameParam,contadorGrid):
    archivo= open(rutaViajes, "r")
    contenido = archivo.read()
    lineas = contenido.split("\n")
    listaRetorno=[]
    for linea in lineas:
        partes = linea.split(",")
        listaRetorno += [partes]
        if largoL(partes) == 9:
            texto = ("Numero de viaje : "+partes[0]+" Pais y ciudad de salida : "+partes[1]+" Fecha y hora salida: "+partes[2]+" Pais y ciudad de llegada: "+partes[3]+ " fecha y hora llegada: "+partes[4]+
                     " empresa: "+partes[5]+" monto asientos clase economica: "+partes[6]+" monto asientos clase normal: "+partes[7]+" monto asientos clase vip"+partes[8])
            labelMensajeTemp=tk.Label(frameParam, text=texto, bg="white", fg="black")
            labelMensajeTemp.grid(row=contadorGrid, column=0)
            contadorGrid += 1




def historialReservaciones():
    pass

def estadisticas():
    pass

def opcionesUsuario():
    global root
    root.destroy()
    root = tk.Tk()
    root.geometry("700x500")
    root.title("Opciones usuario")
    root.config(bg=("white"), cursor="arrow")
    root.resizable(False,False)

    tk.Label(root, text="         Opciones usuario      ", font=("arial", 15),bg="peachpuff" , fg="Black").pack(fill=tk.X)
    tk.Label(root, text="Seleccione una opción" , font=("arial",15),bg="white",fg="gray10").place(x=250,y=40)

    botonOU1= tk.Button(root, text="cunsulta de viajes", width=30, font=("Arial",12), bg="peachpuff",fg="black", command=ventanaConsultaViaje).place(x=225,y=110)
    botonOU2= tk.Button(root, text="Reservación de viaje", width=30,font=("Arial",12), bg="peachpuff",fg="black", command=ventanaReservacionViaje).place(x=225,y=170)
    botonOU3= tk.Button(root, text="Gestión de viaje",width=30, font=("Arial",12), bg="peachpuff",fg="black", command=ventanaGestionviaje).place(x=225,y=230)
    botonou4= tk.Button(root, text="Volver", width=30, font=("Arial",12), bg="peachpuff",fg="black",command=volverPrin).place(x=225, y=290)
                                                                                                                                                                             

def ventanaConsultaViaje():
    pass

def ventanaReservacionViaje():
    pass

def ventanaGestionviaje():
    pass
    



def Salir():
    global root
    root.destroy()
    sys.exit()

menuPrincipal()    

