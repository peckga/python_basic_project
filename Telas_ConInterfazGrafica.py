
from tkinter import *
from tkinter import ttk
l=[{"Código":"TF0","Descripción":"Pinstripe Suit 1","Material":"98%Algodón, 2%Elastán","Ancho (cm)":160.0,"Peso (g/m2)":220.0,"Precio (S/.)":9.4},{"Código":"TF1","Descripción":"Gabardina Oslo 5","Material":"60%Algodón, 37%Poliéster","Ancho (cm)":145.0,"Peso (g/m2)":300.0,"Precio (S/.)":11.3},{"Código":"TF2","Descripción":"Sarga 2","Material":"50%Poliéster, 50%Poliacril","Ancho (cm)":145.0,"Peso (g/m2)":425.0,"Precio (S/.)":31.8},{"Código":"TF3","Descripción":"Leni 1","Material":"50%Poliéster, 50%Poliacril","Ancho (cm)":145.0,"Peso (g/m2)":410.0,"Precio (S/.)":37.2},{"Código":"TF4","Descripción":"Laurent 3","Material":"100%Poliamida","Ancho (cm)":150.0,"Peso (g/m2)":140.0,"Precio (S/.)":18.8}]
pd1=4
pd2=5.5
pd3=7
pd4=8.5
co=20
nombre_obsequio="USB"
numero_cliente=0
numero_cliente_sorpresa=5
regalo_sorpresa="Agenda"
ctv0=0
ctv1=0
ctv2=0
ctv3=0
ctv4=0
ctmv0=0
ctmv1=0
ctmv2=0
ctmv3=0
ctmv4=0
ita0=0
ita1=0
ita2=0
ita3=0
ita4=0
itag=0
cto=10
pm=[]
p=[]
a=[]
def consultartela():
    vct=Toplevel()
    vct.title("Consultar Telas")
    w, h = vct.winfo_screenwidth(), vct.winfo_screenheight() 
    vct.geometry("%dx%d+0+0" % (w, h))    
    label=Label(vct,text="Código: ").grid(row=0,column=0, sticky='W', padx=10, pady=10)
    combo=ttk.Combobox(vct,values=("TF0","TF1","TF2","TF3","TF4"),state="readonly")
    combo.current(0)
    combo.grid(row=0,column=1)
    label2=Label(vct,text="Descripción: ").grid(row=1,column=0, sticky='W', padx=10, pady=10)
    entry=Entry(vct,width=21)
    entry.grid(row=1,column=1)
    label3=Label(vct,text="Material: ").grid(row=2,column=0, sticky='W', padx=10, pady=10)
    entry2=Entry(vct,width=21)
    entry2.grid(row=2,column=1)
    label4=Label(vct,text="Ancho (cm): ").grid(row=3,column=0, sticky='W', padx=10, pady=10)
    entry3=Entry(vct,width=21)
    entry3.grid(row=3,column=1)
    label5=Label(vct,text="Peso (g/m2): ").grid(row=4,column=0, sticky='W', padx=10, pady=10)
    entry4=Entry(vct,width=21)
    entry4.grid(row=4,column=1)
    label6=Label(vct,text="Precio (S/.): ").grid(row=5,column=0, sticky='W', padx=10, pady=10)
    entry5=Entry(vct,width=21)
    entry5.grid(row=5,column=1)
    button=Button(vct,text="Cerrar",width=21,command=vct.destroy).grid(row=0,column=2, sticky='W', padx=50, pady=10)
    

    entry.insert(0,l[0]["Descripción"])
    entry2.insert(0,l[0]["Material"])
    entry3.insert(0,l[0]["Ancho (cm)"])
    entry4.insert(0,l[0]["Peso (g/m2)"])
    entry5.insert(0,l[0]["Precio (S/.)"])
    def cambioconsulta(event):
        if combo.get()=="TF1":
            entry.delete(0,END)
            entry.insert(0,l[1]["Descripción"])
            entry2.delete(0,END)
            entry2.insert(0,l[1]["Material"])
            entry3.delete(0,END)
            entry3.insert(0,l[1]["Ancho (cm)"])
            entry4.delete(0,END)
            entry4.insert(0,l[1]["Peso (g/m2)"])
            entry5.delete(0,END)
            entry5.insert(0,l[1]["Precio (S/.)"])
        elif combo.get()=="TF2":
            entry.delete(0,END)
            entry.insert(0,l[2]["Descripción"])
            entry2.delete(0,END)
            entry2.insert(0,l[2]["Material"])
            entry3.delete(0,END)
            entry3.insert(0,l[2]["Ancho (cm)"])
            entry4.delete(0,END)
            entry4.insert(0,l[2]["Peso (g/m2)"])
            entry5.delete(0,END)
            entry5.insert(0,l[2]["Precio (S/.)"])
        elif combo.get()=="TF3":
            entry.delete(0,END)
            entry.insert(0,l[3]["Descripción"])
            entry2.delete(0,END)
            entry2.insert(0,l[3]["Material"])
            entry3.delete(0,END)
            entry3.insert(0,l[3]["Ancho (cm)"])
            entry4.delete(0,END)
            entry4.insert(0,l[3]["Peso (g/m2)"])
            entry5.delete(0,END)
            entry5.insert(0,l[3]["Precio (S/.)"])
        elif combo.get()=="TF4":
            entry.delete(0,END)
            entry.insert(0,l[4]["Descripción"])
            entry2.delete(0,END)
            entry2.insert(0,l[4]["Material"])
            entry3.delete(0,END)
            entry3.insert(0,l[4]["Ancho (cm)"])
            entry4.delete(0,END)
            entry4.insert(0,l[4]["Peso (g/m2)"])
            entry5.delete(0,END)
            entry5.insert(0,l[4]["Precio (S/.)"])
        else:
            entry.delete(0,END)
            entry.insert(0,l[0]["Descripción"])
            entry2.delete(0,END)
            entry2.insert(0,l[0]["Material"])
            entry3.delete(0,END)
            entry3.insert(0,l[0]["Ancho (cm)"])
            entry4.delete(0,END)
            entry4.insert(0,l[0]["Peso (g/m2)"])
            entry5.delete(0,END)
            entry5.insert(0,l[0]["Precio (S/.)"])
    combo.bind("<<ComboboxSelected>>",cambioconsulta)
