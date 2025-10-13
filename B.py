import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon, QKeySequence, QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QToolBar, QMenu, QStatusBar, QMessageBox, QWidget,
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
		layout.setContentsMargins(0,0,0,0)
		#layout.setSpacing(20)

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
		
		toolbar = QToolBar("The Toolbar")
		toolbar.setMovable(False)
		toolbar.setIconSize(QSize(16, 16))
		toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

		button_action = QAction(QIcon("fugue-icons-3.5.6/icons/bug.png"), "Button &1", self)
		button_action.setStatusTip("This is your button")
		button_action.triggered.connect(self.toolbar_button_clicked)
		button_action.setCheckable(True)
		button_action.setShortcut(QKeySequence.StandardKey.Print)
		toolbar.addAction(button_action)

		toolbar.addSeparator()

		button_action2 = QAction(QIcon("fugue-icons-3.5.6/icons/bug.png"), "Button &2", self)
		button_action2.setStatusTip("This is also your button")
		button_action2.triggered.connect(self.toolbar_button_clicked2)
		toolbar.addAction(button_action2)

		menu = self.menuBar()

		file_menu = menu.addMenu("&File")
		file_menu.addAction(button_action)
		file_menu.addSeparator()
		
		file_submenu = file_menu.addMenu("&Submenu")
		file_submenu.addAction(button_action2)
			
		self.setCentralWidget(container)
		self.setStatusBar(QStatusBar(self))
		self.addToolBar(toolbar)

	def toolbar_button_clicked(self, s):
		print("click", s)
	def toolbar_button_clicked2(self):
		print("click")
		response = QMessageBox.question(self, "Question for you", "Is this ok?")

		if response == QMessageBox.StandardButton.Yes:
			print("Yes")
		else:
			print("No!")

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