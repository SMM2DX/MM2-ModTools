import os
import sys
import json
import oead
from Modules.MM2Things import Theme, GameStyle, SMB1_Theme, SMB3_Theme, SMW_Theme, NSMBU_Theme, SM3DW_Theme, MyWorld_Theme
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon, QKeySequence, QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QToolBar, QMenu, QStatusBar, QMessageBox, QWidget,
	QTabWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QPushButton,
	QAbstractItemView, QListWidget, QListView, QListWidgetItem
)


DIRECTORY = f"{os.path.dirname(__file__)}/"
if not os.path.exists(f"{DIRECTORY}BYML-Input/"):
	os.makedirs(f"{DIRECTORY}BYML-Input/")
if not os.path.exists(f"{DIRECTORY}MM2Theme-Input/"):
	os.makedirs(f"{DIRECTORY}MM2Theme-Input/")

def CompileThemes(window):
	if not os.path.exists(f"{DIRECTORY}BYML-Output/"):
		os.makedirs(f"{DIRECTORY}BYML-Output/")
	
	for style in GameStyle:
		byml_array = []
		for i in range(window.themeLists[style].count()): # This feels super janky but it works !
			themes = window.themeLists[style].item(i).data(100)
			for theme in themes:
				if theme: byml_array.append(theme.as_byml_dict())
		# TODO: THIS FUCKING BLOWS HOLY SHIT ITS SO UGLY
		
		with open(f"{DIRECTORY}BYML-Output/{style.value[1]}.yaml", "wt") as file:
			file.write(oead.byml.to_text(byml_array)) # Write yaml for sanity checking
		with open(f"{DIRECTORY}BYML-Output/{style.value[1]}.byml", "wb") as file:
			file.write(oead.byml.to_binary(byml_array, False, 1))

def DecompileThemes(window): # Technically this could auto-load themes but that felt weird
	if not os.path.exists(f"{DIRECTORY}BYML-Input/"):
		os.makedirs(f"{DIRECTORY}BYML-Input/")
	if not os.path.exists(f"{DIRECTORY}MM2Theme-Output/"):
		os.makedirs(f"{DIRECTORY}MM2Theme-Output/")
	
	for fileName in os.listdir(f"{DIRECTORY}BYML-Input/"):
		if not fileName.upper().endswith(".BYML"): continue
		with open(f"{DIRECTORY}BYML-Input/{fileName}", "rb") as bymlFile:
			for theme_dict in oead.byml.from_binary(bymlFile.read()):
				theme: Theme = None
				if (GameStyle.SMB1.value[1] in fileName): theme = SMB1_Theme.from_byml_dict(theme_dict)
				elif (GameStyle.SMB3.value[1] in fileName): theme = SMB3_Theme.from_byml_dict(theme_dict)
				elif (GameStyle.SMW.value[1] in fileName): theme = SMW_Theme.from_byml_dict(theme_dict)
				elif (GameStyle.NSMBU.value[1] in fileName): theme = NSMBU_Theme.from_byml_dict(theme_dict)
				elif (GameStyle.SM3DW.value[1] in fileName): theme = SM3DW_Theme.from_byml_dict(theme_dict)
				elif (GameStyle.MyWorld.value[1] in fileName): theme = MyWorld_Theme.from_byml_dict(theme_dict)
				else:
					QMessageBox.warning(window, "Invalid File", f"Encountered file {fileName} with invalid Gamestyle, skipping")
					break
				
				if (not theme.Is_Night):
					with open(f"{DIRECTORY}MM2Theme-Output/{theme.Theme_Name}.{theme.Style.value[0]}.MM2Theme", "wt") as jsonFile:
						json.dump(theme.as_json_dict(), jsonFile)
				else:
					with open(f"{DIRECTORY}MM2Theme-Output/{theme.Theme_Name}.{theme.Style.value[0]}.Night.MM2Theme", "wt") as jsonFile:
						json.dump(theme.as_json_dict(), jsonFile)

