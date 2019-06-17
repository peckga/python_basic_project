l=[{"Código":"TF0","Descripción":"Pinstripe Suit 1","Material":"98%Algodón, 2%Elastán","Ancho (cm)":160.0,"Peso (g/m2)":220.0,"Precio (S/.)":9.4},{"Código":"TF1","Descripción":"Gabardina Oslo 5","Material":"60%Algodón, 37%Poliéster","Ancho (cm)":145.0,"Peso (g/m2)":300.0,"Precio (S/.)":11.3},{"Código":"TF2","Descripción":"Sarga 2","Material":"50%Poliéster, 50%Poliacril","Ancho (cm)":145.0,"Peso (g/m2)":425.0,"Precio (S/.)":31.8},{"Código":"TF3","Descripción":"Leni 1","Material":"50%Poliéster, 50%Poliacril","Ancho (cm)":145.0,"Peso (g/m2)":410.0,"Precio (S/.)":37.2},{"Código":"TF4","Descripción":"Laurent 3","Material":"100%Poliamida","Ancho (cm)":150.0,"Peso (g/m2)":140.0,"Precio (S/.)":18.8}]
lv=[]
pm=[]
p=[]
a=[]
p1=0.05
p2=0.1
p3=0.15
p4=0.2
co=20
obsequio="Peluche"
cs=0
ss=5
rs="Una cartuchera"
c=0
o=0
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
print("***************** Sistema de Telas *****************")
while(o not in [1]):
    try:
        o=int(input("Ingrese el número de una opción [1. Salir][2. Mantenimiento][3. Ventas][4. Configuración][5. Ayuda]: "))
        if (o==1):
            print("Selecciono la opción salir. Hasta pronto.")
            break
        elif (o==2):
            m=int(input("Ingrese el número de una opción de mantenimiento de tela [1. Consultar][2. Modificar][3. Listar]: "))
            if(m==1):
                r=int(input("Ingrese el número de registro que quiere visualizar: "))
                for i in l[r-1]:
                    print("{:20}: {}".format(i,l[r-1][i]))
            elif(m==2):
                r=int(input("Ingrese el número de registro que quiere modificar: "))
                for i in l[r-1]:
                    print("{:20}: {}".format(i,l[r-1][i]))
                d=input("Ingrese el campo que quiere modificar: ")
                l[r-1][d]=input("Ingrese el nuevo dato: ")
                for i in l[r-1]:
                    print("{:20}: {}".format(i,l[r-1][i]))
            elif(m==3):
                for i in l:
                    for e in i:
                        print("{:20}: {}".format(e,i[e]))
                    print("")
        elif (o==3):
            v=int(input("Ingrese el número de una opción de Ventas[1. Vender][2. Reportes]: "))
            if(v==1):
                cs+=1
                r=int(input("Ingrese el número del registro que quiere comprar: "))
                for i in l[r-1]:
                    print("{:20}: {}".format(i,l[r-1][i]))
                cant=int(input("Ingrese la cantidad que quiere comprar: "))
                ic=cant*l[r-1]["Precio (S/.)"]
                if 1<=cant<6:
                    id=p1*ic
                elif cant < 11:
                    id=p2*ic
                elif cant < 16:
                    id=p3*ic
                elif cant >=16:
                    id=p4*ic
                if cant>co:
                    regalo=obsequio
                else:
                    regalo="No corresponde"
                if cs==ss:
                    s=rs
                else:
                    s="No corresponde"
                lv.append({"Código":l[r-1]["Código"],"Descripción":l[r-1]["Descripción"],"Cantidad (m)":cant,"Importe Compra (S/.)":ic,"Importe Descuento (S/.)":id,"Importe a Pagar (S/.)":ic-id,"Obsequio":regalo,"Sorpresa":s})
                for i in lv:
                    for e in i:
                        print("{:30}: {}".format(e,i[e]))
                    print()
                if ((r-1)==0):
                    ctv0+=1
                    ctmv0+=cant
                    ita0+=(ic-id)
                elif ((r-1)==1):
                    ctv1+=1
                    ctmv1+=cant
                    ita1+=(ic-id)
                elif ((r-1)==2):
                    ctv2+=1
                    ctmv2+=cant
                    ita2+=(ic-id)
                elif ((r-1)==3):
                    ctv3+=1
                    ctmv3+=cant
                    ita3+=(ic-id)
                elif ((r-1)==4):
                    ctv4+=1
                    ctmv4+=cant
                    ita4+=(ic-id)
                itag=ita0+ita1+ita2+ita3+ita4
            if(v==2):
                re=int(input("Ingrese la opción del reporte que quiere generar[1. V*T][2. TVO][3. TP<75%PMAX][4. TP>75%PMAX][5. PMM]: "))
                if re==1:
                    print("******************* Reporte Ventas por Tela *******************")
                    print("{:40}:{}".format("Código","TF0"))
                    print("{:40}:{}".format("Descripción","Pinstripe Suit 1"))
                    print("{:40}:{}".format("Cantidad total de ventas",ctv0))
                    print("{:40}:{}".format("Cantidad total de metros vendidos",ctmv0))
                    print("{:40}:{}".format("Importe total acumulado",ita0))
                    print()

                    print("{:40}:{}".format("Código","TF1"))
                    print("{:40}:{}".format("Descripción","Gabardina Oslo 5"))
                    print("{:40}:{}".format("Cantidad total de ventas",ctv1))
                    print("{:40}:{}".format("Cantidad total de metros vendidos",ctmv1))
                    print("{:40}:{}".format("Importe total acumulado",ita1))
                    print()

                    print("{:40}:{}".format("Código","TF2"))
                    print("{:40}:{}".format("Descripción","Sarga 2"))
                    print("{:40}:{}".format("Cantidad total de ventas",ctv2))
                    print("{:40}:{}".format("Cantidad total de metros vendidos",ctmv2))
                    print("{:40}:{}".format("Importe total acumulado",ita2))
                    print()

                    print("{:40}:{}".format("Código","TF3"))
                    print("{:40}:{}".format("Descripción","Leni 1"))
                    print("{:40}:{}".format("Cantidad total de ventas",ctv3))
                    print("{:40}:{}".format("Cantidad total de metros vendidos",ctmv3))
                    print("{:40}:{}".format("Importe total acumulado",ita3))
                    print()

                    print("{:40}:{}".format("Código","TF4"))
                    print("{:40}:{}".format("Descripción","Laurent 3"))
                    print("{:40}:{}".format("Cantidad total de ventas",ctv4))
                    print("{:40}:{}".format("Cantidad total de metros vendidos",ctmv4))
                    print("{:40}:{}".format("Importe total acumulado",ita4))
                    print()

                    print("{:40}:{}".format("Importe total acumulado general",itag))
                    print()

                elif re==2:
                    print("******************* Reportes de tela con venta óptima *******************")
                    if (ctmv0>cto):
                        print("{:40}:{}".format("Código","TF0"))
                        print("{:40}:{}".format("Descripción","Pinstripe Suit 1"))
                        print("{:40}:{}".format("Cantidad total de metros vendidos",ctmv0))
                        print()
                    if (ctmv1>cto):
                        print("{:40}:{}".format("Código","TF1"))
                        print("{:40}:{}".format("Descripción","Gabardina Oslo 5"))
                        print("{:40}:{}".format("Cantidad total de metros vendidos",ctmv1))
                        print()
                    if (ctmv2>cto):
                        print("{:40}:{}".format("Código","TF2"))
                        print("{:40}:{}".format("Descripción","Sarga 2"))
                        print("{:40}:{}".format("Cantidad total de metros vendidos",ctmv2))
                        print()
                    if (ctmv3>cto):
                        print("{:40}:{}".format("Código","TF3"))
                        print("{:40}:{}".format("Descripción","Leni 1"))
                        print("{:40}:{}".format("Cantidad total de metros vendidos",ctmv3))
                        print()
                    if (ctmv4>cto):
                        print("{:40}:{}".format("Código","TF4"))
                        print("{:40}:{}".format("Descripción","Laurent 3"))
                        print("{:40}:{}".format("Cantidad total de metros vendidos",ctmv4))
                        print()
                    print("No hay más telas que superen la venta óptima")
                
                elif re==3:
                    print("******************* Telas con precios mayores al 75% del precio máximo *******************")
                    cm=0
                    for i in l:
                        pm.append(i["Precio (S/.)"])

                    p=max(pm)
                    
                    if (l[0]["Precio (S/.)"]>(0.75*p)):
                        print("{:40}:{}".format("Descripción",l[0]["Descripción"]))
                        print("{:40}:{}".format("Precio",l[0]["Precio (S/.)"]))
                        print()
                        cm +=1
                    
                    if (l[1]["Precio (S/.)"]>(0.75*p)):
                        print("{:40}:{}".format("Descripción",l[1]["Descripción"]))
                        print("{:40}:{}".format("Precio",l[1]["Precio (S/.)"]))
                        print()
                        cm +=1
                    
                    if (l[2]["Precio (S/.)"]>(0.75*p)):
                        print("{:40}:{}".format("Descripción",l[2]["Descripción"]))
                        print("{:40}:{}".format("Precio",l[2]["Precio (S/.)"]))
                        print()
                        cm +=1
                    
                    if (l[3]["Precio (S/.)"]>(0.75*p)):
                        print("{:40}:{}".format("Descripción",l[3]["Descripción"]))
                        print("{:40}:{}".format("Precio",l[3]["Precio (S/.)"]))
                        print()
                        cm +=1
                    
                    if (l[4]["Precio (S/.)"]>(0.75*p)):
                        print("{:40}:{}".format("Descripción",l[4]["Descripción"]))
                        print("{:40}:{}".format("Precio",l[4]["Precio (S/.)"]))
                        print()
                        cm +=1
                    
                    print("75% del precio máximo: ",p)
                    print("Número de marcas: ",cm)
                
                elif re==4:
                    print("******************* Telas con precios menores al 75% del precio máximo *******************")
                    cm=0
                    for i in l:
                        pm.append(i["Precio (S/.)"])

                    p=max(pm)
                    
                    if (l[0]["Precio (S/.)"]<(0.75*p)):
                        print("{:40}:{}".format("Descripción",l[0]["Descripción"]))
                        print("{:40}:{}".format("Precio",l[0]["Precio (S/.)"]))
                        print()
                        cm +=1
                    
                    if (l[1]["Precio (S/.)"]<(0.75*p)):
                        print("{:40}:{}".format("Descripción",l[1]["Descripción"]))
                        print("{:40}:{}".format("Precio",l[1]["Precio (S/.)"]))
                        print()
                        cm +=1
                    
                    if (l[2]["Precio (S/.)"]<(0.75*p)):
                        print("{:40}:{}".format("Descripción",l[2]["Descripción"]))
                        print("{:40}:{}".format("Precio",l[2]["Precio (S/.)"]))
                        print()
                        cm +=1
                    
                    if (l[3]["Precio (S/.)"]<(0.75*p)):
                        print("{:40}:{}".format("Descripción",l[3]["Descripción"]))
                        print("{:40}:{}".format("Precio",l[3]["Precio (S/.)"]))
                        print()
                        cm +=1
                    
                    if (l[4]["Precio (S/.)"]<(0.75*p)):
                        print("{:40}:{}".format("Descripción",l[4]["Descripción"]))
                        print("{:40}:{}".format("Precio",l[4]["Precio (S/.)"]))
                        print()
                        cm +=1
                    
                    print("75% del precio máximo: ",p)
                    print("Número de marcas: ",cm)
                
                elif re==5:
                    print("******************* Promedios, máximos y mínimos *******************")
                    for i in l:
                        pm.append(i["Precio (S/.)"])
                        p.append(i["Peso (g/m2)"])
                        a.append(i["Ancho (cm)"])
                    print()
                    print("{:40}:{} cm".format("Ancho promedio",sum(a)/float(len(a))))
                    print("{:40}:{} cm".format("Ancho mínimo",min(a)))
                    print("{:40}:{} cm".format("Ancho máximo",max(a)))

                    print()
                    print("{:40}:{} g/m2".format("Peso promedio",sum(p)/float(len(p))))
                    print("{:40}:{} g/m2".format("Peso mínimo",min(p)))
                    print("{:40}:{} g/m2".format("Peso máximo",max(p)))

                    print()
                    print("{:40}: S/. {}".format("Precio promedio",sum(pm)/float(len(pm))))
                    print("{:40}: S/. {}".format("Precio mínimo",min(pm)))
                    print("{:40}: S/. {}".format("Precio máximo",max(pm)))

        elif (o==4):
            r=int(input("Ingrese el número de la opción de configuración[1. Descuentos][2. Obsequio][3. COMV][4. Premio]: "))
            if r==1:
                print("Configurar porcentajes de descuento:")
                print("1 a 5 metros ",p1)
                print("6 a 10 metros ",p2)
                print("11 a 15 metros ",p3)
                print("Más de 15 metros ",p4)
                i=int(input("Indicar el número de descuento que desea modificar: "))
                if i==1:
                    p1=float(input("Ingrese el porcentaje de descuento: "))/100
                elif i==2:
                    p2=float(input("Ingrese el porcentaje de descuento: "))/100
                elif i==3:
                    p3=float(input("Ingrese el porcentaje de descuento: "))/100
                elif i==4:
                    p4=float(input("Ingrese el porcentaje de descuento: "))/100
                print("Porcentajes de descuento:")
                print("1 a 5 metros ",p1)
                print("6 a 10 metros ",p2)
                print("11 a 15 metros ",p3)
                print("Más de 15 metros ",p4)
            elif r==2:
                co=int(input("Indicar cantidad mínima: "))
                obsequio=input("Indicar el obsequio: ")
            elif r==3:
                cto=int(input("Indicar cantidad optima: "))
            elif r==4:
                ss=int(input("Indicar número de cliente: "))
                rs=input("Indicar el regalo sorpresa: ")
        
        elif (o==5):
            print("Acerca de la tienda: Somos la mejor tienda del país y el sistema se encuentra en la versión 4.0")

    except:
        print("Error, solo se pueden ingresar números entre el 1 y el 5 según las opciones indicadas...")
    