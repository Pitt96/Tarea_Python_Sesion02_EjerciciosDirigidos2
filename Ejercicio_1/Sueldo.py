import array as ary
import sys
from PyQt6.QtWidgets import QMainWindow,QApplication
from PyQt6 import uic
import Funciones as operaciones
class Ejercicio01(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("FormularioS2_01.ui",self)
        self.initUi()
    
    def initUi(self):
        self.bnuevo.clicked.connect(self.limpiar)
        self.bsueldo.clicked.connect(self.sueldo)
        self.bsalir.clicked.connect(self.salir)

    def limpiar(self):
        self.tnombre.setText("")
        self.tapellido.setText("")
        self.tdni.setText("")
        self.cbcategoria.setCurrentIndex(0)
        self.lblarea.setText("")
        self.tnombre.setFocus()

    def sueldo(self):
        categoria=self.cbcategoria.currentText()
        if categoria=="Escoge.." or categoria=="Otros..":
            a="Categoria no valida"
            self.lblarea.setText(a)
        else:
            a=operaciones.categoriaSueldo(categoria)
            ocup=a[0]
            sueldo=a[1]
            des1=a[2]
            des2=a[3]
            bon1=a[4]
            bon2=a[5]
            total=a[6]
            mensaje=operaciones.mostrar(ocup,sueldo,des1,des2,bon1,bon2,total)
            self.lblarea.setText(mensaje)
        

    def salir(self):
        self.close()
if __name__=='__main__':
    app=QApplication(sys.argv)
    ventana_1=Ejercicio01()
    ventana_1.show()
    sys.exit(app.exec())