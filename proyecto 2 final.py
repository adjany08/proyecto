import tkinter as tk
from tkinter import ttk
import os
import sys
from tkinter import filedialog
from tkinter import messagebox
#######################################
rutaEmpresas = "empresas.txt"
rutaTransportes = "transportes.txt"
root = tk.Tk()
#######################################

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
    botonMP2= tk.Button(root, text="opciones generales", width=25,font=("Arial",12), bg="peachpuff",fg="black", command=opcionesUsuario).place(x=250,y=170)
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

    botonIngresando =  tk.Button(root, text="ingresar", font=("Arial",12), bg="peachpuff",fg="black", command=lambda:VerificarClave(clave.get())).place(x=200,y=290)                             
    botonVolver =  tk.Button(root, text="Volver", font=("Arial",12), bg="peachpuff",fg="black", command=menuPrincipal).place(x=500,y=290)


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
    root.geometry("700x400")
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
    botonOA6= tk.Button(root, text="Volver", width=28, font=("Arial",12), bg="peachpuff",fg="black", command=menuPrincipal).place(x=225,y=350)
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
    botonGE3= tk.Button(root, text="Modificar empresa",width=28, font=("Arial",12), bg="peachpuff",fg="black", command=modificarEmpresa).place(x=250,y=230)
    botonGE4= tk.Button(root, text="Mostrar empresas", width=28, font=("Arial",12), bg="peachpuff",fg="black", command=mostrarEmpresas).place(x=250,y=290)
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
    
    

def guardarEmpresa(cedula, nombre, direccion,provincia):
    try:
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
            tk.messagebox.showerror("Error en la cédula", "La cédula debe tener 10 digitos")
    except ValueError:
        tk.messagebox.showerror("Error en la cédula", "La cédula debe tener 10 digitos numericos")

        

def largo(num):
    cont = 0
    while num>0:
        cont += 1
        num = num//10
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
    cedula = tk.StringVar()
    cedulaEntry=tk.Entry(root,textvariable=cedula,width=50).place(x=210, y=150)

    botonEliminarE = tk.Button(root, text="Eliminar empresa", font=("Arial",12), bg="peachpuff",fg="black",command=lambda:eliminarEmpresa(cedula.get()).place(x=300,y=290))
                             
    botonVolver =  tk.Button(root, text="Volver", font=("Arial",12), bg="peachpuff",fg="black", command=opcionesAdmin).place(x=500,y=290)


    root.mainloop

    
def eliminarEmpresa():
    pass

#########################################################################################################################    
def ventanaMostrarEmpresas():

    ventanaMostrar = tk.Toplevel(root)
    frame = tk.Frame(master=ventanaMostrar, width=800, height=800, bg="white")

    botonCerrar = tk.Button(frame, tex="Cerrar", command=lambda:cerrarVentanaMostrar(ventanaMostrar))
    botonCerrar.grid(row=0, column=0)

    labelMensajeLista = tk.Label(frame,text="Lista de empresas", bg="peachpuff")
    labelMensajeLista.grid(row=1, column=0)

    mostrarEmpresas(frame, 3)

    frame.pack
    
def cerrarVentnaMostrar(ventanaMostrar):
    ventanaMostrar.destroy()

def mostrarEmpresas(frameParam,contadorGrid):
    archivo= open(rutaEmpresas, "r")
    contenido = archivo.read()
    lineas = contenido.split("\n")
    listaRetorno=[]
    for linea in lineas:
        partes = linea.split(",")
        listaRetorno += [partes]
        if largo(partes) == 4:
            texto = "Cedula: "+partes[0]+"Empresa: "+partes[1]+"Ubicacion: "+partes[2]+"Provincia: "+partes[3]
            labelMensajeTemp=tk.label(frameParam, text=texto, bg="white", fg="black")
            labelMensajeTemp.grid(row=contadorGrid, column=0)
            contadorGrid += 1
######################################################################################################################

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

    botonGT1= tk.Button(root, text="Agregar transporte", width=28, font=("Arial",12), bg="peachpuff",fg="black", command=VentanaAgregarTransporte).place(x=250,y=110)
    botonGT2= tk.Button(root, text="Eliminar transporte", width=28,font=("Arial",12), bg="peachpuff",fg="black", command=VentanaEliminarTransporte).place(x=250,y=170)
    botonGT3= tk.Button(root, text="Modificar transporte",width=28, font=("Arial",12), bg="peachpuff",fg="black", command=VentanamodificarTransporte).place(x=250,y=230)
    botonGT4= tk.Button(root, text="Mostrar transporte", width=28, font=("Arial",12), bg="peachpuff",fg="black", command=mostrarTransporte).place(x=250,y=290)
    botonGT5= tk.Button(root, text="Volver", width=28, font=("Arial",12), bg="peachpuff",fg="black", command=opcionesAdmin).place(x=250,y=350)

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
                             
    botonVolver =  tk.Button(root, text="Volver", font=("Arial",12), bg="peachpuff",fg="black", command=gestionEmpresas).place(x=500,y=320)

    
    root.mainloop