def modificartela():
    def grabar():
        if combo.current()==0:
            l[0]["Descripción"]=entry.get()
            l[0]["Material"]=entry2.get()
            l[0]["Ancho (cm)"]=entry3.get()
            l[0]["Peso (g/m2)"]=entry4.get()
            l[0]["Precio (S/.)"]=entry5.get()
        elif combo.current()==1:
            l[1]["Descripción"]=entry.get()
            l[1]["Material"]=entry2.get()
            l[1]["Ancho (cm)"]=entry3.get()
            l[1]["Peso (g/m2)"]=entry4.get()
            l[1]["Precio (S/.)"]=entry5.get()
        elif combo.current()==2:
            l[2]["Descripción"]=entry.get()
            l[2]["Material"]=entry2.get()
            l[2]["Ancho (cm)"]=entry3.get()
            l[2]["Peso (g/m2)"]=entry4.get()
            l[2]["Precio (S/.)"]=entry5.get()
        elif combo.current()==3:
            l[3]["Descripción"]=entry.get()
            l[3]["Material"]=entry2.get()
            l[3]["Ancho (cm)"]=entry3.get()
            l[3]["Peso (g/m2)"]=entry4.get()
            l[3]["Precio (S/.)"]=entry5.get()
        elif combo.current()==4:
            l[4]["Descripción"]=entry.get()
            l[4]["Material"]=entry2.get()
            l[4]["Ancho (cm)"]=entry3.get()
            l[4]["Peso (g/m2)"]=entry4.get()
            l[4]["Precio (S/.)"]=entry5.get()
    vmt=Toplevel()
    vmt.title("Modificar Telas")
    w, h = vmt.winfo_screenwidth(), vmt.winfo_screenheight() 
    vmt.geometry("%dx%d+0+0" % (w, h))    
    label=Label(vmt,text="Código: ").grid(row=0,column=0, sticky='W', padx=10, pady=10)
    combo=ttk.Combobox(vmt,values=("TF0","TF1","TF2","TF3","TF4"),state="readonly")
    combo.current(0)
    combo.grid(row=0,column=1)
    label2=Label(vmt,text="Descripción: ").grid(row=1,column=0, sticky='W', padx=10, pady=10)
    entry=Entry(vmt,width=21)
    entry.grid(row=1,column=1)
    label3=Label(vmt,text="Material: ").grid(row=2,column=0, sticky='W', padx=10, pady=10)
    entry2=Entry(vmt,width=21)
    entry2.grid(row=2,column=1)
    label4=Label(vmt,text="Ancho (cm): ").grid(row=3,column=0, sticky='W', padx=10, pady=10)
    entry3=Entry(vmt,width=21)
    entry3.grid(row=3,column=1)
    label5=Label(vmt,text="Peso (g/m2): ").grid(row=4,column=0, sticky='W', padx=10, pady=10)
    entry4=Entry(vmt,width=21)
    entry4.grid(row=4,column=1)
    label6=Label(vmt,text="Precio (S/.): ").grid(row=5,column=0, sticky='W', padx=10, pady=10)
    entry5=Entry(vmt,width=21)
    entry5.grid(row=5,column=1)
    button=Button(vmt,text="Cerrar",width=21,command=vmt.destroy).grid(row=0,column=2, sticky='W', padx=50, pady=10)
    button2=Button(vmt, text="Grabar",width=21,command=grabar).grid(row=1,column=2, sticky='W', padx=50, pady=10)
    entry.insert(0,l[0]["Descripción"])
    entry2.insert(0,l[0]["Material"])
    entry3.insert(0,l[0]["Ancho (cm)"])
    entry4.insert(0,l[0]["Peso (g/m2)"])
    entry5.insert(0,l[0]["Precio (S/.)"])
    def cambioconsulta(event):
        if combo.get()=="TF1":
            entry.delete(0,END)
            entry.insert(0,l[1]["Descripción"])
            entry2.delete(0,END)
            entry2.insert(0,l[1]["Material"])
            entry3.delete(0,END)
            entry3.insert(0,l[1]["Ancho (cm)"])
            entry4.delete(0,END)
            entry4.insert(0,l[1]["Peso (g/m2)"])
            entry5.delete(0,END)
            entry5.insert(0,l[1]["Precio (S/.)"])
        elif combo.get()=="TF2":
            entry.delete(0,END)
            entry.insert(0,l[2]["Descripción"])
            entry2.delete(0,END)
            entry2.insert(0,l[2]["Material"])
            entry3.delete(0,END)
            entry3.insert(0,l[2]["Ancho (cm)"])
            entry4.delete(0,END)
            entry4.insert(0,l[2]["Peso (g/m2)"])
            entry5.delete(0,END)
            entry5.insert(0,l[2]["Precio (S/.)"])
        elif combo.get()=="TF3":
            entry.delete(0,END)
            entry.insert(0,l[3]["Descripción"])
            entry2.delete(0,END)
            entry2.insert(0,l[3]["Material"])
            entry3.delete(0,END)
            entry3.insert(0,l[3]["Ancho (cm)"])
            entry4.delete(0,END)
            entry4.insert(0,l[3]["Peso (g/m2)"])
            entry5.delete(0,END)
            entry5.insert(0,l[3]["Precio (S/.)"])
        elif combo.get()=="TF4":
            entry.delete(0,END)
            entry.insert(0,l[4]["Descripción"])
            entry2.delete(0,END)
            entry2.insert(0,l[4]["Material"])
            entry3.delete(0,END)
            entry3.insert(0,l[4]["Ancho (cm)"])
            entry4.delete(0,END)
            entry4.insert(0,l[4]["Peso (g/m2)"])
            entry5.delete(0,END)
            entry5.insert(0,l[4]["Precio (S/.)"])
        else:
            entry.delete(0,END)
            entry.insert(0,l[0]["Descripción"])
            entry2.delete(0,END)
            entry2.insert(0,l[0]["Material"])
            entry3.delete(0,END)
            entry3.insert(0,l[0]["Ancho (cm)"])
            entry4.delete(0,END)
            entry4.insert(0,l[0]["Peso (g/m2)"])
            entry5.delete(0,END)
            entry5.insert(0,l[0]["Precio (S/.)"])
    combo.bind("<<ComboboxSelected>>",cambioconsulta)
