import os
import sys
import json
import oead
from Modules.MM2Things import THEMES, GameStyle, SMB1_Theme, SMB3_Theme, SMW_Theme, NSMBU_Theme, SM3DW_Theme, MyWorld_Theme
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon, QKeySequence, QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QToolBar, QMenu, QStatusBar, QMessageBox, QWidget,
	QTabWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QPushButton
)

from Modules.ThemeCompiler.ThemeCompiler import main as CompileThemes
#from Modules.MarginTool.margintool import main as RemoveMargins
#from Modules.MarginTool.reversemargintool import main as AddMargins

DIRECTORY = os.path.dirname(__file__)+"/"
if not os.path.exists(DIRECTORY+"BYML-Input/"):
	os.makedirs(DIRECTORY+"BYML-Input/")

#def CompileThemes(window): THEMES[GameStyle.SMB1][0].print()

def DecompileThemes(window):
	if not os.path.exists(DIRECTORY+"BYML-Input/"):
		os.makedirs(DIRECTORY+"BYML-Input/")
	if not os.path.exists(DIRECTORY+"MM2Theme-Output/"):
		os.makedirs(DIRECTORY+"MM2Theme-Output/")
	
	for fileName in os.listdir(DIRECTORY+"BYML-Input/"):
		if not fileName.endswith(".byml"): continue
		with open(DIRECTORY+"BYML-Input/"+fileName, "rb") as bymlFile:
			for theme_dict in oead.byml.from_binary(bymlFile.read()):
				Theme = None
				if (fileName.startswith("M1_")): Theme = SMB1_Theme.from_byml_dict(theme_dict)
				elif (fileName.startswith("M3_")): Theme = SMB3_Theme.from_byml_dict(theme_dict)
				elif (fileName.startswith("MW_")): Theme = SMW_Theme.from_byml_dict(theme_dict)
				elif (fileName.startswith("WU_")): Theme = NSMBU_Theme.from_byml_dict(theme_dict)
				elif (fileName.startswith("3W_")): Theme = SM3DW_Theme.from_byml_dict(theme_dict)
				elif (fileName.endswith("_MyWorld.byml")): Theme = MyWorld_Theme.from_byml_dict(theme_dict)
				else:
					QMessageBox.warning(window, "Invalid File", f"Encountered file {fileName} with invalid Gamestyle, skipping")
					break
				
				with open(DIRECTORY+"MM2Theme-Output/"+Theme.Theme_Name+"."+Theme.Style.value+".MM2Theme", "wt") as jsonFile:
					json.dump(Theme.as_json_dict(), jsonFile)
	window.themeCountTxtWidget.setText(f"{GameStyle.SMB1.name}: {len(THEMES[GameStyle.SMB1])} - " +
										f"{GameStyle.SMB3.name}: {len(THEMES[GameStyle.SMB3])} - " +
										f"{GameStyle.SMW.name}: {len(THEMES[GameStyle.SMW])} - " +
										f"{GameStyle.NSMBU.name}: {len(THEMES[GameStyle.NSMBU])}\n" +
										f"{GameStyle.SM3DW.name}: {len(THEMES[GameStyle.SM3DW])} - " +
										f"{GameStyle.MyWorld.name}: {len(THEMES[GameStyle.MyWorld])}")


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("MM2MT - Mario Maker 2 Mod Tools")
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
			self.themeCountTxtWidget = QLabel()
			self.themeCountTxtWidget.setAlignment(Qt.AlignmentFlag.AlignCenter)
			self.themeCountTxtWidget.setText(f"{GameStyle.SMB1.name}: {len(THEMES[GameStyle.SMB1])} - " +
											f"{GameStyle.SMB3.name}: {len(THEMES[GameStyle.SMB3])} - " +
											f"{GameStyle.SMW.name}: {len(THEMES[GameStyle.SMW])} - " +
											f"{GameStyle.NSMBU.name}: {len(THEMES[GameStyle.NSMBU])}\n" +
											f"{GameStyle.SM3DW.name}: {len(THEMES[GameStyle.SM3DW])} - " +
											f"{GameStyle.MyWorld.name}: {len(THEMES[GameStyle.MyWorld])}")
			tempLayout.addWidget(self.themeCountTxtWidget)
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
			CompileThemes(self)
			QMessageBox.information(self, "Success", "Finished Successfully")
	def decompile_button_clicked(self):
		response = QMessageBox.question(self, "Are you sure?", "Are you sure you want to decompile .byml files to .MM2Theme?")
		if response == QMessageBox.StandardButton.Yes:
			DecompileThemes(self)
			QMessageBox.information(self, "Success", "Finished Successfully")
	def margin_remove_button_clicked(self):
		QMessageBox.warning(self, "Unimplemented", "This feature is currently unimplemented.")
		# response = QMessageBox.question(self, "Are you sure?", "Are you sure you want to remove tileset margins?")
		# if response == QMessageBox.StandardButton.Yes:
		# 	RemoveMargins()
		#	QMessageBox.information(self, "Success", "Finished Successfully")
	def margin_add_button_clicked(self):
		QMessageBox.warning(self, "Unimplemented", "This feature is currently unimplemented.")
		# response = QMessageBox.question(self, "Are you sure?", "Are you sure you want to add tileset margins?")
		# if response == QMessageBox.StandardButton.Yes:
		# 	AddMargins()
		#	QMessageBox.information(self, "Success", "Finished Successfully")

	def context_menu(self, pos):
		context = QMenu(self)
		context.addAction(QAction("No Right-Click Actions available", self))
		context.exec(self.mapToGlobal(pos))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()