def LoadThemes(window):
	if not os.path.exists(f"{DIRECTORY}MM2Theme-Input/"):
		os.makedirs(f"{DIRECTORY}MM2Theme-Input/")
	
	for fileName in os.listdir(f"{DIRECTORY}MM2Theme-Input/"):
		if not fileName.upper().endswith(".MM2THEME"): continue
		if fileName.upper().endswith(".NIGHT.MM2THEME"): continue
		with open(f"{DIRECTORY}MM2Theme-Input/{fileName}", "rb") as jsonFile:
			theme: Theme = None
			theme_night: Theme = None
			if (fileName.upper().endswith(".M1.MM2THEME")):
				theme = SMB1_Theme.from_json_dict(json.load(jsonFile))
				if (os.path.exists(f"{DIRECTORY}MM2Theme-Input/{fileName[:-8]}Night.MM2Theme")):
					with open(f"{DIRECTORY}MM2Theme-Input/{fileName[:-8]}Night.MM2Theme", "rb") as nightFile:
						theme_night = SMB1_Theme.from_json_dict(json.load(nightFile))
			elif (fileName.upper().endswith(".M3.MM2THEME")):
				theme = SMB3_Theme.from_json_dict(json.load(jsonFile))
				if (os.path.exists(f"{DIRECTORY}MM2Theme-Input/{fileName[:-8]}Night.MM2Theme")):
					with open(f"{DIRECTORY}MM2Theme-Input/{fileName[:-8]}Night.MM2Theme", "rb") as nightFile:
						theme_night = SMB3_Theme.from_json_dict(json.load(nightFile))
			elif (fileName.upper().endswith(".MW.MM2THEME")):
				theme = SMW_Theme.from_json_dict(json.load(jsonFile))
				if (os.path.exists(f"{DIRECTORY}MM2Theme-Input/{fileName[:-8]}Night.MM2Theme")):
					with open(f"{DIRECTORY}MM2Theme-Input/{fileName[:-8]}Night.MM2Theme", "rb") as nightFile:
						theme_night = SMW_Theme.from_json_dict(json.load(nightFile))
			elif (fileName.upper().endswith(".WU.MM2THEME")):
				theme = NSMBU_Theme.from_json_dict(json.load(jsonFile))
				if (os.path.exists(f"{DIRECTORY}MM2Theme-Input/{fileName[:-8]}Night.MM2Theme")):
					with open(f"{DIRECTORY}MM2Theme-Input/{fileName[:-8]}Night.MM2Theme", "rb") as nightFile:
						theme_night = NSMBU_Theme.from_json_dict(json.load(nightFile))
			elif (fileName.upper().endswith(".3W.MM2THEME")):
				theme = SM3DW_Theme.from_json_dict(json.load(jsonFile))
				if (os.path.exists(f"{DIRECTORY}MM2Theme-Input/{fileName[:-8]}Night.MM2Theme")):
					with open(f"{DIRECTORY}MM2Theme-Input/{fileName[:-8]}Night.MM2Theme", "rb") as nightFile:
						theme_night = SM3DW_Theme.from_json_dict(json.load(nightFile))
			elif (fileName.upper().endswith(".MYWORLD.MM2THEME")):
				theme = MyWorld_Theme.from_json_dict(json.load(jsonFile))
				if (os.path.exists(f"{DIRECTORY}MM2Theme-Input/{fileName[:-8]}Night.MM2Theme")):
					with open(f"{DIRECTORY}MM2Theme-Input/{fileName[:-8]}Night.MM2Theme", "rb") as nightFile:
						theme_night = MyWorld_Theme.from_json_dict(json.load(nightFile))
			else:
				QMessageBox.warning(window, "Invalid File", f"Encountered file {fileName} with invalid Gamestyle, skipping")
				continue

			listItem = QListWidgetItem()
			if (theme_night):
				listItem.setText(f"{theme.Theme_Name} + Night")
			else:
				listItem.setText(theme.Theme_Name)
			listItem.setData(100, (theme, theme_night)) # No idea if this is how you're supposed to do it, but its working so.
			# TODO: THIS FUCKING BLOWS HOLY SHIT ITS SO UGLY
			window.themeLists[theme.Style].addItem(listItem)

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
				tabLabel.setText("Theme Decompiler")
				tabLayout.addWidget(tabLabel)
				tabButton = QPushButton()
				tabButton.setText("Run")
				tabButton.setStatusTip("Run Theme Decompiler")
				tabButton.clicked.connect(self.decompile_button_clicked)
				tabLayout.addWidget(tabButton)
				tab.setLayout(tabLayout)
				tabsWidget.addTab(tab, "Decompile Themes")
			if True:
				tab = QWidget()
				tabLayout = QVBoxLayout()
				tabLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
				tabLabel = QLabel()
				tabLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
				tabLabel.setText("Theme Loader")
				tabLayout.addWidget(tabLabel)
				tabButton = QPushButton()
				tabButton.setText("Run")
				tabButton.setStatusTip("Run Theme Loader")
				tabButton.clicked.connect(self.load_button_clicked)
				tabLayout.addWidget(tabButton)
				tab.setLayout(tabLayout)
				tabsWidget.addTab(tab, "Load Themes")
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
				tabsWidget.addTab(tab, "Compile Themes")
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
		if True:
			area1 = QWidget()
			area1Layout = QVBoxLayout()
			if True:
				tabsWidget = QTabWidget()
				tabsWidget.setTabPosition(QTabWidget.TabPosition.East)
				tabsWidget.setDocumentMode(True)
				tabsWidget.setMovable(True)
				self.themeLists: dict[GameStyle, QListWidget] = {} # TODO: This probably needs to be far more hardcoded and use a subclassed QListWidgetItem class
				for style in GameStyle:
					self.themeLists[style] = QListWidget()
					self.themeLists[style].setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
					self.themeLists[style].setFlow(QListView.Flow.TopToBottom)
					self.themeLists[style].setMovement(QListView.Movement.Snap)
					tabsWidget.addTab(self.themeLists[style], f"{style.name}")
				area1Layout.addWidget(tabsWidget)
			if True:
				Widget = QWidget()
				area1Layout.addWidget(Widget)
			area1.setLayout(area1Layout)
			mainLayout.addWidget(area1)

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
	def decompile_button_clicked(self):
		response = QMessageBox.question(self, "Are you sure?", "Are you sure you want to decompile .byml files to .MM2Theme?")
		if response == QMessageBox.StandardButton.Yes:
			DecompileThemes(self)
			QMessageBox.information(self, "Success", "Finished Successfully")
	def load_button_clicked(self):
		response = QMessageBox.question(self, "Are you sure?", "Are you sure you want to load all .MM2Theme files?")
		if response == QMessageBox.StandardButton.Yes:
			LoadThemes(self)
			QMessageBox.information(self, "Success", "Finished Successfully")
	def compile_button_clicked(self):
		response = QMessageBox.question(self, "Are you sure?", "Are you sure you want to compile loaded themes to .byml?")
		if response == QMessageBox.StandardButton.Yes:
			CompileThemes(self)
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