import os
import sys
import json
import oead
from Modules.MM2Things import Theme, GameStyle, SMB1_Theme, SMB3_Theme, SMW_Theme, NSMBU_Theme, SM3DW_Theme, MyWorld_Theme
from PyQt6.QtCore import Qt, QDir, QSettings, QByteArray, QSize
from PyQt6.QtGui import QAction, QIcon, QKeySequence, QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QToolBar, QMenu, QStatusBar, QMessageBox, QWidget,
	QTabWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QPushButton, QFileDialog, 
	QAbstractItemView, QListWidget, QListView, QListWidgetItem
)

app = QApplication(sys.argv)
app.setOrganizationName("SMM2DX")
app.setApplicationName("MM2MT")
app.setApplicationDisplayName

settings = QSettings()
CLEANROMFSDIR: QDir = QDir(settings.value("romfsDir", QDir.rootPath()))
if not QDir.current().exists("BYML-Input"): QDir.current().mkdir("BYML-Input")
if not QDir.current().exists("BYML-Output"): QDir.current().mkdir("BYML-Output")
if not QDir.current().exists("MM2Theme-Input"): QDir.current().mkdir("MM2Theme-Input")
if not QDir.current().exists("MM2Theme-Output"): QDir.current().mkdir("MM2Theme-Output")

def CompileThemes(window):
	outputDir: QDir = QDir().current()
	if not outputDir.exists("BYML-Output"): outputDir.mkdir("BYML-Output")
	outputDir.cd("BYML-Output")
	
	for style in GameStyle:
		byml_array = []
		for i in range(window.themeLists[style].count()): # This feels super janky but it works !
			themes = window.themeLists[style].item(i).data(100)
			for theme in themes:
				if theme: byml_array.append(theme.as_byml_dict())
		# TODO: THIS FUCKING BLOWS HOLY SHIT ITS SO UGLY
		
		with open(outputDir.filePath(f"{style.value[1]}.yaml"), "wt") as file:
			file.write(oead.byml.to_text(byml_array)) # Write yaml for sanity checking
		with open(outputDir.filePath(f"{style.value[1]}.byml"), "wb") as file:
			file.write(oead.byml.to_binary(byml_array, False, 1))

def DecompileThemes(window): # Technically this could auto-load themes but that felt weird
	inputDir: QDir = QDir().current()
	if not inputDir.exists("BYML-Input"): inputDir.mkdir("BYML-Input")
	inputDir.cd("BYML-Input")
	outputDir: QDir = QDir().current()
	if not outputDir.exists("MM2Theme-Output"): outputDir.mkdir("MM2Theme-Output")
	outputDir.cd("MM2Theme-Output")
	
	for fileName in os.listdir(inputDir.path()):
		if not fileName.upper().endswith(".BYML"): continue
		with open(inputDir.filePath(f"{fileName}"), "rb") as bymlFile:
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
					with open(outputDir.filePath(f"{theme.Theme_Name}.{theme.Style.value[0]}.MM2Theme"), "wt") as jsonFile:
						json.dump(theme.as_json_dict(), jsonFile)
				else:
					with open(outputDir.filePath(f"{theme.Theme_Name}.{theme.Style.value[0]}.Night.MM2Theme"), "wt") as jsonFile:
						json.dump(theme.as_json_dict(), jsonFile)

