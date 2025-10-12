import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QMenu, QWidget,
	QTabWidget,
    QHBoxLayout,
    QVBoxLayout,
	QGridLayout,
	QLabel,
)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("MM2MM - Mario Maker 2 Mod Manager")
		self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
		self.customContextMenuRequested.connect(self.context_menu)

		layout = QHBoxLayout()

		temp1 = QLabel()
		temp1.setText("Placeholder Text 1")
		temp2 = QLabel()
		temp2.setText("Placeholder Text 2")

		tabs = QTabWidget()
		tabs.setDocumentMode(True)
		tabs.setTabPosition(QTabWidget.TabPosition.West)
		tabs.setMovable(True)
		tabs.addTab(temp1, "1")
		tabs.addTab(temp2, "2")
		layout.addWidget(tabs)

		label = QLabel()
		label.setPixmap(QPixmap("placeholder.png"))
		layout.addWidget(label)

		container = QWidget()
		container.setLayout(layout)
			
		self.setCentralWidget(container)

	def context_menu(self, pos):
		context = QMenu(self)
		context.addAction(QAction("test 1", self))
		context.addAction(QAction("test 2", self))
		context.addAction(QAction("test 3", self))
		context.exec(self.mapToGlobal(pos))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()