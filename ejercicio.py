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
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QButtonGroup, QRadioButton, QComboBox, QCheckBox, QPushButton, QMessageBox
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

        label_pais = QLabel("País:")
        self.combo_pais = QComboBox()
        self.combo_pais.addItems(
            ["Argentina", "Chile", "Uruguay", "México", "España"]
        )
        layout.addWidget(label_pais, 6, 0)
        layout.addWidget(self.combo_pais, 6, 1)

        self.chk_terminos = QCheckBox("Acepto los términos y condiciones")
        layout.addWidget(self.chk_terminos, 7, 0, 1, 2)

        btn_registrar = QPushButton("Registrarse")
        btn_registrar.clicked.connect(self.registrar)
        layout.addWidget(btn_registrar, 8, 0, 1, 2)
        
        self.setStyleSheet("""
            QWidget {
                background-color: #f4f4f9;
            }
            QLabel {
                font-size: 14px;
            }
            QLineEdit, QComboBox {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                padding: 8px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

    def registrar(self):
        nombre = self.txt_nombre.text().strip()
        email = self.txt_email.text().strip()
        password = self.txt_pass.text().strip()
        genero = None
        if self.radio_m.isChecked():
            genero = "Masculino"
        elif self.radio_f.isChecked():
            genero = "Femenino"
        pais = self.combo_pais.currentText()
        terminos = self.chk_terminos.isChecked()

        if not nombre or not email or not password or genero is None or not terminos:
            QMessageBox.warning(self, "Error", "Por favor completa todos los campos y acepta los términos.")
        else:
            QMessageBox.information(self, "Éxito", f"Usuario {nombre} registrado correctamente.")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())