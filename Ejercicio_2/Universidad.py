import array as ary
import sys
from PyQt6.QtWidgets import QMainWindow,QApplication
from PyQt6 import uic
import Funciones as operaciones
class Ejercicio02(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("Formulario2.ui",self)
        self.initUi()

    def initUi(self):
        self.blimpiar.clicked.connect(self.limpiar)
        #self.blimparn.clicked.connect(self.limpiarNotas)
        self.blimpiartodo.clicked.connect(self.limpiarTodo)
        self.bcurso.clicked.connect(self.mostrarCurso)
        self.bnotas.clicked.connect(self.digitarNotas)
        self.bcalcular.clicked.connect(self.calcular)
        self.bsalir.clicked.connect(self.salir)

    def limpiar(self):
        self.tcodigo.setText("")
        self.tnombre.setText("")
        self.tapellido.setText("")
        self.cbciclo.setCurrentIndex(0)
        self.lblcurso.setText("")
        self.tcodigo.setFocus()

    def limpiarNotas(self):
        self.tnota1.setText("")
        self.tnota2.setText("")
        self.tnota3.setText("")
        self.tnota4.setText("")
        self.tnota1.setFocus()
    
    def limpiarTodo(self):
        self.tcodigo.setText("")
        self.tnombre.setText("")
        self.tapellido.setText("")
        self.cbciclo.setCurrentIndex(0)
        self.lblcurso.setText("")
        self.lblc1.setText("Curso 1:")
        self.lblc2.setText("Curso 2:")
        self.lblc3.setText("Curso 3:")
        self.lblc4.setText("Curso 4:")
        self.tnota1.setText("")
        self.tnota2.setText("")
        self.tnota3.setText("")
        self.tnota4.setText("")
        self.lblpromedio.setText("")
        self.lblobservacion.setText("")
        self.tcodigo.setFocus()
    
    def mostrarCurso(self):
        ciclo=self.cbciclo.currentText()
        mensaje=operaciones.buscarCursos(ciclo)
        self.lblcurso.setText(mensaje)

    def digitarNotas(self):
        ciclo=self.cbciclo.currentText()
        a=operaciones.mostrarCurso(ciclo)
        self.lblc1.setText(a[0])
        self.lblc2.setText(a[1])
        self.lblc3.setText(a[2])
        self.lblc4.setText(a[3])
        self.tnota1.setFocus()
        
    def calcular(self):
        n1=int(self.tnota1.text())
        n2=int(self.tnota2.text())
        n3=int(self.tnota3.text())
        n4=int(self.tnota4.text())
        prom=operaciones.promediar(n1,n2,n3,n4)
        obs=operaciones.Observacion(prom)
        self.lblpromedio.setText(str(prom))
        self.lblobservacion.setText(obs)

    def salir(self):
        self.close()
if __name__=='__main__':
    app=QApplication(sys.argv)
    ventana_2=Ejercicio02()
    ventana_2.show()
    sys.exit(app.exec())