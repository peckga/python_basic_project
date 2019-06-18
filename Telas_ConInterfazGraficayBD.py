import sqlite3
from tkinter import *
from tkinter import ttk
conexion=sqlite3.connect('Telas.db')
cursor=conexion.cursor()



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

        telas=cursor.execute('select * from Tela where codigo="TF0"')
        for i in telas:       
                entry.insert(0,i[1])
                entry2.insert(0,i[2])
                entry3.insert(0,i[3])
                entry4.insert(0,i[4])
                entry5.insert(0,i[5])

        def cambioconsulta(event):
                if combo.get()=="TF1":
                        telas2=cursor.execute('select * from Tela where codigo="TF1"')
                        for i in telas2:  
                                entry.delete(0,END)
                                entry.insert(0,i[1])
                                entry2.delete(0,END)
                                entry2.insert(0,i[2])
                                entry3.delete(0,END)
                                entry3.insert(0,i[3])
                                entry4.delete(0,END)
                                entry4.insert(0,i[4])
                                entry5.delete(0,END)
                                entry5.insert(0,i[5])
                elif combo.get()=="TF2":
                        telas3=cursor.execute('select * from Tela where codigo="TF2"')
                        for i in telas3:
                                entry.delete(0,END)
                                entry.insert(0,i[1])
                                entry2.delete(0,END)
                                entry2.insert(0,i[2])
                                entry3.delete(0,END)
                                entry3.insert(0,i[3])
                                entry4.delete(0,END)
                                entry4.insert(0,i[4])
                                entry5.delete(0,END)
                                entry5.insert(0,i[5])
                elif combo.get()=="TF3":
                        telas4=cursor.execute('select * from Tela where codigo="TF3"')
                        for i in telas4:
                                entry.delete(0,END)
                                entry.insert(0,i[1])
                                entry2.delete(0,END)
                                entry2.insert(0,i[2])
                                entry3.delete(0,END)
                                entry3.insert(0,i[3])
                                entry4.delete(0,END)
                                entry4.insert(0,i[4])
                                entry5.delete(0,END)
                                entry5.insert(0,i[5])
                elif combo.get()=="TF4":
                        telas5=cursor.execute('select * from Tela where codigo="TF4"')
                        for i in telas5:
                                entry.delete(0,END)
                                entry.insert(0,i[1])
                                entry2.delete(0,END)
                                entry2.insert(0,i[2])
                                entry3.delete(0,END)
                                entry3.insert(0,i[3])
                                entry4.delete(0,END)
                                entry4.insert(0,i[4])
                                entry5.delete(0,END)
                                entry5.insert(0,i[5])
                else:
                        telas6=cursor.execute('select * from Tela where codigo="TF0"')
                        for i in telas6:
                                entry.delete(0,END)
                                entry.insert(0,i[1])
                                entry2.delete(0,END)
                                entry2.insert(0,i[2])
                                entry3.delete(0,END)
                                entry3.insert(0,i[3])
                                entry4.delete(0,END)
                                entry4.insert(0,i[4])
                                entry5.delete(0,END)
                                entry5.insert(0,i[5])
        combo.bind("<<ComboboxSelected>>",cambioconsulta)


