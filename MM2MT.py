import os
import sys
import json
import oead
from Modules.MM2Things import Theme, GameStyle, SMB1_Theme, SMB3_Theme, SMW_Theme, NSMBU_Theme, SM3DW_Theme, MyWorld_Theme
from Modules.QtThings import QActionButton
from PyQt6.QtCore import Qt, QDir, QSettings, QByteArray, QSize
from PyQt6.QtGui import QAction, QIcon, QKeySequence, QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QToolBar, QMenu, QStatusBar, QMessageBox, QWidget,
	QTabWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QFileDialog, 
	QAbstractItemView, QListWidget, QListView, QListWidgetItem
)
from zstd import ZSTD_uncompress

app = QApplication(sys.argv)
app.setOrganizationName("SMM2DX")
app.setApplicationName("MM2MT")
app.setApplicationDisplayName

settings = QSettings()
CLEANROMFSDIR: QDir = QDir(settings.value("RomFSDir", QDir.rootPath()))
QDir.current().mkpath("Input/BYML")
QDir.current().mkpath("Input/MM2Theme")
QDir.current().mkpath("Output/BYML")
QDir.current().mkpath("Output/MM2Theme")
QDir.current().mkpath("Output/RomFS")

def ThemesLoad(window):
	QDir.current().mkpath("Input/MM2Theme")
	inputDir: QDir = QDir().current()
	inputDir.cd("Input/MM2Theme")
	
	for fileName in os.listdir(inputDir.path()):
		if not fileName.upper().endswith(".MM2THEME"): continue
		with open(inputDir.filePath(f"{fileName}"), "rb") as jsonFile:
			theme: Theme = None
			if   (     ".M1." in fileName.upper()): theme =    SMB1_Theme.from_json_dict(json.load(jsonFile))
			elif (     ".M3." in fileName.upper()): theme =    SMB3_Theme.from_json_dict(json.load(jsonFile))
			elif (     ".MW." in fileName.upper()): theme =     SMW_Theme.from_json_dict(json.load(jsonFile))
			elif (     ".WU." in fileName.upper()): theme =   NSMBU_Theme.from_json_dict(json.load(jsonFile))
			elif (     ".3W." in fileName.upper()): theme =   SM3DW_Theme.from_json_dict(json.load(jsonFile))
			elif (".MYWORLD." in fileName.upper()): theme = MyWorld_Theme.from_json_dict(json.load(jsonFile))
			else:
				QMessageBox.warning(window, "Invalid File", f"Encountered file {fileName} with invalid Gamestyle, skipping")
				continue

			listItem = QListWidgetItem()
			if (theme.Is_Night):
				listItem.setText(f"{theme.Theme_Name} (Night)")
			else:
				listItem.setText(theme.Theme_Name)
			# TODO: THIS FUCKING BLOWS HOLY SHIT ITS SO UGLY
			listItem.setData(100, (theme, None)) # No idea if this is how you're supposed to do it, but its working so.
			window.themeLists[theme.Style].addItem(listItem)

def ThemesSave(window):
	QDir.current().mkpath("Output/MM2Theme")
	outputDir: QDir = QDir().current()
	outputDir.cd("Output/MM2Theme")

	for style in GameStyle:
		for i in range(window.themeLists[style].count()): # WARN: This feels super janky but it works !
			themes = window.themeLists[style].item(i).data(100)
			for theme in themes:
				if not theme: continue
				if not theme.Is_Night:
					with open(outputDir.filePath(f"{theme.Theme_Name}.{theme.Style.value[0]}.MM2Theme"), "wt") as jsonFile:
						json.dump(theme.as_json_dict(), jsonFile)
				else:
					with open(outputDir.filePath(f"{theme.Theme_Name}.{theme.Style.value[0]}.Night.MM2Theme"), "wt") as jsonFile:
						json.dump(theme.as_json_dict(), jsonFile)