def listartela():
    def listar():
        text.insert(INSERT,"Código: "+l[0]["Código"]+"\n")
        text.insert(INSERT,"Descripción: "+l[0]["Descripción"]+"\n")
        text.insert(INSERT,"Material: "+l[0]["Material"]+"\n")
        text.insert(INSERT,"Ancho (cm): "+str(l[0]["Ancho (cm)"])+"\n")
        text.insert(INSERT,"Peso (g/m2): "+str(l[0]["Peso (g/m2)"])+"\n")
        text.insert(INSERT,"Precio (S/.): "+str(l[0]["Precio (S/.)"])+"\n\n\n")
        
        text.insert(INSERT,"Código: "+l[1]["Código"]+"\n")
        text.insert(INSERT,"Descripción: "+l[1]["Descripción"]+"\n")
        text.insert(INSERT,"Material: "+l[1]["Material"]+"\n")
        text.insert(INSERT,"Ancho (cm): "+str(l[1]["Ancho (cm)"])+"\n")
        text.insert(INSERT,"Peso (g/m2): "+str(l[1]["Peso (g/m2)"])+"\n")
        text.insert(INSERT,"Precio (S/.): "+str(l[1]["Precio (S/.)"])+"\n\n\n")
        
        text.insert(INSERT,"Código: "+l[2]["Código"]+"\n")
        text.insert(INSERT,"Descripción: "+l[2]["Descripción"]+"\n")
        text.insert(INSERT,"Material: "+l[2]["Material"]+"\n")
        text.insert(INSERT,"Ancho (cm): "+str(l[2]["Ancho (cm)"])+"\n")
        text.insert(INSERT,"Peso (g/m2): "+str(l[2]["Peso (g/m2)"])+"\n")
        text.insert(INSERT,"Precio (S/.): "+str(l[2]["Precio (S/.)"])+"\n\n\n")

        text.insert(INSERT,"Código: "+l[3]["Código"]+"\n")
        text.insert(INSERT,"Descripción: "+l[3]["Descripción"]+"\n")
        text.insert(INSERT,"Material: "+l[3]["Material"]+"\n")
        text.insert(INSERT,"Ancho (cm): "+str(l[3]["Ancho (cm)"])+"\n")
        text.insert(INSERT,"Peso (g/m2): "+str(l[3]["Peso (g/m2)"])+"\n")
        text.insert(INSERT,"Precio (S/.): "+str(l[3]["Precio (S/.)"])+"\n\n\n")
        
        text.insert(INSERT,"Código: "+l[4]["Código"]+"\n")
        text.insert(INSERT,"Descripción: "+l[4]["Descripción"]+"\n")
        text.insert(INSERT,"Material: "+l[4]["Material"]+"\n")
        text.insert(INSERT,"Ancho (cm): "+str(l[4]["Ancho (cm)"])+"\n")
        text.insert(INSERT,"Peso (g/m2): "+str(l[4]["Peso (g/m2)"])+"\n")
        text.insert(INSERT,"Precio (S/.): "+str(l[4]["Precio (S/.)"])+"\n\n\n")

    vlt=Toplevel()
    vlt.title("Listar Telas")
    w, h = vlt.winfo_screenwidth(), vlt.winfo_screenheight() 
    vlt.geometry("%dx%d+0+0" % (w, h))
    text=Text(vlt, height=30, width=170,background="#D3D3D3")
    text.grid(row=0,columnspan=2,padx=15,pady=15)
    button=Button(vlt,text="Cerrar",width=21,command=vlt.destroy).grid(row=1,column=0,sticky=E,padx=20)
    button2=Button(vlt,text="Listar",width=21,command=listar).grid(row=1,column=1,sticky=W,padx=20)