def modificartela():
        def grabar():
                
                if combo.current()==0:
                        cursor.execute('update Tela SET Descripcion=? where codigo="TF0"',(entry.get(),))
                        cursor.execute('update Tela SET Material=? where codigo="TF0"',(entry2.get(),))
                        cursor.execute('update Tela SET Ancho=? where codigo="TF0"',(entry3.get(),))
                        cursor.execute('update Tela SET Peso=? where codigo="TF0"',(entry4.get(),))
                        cursor.execute('update Tela SET Precio=? where codigo="TF0"',(entry5.get(),))
                        conexion.commit()
        
                elif combo.current()==1:
                        cursor.execute('update Tela SET Descripcion=? where codigo="TF1"',(entry.get(),))
                        cursor.execute('update Tela SET Material=? where codigo="TF1"',(entry2.get(),))
                        cursor.execute('update Tela SET Ancho=? where codigo="TF1"',(entry3.get(),))
                        cursor.execute('update Tela SET Peso=? where codigo="TF1"',(entry4.get(),))
                        cursor.execute('update Tela SET Precio=? where codigo="TF1"',(entry5.get(),))
                        conexion.commit()
                elif combo.current()==2:
                        cursor.execute('update Tela SET Descripcion=? where codigo="TF2"',(entry.get(),))
                        cursor.execute('update Tela SET Material=? where codigo="TF2"',(entry2.get(),))
                        cursor.execute('update Tela SET Ancho=? where codigo="TF2"',(entry3.get(),))
                        cursor.execute('update Tela SET Peso=? where codigo="TF2"',(entry4.get(),))
                        cursor.execute('update Tela SET Precio=? where codigo="TF2"',(entry5.get(),))
                        conexion.commit()
                elif combo.current()==3:
                        cursor.execute('update Tela SET Descripcion=? where codigo="TF3"',(entry.get(),))
                        cursor.execute('update Tela SET Material=? where codigo="TF3"',(entry2.get(),))
                        cursor.execute('update Tela SET Ancho=? where codigo="TF3"',(entry3.get(),))
                        cursor.execute('update Tela SET Peso=? where codigo="TF3"',(entry4.get(),))
                        cursor.execute('update Tela SET Precio=? where codigo="TF3"',(entry5.get(),))
                        conexion.commit()
                elif combo.current()==4:
                        cursor.execute('update Tela SET Descripcion=? where codigo="TF4"',(entry.get(),))
                        cursor.execute('update Tela SET Material=? where codigo="TF4"',(entry2.get(),))
                        cursor.execute('update Tela SET Ancho=? where codigo="TF4"',(entry3.get(),))
                        cursor.execute('update Tela SET Peso=? where codigo="TF4"',(entry4.get(),))
                        cursor.execute('update Tela SET Precio=? where codigo="TF4"',(entry5.get(),))
                        conexion.commit()
        
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
    
        telas=cursor.execute('select * from Tela where codigo="TF0"')
        for i in telas:       
                entry.insert(0,i[1])
                entry2.insert(0,i[2])
                entry3.insert(0,i[3])
                entry4.insert(0,i[4])
                entry5.insert(0,i[5])
    
        def cambioconsulta(event):
                if combo.get()=="TF1":
                        telas2=cursor.execute('select * from Tela where codigo="TF1"')
                        for i in telas2:  
                                entry.delete(0,END)
                                entry.insert(0,i[1])
                                entry2.delete(0,END)
                                entry2.insert(0,i[2])
                                entry3.delete(0,END)
                                entry3.insert(0,i[3])
                                entry4.delete(0,END)
                                entry4.insert(0,i[4])
                                entry5.delete(0,END)
                                entry5.insert(0,i[5])
                elif combo.get()=="TF2":
                        telas3=cursor.execute('select * from Tela where codigo="TF2"')
                        for i in telas3:
                                entry.delete(0,END)
                                entry.insert(0,i[1])
                                entry2.delete(0,END)
                                entry2.insert(0,i[2])
                                entry3.delete(0,END)
                                entry3.insert(0,i[3])
                                entry4.delete(0,END)
                                entry4.insert(0,i[4])
                                entry5.delete(0,END)
                                entry5.insert(0,i[5])
                elif combo.get()=="TF3":
                        telas4=cursor.execute('select * from Tela where codigo="TF3"')
                        for i in telas4:
                                entry.delete(0,END)
                                entry.insert(0,i[1])
                                entry2.delete(0,END)
                                entry2.insert(0,i[2])
                                entry3.delete(0,END)
                                entry3.insert(0,i[3])
                                entry4.delete(0,END)
                                entry4.insert(0,i[4])
                                entry5.delete(0,END)
                                entry5.insert(0,i[5])
                elif combo.get()=="TF4":
                        telas5=cursor.execute('select * from Tela where codigo="TF4"')
                        for i in telas5:
                                entry.delete(0,END)
                                entry.insert(0,i[1])
                                entry2.delete(0,END)
                                entry2.insert(0,i[2])
                                entry3.delete(0,END)
                                entry3.insert(0,i[3])
                                entry4.delete(0,END)
                                entry4.insert(0,i[4])
                                entry5.delete(0,END)
                                entry5.insert(0,i[5])
                else:
                        telas6=cursor.execute('select * from Tela where codigo="TF0"')
                        for i in telas6:
                                entry.delete(0,END)
                                entry.insert(0,i[1])
                                entry2.delete(0,END)
                                entry2.insert(0,i[2])
                                entry3.delete(0,END)
                                entry3.insert(0,i[3])
                                entry4.delete(0,END)
                                entry4.insert(0,i[4])
                                entry5.delete(0,END)
                                entry5.insert(0,i[5])
        combo.bind("<<ComboboxSelected>>",cambioconsulta)

