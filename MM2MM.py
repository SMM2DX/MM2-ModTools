import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon, QKeySequence, QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QToolBar, QMenu, QStatusBar, QMessageBox, QWidget,
	QTabWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QPushButton
)

from Modules.ThemeCompiler.ThemeCompiler import main as CompileThemes
from Modules.ThemeDecompiler.ThemeDecompiler import main as DecompileThemes
#from Modules.MarginTool.margintool import main as RemoveMargins
#from Modules.MarginTool.reversemargintool import main as AddMargins

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("MM2MM - Mario Maker 2 Mod Manager")
		self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
		self.customContextMenuRequested.connect(self.context_menu)
		self.setStatusBar(QStatusBar(self))

		mainWidget = QWidget()
		mainLayout = QHBoxLayout()
		mainLayout.setContentsMargins(0,0,0,0) # Spacing and stuff for visuals
		mainLayout.setSpacing(0)
		mainWidget.setLayout(mainLayout)
		self.setCentralWidget(mainWidget)
		if True:
			tabsWidget = QTabWidget()
			tabsWidget.setTabPosition(QTabWidget.TabPosition.West)
			tabsWidget.setDocumentMode(True)
			tabsWidget.setMovable(True)
			mainLayout.addWidget(tabsWidget)
			if True:
				tab = QWidget()
				tabLayout = QVBoxLayout()
				tabLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
				tabLabel = QLabel()
				tabLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
				tabLabel.setText("Theme Compiler")
				tabLayout.addWidget(tabLabel)
				tabButton = QPushButton()
				tabButton.setText("Run")
				tabButton.setStatusTip("Run Theme Compiler")
				tabButton.clicked.connect(self.compile_button_clicked)
				tabLayout.addWidget(tabButton)
				tab.setLayout(tabLayout)
				tabsWidget.addTab(tab, "Compiler")
			if True:
				tab = QWidget()
				tabLayout = QVBoxLayout()
				tabLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
				tabLabel = QLabel()
				tabLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
				tabLabel.setText("Theme Decompiler")
				tabLayout.addWidget(tabLabel)
				tabButton = QPushButton()
				tabButton.setText("Run")
				tabButton.setStatusTip("Run Theme Decompiler")
				tabButton.clicked.connect(self.decompile_button_clicked)
				tabLayout.addWidget(tabButton)
				tab.setLayout(tabLayout)
				tabsWidget.addTab(tab, "Decompiler")
			if True:
				tab = QWidget()
				tabLayout = QVBoxLayout()
				tabLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
				tabLabel = QLabel()
				tabLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
				tabLabel.setText("NSMBU Margin Tool\n(UNIMPLEMENTED)")
				tabLayout.addWidget(tabLabel)
				if True:
					buttonsWidget = QWidget()
					buttonsLayout = QHBoxLayout()
					buttonsLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
					tabButton1 = QPushButton()
					tabButton1.setText("Remove")
					tabButton1.setStatusTip("Remove Tileset Margins")
					tabButton1.clicked.connect(self.margin_remove_button_clicked)
					buttonsLayout.addWidget(tabButton1)
					tabButton2 = QPushButton()
					tabButton2.setText("Add")
					tabButton2.setStatusTip("Add Tileset Margins")
					tabButton2.clicked.connect(self.margin_add_button_clicked)
					buttonsLayout.addWidget(tabButton2)
					buttonsWidget.setLayout(buttonsLayout)
					tabLayout.addWidget(buttonsWidget)
				tab.setLayout(tabLayout)
				tabsWidget.addTab(tab, "Margin Tool")
			
			temp = QWidget()
			tempLayout = QVBoxLayout()
			tempLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
			placeholderImgWidget = QLabel()
			placeholderImgWidget.setAlignment(Qt.AlignmentFlag.AlignCenter)
			placeholderImgWidget.setPixmap(QPixmap("Assets/placeholder.png"))
			tempLayout.addWidget(placeholderImgWidget)
			placeholderTxtWidget = QLabel()
			placeholderTxtWidget.setAlignment(Qt.AlignmentFlag.AlignCenter)
			placeholderTxtWidget.setText("Please enjoy this pretty placeholder image")
			tempLayout.addWidget(placeholderTxtWidget)
			temp.setLayout(tempLayout)
			mainLayout.addWidget(temp)

		toolbar = QToolBar("Toolbar")
		toolbar.setMovable(False)
		toolbar.setIconSize(QSize(16, 16))
		toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
		self.addToolBar(toolbar)
		menu = self.menuBar()
		if True:
			# Actions
			button_action = QAction(QIcon("Assets/fugue-icons/icons/bug.png"), "Button &1", self)
			button_action.setStatusTip("This does nothing")
			button_action.triggered.connect(self.placeholder_button_clicked)
			#button_action.setShortcut(QKeySequence.StandardKey.Print)

			button_action2 = QAction(QIcon("Assets/fugue-icons/icons/bug.png"), "Button &2", self)
			button_action2.setStatusTip("This does nothing")
			button_action2.triggered.connect(self.placeholder_button_clicked)

			# Toolbar
			toolbar.addAction(button_action)
			toolbar.addSeparator()
			toolbar.addAction(button_action2)
			
			# Menu Bar
			file_menu = menu.addMenu("&File")
			file_menu.addAction(button_action)
			file_menu.addSeparator()
			file_submenu = file_menu.addMenu("&Submenu")
			file_submenu.addAction(button_action2)

	def placeholder_button_clicked(self):
		# print("click")
		pass
	def compile_button_clicked(self):
		response = QMessageBox.question(self, "Are you sure?", "Are you sure you want to compile .MM2Theme files to .byml?")
		if response == QMessageBox.StandardButton.Yes:
			CompileThemes()
			QMessageBox.information(self, "Success", "Finished Successfully")
	def decompile_button_clicked(self):
		response = QMessageBox.question(self, "Are you sure?", "Are you sure you want to decompile .byml files to .MM2Theme?")
		if response == QMessageBox.StandardButton.Yes:
			DecompileThemes()
			QMessageBox.information(self, "Success", "Finished Successfully")
	def margin_remove_button_clicked(self):
		QMessageBox.warning(self, "Unimplemented", "This feature is currently unimplemented.")
		# response = QMessageBox.question(self, "Are you sure?", "Are you sure you want to remove tileset margins?")
		# if response == QMessageBox.StandardButton.Yes:
		# 	RemoveMargins()
	def margin_add_button_clicked(self):
		QMessageBox.warning(self, "Unimplemented", "This feature is currently unimplemented.")
		# response = QMessageBox.question(self, "Are you sure?", "Are you sure you want to add tileset margins?")
		# if response == QMessageBox.StandardButton.Yes:
		# 	AddMargins()

	def context_menu(self, pos):
		context = QMenu(self)
		context.addAction(QAction("No Right-Click Actions available", self))
		context.exec(self.mapToGlobal(pos))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()