def LoadThemes(window):
	inputDir: QDir = QDir().current()
	if not inputDir.exists("MM2Theme-Input"): inputDir.mkdir("MM2Theme-Input")
	inputDir.cd("MM2Theme-Input")
	
	for fileName in os.listdir(inputDir.path()):
		if not fileName.upper().endswith(".MM2THEME"): continue
		if fileName.upper().endswith(".NIGHT.MM2THEME"): continue
		with open(inputDir.filePath(f"{fileName}"), "rb") as jsonFile:
			theme: Theme = None
			theme_night: Theme = None
			if (fileName.upper().endswith(".M1.MM2THEME")):
				theme = SMB1_Theme.from_json_dict(json.load(jsonFile))
				if (os.path.exists(inputDir.filePath(f"{fileName[:-8]}Night.MM2Theme"))):
					with open(inputDir.filePath(f"{fileName[:-8]}Night.MM2Theme"), "rb") as nightFile:
						theme_night = SMB1_Theme.from_json_dict(json.load(nightFile))
			elif (fileName.upper().endswith(".M3.MM2THEME")):
				theme = SMB3_Theme.from_json_dict(json.load(jsonFile))
				if (os.path.exists(inputDir.filePath(f"{fileName[:-8]}Night.MM2Theme"))):
					with open(inputDir.filePath(f"{fileName[:-8]}Night.MM2Theme"), "rb") as nightFile:
						theme_night = SMB3_Theme.from_json_dict(json.load(nightFile))
			elif (fileName.upper().endswith(".MW.MM2THEME")):
				theme = SMW_Theme.from_json_dict(json.load(jsonFile))
				if (os.path.exists(inputDir.filePath(f"{fileName[:-8]}Night.MM2Theme"))):
					with open(inputDir.filePath(f"{fileName[:-8]}Night.MM2Theme"), "rb") as nightFile:
						theme_night = SMW_Theme.from_json_dict(json.load(nightFile))
			elif (fileName.upper().endswith(".WU.MM2THEME")):
				theme = NSMBU_Theme.from_json_dict(json.load(jsonFile))
				if (os.path.exists(inputDir.filePath(f"{fileName[:-8]}Night.MM2Theme"))):
					with open(inputDir.filePath(f"{fileName[:-8]}Night.MM2Theme"), "rb") as nightFile:
						theme_night = NSMBU_Theme.from_json_dict(json.load(nightFile))
			elif (fileName.upper().endswith(".3W.MM2THEME")):
				theme = SM3DW_Theme.from_json_dict(json.load(jsonFile))
				if (os.path.exists(inputDir.filePath(f"{fileName[:-8]}Night.MM2Theme"))):
					with open(inputDir.filePath(f"{fileName[:-8]}Night.MM2Theme"), "rb") as nightFile:
						theme_night = SM3DW_Theme.from_json_dict(json.load(nightFile))
			elif (fileName.upper().endswith(".MYWORLD.MM2THEME")):
				theme = MyWorld_Theme.from_json_dict(json.load(jsonFile))
				if (os.path.exists(inputDir.filePath(f"{fileName[:-8]}Night.MM2Theme"))):
					with open(inputDir.filePath(f"{fileName[:-8]}Night.MM2Theme"), "rb") as nightFile:
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
	def placeholder_button_clicked(self):
		pass
	def theme_decompile_button_clicked(self):
		response = QMessageBox.question(self, "Are you sure?", "Are you sure you want to decompile .byml files to .MM2Theme?")
		if response == QMessageBox.StandardButton.Yes:
			DecompileThemes(self)
			QMessageBox.information(self, "Success", "Finished Successfully")
	def theme_load_button_clicked(self):
		response = QMessageBox.question(self, "Are you sure?", "Are you sure you want to load all .MM2Theme files?")
		if response == QMessageBox.StandardButton.Yes:
			LoadThemes(self)
			QMessageBox.information(self, "Success", "Finished Successfully")
	def theme_compile_button_clicked(self):
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
	def romfs_button_clicked(self):
		global CLEANROMFSDIR
		CLEANROMFSDIR = QDir(QFileDialog.getExistingDirectory(
			self,
			"Select romfs directory",
			CLEANROMFSDIR.path(),
			QFileDialog.Option.ShowDirsOnly
		))
		self.romfsDirLabel.setText("<b>romfs dir:</b> <i>\""+CLEANROMFSDIR.path()+"\"</i>")

	def __init__(self):
		super().__init__()

		self.setWindowTitle("MM2MT - Mario Maker 2 Mod Tools")
		self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
		self.customContextMenuRequested.connect(self.context_menu)
		self.setStatusBar(QStatusBar(self))

		mainWidget = QWidget()
		mainLayout = QHBoxLayout()
		mainLayout.setContentsMargins(0,0,0,0) # Spacing and stuff for visuals
		mainLayout.setSpacing(0) # Spacing and stuff for visuals
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
				tabButton.clicked.connect(self.theme_decompile_button_clicked)
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
				tabButton.clicked.connect(self.theme_load_button_clicked)
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
				tabButton.clicked.connect(self.theme_compile_button_clicked)
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
			romfs_button_action = QAction(QIcon("Assets/fugue-icons/icons/folder-open.png"), "Select romfs dir", self)
			romfs_button_action.setStatusTip("Select a clean, exported MM2 romfs folder")
			romfs_button_action.triggered.connect(self.romfs_button_clicked)

			placeholder_button_action = QAction(QIcon("Assets/fugue-icons/icons/cross-circle.png"), "&Placeholder", self)
			placeholder_button_action.setStatusTip("This does nothing")
			placeholder_button_action.triggered.connect(self.placeholder_button_clicked)
			#placeholder_button_action.setShortcut(QKeySequence.StandardKey.Print)

			# Toolbar
			self.romfsDirLabel = QLabel()
			self.romfsDirLabel.setText("<b>romfs dir:</b> <i>\""+CLEANROMFSDIR.path()+"\"</i>")
			toolbar.addWidget(self.romfsDirLabel)
			toolbar.addAction(romfs_button_action)
			#toolbar.addSeparator()
			
			# Menu Bar
			file_menu = menu.addMenu("&File")
			file_menu.addAction(placeholder_button_action)
			#file_menu.addSeparator()
			#file_submenu = file_menu.addMenu("&Submenu")

			settings_menu = menu.addMenu("&Settings")
			settings_menu.addAction(romfs_button_action)
		
		oldGeometry: QByteArray = settings.value("MainWindow/geometry")
		if oldGeometry: self.restoreGeometry(oldGeometry)
	def closeEvent(self, event):
		settings.setValue("MainWindow/geometry", self.saveGeometry())
		settings.setValue("romfsDir", CLEANROMFSDIR.path())
	def context_menu(self, pos):
		context = QMenu(self)
		context.addAction(QAction("No Right-Click Actions available", self))
		context.exec(self.mapToGlobal(pos))

window = MainWindow()
window.show()

app.exec()