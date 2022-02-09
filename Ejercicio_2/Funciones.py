
import numpy as ary
def buscarCursos(curso):
    if curso=="I":
        m="  Curso 1\t\t       Curso 2  \t     Curso 3    \t    Curso 4\n"
        m=m+"Windows\t\t       Word    \t       Excel       \t    Acces"
    elif curso=="II":
        m=  "  Curso 1  \tCurso 2  \tCurso 3    \tCurso 4\n"
        m=m+"Power Point\tInternet\t\tExtranet\t\tIntranet"
    elif curso == "III":
        m=  "     Curso 1       \t     Curso 2  \t   Curso 3\t   Curso 4\n"
        m=m+"Visual Basic 6.0\t   .net 2019-I\t    SQL-I  \t  Analisis-I"
    elif curso == "IV":
        m=  "Curso 1 \t      Curso 2  \t Curso 3\t      Curso 4\n"
        m=m+" Java I \t   .net 2019-II\t  SQL-II \t     Analisis-II"
    elif curso == "V":
        m=  "Curso 1\t     Curso 2   \t  Curso 3\tCurso 4\n"
        m=m+"Java II\t  Asp .net 2019\t  Oracle-I\tProyectos"
    elif curso == "VI":
        m="Curso 1\t      Curso 2\tCurso 3\t       Curso 4\n"
        m=m+"Java III\t    Linux\t\t  Php\t        Sistemas"
    elif curso == "Otros":
        m="<-------Ciclo no valido------->"
    return m


def promediar(n1,n2,n3,n4):
    prom=(n1+n2+n3+n4)/4
    return prom

def Observacion(prom):
    if prom >=0 and prom < 6:
        obs="Bajo Rendimiento"
    elif prom >= 6 and prom < 10:
        obs="Malo"
    elif prom >=10 and prom < 15:
        obs="Rendimiento Regular"
    elif prom >=15 and prom <18:
        obs="Rendimiento Bueno"
    elif prom >= 18 and prom <=20:
        obs="Rendimiento Excelente"
    else:
        obs="Las notas son de 0-20"
    return obs

def mostrarCurso(ciclo):
    if ciclo=="I":
        a=['Windows','Word','Excel','Acces']
    elif ciclo=="II":
        a=['Power Point','Internet','Extranet','Intranet']
    elif ciclo == "III":
        a=['Visual Basic 6.0','.net 2019-I','SQL-I','Analisis-I']
    elif ciclo == "IV":
        a=['Java I','.net 2019-II','SQL-II','Analisis-II']
    elif ciclo == "V":
        a=['Java II','Asp .net 2019','Oracle-I','Proyectos']
    elif ciclo == "VI":
        a=['Java III','Linux','Php','Sistemas']
    return a