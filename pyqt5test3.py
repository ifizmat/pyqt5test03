from mainwindow import *
    
def start_button_onclick():
    ui.test_label.setText("Start")        

def stop_button_onclick(self):
    ui.test_label.setText("Stop")
    
import sys
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

ui.test_label.setText("UI started... OK!")
ui.start_button.clicked.connect(start_button_onclick)
ui.stop_button.clicked.connect(stop_button_onclick)

sys.exit(app.exec_())