def listartela():
        def listar():
                telas=cursor.execute('select * from Tela where codigo="TF0"')
                for i in telas:       
                        text.insert(INSERT,"Código: "+i[0]+"\n")
                        text.insert(INSERT,"Descripción: "+i[1]+"\n")
                        text.insert(INSERT,"Material: "+i[2]+"\n")
                        text.insert(INSERT,"Ancho (cm): "+str(i[3])+"\n")
                        text.insert(INSERT,"Peso (g/m2): "+str(i[4])+"\n")
                        text.insert(INSERT,"Precio (S/.): "+str(i[5])+"\n\n\n")
                
                telas2=cursor.execute('select * from Tela where codigo="TF1"')
                for i in telas2:       
                        text.insert(INSERT,"Código: "+i[0]+"\n")
                        text.insert(INSERT,"Descripción: "+i[1]+"\n")
                        text.insert(INSERT,"Material: "+i[2]+"\n")
                        text.insert(INSERT,"Ancho (cm): "+str(i[3])+"\n")
                        text.insert(INSERT,"Peso (g/m2): "+str(i[4])+"\n")
                        text.insert(INSERT,"Precio (S/.): "+str(i[5])+"\n\n\n")
                
                telas3=cursor.execute('select * from Tela where codigo="TF2"')
                for i in telas3:       
                        text.insert(INSERT,"Código: "+i[0]+"\n")
                        text.insert(INSERT,"Descripción: "+i[1]+"\n")
                        text.insert(INSERT,"Material: "+i[2]+"\n")
                        text.insert(INSERT,"Ancho (cm): "+str(i[3])+"\n")
                        text.insert(INSERT,"Peso (g/m2): "+str(i[4])+"\n")
                        text.insert(INSERT,"Precio (S/.): "+str(i[5])+"\n\n\n")
                
                telas4=cursor.execute('select * from Tela where codigo="TF3"')
                for i in telas4:       
                        text.insert(INSERT,"Código: "+i[0]+"\n")
                        text.insert(INSERT,"Descripción: "+i[1]+"\n")
                        text.insert(INSERT,"Material: "+i[2]+"\n")
                        text.insert(INSERT,"Ancho (cm): "+str(i[3])+"\n")
                        text.insert(INSERT,"Peso (g/m2): "+str(i[4])+"\n")
                        text.insert(INSERT,"Precio (S/.): "+str(i[5])+"\n\n\n")

                telas5=cursor.execute('select * from Tela where codigo="TF4"')
                for i in telas5:       
                        text.insert(INSERT,"Código: "+i[0]+"\n")
                        text.insert(INSERT,"Descripción: "+i[1]+"\n")
                        text.insert(INSERT,"Material: "+i[2]+"\n")
                        text.insert(INSERT,"Ancho (cm): "+str(i[3])+"\n")
                        text.insert(INSERT,"Peso (g/m2): "+str(i[4])+"\n")
                        text.insert(INSERT,"Precio (S/.): "+str(i[5])+"\n\n\n")
                        
                
        vlt=Toplevel()
        vlt.title("Listar Telas")
        w, h = vlt.winfo_screenwidth(), vlt.winfo_screenheight() 
        vlt.geometry("%dx%d+0+0" % (w, h))
        text=Text(vlt, height=40, width=170,background="#D3D3D3")
        text.grid(row=0,columnspan=2,padx=15,pady=15)
        button=Button(vlt,text="Cerrar",width=21,command=vlt.destroy).grid(row=1,column=0,sticky=E,padx=20)
        button2=Button(vlt,text="Listar",width=21,command=listar).grid(row=1,column=1,sticky=W,padx=20)

