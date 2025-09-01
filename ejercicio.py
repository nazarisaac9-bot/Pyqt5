# Práctico PyQt5: Construcción guiada de una interfaz completa
# ------------------------------------------------------------
#
# Objetivo: Construir paso a paso un formulario de registro moderno y funcional.
# Cada ejercicio suma widgets y lógica, guiando al alumno en el uso de PyQt5 y QGridLayout.
#
# -----------------------------------------------------------------------------
# Ejercicio 1: Estructura básica y primer campo
# -----------------------------------------------------------------------------
# Teoría:
# - QLabel muestra texto en la interfaz.
# - QLineEdit permite ingresar texto.
# - QGridLayout organiza los widgets en filas y columnas.
#
# Consigna:
# - Ventana 400x300, título “Registro de Usuario”.
# - QLabel grande y centrado: “Formulario de Registro”.
# - QLabel “Nombre:” y QLineEdit al lado, usando QGridLayout.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QButtonGroup, QRadioButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        titulo = QLabel("Formulario de Registro")
        fuente = QFont()
        fuente.setFamily("Arial")
        fuente.setPointSize(16)
        fuente.setBold(True)

        titulo.setFont(fuente)
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo, 0,0,1,2)
        label_nombre = QLabel("Nombre: ")
        self.txt_nombre = QLineEdit()
        layout.addWidget(label_nombre, 1, 0)
        layout.addWidget(self.txt_nombre, 1, 1)

        label_email = QLabel("Email:")
        self.txt_email = QLineEdit()
        layout.addWidget(label_email, 2, 0)
        layout.addWidget(self.txt_email, 2, 1)

        lbl_pass = QLabel("Contraseña:")
        self.txt_pass = QLineEdit()
        self.txt_pass.setEchoMode(QLineEdit.Password)
        layout.addWidget(lbl_pass, 3, 0)
        layout.addWidget(self.txt_pass, 3, 1)

        label_genero = QLabel("Género:")
        self.radio_m = QRadioButton("Masculino")
        self.radio_f = QRadioButton("Femenino")

        self.grupo_genero = QButtonGroup()
        self.grupo_genero.addButton(self.radio_m)
        self.grupo_genero.addButton(self.radio_f)

        layout.addWidget(label_genero, 4, 0)
        layout.addWidget(self.radio_m, 4, 1)
        layout.addWidget(self.radio_f, 5, 1)



# -----------------------------------------------------------------------------
# Ejercicio 4: Selección de país
# -----------------------------------------------------------------------------
# Teoría:
# - QComboBox permite elegir una opción de una lista desplegable.
#
# Consigna:
# - Agregar QLabel “País:” y QComboBox con al menos 5 países.

# -----------------------------------------------------------------------------
# Ejercicio 5: Checkbox de términos
# -----------------------------------------------------------------------------
# Teoría:
# - QCheckBox permite aceptar o rechazar condiciones.
#
# Consigna:
# - Agregar QCheckBox: “Acepto los términos y condiciones”.

# -----------------------------------------------------------------------------
# Ejercicio 6: Botón de envío y validación
# -----------------------------------------------------------------------------
# Teoría:
# - QPushButton ejecuta una función al hacer clic.
# - QMessageBox muestra mensajes emergentes.
#
# Consigna:
# - Agregar QPushButton “Registrarse”.
# - Al hacer clic, validar que todos los campos estén completos y el checkbox marcado.
# - Mostrar mensaje de éxito o error.

# -----------------------------------------------------------------------------
# Ejercicio 7: Personalización visual
# -----------------------------------------------------------------------------
# Consigna:
# - Cambiar colores de fondo, fuentes y tamaño de los widgets.
# - Centrar el formulario en la ventana.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())