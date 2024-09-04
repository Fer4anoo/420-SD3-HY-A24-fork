from PySide6.QtWidgets import QMainWindow, QStatusBar, QToolBar, QApplication, QPushButton, QDialog, QVBoxLayout
from PySide6.QtGui import QAction, QKeySequence, QIcon
from PySide6.QtCore import QSize

class Fenetreprincipale(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mon application")

        menus = self.menuBar()
        self.creer_menus(menus)

        self.barre_status = QStatusBar()
        self.barre_status.setStatusTip("cliquer un bouton")

        #barre d'outils
        boutton_test = QPushButton("Test")
        boutton_test.pressed.connect(self.outil)
        barre_outils = QToolBar("barre d'outils")
        barre_outils.addWidget(boutton_test)
        self.addToolBar(barre_outils)

        #Qdialog
        boutton_dialog = QPushButton("Qdialog")
        boutton_dialog.clicked.connect(self.dialog)
        layout = QVBoxLayout()
        layout.addWidget(boutton_dialog)

    def creer_menus(self, menus):
        #premier menu
        nom_menu = menus.addMenu("&Menu1")
        action1 = QAction(text="test!", parent=self)
        action1.setStatusTip("Menu1")
        action1.triggered.connect(self.action1_execute)
        nom_menu.addAction(action1)

        #deuxieme menu
        nom_menu2 = menus.addMenu("M&enu2")
        action2 = QAction(text="Hello!", parent=self)
        action2.setStatusTip("Menu2")
        action2.triggered.connect(self.action2_execute)
        nom_menu2.addAction(action2)

    def action1_execute(self):
        print("yeahhh!")

    def action2_execute(self):
        print("nooooo!")

    def outil(self):
        print("boutton outil")

    def dialog(self):
        dialogue = QDialog(self)
        dialogue.setWindowTitle("Fenêtre de dialogue")
        boutton_fermer = QPushButton("fermeture")
        boutton_fermer.clicked.connect(dialogue.exec())


app = QApplication()
affichage = Fenetreprincipale()
affichage.show()
app.exec()