def vender():
    
        def venta():
                descuentos=cursor.execute('select * from Descuentos')
                for i in descuentos:
                        porcentaje_descuento_1=i[0]
                        porcentaje_descuento_2=i[1]
                        porcentaje_descuento_3=i[2]
                        porcentaje_descuento_4=i[3]
                obsequio=cursor.execute('select * from Obsequio')
                for i in obsequio:
                        cantidad_minima_metros_adquiridos=i[0]
                        obsequio=i[1]
                
                sorpresa=cursor.execute('select * from Sorpresa')
                for i in sorpresa:
                        numero_cliente_sorpresa=i[0]
                        premio_sorpresa=i[1]
                cantidad_comprar=entry2.get()
                text.delete(1.0,END)
                text.insert(INSERT,"Código: "+"\t\t\t\t"+combo.get()+"\n")
                text.insert(INSERT,"Descripción: "+"\t\t\t\t"+entry.get()+"\n")
                if combo.get()=="TF1":
                        telas2=cursor.execute('select * from Tela where codigo="TF1"')
                        for i in telas2:       
                                precio=i[5]
                
                elif combo.get()=="TF2":
                        telas3=cursor.execute('select * from Tela where codigo="TF2"')
                        for i in telas3:       
                                precio=i[5]
                
                elif combo.get()=="TF3":
                        telas4=cursor.execute('select * from Tela where codigo="TF3"')
                        for i in telas4:       
                                precio=i[5]
                
                elif combo.get()=="TF4":
                        telas5=cursor.execute('select * from Tela where codigo="TF4"')
                        for i in telas5:       
                                precio=i[5]
                
                else:
                        telas1=cursor.execute('select * from Tela where codigo="TF0"')
                        for i in telas1:       
                                precio=i[5]
                
                text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f"{precio: 12.2f}"+"\n")
                cantidad = int(entry2.get())
                text.insert(INSERT,"Cantidad de metros: "+"\t\t\t\t"+f"{cantidad: 16.2f}"+"\n")
                
                importe_compra = round(precio * cantidad,2)
                text.insert(INSERT,"Importe de compra: "+"\t\t\t\t"+"S/. "+f"{importe_compra: 12.2f}"+"\n")
                if 1<=cantidad<6:
                        importe_descuento=round((porcentaje_descuento_1/100)*importe_compra,2)
                elif cantidad < 11:
                        importe_descuento=round((porcentaje_descuento_2/100)*importe_compra,2)
                elif cantidad < 16:
                        importe_descuento=round((porcentaje_descuento_3/100)*importe_compra,2)
                elif cantidad >=16:
                        importe_descuento=round((porcentaje_descuento_4/100)*importe_compra,2)
                text.insert(INSERT,"Importe de descuento: "+"\t\t\t\t"+"S/. "+f"{importe_descuento: 12.2f}"+"\n")
                importe_pagar=importe_compra-importe_descuento
                text.insert(INSERT,"Importe a pagar: "+"\t\t\t\t"+"S/. "+f"{importe_pagar: 12.2f}"+"\n")
                if cantidad>=cantidad_minima_metros_adquiridos:
                        nombre_obsequio=obsequio
                else:
                        nombre_obsequio="No corresponde"
                text.insert(INSERT,"Obsequio: "+"\t\t\t\t"+nombre_obsequio+"\n")
                
                clientes=cursor.execute('select * from Ventas')
                for i in clientes:
                        numero_cliente=i[0]+1
                
                
                if numero_cliente==numero_cliente_sorpresa:
                        sorpresa=premio_sorpresa
                else:
                        sorpresa="No corresponde"
                text.insert(INSERT,"Premio sorpresa: "+"\t\t\t\t"+sorpresa+"\n")
                cursor.execute('insert into Ventas values (null,"{}","{}",{},{},{},{},{},"{}","{}") '.format(combo.get(),entry.get(),precio,cantidad,importe_compra,importe_descuento,importe_pagar,nombre_obsequio,sorpresa))
                conexion.commit()
                
        

                
                

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


        telas=cursor.execute('select * from Tela where codigo="TF0"')
        for i in telas:       
                entry.insert(0,i[1])
                
        
        def cambioconsulta(event):
                
                if combo.get()=="TF1":
                        telas2=cursor.execute('select * from Tela where codigo="TF1"')
                        for i in telas2:  
                                entry.delete(0,END)
                                entry.insert(0,i[1])
                                
                
                elif combo.get()=="TF2":
                        telas3=cursor.execute('select * from Tela where codigo="TF2"')
                        for i in telas3:  
                                entry.delete(0,END)
                                entry.insert(0,i[1])
                
                elif combo.get()=="TF3":
                        telas4=cursor.execute('select * from Tela where codigo="TF3"')
                        for i in telas4:  
                                entry.delete(0,END)
                                entry.insert(0,i[1])
                
                elif combo.get()=="TF4":
                        telas5=cursor.execute('select * from Tela where codigo="TF4"')
                        for i in telas5:  
                                entry.delete(0,END)
                                entry.insert(0,i[1])
                
                else:
                        telas6=cursor.execute('select * from Tela where codigo="TF0"')
                        for i in telas6:  
                                entry.delete(0,END)
                                entry.insert(0,i[1])
                
        combo.bind("<<ComboboxSelected>>",cambioconsulta)
        