def vender():
    
    def venta():
        global numero_cliente, ctv0, ctmv0,ita0,ctv1, ctmv1,ita1, ctv2, ctmv2,ita2, ctv3, ctmv3,ita3, ctv4, ctmv4,ita4, itag
        text.delete(1.0,END)
        text.insert(INSERT,"Código: "+"\t\t\t\t"+combo.get()+"\n")
        text.insert(INSERT,"Descripción: "+"\t\t\t\t"+entry.get()+"\n")
        if combo.get()=="TF1":
            precio=l[1]["Precio (S/.)"]
        elif combo.get()=="TF2":
            precio=l[2]["Precio (S/.)"]
        elif combo.get()=="TF3":
            precio=l[3]["Precio (S/.)"]
        elif combo.get()=="TF4":
            precio=l[4]["Precio (S/.)"]
        else:
            precio=l[0]["Precio (S/.)"]
        text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f"{precio: 12.2f}"+"\n")
        cantidad = int(entry2.get())
        text.insert(INSERT,"Cantidad de metros: "+"\t\t\t\t"+f"{cantidad: 16.2f}"+"\n")
        importe_compra = round(float(precio) * cantidad,2)
        text.insert(INSERT,"Importe de compra: "+"\t\t\t\t"+"S/. "+f"{importe_compra: 12.2f}"+"\n")
        if 1<=cantidad<6:
            id=round((pd1/100)*importe_compra,2)
        elif cantidad < 11:
            id=round((pd2/100)*importe_compra,2)
        elif cantidad < 16:
            id=round((pd3/100)*importe_compra,2)
        elif cantidad >=16:
            id=round((pd4/100)*importe_compra,2)
        text.insert(INSERT,"Importe de descuento: "+"\t\t\t\t"+"S/. "+f"{id: 12.2f}"+"\n")
        importe_pagar=importe_compra-id
        text.insert(INSERT,"Importe a pagar: "+"\t\t\t\t"+"S/. "+f"{importe_pagar: 12.2f}"+"\n")
        if cantidad>=co:
            obsequio=nombre_obsequio
        else:
            obsequio="No corresponde"
        text.insert(INSERT,"Obsequio: "+"\t\t\t\t"+obsequio+"\n")
        
        numero_cliente+=1
        if numero_cliente==numero_cliente_sorpresa:
            sorpresa=regalo_sorpresa
        else:
            sorpresa="No corresponde"
        text.insert(INSERT,"Premio sorpresa: "+"\t\t\t\t"+sorpresa+"\n")
        if combo.get()=="TF1":
            ctv1+=1
            ctmv1+=cantidad
            ita1+=importe_pagar
        elif combo.get()=="TF2":
            ctv2+=1
            ctmv2+=cantidad
            ita2+=importe_pagar
        elif combo.get()=="TF3":
            ctv3+=1
            ctmv3+=cantidad
            ita3+=importe_pagar
        elif combo.get()=="TF4":
            ctv4+=1
            ctmv4+=cantidad
            ita4+=importe_pagar
        else:
            ctv0+=1
            ctmv0+=cantidad
            ita0+=importe_pagar
        itag=ita0+ita1+ita2+ita3+ita4

    vve=Toplevel()
    vve.title("Vender")
    w, h = vve.winfo_screenwidth(), vve.winfo_screenheight() 
    vve.geometry("%dx%d+0+0" % (w, h))    
    label=Label(vve,text="Código: ").grid(row=0,column=0, sticky='W', padx=10, pady=10)
    combo=ttk.Combobox(vve,values=("TF0","TF1","TF2","TF3","TF4"),state="readonly")
    combo.current(0)
    combo.grid(row=0,column=1)
    label2=Label(vve,text="Descripción: ").grid(row=1,column=0, sticky='W', padx=10, pady=10)
    entry=Entry(vve,width=21)
    entry.grid(row=1,column=1)
    
    label3=Label(vve,text="Cantidad de metros: ").grid(row=2,column=0, sticky='W', padx=10, pady=10)
    entry2=Entry(vve,width=21)
    entry2.grid(row=2,column=1)

    text=Text(vve, height=30, width=170,background="#D3D3D3")
    text.grid(row=3,columnspan=4,padx=15,pady=15)

    button=Button(vve,text="Cerrar",width=21,command=vve.destroy).grid(row=1,column=3,sticky=E,padx=20)
    button2=Button(vve,text="Vender",width=21,command=venta).grid(row=0,column=3,sticky=E,padx=20)

    entry.insert(0,l[0]["Descripción"])
    
    def cambioconsulta(event):
        if combo.get()=="TF1":
            entry.delete(0,END)
            entry.insert(0,l[1]["Descripción"])
            
        elif combo.get()=="TF2":
            entry.delete(0,END)
            entry.insert(0,l[2]["Descripción"])
            
        elif combo.get()=="TF3":
            entry.delete(0,END)
            entry.insert(0,l[3]["Descripción"])
            
        elif combo.get()=="TF4":
            entry.delete(0,END)
            entry.insert(0,l[4]["Descripción"])
            
        else:
            entry.delete(0,END)
            entry.insert(0,l[0]["Descripción"])
            
    combo.bind("<<ComboboxSelected>>",cambioconsulta)