def ThemesDecompile(window):
	QDir.current().mkpath("Input/BYML")
	inputDir: QDir = QDir().current()
	inputDir.cd("Input/BYML")
	
	for fileName in os.listdir(inputDir.path()):
		if not fileName.upper().endswith(".BYML"): continue
		with open(inputDir.filePath(f"{fileName}"), "rb") as bymlFile:
			for theme_dict in oead.byml.from_binary(bymlFile.read()):
				theme: Theme = None
				if   (   GameStyle.SMB1.value[1] in fileName): theme =    SMB1_Theme.from_byml_dict(theme_dict)
				elif (   GameStyle.SMB3.value[1] in fileName): theme =    SMB3_Theme.from_byml_dict(theme_dict)
				elif (    GameStyle.SMW.value[1] in fileName): theme =     SMW_Theme.from_byml_dict(theme_dict)
				elif (  GameStyle.NSMBU.value[1] in fileName): theme =   NSMBU_Theme.from_byml_dict(theme_dict)
				elif (  GameStyle.SM3DW.value[1] in fileName): theme =   SM3DW_Theme.from_byml_dict(theme_dict)
				elif (GameStyle.MyWorld.value[1] in fileName): theme = MyWorld_Theme.from_byml_dict(theme_dict)
				else:
					QMessageBox.warning(window, "Invalid File", f"Encountered file {fileName} with invalid Gamestyle, skipping")
					break
				
				listItem = QListWidgetItem()
				if (theme.Is_Night):
					listItem.setText(f"{theme.Theme_Name} (Night)")
				else:
					listItem.setText(theme.Theme_Name)
				# TODO: THIS FUCKING BLOWS HOLY SHIT ITS SO UGLY
				listItem.setData(100, (theme, None)) # No idea if this is how you're supposed to do it, but its working so.
				window.themeLists[theme.Style].addItem(listItem)

def ThemesCompile(window):
	QDir.current().mkpath("Output/BYML")
	outputDir: QDir = QDir().current()
	outputDir.cd("Output/BYML")
	
	for style in GameStyle:
		byml_array = []
		for i in range(window.themeLists[style].count()): # This feels super janky but it works !
			themes = window.themeLists[style].item(i).data(100)
			for theme in themes: # TODO: THIS FUCKING BLOWS HOLY SHIT ITS SO UGLY
				if not theme: continue
				byml_array.append(theme.as_byml_dict())
		
		with open(outputDir.filePath(f"{style.value[1]}.yaml"), "wt") as file:
			file.write(oead.byml.to_text(byml_array)) # Write yaml for sanity checking
		with open(outputDir.filePath(f"{style.value[1]}.byml"), "wb") as file:
			file.write(oead.byml.to_binary(byml_array, False, 1))

def RomFSDecompile(window):
	workingDir: QDir = QDir(CLEANROMFSDIR.path())
	if not workingDir.cd("Model"): raise FileNotFoundError()
	if not workingDir.exists("M1_DV_plain.Nin_NX_NVN.zs"): raise FileNotFoundError()
	with open(workingDir.filePath("M1_DV_plain.Nin_NX_NVN.zs"), "rb") as zsSarcFile:
		for file in oead.Sarc(ZSTD_uncompress(zsSarcFile.read())).get_files():
			print(file.name+": "+str(file.data))
			print(type(file.data))