def generar_reportes():
    
        vgr=Toplevel()
        vgr.title("Generar Reportes")
        w, h = vgr.winfo_screenwidth(), vgr.winfo_screenheight() 
        vgr.geometry("%dx%d+0+0" % (w, h))    
        label=Label(vgr,text="Tipo de reporte: ").grid(row=0,column=0, sticky='W', padx=10, pady=10)
        combo=ttk.Combobox(vgr,values=("Ventas por tela","Telas con venta óptima","Telas con precios mayores al 75% del precio máximo","Telas con precios menores al 75% del precio máximo","Precios menor, mayor y promedio"),state="readonly", width=81)
        combo.current(0)
        combo.grid(row=0,column=1, sticky='W')

        text=Text(vgr, height=50, width=170)#,background="#D3D3D3"
        text.grid(row=1,columnspan=3,padx=15,pady=15)

        button=Button(vgr,text="Cerrar",width=21,command=vgr.destroy).grid(row=0,column=2,sticky=E,padx=20)
        
        text.insert(INSERT,"VENTAS POR TELA "+"\n\n")
        
        telas=cursor.execute('select * from Tela where codigo="TF0"')
        for i in telas:       
                text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+i[0]+"\n")
                text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+i[1]+"\n")

        hay=cursor.execute("select count(*) from Ventas where codigo ='TF0'")
        for i in hay:
                registros_hay=i[0]
        if registros_hay>0:

                ventas=cursor.execute("select count(*),sum(cantidad),sum(Importe_pagar) from Ventas where codigo ='TF0'")
        
                for i in ventas:                        
                        text.insert(INSERT,"Cantidad total de ventas: "+"\t\t\t\t\t\t"+f"{i[0]: 16.2f}"+"\n")
                        text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{i[1]: 16.2f}"+"\n")
                        text.insert(INSERT,"Importe total acumulado: "+"\t\t\t\t\t\t"+"S/. "+f"{i[2]: 12.2f}"+"\n\n")
        
        else:
                text.insert(INSERT,"Cantidad total de ventas: "+"\t\t\t\t\t\t"+f"{0: 16.2f}"+"\n")
                text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{0: 16.2f}"+"\n")
                text.insert(INSERT,"Importe total acumulado: "+"\t\t\t\t\t\t"+"S/. "+f"{0: 12.2f}"+"\n\n")
        
        telas1=cursor.execute('select * from Tela where codigo="TF1"')
        for i in telas1:       
                text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+i[0]+"\n")
                text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+i[1]+"\n")

        hay=cursor.execute("select count(*) from Ventas where codigo ='TF1'")
        for i in hay:
                registros_hay2=i[0]
        if registros_hay2>0:

                ventas1=cursor.execute("select count(*),sum(cantidad),sum(Importe_pagar) from Ventas where codigo ='TF1'")
        
                for i in ventas1:                        
                        text.insert(INSERT,"Cantidad total de ventas: "+"\t\t\t\t\t\t"+f"{i[0]: 16.2f}"+"\n")
                        text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{i[1]: 16.2f}"+"\n")
                        text.insert(INSERT,"Importe total acumulado: "+"\t\t\t\t\t\t"+"S/. "+f"{i[2]: 12.2f}"+"\n\n")
        
        else:
                text.insert(INSERT,"Cantidad total de ventas: "+"\t\t\t\t\t\t"+f"{0: 16.2f}"+"\n")
                text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{0: 16.2f}"+"\n")
                text.insert(INSERT,"Importe total acumulado: "+"\t\t\t\t\t\t"+"S/. "+f"{0: 12.2f}"+"\n\n")
        
        
        telas2=cursor.execute('select * from Tela where codigo="TF2"')
        for i in telas2:       
                text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+i[0]+"\n")
                text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+i[1]+"\n")

        hay=cursor.execute("select count(*) from Ventas where codigo ='TF2'")
        for i in hay:
                registros_hay3=i[0]
        if registros_hay3>0:

                ventas2=cursor.execute("select count(*),sum(cantidad),sum(Importe_pagar) from Ventas where codigo ='TF2'")
        
                for i in ventas2:                        
                        text.insert(INSERT,"Cantidad total de ventas: "+"\t\t\t\t\t\t"+f"{i[0]: 16.2f}"+"\n")
                        text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{i[1]: 16.2f}"+"\n")
                        text.insert(INSERT,"Importe total acumulado: "+"\t\t\t\t\t\t"+"S/. "+f"{i[2]: 12.2f}"+"\n\n")
        
        else:
                text.insert(INSERT,"Cantidad total de ventas: "+"\t\t\t\t\t\t"+f"{0: 16.2f}"+"\n")
                text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{0: 16.2f}"+"\n")
                text.insert(INSERT,"Importe total acumulado: "+"\t\t\t\t\t\t"+"S/. "+f"{0: 12.2f}"+"\n\n")

        
        telas3=cursor.execute('select * from Tela where codigo="TF3"')
        for i in telas3:       
                text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+i[0]+"\n")
                text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+i[1]+"\n")

        hay=cursor.execute("select count(*) from Ventas where codigo ='TF3'")
        for i in hay:
                registros_hay4=i[0]
        if registros_hay4>0:

                ventas3=cursor.execute("select count(*),sum(cantidad),sum(Importe_pagar) from Ventas where codigo ='TF3'")
        
                for i in ventas3:                        
                        text.insert(INSERT,"Cantidad total de ventas: "+"\t\t\t\t\t\t"+f"{i[0]: 16.2f}"+"\n")
                        text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{i[1]: 16.2f}"+"\n")
                        text.insert(INSERT,"Importe total acumulado: "+"\t\t\t\t\t\t"+"S/. "+f"{i[2]: 12.2f}"+"\n\n")
        
        else:
                text.insert(INSERT,"Cantidad total de ventas: "+"\t\t\t\t\t\t"+f"{0: 16.2f}"+"\n")
                text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{0: 16.2f}"+"\n")
                text.insert(INSERT,"Importe total acumulado: "+"\t\t\t\t\t\t"+"S/. "+f"{0: 12.2f}"+"\n\n")

        telas4=cursor.execute('select * from Tela where codigo="TF4"')
        for i in telas4:       
                text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+i[0]+"\n")
                text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+i[1]+"\n")

        hay=cursor.execute("select count(*) from Ventas where codigo ='TF4'")
        for i in hay:
                registros_hay5=i[0]
        if registros_hay5>0:

                ventas4=cursor.execute("select count(*),sum(cantidad),sum(Importe_pagar) from Ventas where codigo ='TF4'")
        
                for i in ventas4:                        
                        text.insert(INSERT,"Cantidad total de ventas: "+"\t\t\t\t\t\t"+f"{i[0]: 16.2f}"+"\n")
                        text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{i[1]: 16.2f}"+"\n")
                        text.insert(INSERT,"Importe total acumulado: "+"\t\t\t\t\t\t"+"S/. "+f"{i[2]: 12.2f}"+"\n\n")
        
        else:
                text.insert(INSERT,"Cantidad total de ventas: "+"\t\t\t\t\t\t"+f"{0: 16.2f}"+"\n")
                text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{0: 16.2f}"+"\n")
                text.insert(INSERT,"Importe total acumulado: "+"\t\t\t\t\t\t"+"S/. "+f"{0: 12.2f}"+"\n\n")

        
        hay=cursor.execute("select sum(Importe_pagar) from Ventas")
        for i in hay:
                registros_hay=i[0]
        if registros_hay>0:
                text.insert(INSERT,"Importe total acumulado general: "+"\t\t\t\t\t\t"+"S/. "+f"{i[0]: 12.2f}"+"\n")
                        
        
        else:
                text.insert(INSERT,"Importe total acumulado general: "+"\t\t\t\t\t\t"+"S/. "+f"{0: 12.2f}"+"\n")

        
                
        
        def cambioconsulta(event):
                
                text.delete(1.0,END)
                if combo.current()==1:
                        text.insert(INSERT,"TELAS CON VENTA ÓPTIMA: "+"\n\n")
                
                        if registros_hay>0:
                                resultado = cursor.execute('select sum(Cantidad) from Ventas where Codigo="TF0" group by Codigo ')
                                for i in resultado:
                                        CTMV0 = i[0]
                                optima = cursor.execute('select * from Metros_vendidos')
                                for i in optima:
                                        CTO = i[0] 

                                if CTMV0 >= CTO:
                                        telas=cursor.execute('select * from Tela where codigo="TF0"')
                                        for i in telas:       
                                                text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+i[0]+"\n")
                                                text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+i[1]+"\n")
                                        text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{CTMV0: 16.2f}"+"\n\n")
                        
                        if registros_hay2 > 0:
                                resultado2 = cursor.execute('select sum(Cantidad) from Ventas where Codigo="TF1" group by Codigo ')
                                for i in resultado2:
                                        CTMV1 = i[0]

                                if CTMV1 >= CTO:
                                        telas=cursor.execute('select * from Tela where codigo="TF1"')
                                        for i in telas:       
                                                text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+i[0]+"\n")
                                                text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+i[1]+"\n")
                                        text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{CTMV1: 16.2f}"+"\n\n")
                        
                        if registros_hay3>0:
                                resultado3 = cursor.execute('select sum(Cantidad) from Ventas where Codigo="TF2" group by Codigo ')
                                for i in resultado3:
                                        CTMV2 = i[0]



                                if CTMV2 >= CTO:
                                        telas=cursor.execute('select * from Tela where codigo="TF2"')
                                        for i in telas:       
                                                text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+i[0]+"\n")
                                                text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+i[1]+"\n")
                                        text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{CTMV2: 16.2f}"+"\n\n")
                        
                        if registros_hay4>0:
                                resultado4 = cursor.execute('select sum(Cantidad) from Ventas where Codigo="TF3" group by Codigo ')
                                for i in resultado4:
                                        CTMV3 = i[0]

                                if CTMV3 >= CTO:
                                        telas=cursor.execute('select * from Tela where codigo="TF3"')
                                        for i in telas:       
                                                text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+i[0]+"\n")
                                                text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+i[1]+"\n")
                                        text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{CTMV3: 16.2f}"+"\n\n")

                        if registros_hay5>0:
                                resultado5 = cursor.execute('select sum(Cantidad) from Ventas where Codigo="TF4" group by Codigo ')
                                for i in resultado5:
                                        CTMV4 = i[0]

                                if CTMV4 >= CTO:
                                        telas=cursor.execute('select * from Tela where codigo="TF4"')
                                        for i in telas:       
                                                text.insert(INSERT,"Código: "+"\t\t\t\t\t\t"+i[0]+"\n")
                                                text.insert(INSERT,"Descripción: "+"\t\t\t\t\t\t"+i[1]+"\n")
                                        text.insert(INSERT,"Cantidad total de metros vendidos: "+"\t\t\t\t\t\t"+f"{CTMV4: 16.2f}"+"\n\n")


                elif combo.current()==2:
                        numero_marcas=0
                        text.insert(INSERT,"TELAS CON PRECIOS MAYORES AL 75% DEL PRECIO MÁXIMO: "+"\n\n")

                        pmaximo = cursor.execute('select max(precio) from Tela')
                        for i in pmaximo:
                                precio_maximo = i[0]
                        print(precio_maximo)

                        pTFO = cursor.execute('select precio from Tela where Codigo="TF0"')
                        for i in pTFO:
                                precio_TFO = i[0]
                        if precio_TFO > 0.75*precio_maximo:
                                telas=cursor.execute('select * from Tela where codigo="TF0"')
                                for i in telas:       
                                        text.insert(INSERT,"Descripción: "+"\t\t\t\t"+i[1]+"\n")
                                        text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{i[5]: 12.2f}'+"\n\n")
                                        numero_marcas+=1
                        
                        
                        pTF1 = cursor.execute('select precio from Tela where Codigo="TF1"')
                        for i in pTF1:
                                precio_TF1 = i[0]
                        if precio_TF1 > 0.75*precio_maximo:
                                telas=cursor.execute('select * from Tela where codigo="TF1"')
                                for i in telas:       
                                        text.insert(INSERT,"Descripción: "+"\t\t\t\t"+i[1]+"\n")
                                        text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{i[5]: 12.2f}'+"\n\n")
                                        numero_marcas+=1

                        pTF2 = cursor.execute('select precio from Tela where Codigo="TF2"')
                        for i in pTF2:
                                precio_TF2 = i[0]
                        if precio_TF2 > 0.75*precio_maximo:
                                telas=cursor.execute('select * from Tela where codigo="TF2"')
                                for i in telas:       
                                        text.insert(INSERT,"Descripción: "+"\t\t\t\t"+i[1]+"\n")
                                        text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{i[5]: 12.2f}'+"\n\n")
                                        numero_marcas+=1

                        pTF3 = cursor.execute('select precio from Tela where Codigo="TF3"')
                        for i in pTF3:
                                precio_TF3 = i[0]
                        if precio_TF3 > 0.75*precio_maximo:
                                telas=cursor.execute('select * from Tela where codigo="TF3"')
                                for i in telas:       
                                        text.insert(INSERT,"Descripción: "+"\t\t\t\t"+i[1]+"\n")
                                        text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{i[5]: 12.2f}'+"\n\n")
                                        numero_marcas+=1

                        pTF4 = cursor.execute('select precio from Tela where Codigo="TF4"')
                        for i in pTF4:
                                precio_TF4 = i[0]
                        if precio_TF4 > 0.75*precio_maximo:
                                telas=cursor.execute('select * from Tela where codigo="TF4"')
                                for i in telas:       
                                        text.insert(INSERT,"Descripción: "+"\t\t\t\t"+i[1]+"\n")
                                        text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{i[5]: 12.2f}'+"\n\n")
                                        numero_marcas+=1
                        
                        text.insert(INSERT,"\n\n"+"75% del precio máximo: "+"\t\t\t\t"+"S/. "+f'{precio_maximo*0.75: 12.2f}'+"\n\n")
                
                        text.insert(INSERT,"Número de marcas: "+"\t\t\t\t"+f'{numero_marcas: 16.2f}'+"\n\n")
                        
                elif combo.current()==3:
                        numero_marcas=0
                        text.insert(INSERT,"TELAS CON PRECIOS MENORES AL 75% DEL PRECIO MÁXIMO: "+"\n\n")

                        pmaximo = cursor.execute('select max(precio) from Tela')
                        for i in pmaximo:
                                precio_maximo = i[0]
                        print(precio_maximo)

                        pTFO = cursor.execute('select precio from Tela where Codigo="TF0"')
                        for i in pTFO:
                                precio_TFO = i[0]
                        if precio_TFO < 0.75*precio_maximo:
                                telas=cursor.execute('select * from Tela where codigo="TF0"')
                                for i in telas:       
                                        text.insert(INSERT,"Descripción: "+"\t\t\t\t"+i[1]+"\n")
                                        text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{i[5]: 12.2f}'+"\n\n")
                                        numero_marcas+=1

                        pTF1 = cursor.execute('select precio from Tela where Codigo="TF1"')
                        for i in pTF1:
                                precio_TF1 = i[0]
                        if precio_TF1 < 0.75*precio_maximo:
                                telas=cursor.execute('select * from Tela where codigo="TF1"')
                                for i in telas:       
                                        text.insert(INSERT,"Descripción: "+"\t\t\t\t"+i[1]+"\n")
                                        text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{i[5]: 12.2f}'+"\n\n")
                                        numero_marcas+=1

                        pTF2 = cursor.execute('select precio from Tela where Codigo="TF2"')
                        for i in pTF2:
                                precio_TF2 = i[0]
                        if precio_TF2 < 0.75*precio_maximo:
                                telas=cursor.execute('select * from Tela where codigo="TF2"')
                                for i in telas:       
                                        text.insert(INSERT,"Descripción: "+"\t\t\t\t"+i[1]+"\n")
                                        text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{i[5]: 12.2f}'+"\n\n")
                                        numero_marcas+=1

                        pTF3 = cursor.execute('select precio from Tela where Codigo="TF3"')
                        for i in pTF3:
                                precio_TF3 = i[0]
                        if precio_TF3 < 0.75*precio_maximo:
                                telas=cursor.execute('select * from Tela where codigo="TF3"')
                                for i in telas:       
                                        text.insert(INSERT,"Descripción: "+"\t\t\t\t"+i[1]+"\n")
                                        text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{i[5]: 12.2f}'+"\n\n")
                                        numero_marcas+=1

                        pTF4 = cursor.execute('select precio from Tela where Codigo="TF4"')
                        for i in pTF4:
                                precio_TF4 = i[0]
                        if precio_TF4 < 0.75*precio_maximo:
                                telas=cursor.execute('select * from Tela where codigo="TF4"')
                                for i in telas:       
                                        text.insert(INSERT,"Descripción: "+"\t\t\t\t"+i[1]+"\n")
                                        text.insert(INSERT,"Precio: "+"\t\t\t\t"+"S/. "+f'{i[5]: 12.2f}'+"\n\n")
                                        numero_marcas+=1
                        
                        text.insert(INSERT,"\n\n"+"75% del precio máximo: "+"\t\t\t\t"+"S/. "+f'{precio_maximo*0.75: 12.2f}'+"\n\n")
                
                        text.insert(INSERT,"Número de marcas: "+"\t\t\t\t"+f'{numero_marcas: 16.2f}'+"\n\n")
                
                elif combo.current()==4:
                        text.insert(INSERT,"PROMEDIOS, MÁXIMOS Y MÍNIMOS: "+"\n\n")
                        promminmax=cursor.execute('select avg(Ancho), min(Ancho), max(Ancho),avg(Peso),min(Peso),max(Peso),avg(Precio),min(Precio),max(Precio) from Tela')
                        for i in promminmax:       
                                text.insert(INSERT,"Ancho promedio: "+"\t\t\t\t"+f'{i[0]: 12.2f}'+" cm"+"\n")
                                text.insert(INSERT,"Ancho mínimo: "+"\t\t\t\t"+f'{i[1]: 12.2f}'+" cm"+"\n")
                                text.insert(INSERT,"Ancho máximo: "+"\t\t\t\t"+f'{i[2]: 12.2f}'+" cm"+"\n\n")

                                text.insert(INSERT,"Peso promedio: "+"\t\t\t\t"+f'{i[3]: 12.2f}'+" g/m2"+"\n")
                                text.insert(INSERT,"Peso mínimo: "+"\t\t\t\t"+f'{i[4]: 12.2f}'+" g/m2"+"\n")
                                text.insert(INSERT,"Peso máximo: "+"\t\t\t\t"+f'{i[5]: 12.2f}'+" g/m2"+"\n\n")

                                text.insert(INSERT,"Precio promedio: "+"\t\t\t\t"+"S/. "+f'{i[6]: 12.2f}'+"\n")
                                text.insert(INSERT,"Precio mínimo: "+"\t\t\t\t"+"S/. "+f'{i[7]: 12.2f}'+"\n")
                                text.insert(INSERT,"Precio máximo: "+"\t\t\t\t"+"S/. "+f'{i[8]: 12.2f}'+"\n\n")
        
        combo.bind("<<ComboboxSelected>>",cambioconsulta)
        