def generar_reportes():
    
    vgr=Toplevel()
    vgr.title("Generar Reportes")
    w, h = vgr.winfo_screenwidth(), vgr.winfo_screenheight() 
    vgr.geometry("%dx%d+0+0" % (w, h))    
    label=Label(vgr,text="Tipo de reporte: ").grid(row=0,column=0, sticky='W', padx=10, pady=10)
    combo=ttk.Combobox(vgr,values=("Ventas por tela","Telas con venta óptima","Telas con precios menores al 75% del precio máximo","Telas con precios mayores al 75% del precio máximo","Precios menor, mayor y promedio"),state="readonly", width=81)
    combo.current(0)
    combo.grid(row=0,column=1, sticky='W')

    text=Text(vgr, height=50, width=170)#,background="#D3D3D3"
    text.grid(row=1,columnspan=3,padx=15,pady=15)

    button=Button(vgr,text="Cerrar",width=21,command=vgr.destroy).grid(row=0,column=2,sticky=E,padx=20)
    
    text.insert(INSERT,"VENTAS POR TELA "+"\n\n")

    text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+l[0]["Código"]+"\n")
    text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+l[0]["Descripción"]+"\n")
    text.insert(INSERT,"Cantidad total de ventas: "+"\t\t\t\t\t\t"+f"{ctv0: 16.2f}"+"\n")
    text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{ctmv0: 16.2f}"+"\n")
    text.insert(INSERT,"Importe total acumulado: "+"\t\t\t\t\t\t"+"S/. "+f"{ita0: 12.2f}"+"\n\n")
    
    text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+l[1]["Código"]+"\n")
    text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+l[1]["Descripción"]+"\n")
    text.insert(INSERT,"Cantidad total de ventas: "+"\t\t\t\t\t\t"+f"{ctv1: 16.2f}"+"\n")
    text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{ctmv1: 16.2f}"+"\n")
    text.insert(INSERT,"Importe total acumulado: "+"\t\t\t\t\t\t"+"S/. "+f"{ita1: 12.2f}"+"\n\n")
    
    text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+l[2]["Código"]+"\n")
    text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+l[2]["Descripción"]+"\n")
    text.insert(INSERT,"Cantidad total de ventas: "+"\t\t\t\t\t\t"+f"{ctv2: 16.2f}"+"\n")
    text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{ctmv2: 16.2f}"+"\n")
    text.insert(INSERT,"Importe total acumulado: "+"\t\t\t\t\t\t"+"S/. "+f"{ita2: 12.2f}"+"\n\n")
    
    text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+l[3]["Código"]+"\n")
    text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+l[3]["Descripción"]+"\n")
    text.insert(INSERT,"Cantidad total de ventas: "+"\t\t\t\t\t\t"+f"{ctv3: 16.2f}"+"\n")
    text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{ctmv3: 16.2f}"+"\n")
    text.insert(INSERT,"Importe total acumulado: "+"\t\t\t\t\t\t"+"S/. "+f"{ita3: 12.2f}"+"\n\n")

    text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+l[4]["Código"]+"\n")
    text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+l[4]["Descripción"]+"\n")
    text.insert(INSERT,"Cantidad total de ventas: "+"\t\t\t\t\t\t"+f"{ctv4: 16.2f}"+"\n")
    text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{ctmv4: 16.2f}"+"\n")
    text.insert(INSERT,"Importe total acumulado: "+"\t\t\t\t\t\t"+"S/. "+f"{ita4: 12.2f}"+"\n\n")
    
    text.insert(INSERT,"Importe total acumulado general: "+"\t\t\t\t\t\t"+"S/. "+f"{itag: 12.2f}"+"\n")
    
    def cambioconsulta(event):
        global p, a
        text.delete(1.0,END)
        if combo.current()==1:
            text.insert(INSERT,"TELAS CON VENTA ÓPTIMA: "+"\n\n")
            if ctmv0>=cto:
                text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+l[0]["Código"]+"\n")
                text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+l[0]["Descripción"]+"\n")
                text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{ctmv0: 16.2f}"+"\n\n")
                
            if ctmv1>=cto:
                text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+l[1]["Código"]+"\n")
                text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+l[1]["Descripción"]+"\n")
                text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{ctmv1: 16.2f}"+"\n\n")
            
            if ctmv2>=cto:
                text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+l[2]["Código"]+"\n")
                text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+l[2]["Descripción"]+"\n")
                text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{ctmv2: 16.2f}"+"\n\n")

            if ctmv3>=cto:
                text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+l[3]["Código"]+"\n")
                text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+l[3]["Descripción"]+"\n")
                text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{ctmv3: 16.2f}"+"\n\n")

            if ctmv4>=cto:
                text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+l[4]["Código"]+"\n")
                text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+l[4]["Descripción"]+"\n")
                text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{ctmv4: 16.2f}"+"\n\n")
        elif combo.current()==2:
            text.insert(INSERT,"TELAS CON PRECIOS MAYORES AL 75% DEL PRECIO MÁXIMO: "+"\n\n")
            cm=0
            for i in l:
                pm.append(i["Precio (S/.)"])

            p=max(pm)
            
            if (l[0]["Precio (S/.)"]>(0.75*p)):
                text.insert(INSERT,"Descripción: "+"\t\t\t\t"+l[0]["Descripción"]+"\n")
                text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{l[0]["Precio (S/.)"]: 12.2f}'+"\n\n")
                cm +=1
                
            if (l[1]["Precio (S/.)"]>(0.75*p)):
                text.insert(INSERT,"Descripción: "+"\t\t\t\t"+l[1]["Descripción"]+"\n")
                text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{l[1]["Precio (S/.)"]: 12.2f}'+"\n\n")
                cm +=1
                
            if (l[2]["Precio (S/.)"]>(0.75*p)):
                text.insert(INSERT,"Descripción: "+"\t\t\t\t"+l[2]["Descripción"]+"\n")
                text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{l[2]["Precio (S/.)"]: 12.2f}'+"\n\n")
                cm +=1
                
            if (l[3]["Precio (S/.)"]>(0.75*p)):
                text.insert(INSERT,"Descripción: "+"\t\t\t\t"+l[3]["Descripción"]+"\n")
                text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{l[3]["Precio (S/.)"]: 12.2f}'+"\n\n")
                cm +=1
                
            if (l[4]["Precio (S/.)"]>(0.75*p)):
                text.insert(INSERT,"Descripción: "+"\t\t\t\t"+l[4]["Descripción"]+"\n")
                text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{l[4]["Precio (S/.)"]: 12.2f}'+"\n\n")
                cm +=1
                
            text.insert(INSERT,"75% del precio máximo: "+"\t\t\t\t"+"S/. "+f'{p*0.75: 12.2f}'+"\n\n")
            
            text.insert(INSERT,"Número de marcas: "+"\t\t\t\t"+f'{cm: 16.2f}'+"\n\n")
        
        elif combo.current()==3:
            text.insert(INSERT,"TELAS CON PRECIOS MENORES AL 75% DEL PRECIO MÁXIMO: "+"\n\n")
            cm=0
            for i in l:
                pm.append(i["Precio (S/.)"])

            p=max(pm)
            
            if (l[0]["Precio (S/.)"]<(0.75*p)):
                text.insert(INSERT,"Descripción: "+"\t\t\t\t"+l[0]["Descripción"]+"\n")
                text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{l[0]["Precio (S/.)"]: 12.2f}'+"\n\n")
                cm +=1
                
            if (l[1]["Precio (S/.)"]<(0.75*p)):
                text.insert(INSERT,"Descripción: "+"\t\t\t\t"+l[1]["Descripción"]+"\n")
                text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{l[1]["Precio (S/.)"]: 12.2f}'+"\n\n")
                cm +=1
                
            if (l[2]["Precio (S/.)"]<(0.75*p)):
                text.insert(INSERT,"Descripción: "+"\t\t\t\t"+l[2]["Descripción"]+"\n")
                text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{l[2]["Precio (S/.)"]: 12.2f}'+"\n\n")
                cm +=1
                
            if (l[3]["Precio (S/.)"]<(0.75*p)):
                text.insert(INSERT,"Descripción: "+"\t\t\t\t"+l[3]["Descripción"]+"\n")
                text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{l[3]["Precio (S/.)"]: 12.2f}'+"\n\n")
                cm +=1
                
            if (l[4]["Precio (S/.)"]<(0.75*p)):
                text.insert(INSERT,"Descripción: "+"\t\t\t\t"+l[4]["Descripción"]+"\n")
                text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{l[4]["Precio (S/.)"]: 12.2f}'+"\n\n")
                cm +=1
                
            text.insert(INSERT,"75% del precio máximo: "+"\t\t\t\t"+"S/. "+f'{p*0.75: 12.2f}'+"\n\n")
            
            text.insert(INSERT,"Número de marcas: "+"\t\t\t\t"+f'{cm: 16.2f}'+"\n\n")
        
        elif combo.current()==4:
            text.insert(INSERT,"PROMEDIOS, MÁXIMOS Y MÍNIMOS: "+"\n\n")
            
            for i in l:
                pm.append(i["Precio (S/.)"])
                p.append(i["Peso (g/m2)"])
                a.append(i["Ancho (cm)"])
            
            text.insert(INSERT,"Ancho promedio: "+"\t\t\t\t"+f'{sum(a)/float(len(a)): 12.2f}'+" cm"+"\n")
            text.insert(INSERT,"Ancho mínimo: "+"\t\t\t\t"+f'{min(a): 12.2f}'+" cm"+"\n")
            text.insert(INSERT,"Ancho máximo: "+"\t\t\t\t"+f'{max(a): 12.2f}'+" cm"+"\n\n")

            text.insert(INSERT,"Peso promedio: "+"\t\t\t\t"+f'{sum(p)/float(len(p)): 12.2f}'+" g/m2"+"\n")
            text.insert(INSERT,"Peso mínimo: "+"\t\t\t\t"+f'{min(p): 12.2f}'+" g/m2"+"\n")
            text.insert(INSERT,"Peso máximo: "+"\t\t\t\t"+f'{max(p): 12.2f}'+" g/m2"+"\n\n")

            text.insert(INSERT,"Precio promedio: "+"\t\t\t\t"+"S/. "+f'{sum(pm)/float(len(pm)): 12.2f}'+"\n")
            text.insert(INSERT,"Precio mínimo: "+"\t\t\t\t"+"S/. "+f'{min(pm): 12.2f}'+"\n")
            text.insert(INSERT,"Precio máximo: "+"\t\t\t\t"+"S/. "+f'{max(pm): 12.2f}'+"\n\n")

    combo.bind("<<ComboboxSelected>>",cambioconsulta)

