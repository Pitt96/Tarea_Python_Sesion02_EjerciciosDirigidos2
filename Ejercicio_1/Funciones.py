import array as ary
def categoriaSueldo(categoria):
    if categoria == "A":
        ocupacion="Analista"
        sueldo=2500
        d1=porcentaje(sueldo,0.12)
        d2=porcentaje(sueldo,0.1)
        b1=porcentaje(sueldo,0.14)
        b2=porcentaje(sueldo,0.16)
        t=sueldo-d1-d2+b1+b2
        s=[ocupacion,str(sueldo),str(d1),str(d2),str(round(b1,2)),str(b2),str(round(t,2))]
    elif categoria == "B":
        ocupacion="Programador"
        sueldo=1500
        d1=porcentaje(sueldo,0.1)
        d2=porcentaje(sueldo,0.08)
        b1=porcentaje(sueldo,0.12)
        b2=porcentaje(sueldo,0.14)
        t=sueldo-d1-d2+b1+b2
        s=[ocupacion,str(sueldo),str(d1),str(d2),str(b1),str(round(b2,2)),str(round(t,2))]
    elif categoria == "C":
        ocupacion="Asistente"
        sueldo=1000
        d1=porcentaje(sueldo,0.08)
        d2=porcentaje(sueldo,0.06)
        b1=porcentaje(sueldo,0.10)
        b2=porcentaje(sueldo,0.12)
        t=sueldo-d1-d2+b1+b2
        s=[ocupacion,str(sueldo),str(d1),str(d2),str(b1),str(b2),str(round(t,2))]
    elif categoria == "D":
        ocupacion="Tecnico"
        sueldo=700
        d1=porcentaje(sueldo,0.06)
        d2=porcentaje(sueldo,0.04)
        b1=porcentaje(sueldo,0.08)
        b2=porcentaje(sueldo,0.10)
        t=sueldo-d1-d2+b1+b2
        s=[ocupacion,str(sueldo),str(d1),str(d2),str(b1),str(b2),str(round(t,2))]
    elif categoria == "E":
        ocupacion="Operador"
        sueldo=500
        d1=porcentaje(sueldo,0.04)
        d2=porcentaje(sueldo,0.02)
        b1=porcentaje(sueldo,0.06)
        b2=porcentaje(sueldo,0.08)
        t=sueldo-d1-d2+b1+b2
        s=[ocupacion,str(sueldo),str(d1),str(d2),str(b1),str(b2),str(round(t,2))]
    return s

def porcentaje(s,por):
    return s*por

def mostrar(a0,a1,a2,a3,a4,a5,t):
    m=  "Ocupacion         :    "+a0
    m=m+"\nSueldo          : S/."+a1
    m=m+"\nDescuento 1     : S/."+a2
    m=m+"\nDescuento 2     : S/."+a3
    m=m+"\nBonificacion 1  : S/."+a4
    m=m+"\nBonificacion 2  : S/."+a5
    m=m+"\n****************************************"
    m=m+"\nSueldo Final      : S/."+t
    return m