def configurar_descuentos():
        def guardar_descuentos():
                cursor.execute('update Descuentos set Descuento1="{}"'.format(float(d1.get())))
                cursor.execute('update Descuentos set Descuento2="{}"'.format(float(d2.get())))
                cursor.execute('update Descuentos set Descuento3="{}"'.format(float(d3.get())))
                cursor.execute('update Descuentos set Descuento4="{}"'.format(float(d4.get())))
                conexion.commit()
                
                
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
        descuentos = cursor.execute('select * from Descuentos')
        for i in descuentos:
                entry.insert(0,f"{i[0]: 2.1f}")
                entry1.insert(0,f"{i[1]: 2.1f}")
                entry2.insert(0,f"{i[2]: 2.1f}")
                entry3.insert(0,f"{i[3]: 2.1f}")

def configurar_obsequio():
        def guardar_obsequio():
                cursor.execute('update Obsequio set Cantidad="{}"'.format(float(d1.get())))
                cursor.execute('update Obsequio set Obsequio="{}"'.format(d2.get()))
                conexion.commit()
        
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
        obsequios = cursor.execute('select * from Obsequio')
        for i in obsequios:
                entry.insert(0,f"{i[0]: 2.1f}")
                entry1.insert(0,f"{i[1]}")

def configurar_comv():
        def guardar_comv():
                cursor.execute('update Metros_vendidos set Cantidad="{}"'.format(float(d1.get())))
                conexion.commit()

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
        mvendidos = cursor.execute('select * from Metros_vendidos')
        for i in mvendidos:
                entry.insert(0,f"{i[0]: 7.1f}")


def configurar_premio_sorpresa():
        def guardar_premio_sorpresa():
                cursor.execute('update Sorpresa set Numero_cliente="{}"'.format(float(d1.get())))
                cursor.execute('update Sorpresa set Sorpresa="{}"'.format(d2.get()))
                conexion.commit()

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
        psorpresa = cursor.execute('select * from Sorpresa')
        for i in psorpresa:
                entry.insert(0,f"{i[0]: 2.1f}")
                entry1.insert(0,f"{i[1]}")


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
ayudamenu.add_command(label="Acerca de tienda",command=ayuda)
menubar.add_cascade(label="Archivo",menu=filemenu)
menubar.add_cascade(label="Mantenimiento",menu=mantenimientomenu)
menubar.add_cascade(label="Ventas",menu=ventasmenu)
menubar.add_cascade(label="Configuración",menu=configuracionmenu)
menubar.add_cascade(label="Ayuda",menu=ayudamenu)
ventana.mainloop()

conexion.close()
#gracias a todos
#modificando desde linux