def configurar_descuentos():
    def guardar_descuentos():
        global pd1,pd2,pd3,pd4
        pd1=float(d1.get())
        pd2=float(d2.get())
        pd3=float(d3.get())
        pd4=float(d4.get())
    vcd=Toplevel()
    vcd.title("Configurar Descuentos")
    w, h = vcd.winfo_screenwidth(), vcd.winfo_screenheight() 
    vcd.geometry("%dx%d+0+0" % (w, h))    
    d1=StringVar()
    d2=StringVar()
    d3=StringVar()
    d4=StringVar()
    label=Label(vcd,text="1 a 5 metros: ").grid(row=0,column=0, sticky='W', padx=10, pady=10)
    entry=Entry(vcd,width=21,textvariable=d1)
    entry.grid(row=0,column=1)
    label3=Label(vcd,text="%").grid(row=0,column=2, sticky='W', padx=10, pady=10)
    label=Label(vcd,text="6 a 10 metros: ").grid(row=1,column=0, sticky='W', padx=10, pady=10)
    entry1=Entry(vcd,width=21,textvariable=d2)
    entry1.grid(row=1,column=1)
    label3=Label(vcd,text="%").grid(row=1,column=2, sticky='W', padx=10, pady=10)
    label=Label(vcd,text="11 a 15 metros: ").grid(row=2,column=0, sticky='W', padx=10, pady=10)
    entry2=Entry(vcd,width=21,textvariable=d3)
    entry2.grid(row=2,column=1)
    label3=Label(vcd,text="%").grid(row=2,column=2, sticky='W', padx=10, pady=10)
    label=Label(vcd,text="Más de 15 metros: ").grid(row=3,column=0, sticky='W', padx=10, pady=10)
    entry3=Entry(vcd,width=21,textvariable=d4)
    entry3.grid(row=3,column=1)
    label3=Label(vcd,text="%").grid(row=3,column=2, sticky='W', padx=10, pady=10)
    button2=Button(vcd,text="Aceptar",width=21,command=guardar_descuentos).grid(row=0,column=3,sticky=E,padx=20)
    button=Button(vcd,text="Cancelar",width=21,command=vcd.destroy).grid(row=1,column=3,sticky=E,padx=20)
    entry.insert(0,f"{pd1: 2.1f}")
    entry1.insert(0,f"{pd2: 2.1f}")
    entry2.insert(0,f"{pd3: 2.1f}")
    entry3.insert(0,f"{pd4: 2.1f}")
    
