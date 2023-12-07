import matplotlib.pyplot as plt
import pyqtgraph as pg
from PySide6.QtCore import Slot
import sys
from PySide6 import QtWidgets
import numpy as np

#set colour of the background and graph
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        vbox = QtWidgets.QVBoxLayout(central_widget)
        plot_1_widget = pg.PlotWidget()
        vbox.addWidget(plot_1_widget)        
        plot_2_widget = pg.PlotWidget()
        vbox.addWidget(plot_2_widget)        
        plot_3_widget = pg.PlotWidget()
        vbox.addWidget(plot_3_widget)







def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()  