class MainWindow(QMainWindow):
	# TODO: These could be lambdas
	def placeholder_button_clicked(self):
		pass
	def theme_load_button_clicked(self):
		response = QMessageBox.question(self, "Are you sure?", "Are you sure you want to load all .MM2Theme files?")
		if response == QMessageBox.StandardButton.Yes:
			ThemesLoad(self)
			QMessageBox.information(self, "Success", "Finished Successfully")
	def theme_save_button_clicked(self):
		response = QMessageBox.question(self, "Are you sure?", "Are you sure you want to save all loaded themes to .MM2Theme files?")
		if response == QMessageBox.StandardButton.Yes:
			ThemesSave(self)
			QMessageBox.information(self, "Success", "Finished Successfully")
	def theme_decompile_button_clicked(self):
		response = QMessageBox.question(self, "Are you sure?", "Are you sure you want to decompile and load all .BYML files?")
		if response == QMessageBox.StandardButton.Yes:
			ThemesDecompile(self)
			QMessageBox.information(self, "Success", "Finished Successfully")
	def theme_compile_button_clicked(self):
		response = QMessageBox.question(self, "Are you sure?", "Are you sure you want to compile all loaded themes to .BYML files?")
		if response == QMessageBox.StandardButton.Yes:
			ThemesCompile(self)
			QMessageBox.information(self, "Success", "Finished Successfully")
	def romfs_select_button_clicked(self):
		global CLEANROMFSDIR
		CLEANROMFSDIR = QDir(QFileDialog.getExistingDirectory(
			self,
			"Select RomFS directory",
			CLEANROMFSDIR.path(),
			QFileDialog.Option.ShowDirsOnly
		))
		self.romFSDirLabel.setText("<b>RomFS dir:</b> <i>\""+CLEANROMFSDIR.path()+"\"</i>")
	def romfs_decompile_button_clicked(self):
		response = QMessageBox.question(self, "This is Work-in-progress.", "Are you sure you meant to click this button?")
		if response == QMessageBox.StandardButton.Yes:
			RomFSDecompile(self)
			QMessageBox.information(self, "Success", "Finished Successfully")

	def __init__(self):
		super().__init__()
		self.setWindowIcon(QIcon("Assets/SMM2DX.png"))
		self.setWindowTitle("MM2MT - Mario Maker 2 Mod Tools")
		self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
		self.customContextMenuRequested.connect(self.context_menu)
		self.setStatusBar(QStatusBar(self))

		# region Actions
		placeholder_1_button_action = QAction(QIcon("Assets/fugue-icons/icons/cross-circle.png"), "&Placeholder", self)
		placeholder_1_button_action.setStatusTip("This does nothing")
		placeholder_1_button_action.triggered.connect(self.placeholder_button_clicked)
		#placeholder_1_button_action.setShortcut(QKeySequence.StandardKey.Print)
		placeholder_2_button_action = QAction(QIcon("Assets/fugue-icons/icons/cross-circle.png"), "&Placeholder", self)
		placeholder_2_button_action.setStatusTip("This does nothing")
		placeholder_2_button_action.triggered.connect(self.placeholder_button_clicked)
		placeholder_3_button_action = QAction(QIcon("Assets/fugue-icons/icons/cross-circle.png"), "&Placeholder", self)
		placeholder_3_button_action.setStatusTip("This does nothing")
		placeholder_3_button_action.triggered.connect(self.placeholder_button_clicked)

		theme_load_button_action = QAction(QIcon("Assets/fugue-icons/icons/document--plus.png"), "Load MM2Themes", self)
		theme_load_button_action.setStatusTip("Load MM2Theme files")
		theme_load_button_action.triggered.connect(self.theme_load_button_clicked)

		theme_save_button_action = QAction(QIcon("Assets/fugue-icons/icons/disk.png"), "Save MM2Themes", self)
		theme_save_button_action.setStatusTip("Save MM2Theme files")
		theme_save_button_action.triggered.connect(self.theme_save_button_clicked)

		theme_decompile_button_action = QAction(QIcon("Assets/fugue-icons/icons/document-import.png"), "Decompile BYMLs", self)
		theme_decompile_button_action.setStatusTip("Decompile and load BYML files")
		theme_decompile_button_action.triggered.connect(self.theme_decompile_button_clicked)

		theme_compile_button_action = QAction(QIcon("Assets/fugue-icons/icons/document-export.png"), "Compile BYML/YAMLs", self)
		theme_compile_button_action.setStatusTip("Compile loaded themes to BYML/YAML files")
		theme_compile_button_action.triggered.connect(self.theme_compile_button_clicked)

		romfs_select_button_action = QAction(QIcon("Assets/fugue-icons/icons/folder-open.png"), "Select RomFS dir", self)
		romfs_select_button_action.setStatusTip("Select a clean, exported MM2 RomFS folder")
		romfs_select_button_action.triggered.connect(self.romfs_select_button_clicked)

		romfs_decompile_button_action = QAction(QIcon("Assets/fugue-icons/icons/folder-import.png"), "\"Decompile\" RomFS", self)
		romfs_decompile_button_action.setStatusTip("\"Decompile\" your RomFS to human-readable formats")
		romfs_decompile_button_action.triggered.connect(self.romfs_decompile_button_clicked)
		# endregion

		mainWidget = QWidget()
		mainLayout = QHBoxLayout()
		mainLayout.setContentsMargins(0,0,0,0) # Spacing and stuff for visuals
		mainLayout.setSpacing(0) # Spacing and stuff for visuals
		mainWidget.setLayout(mainLayout)
		self.setCentralWidget(mainWidget)
		self.romFSDirLabel = QLabel()
		self.romFSDirLabel.setText("<b>RomFS dir:</b> <i>\""+CLEANROMFSDIR.path()+"\"</i>")
		if True:
			area = QWidget()
			areaLayout = QVBoxLayout()
			area.setLayout(areaLayout)
			mainLayout.addWidget(area)
			if True:
				tabsWidget = QTabWidget()
				tabsWidget.setTabPosition(QTabWidget.TabPosition.West)
				tabsWidget.setDocumentMode(True)
				tabsWidget.setMovable(True)
				self.themeLists: dict[GameStyle, QListWidget] = {} # TODO: This probably needs to be far more hardcoded and use a subclassed QListWidgetItem class
				for style in GameStyle:
					self.themeLists[style] = QListWidget()
					self.themeLists[style].setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
					self.themeLists[style].setFlow(QListView.Flow.TopToBottom)
					self.themeLists[style].setMovement(QListView.Movement.Snap)
					tabsWidget.addTab(self.themeLists[style], f"{style.name}")
				areaLayout.addWidget(tabsWidget)
			if True:
				buttonSection = QWidget()
				buttonSectionLayout = QHBoxLayout()
				buttonSectionLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
				buttonSection.setLayout(buttonSectionLayout)
				areaLayout.addWidget(buttonSection)
				if True:
					button = QActionButton(theme_load_button_action)
					buttonSectionLayout.addWidget(button)
				if True:
					button = QActionButton(theme_save_button_action)
					buttonSectionLayout.addWidget(button)
				if True:
					button = QActionButton(theme_decompile_button_action)
					buttonSectionLayout.addWidget(button)
				if True:
					button = QActionButton(theme_compile_button_action)
					buttonSectionLayout.addWidget(button)
		if True:
			area = QWidget()
			areaLayout = QVBoxLayout()
			areaLayout.setAlignment(Qt.AlignmentFlag.AlignBottom)
			area.setLayout(areaLayout)
			mainLayout.addWidget(area)
			if True:
				buttonSection = QWidget()
				buttonSectionLayout = QHBoxLayout()
				buttonSectionLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
				buttonSection.setLayout(buttonSectionLayout)
				areaLayout.addWidget(buttonSection)
				if True:
					button = QActionButton(romfs_select_button_action)
					buttonSectionLayout.addWidget(button)
				if True:
					button = QActionButton(romfs_decompile_button_action)
					buttonSectionLayout.addWidget(button)
			if True:
				labelSection = QWidget()
				labelSectionLayout = QHBoxLayout()
				labelSectionLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
				labelSection.setLayout(labelSectionLayout)
				areaLayout.addWidget(labelSection)
				if True:
					labelSectionLayout.addWidget(self.romFSDirLabel)

		toolbar = QToolBar("Toolbar")
		toolbar.setMovable(False)
		toolbar.setIconSize(QSize(16, 16))
		toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
		self.addToolBar(toolbar)
		menu = self.menuBar()
		if True:
			# Toolbar
			toolbar.addAction(placeholder_1_button_action)
			toolbar.addAction(placeholder_2_button_action)
			toolbar.addSeparator()
			toolbar.addAction(placeholder_3_button_action)
			
			# Menu Bar
			file_menu = menu.addMenu("&File")
			file_menu.addAction(placeholder_1_button_action)
			file_menu.addAction(placeholder_2_button_action)
			file_menu.addSeparator()
			file_menu.addAction(placeholder_3_button_action)
			#file_submenu = file_menu.addMenu("&Submenu")

			settings_menu = menu.addMenu("&Settings")
			settings_menu.addAction(romfs_select_button_action)
		
		oldGeometry: QByteArray = settings.value("MainWindow/geometry")
		if oldGeometry: self.restoreGeometry(oldGeometry)
	def closeEvent(self, event):
		settings.setValue("MainWindow/geometry", self.saveGeometry())
		settings.setValue("RomFSDir", CLEANROMFSDIR.path())
	def context_menu(self, pos):
		context = QMenu(self)
		context.addAction(QAction("No Right-Click Actions available", self))
		context.exec(self.mapToGlobal(pos))

window = MainWindow()
window.show()

app.exec()