def configurar_obsequio():
    def guardar_obsequio():
        global co,nombre_obsequio
        co=float(d1.get())
        nombre_obsequio=d2.get()
        
    vco=Toplevel()
    vco.title("Configurar Obsequio")
    w, h = vco.winfo_screenwidth(), vco.winfo_screenheight() 
    vco.geometry("%dx%d+0+0" % (w, h))    
    d1=StringVar()
    d2=StringVar()
    
    label=Label(vco,text="Cantidad mínima de metros adquiridos: ").grid(row=0,column=0, sticky='W', padx=10, pady=10)
    entry=Entry(vco,width=21,textvariable=d1)
    entry.grid(row=0,column=1)
    
    label=Label(vco,text="Obsequio: ").grid(row=1,column=0, sticky='W', padx=10, pady=10)
    entry1=Entry(vco,width=21,textvariable=d2)
    entry1.grid(row=1,column=1)
    
    button2=Button(vco,text="Aceptar",width=21,command=guardar_obsequio).grid(row=0,column=5,sticky=E,padx=120)
    button=Button(vco,text="Cancelar",width=21,command=vco.destroy).grid(row=1,column=5,sticky=E,padx=120)
    entry.insert(0,f"{co: 7.1f}")
    entry1.insert(0,nombre_obsequio)

