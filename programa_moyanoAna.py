from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
#CONEXION#######
conexion=sqlite3.connect("final1.db")
conexion.cursor()
#COLORES
colorVerde = "#88C64E"
colorVerde2 = "#77AB47"
colorGris = "#A0A0A0"
colorGris2 = "#50514E"
colorBase = "#FBFAF7"
colorBase2 = "#EEEDEB"
#VENTANA######
ventana= Tk()
ventana.title("Programa Ventas")
#ventana.iconbitmap("imagenes/logo.ico")
ventana.geometry("800x500")
ventana.config(bg=colorBase2)
ventana.resizable(0,0)
#centrarVentana
ancho = ventana.winfo_screenwidth()
largo = ventana.winfo_screenheight()
x = (ancho // 2) - (800//2)
y = (largo // 2) - (700//2)
ventana.geometry(f"{800}x{700}+{x}+{y}")
#INTERFAZ########
frameTitulo= Frame(ventana,bg=colorGris)
frameTitulo.pack()
titulo= Label(frameTitulo,text="PROGRAMA VENTAS",
              font=("Segoe UI Black",13), width=50,
                bg=colorGris)
titulo.pack()
frameBotones=Frame(ventana,bg=colorVerde2)
frameBotones.pack(side=LEFT,fill=Y)
#frameListado=Frame(ventana)

#INICIO#######FRAME LABELL Y ENTRY
frameEntrada=Frame(ventana,bg=colorBase)
frameEntrada.pack(side=LEFT,fill=BOTH,expand=1)
entryBuscador = Entry(frameEntrada,
                      font=("Segoe UI Black",13), 
                      width=40, bg=colorBase2, fg=colorVerde2) 
labelCodigo = Label(frameEntrada, 
                    text="Codigo",font=("Segoe UI Black",12),
                    bg=colorBase,fg=colorGris2)
entryC = Entry(frameEntrada,
                font=("Segoe UI Black",12), state="readonly")
labelTipo = Label(frameEntrada, text="Tipo",
                  font=("Segoe UI Black",12),
                  bg=colorBase,fg=colorGris2)
entryT = Entry(frameEntrada, font=("Segoe UI Black",12),
               bg=colorBase2, fg=colorVerde2)
labelMarca = Label(frameEntrada, text="Marca",
                   font=("Segoe UI Black",12),
                   bg=colorBase,fg=colorGris2)
entryM = Entry(frameEntrada, font=("Segoe UI Black",12),
               bg=colorBase2, fg=colorVerde2)
labelKilos= Label(frameEntrada, text="Kg",
                  font=("Segoe UI Black",12),
                  bg=colorBase,fg=colorGris2)
entryK = Entry(frameEntrada, font=("Segoe UI Black",12),
               bg=colorBase2, fg=colorVerde2)
labelPrecio= Label(frameEntrada, text="Precio",
                   font=("Segoe UI Black",12),
                    bg=colorBase,fg=colorGris2)
entryP = Entry(frameEntrada, font=("Segoe UI Black",12),
               bg=colorBase2, fg=colorVerde2)
labelStock= Label(frameEntrada, text="Stock",
                  font=("Segoe UI Black",12),
                  bg=colorBase,fg=colorGris2)
entryS = Entry(frameEntrada,font=("Segoe UI Black",12),
                bg=colorBase2, fg=colorVerde2)
labelProveedor= Label(frameEntrada, text="Proveedores",
                      font=("Segoe UI Black",12),
                      bg=colorBase,fg=colorGris2)
entryPr = Entry(frameEntrada, font=("Segoe UI Black",12),
                 bg=colorBase2, fg=colorVerde2)
#LUGARRR#########
entryBuscador.grid(row=0,columnspan=4, pady=25,padx=20, sticky=E)
labelCodigo.grid(row=5,column=2, padx=(20,0))
entryC.grid(row=6,column=2,padx=(20,0))
labelTipo.grid(row=7,column=2, padx=(20,0))
entryT.grid(row=8,column=2,padx=(20,0))
labelMarca.grid(row=7,column=3, padx=(20,0))
entryM.grid(row=8,column=3,padx=(20,0))
labelKilos.grid(row=9,column=2, padx=(20,0))
entryK.grid(row=10,column=2,padx=(20,0))
labelPrecio.grid(row=9,column=3, padx=(20,0))
entryP.grid(row=10,column=3,padx=(20,0))
labelStock.grid(row=11,column=2, padx=(20,0))
entryS.grid(row=12,column=2,padx=(20,0))
labelProveedor.grid(row=11,column=3, padx=(20,0))
entryPr.grid(row=12,column=3,padx=(20,0))

#BORONES#########
def buscar():
    #CONEXION
    datoBuscar = (entryBuscador.get(),)
    tabla = conexion.cursor()
    tabla.execute("SELECT * FROM alimentos WHERE codigo =?", datoBuscar)
    datosBuscados = tabla.fetchall()
    tabla.close()
    #CODIGO ABIERTO
    entryC.config(state="normal")
    #SE BORRAN ENTRADAS ANTERIORES
    entryC.delete(0,END)
    entryT.delete(0,END)
    entryM.delete(0,END)
    entryK.delete(0,END)
    entryP.delete(0,END)
    entryS.delete(0,END)
    entryPr.delete(0,END)
    #PARA Q PONGA EL DATO Q VA EN EL LUGAR Q TIENE Q IR
    if(len(datosBuscados) > 0):
        for fila in  datosBuscados:
            entryC.insert(0,fila[0])
            entryT.insert(0,fila[1])
            entryM.insert(0,fila[2])
            entryK.insert(0,fila[3])
            entryP.insert(0,fila[4])
            entryS.insert(0,fila[5])
            entryPr.insert(0,fila[6])
            #AHORA C PUEDE EDITAR Y ELIMINAR
        botonModificar.config(state="normal")
        botonEliminar.config(state="normal")
    else:
        messagebox.showinfo("Programa Ana", "NO EXISTE :(")
    #CODIGO CERRADO
    entryC.config(state="readonly")
botonBuscar = Button(frameEntrada, text="Buscar",
                     command=buscar,font=("Segoe UI Black",11),
                     bg=colorVerde, fg=colorGris2,relief="ridge")
botonBuscar.grid(row=0,column=5, pady=25,sticky=E)

def salir():
    #PREGUNTA
    salir = messagebox.askquestion("Programa Ana",
                                   "Seguro desea salir del programa? ^^")
    if(salir == "yes"):
        ventana.destroy()
#imagenSalir=PhotoImage(file="imagenes/chau.png")
botonSalir = Button(frameBotones,command=salir,text="Salir",
                    #image=imagenSalir,
                    compound="top",
                    font=("Segoe UI Black",11),bg=colorVerde,
                      fg=colorGris2,relief="flat")
botonSalir.pack(side=BOTTOM,fill=X,ipady=10,ipadx=30)

def guardar():
    #PARA Q NO TENGA CAMPOS VACIOS
    if(entryT.get() == "" or
       entryM.get() == "" or
       entryK.get() == "" or
       entryP.get() == "" or
       entryS.get() == "" or
       entryPr.get() == ""):
        messagebox.showwarning("Programa Ana" ,  "Complete todos los campos :|")
    else:
        #SI ESTA LISTO LO GUARDA EN LA BASSE D DATOS
        datos = (entryT.get(),
                 entryM.get(),
                 entryK.get(),
                 entryP.get(),
                 entryS.get(),
                 entryPr.get(),)
        tabla= conexion.cursor()
        tabla.execute("INSERT INTO alimentos(tipo, marca,kilos,precio, stock, proveedor) VALUES(?,?,?,?,?,?)", datos)
        conexion.commit()
        tabla.close()
        messagebox.showinfo("Programa Ana","Guardado correctamente")
        #BORRA LAS ENTRADAS
        entryT.delete(0,END)
        entryM.delete(0,END)
        entryK.delete(0,END)
        entryP.delete(0,END)
        entryS.delete(0,END)
        entryPr.delete(0,END)
    
#imagenGuardar=PhotoImage(file="imagenes/guardar1.png")
botonGuardar = Button(frameBotones,
                      command=guardar,text="Guardar",
                      #image=imagenGuardar,
                      compound="top",
                      font=("Segoe UI Black",11),bg=colorVerde, 
                      fg=colorGris2,relief="flat")
botonGuardar.pack(fill=X,ipady=10,ipadx=30)

def modificar():
    #LO MISMO NO ENTRADAS VACIAS
    if(entryT.get() == "" or
       entryM.get() == "" or
       entryK.get() == "" or
       entryP.get() == "" or
       entryS.get() == "" or
       entryPr.get() == ""):
        messagebox.showwarning("Programa Ana" ,  "Complete todos los campos :|")
    else:
        #BUSCA LOS DATOS DEL COSO GUARDADO
        entryC.config(state="normal")
        datos = (entryT.get(),
                 entryM.get(),
                 entryK.get(),
                 entryP.get(),
                 entryS.get(),
                 entryPr.get(),
                 entryC.get())
        entryC.config(state="readonly")
        tabla = conexion.cursor()
        tabla.execute("UPDATE alimentos SET tipo=?,marca=?,kilos=?,precio=?,stock=?, proveedor=? WHERE codigo=?",datos)
        conexion.commit()
        tabla.close()
        messagebox.showinfo("Programa Ana","Se ha modificado correctamente :)")
#imagenModificar=PhotoImage(file="imagenes/editar.png")
botonModificar = Button(frameBotones,state="disabled",
                        command=modificar,text="Editar",
                        #image=imagenModificar,
                        compound="top",font=("Segoe UI Black",11),
                        bg=colorVerde, fg=colorGris2,relief="flat")
botonModificar.pack(fill=X,ipady=10,ipadx=30)

def eliminar():
    #SI LA COSA DICE SI SE ELIMINA EL REGISTRO
    eliminarCosas = messagebox.askquestion("Programa","Seguro que desea eliminar? :/")
    if(eliminarCosas == "yes"):
        entryC.config(state="normal")
        datos = (entryC.get(), )
        tabla = conexion.cursor()
        tabla.execute("DELETE FROM alimentos WHERE codigo=?",datos)
        conexion.commit()
        tabla.close()
        messagebox.showinfo("Programa Ana","Se ha eliminado correctamente :)")
        entryC.delete(0, END)
        entryT.delete(0,END)
        entryM.delete(0,END)
        entryK.delete(0,END)
        entryP.delete(0,END)
        entryS.delete(0,END)
        entryPr.delete(0,END)
        entryC.config(state="readonly")
        botonModificar.config(state="disabled")
        botonEliminar.config(state="disabled")
#imagenEliminar=PhotoImage(file="imagenes/eliminar.png")
botonEliminar = Button(frameBotones,state="disabled",
                       command=eliminar,text="Borrar",
                       #image=imagenEliminar,
                       compound="top",font=("Segoe UI Black",11),
                       bg=colorVerde, fg=colorGris2,relief="flat")
botonEliminar.pack(fill=X,ipady=10,ipadx=30)

#HACERLISTTTTTTA##############################
conexion = sqlite3.connect("final1.db")
conexion.cursor()

def Listar():
    #OTRA VENTANA
     lista = Toplevel()
     lista.title("LISTA ALIMENTOS")
     lista.geometry("900x800")
     lista.iconbitmap("C:imagenes/lupaico.ico")
     lista.config(bg=colorBase)
     #NO SE CAMBIA D TAMAO
     lista.resizable(0,0)
     #LABEL Y FRAME DE TITULO
     tituloaLista = Label(lista,text="LISTA ALIMENTOS",
                          bg=colorBase2, fg=colorGris2,
                          font=("OCR-B 10 BT",30))
     tituloaLista.pack()
     frameTituloL= Frame(lista,bg="")
     frameTituloL.pack()
     #LISTA FEA
     messagebox.showinfo("LISTA","Se esta mejorando!:D")
     #FRAME LISTBOX Y SU PACK
     framelistado=Frame(lista,bg="")
     framelistado.pack(expand=1,fill=BOTH,pady=10,padx=10)
     cod=Listbox(framelistado,relief="flat",fg="purple")
     cod.pack(side=LEFT,fill=Y)
     tip=Listbox(framelistado,relief="flat",fg="purple")
     tip.pack(side=LEFT,fill=Y)
     mar=Listbox(framelistado,relief="flat",fg="purple")
     mar.pack(side=LEFT,fill=Y)
     kg=Listbox(framelistado,relief="flat",fg="purple")
     kg.pack(side=LEFT,fill=Y)
     pre=Listbox(framelistado,relief="flat",fg="purple")
     pre.pack(side=LEFT,fill=Y)
     sto=Listbox(framelistado,relief="flat",fg="purple")
     sto.pack(side=LEFT,fill=Y)
     pro=Listbox(framelistado,relief="flat",fg="purple")
     pro.pack(side=LEFT,fill=Y)
     #CONEXION CON CADA LISTA
     tabla=conexion.cursor()
     tabla.execute("SELECT codigo FROM alimentos")
     listaC=tabla.fetchall()
     for fila in listaC:
         verCo= fila[0]
         cod.insert(END,verCo)
     tabla=conexion.cursor()
     tabla.execute("SELECT tipo FROM alimentos")
     listaT=tabla.fetchall()
     for fila in listaT:
         verTi= fila[0]
         tip.insert(END,verTi)
     tabla=conexion.cursor()
     tabla.execute("SELECT marca FROM alimentos")
     listaM=tabla.fetchall()
     for fila in listaM:
         verMa= fila[0]
         mar.insert(END,verMa)
     tabla=conexion.cursor()
     tabla.execute("SELECT kilos FROM alimentos")
     listaK=tabla.fetchall()
     for fila in listaK:
         verKg= fila[0]
         kg.insert(END,verKg)
     tabla=conexion.cursor()
     tabla.execute("SELECT precio FROM alimentos")
     listaP=tabla.fetchall()
     for fila in listaP:
         verPre= fila[0]
         pre.insert(END,verPre)
     tabla=conexion.cursor()
     tabla.execute("SELECT stock FROM alimentos")
     listaS=tabla.fetchall()
     for fila in listaS:
         verSt= fila[0]
         sto.insert(END,verSt)
     tabla=conexion.cursor()
     tabla.execute("SELECT proveedor FROM alimentos")
     listaPr=tabla.fetchall()
     for fila in listaPr:
         verPro= fila[0]
         pro.insert(END,verPro)

#imagenListar=PhotoImage(file="imagenes/lista1.png") 
botonListar = Button(frameBotones,command=Listar,text="Listar",
                     #image=imagenListar,
                     compound="top",font=("Segoe UI Black",11),
                     bg=colorVerde, fg=colorGris2,relief="flat")
botonListar.pack(fill=X,ipady=10,ipadx=30)


ventana.mainloop()