##################################################################################################################################

def agregarTransporte(placa, marca,modelo,anno,cantEco,cantNor,cantVip):
    try:
        retorno = verificarArchivos(rutaEmpresas)
        contenido = retornaContenidoArchivo(rutaEmpresas)
        existeEmpre = existeEmpresa(contenido, cedula)
        if existeEmpre == True:  
            if placa !="" and marca != "" and modelo != "" and anno != "" and cantEco !="" and cantNor != "" and cantVip !="":
                archivo = open(rutaTransportes,"a")
                archivo.write(str(placa))
                archivo.write(",")
                archivo.write(str(marca))
                archivo.write(",")
                archivo.write(str(modelo))
                archivo.write(",")
                archivo.write(str(anno))
                archivo.write("\n")
                archivo.write(str(cantEco))
                archivo.write("\n")
                archivo.write(str(cantNor))
                archivo.write("\n")
                archivo.write(str(cantVip))
                archivo.write("\n")
                archivo.close
                tk.messagebox.showinfo("Transporte agregado", ("El transporte placa"+" " +placa+" " "ha sido agregada con exito"))
            else:
                tk.messagebox.showerror("Error en los datos", "No deben de haber espacios vacios")
        else:
            tk.messagebox.showerror("Error en los datos", "No deben de haber empresas repetidas")
            
    except ValueError:
        tk.messagebox.showerror("Error en los datos", "Ingrese los datos de forma correcta")
        

def VentanaEliminarTransporte():
    pass

def VentanamodificarTransporte():
    pass

def mostrarTransporte():
    pass
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
    botonGE4= tk.Button(root, text="Mostrar viaje", width=28, font=("Arial",12), bg="peachpuff",fg="black", command=VentanamostrarViaje).place(x=250,y=290)
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
                              command=lambda:guardarViaje(PaisSal.get(),fechaSal.get(),PaisLLe.get(),fechaLLe.get(),empresaYtransporte.get(),MontEco.get(),MontNor.get(),MontVip)).place(x=300,y=320))
                             
    botonVolver =  tk.Button(root, text="Volver", font=("Arial",12), bg="peachpuff",fg="black", command=gestionViaje).place(x=500,y=320)
#########################################################################
def guardarViaje(PaisSal,fechaSal,PaisLLe,fechaLLe,empresaYtransporte,MontEco,MontNor,MontVip):
    try:
        if PaisSal !="" and fechaSal != "" and PaisLLe != "" and fechaLLe != "" and empresaYtransporte !="" and MontEco != "" and MontNor !="" and MontVip !="":
                    archivo = open(rutaTransportes,"a")
                    archivo.write(str(PaisSal))
                    archivo.write(",")
                    archivo.write(str(fechaSal))
                    archivo.write(",")
                    archivo.write(str(PaisLLe))
                    archivo.write(",")
                    archivo.write(str(fechaLLe))
                    archivo.write(",")
                    archivo.write(str(empresaYtransporte))
                    archivo.write("\n")
                    archivo.write(str(MontEco))
                    archivo.write("\n")
                    archivo.write(str(MontNor))
                    archivo.write("\n")
                    archivo.write(str(MontVip))
                    archivo.write("\n")
                    archivo.close
                    tk.messagebox.showinfo("Viaje agregado", ("El viaje numero"+" " +numero+" " "ha sido agregada con exito"))
        
        else:
            tk.messagebox.showerror("Error en los datos", "No deben de haber viajes repetidos")
            
    except ValueError:
        tk.messagebox.showerror("Error en los datos", "Ingrese los datos de forma correcta")
    
def VentanaEliminarViaje():
    pass

def VentanamodificarViaje():
    pass

def VentanamostrarViaje():
    pass
def volverPrincipal():
    pass

def historialReservaciones():
    pass

def estadisticas():
    pass

    
def historialReservaciones():
    pass

def modificarEmpresa():
    pass

    
def opcionesAdministrativas():
    pass

def opcionesUsuario():
    pass

def Salir():
    global root
    root.destroy()
    sys.exit()
#############################################################################


menuPrincipal()    