def configurar_comv():
    def guardar_comv():
        global cto
        cto=float(d1.get())
        
    vcc=Toplevel()
    vcc.title("Configurar cantidad óptima de metros vendidos")
    w, h = vcc.winfo_screenwidth(), vcc.winfo_screenheight() 
    vcc.geometry("%dx%d+0+0" % (w, h))    
    d1=StringVar()
    
    label=Label(vcc,text="Cantidad óptima de metros vendidos: ").grid(row=0,column=0, sticky='W', padx=10, pady=10)
    entry=Entry(vcc,width=21,textvariable=d1)
    entry.grid(row=0,column=1)
    
    button2=Button(vcc,text="Aceptar",width=21,command=guardar_comv).grid(row=0,column=5,sticky=E,padx=120)
    button=Button(vcc,text="Cancelar",width=21,command=vcc.destroy).grid(row=1,column=5,sticky=E,padx=120)
    entry.insert(0,f"{cto: 7.1f}")


def configurar_premio_sorpresa():
    def guardar_premio_sorpresa():
        global numero_cliente_sorpresa, regalo_sorpresa
        numero_cliente_sorpresa=int(d1.get())
        regalo_sorpresa=d2.get()
        
    vcp=Toplevel()
    vcp.title("Configurar Premio Sorpresa")
    w, h = vcp.winfo_screenwidth(), vcp.winfo_screenheight() 
    vcp.geometry("%dx%d+0+0" % (w, h))    
    d1=StringVar()
    d2=StringVar()
    
    label=Label(vcp,text="Número de cliente: ").grid(row=0,column=0, sticky='W', padx=10, pady=10)
    entry=Entry(vcp,width=21,textvariable=d1)
    entry.grid(row=0,column=1)
    
    label=Label(vcp,text="Premio sorpresa: ").grid(row=1,column=0, sticky='W', padx=10, pady=10)
    entry1=Entry(vcp,width=21,textvariable=d2)
    entry1.grid(row=1,column=1)
    
    button2=Button(vcp,text="Aceptar",width=21,command=guardar_premio_sorpresa).grid(row=0,column=5,sticky=E,padx=120)
    button=Button(vcp,text="Cancelar",width=21,command=vcp.destroy).grid(row=1,column=5,sticky=E,padx=120)
    entry.insert(0,numero_cliente_sorpresa)
    entry1.insert(0,regalo_sorpresa)
    
def ayuda():
    vay=Toplevel()
    vay.title("Acerca de Tienda")
    w, h = vay.winfo_screenwidth(), vay.winfo_screenheight() 
    vay.geometry("%dx%d+0+0" % (w, h))
    label=Label(vay,text="Tienda 1.0")
    label.pack(anchor=CENTER,padx=40, pady=80)
    label.config(font=("Verdana",40,"bold")) 

    label=Label(vay,text="-------------------------------------------------------------------")
    label.pack(anchor=CENTER,padx=40)
    label.config(font=("Verdana",24))

    label=Label(vay,text="Autor:")
    label.pack(anchor=CENTER,padx=40, pady=20)
    label.config(font=("Verdana",24,"bold"))

    label=Label(vay,text="Pedro Iván Gamero Butorac")
    label.pack(anchor=CENTER,padx=40, pady=20)
    label.config(font=("Verdana",24))

    button=Button(vay,text="Cerrar",width=21,height=2,command=vay.destroy).pack(padx=120,pady=60)




ventana=Tk()
ventana.title("Sistema de Ventas de Telas")
w, h = ventana.winfo_screenwidth(), ventana.winfo_screenheight() 
ventana.geometry("%dx%d+0+0" % (w, h)) 
menubar=Menu(ventana)
ventana.config(menu=menubar)
filemenu=Menu(menubar)
mantenimientomenu=Menu(menubar)
ventasmenu=Menu(menubar)
configuracionmenu=Menu(menubar)
ayudamenu=Menu(menubar)
filemenu.add_command(label="Salir", command=ventana.quit)
mantenimientomenu.add_command(label="Consultar Tela",command=consultartela)
mantenimientomenu.add_command(label="Modificar Tela",command=modificartela)
mantenimientomenu.add_command(label="Listar Telas",command=listartela)
ventasmenu.add_command(label="Vender",command=vender)
ventasmenu.add_command(label="Generar Reportes",command=generar_reportes)
configuracionmenu.add_command(label="Configurar descuentos",command=configurar_descuentos)
configuracionmenu.add_command(label="Configurar obsequio",command=configurar_obsequio)
configuracionmenu.add_command(label="Configurar cantidad óptima de metros vendidos",command=configurar_comv)
configuracionmenu.add_command(label="Configurar premio sorpresa",command=configurar_premio_sorpresa)
ayudamenu.add_command(label="Acerca de tienda", command=ayuda)
menubar.add_cascade(label="Archivo",menu=filemenu)
menubar.add_cascade(label="Mantenimiento",menu=mantenimientomenu)
menubar.add_cascade(label="Ventas",menu=ventasmenu)
menubar.add_cascade(label="Configuración",menu=configuracionmenu)
menubar.add_cascade(label="Ayuda",menu=ayudamenu)
ventana.mainloop()