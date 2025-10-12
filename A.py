import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QPixmap, QColor, QPalette
from PyQt6.QtWidgets import (QApplication, QMainWindow,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QHBoxLayout,
    QVBoxLayout,
	QGridLayout,
	QStackedLayout,
	QTabWidget,
    QWidget,
	QMenu,
	QListWidget,
)

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("MM2MM - Mario Maker 2 Mod Manager")
		self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
		self.customContextMenuRequested.connect(self.context_menu)


	#	layout = QVBoxLayout()

	#	label = QLabel()
	#	label.setPixmap(QPixmap("placeholder.png"))
	#	layout.addWidget(label)

	#	combo = QComboBox()
	#	combo.addItems(["Normal", "Dark"])
	#	combo.setEditable(True)
	#	combo.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
	#	layout.addWidget(combo)

	#	dial = QDial()
	#	dial.setRange(0, 359)
	#	dial.setSingleStep(1)
	#	layout.addWidget(dial)

		tabs = QTabWidget()
		tabs.setDocumentMode(True)

		tabs.setTabPosition(QTabWidget.TabPosition.North)
		tabs.setMovable(True)

		for color in ["red", "green", "blue", "yellow"]:
			tabs.addTab(Color(color), color)

	#	container = QWidget()
	#	container.setLayout(layout)
			
		self.setCentralWidget(tabs)
		
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