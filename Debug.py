import os
import json
import oead
from Modules.MM2Things import SMB1_Theme, SMB3_Theme, SMW_Theme, NSMBU_Theme, SM3DW_Theme, MyWorld_Theme

DEBUG_OUTPUT = False
DIRECTORY = os.path.dirname(__file__)+"/"+"Modules/ThemeDecompiler/"
if not os.path.exists(DIRECTORY+"BYML-Input/"):
	os.makedirs(DIRECTORY+"BYML-Input/")
if not os.path.exists(DIRECTORY+"MM2Theme-Output/"):
	os.makedirs(DIRECTORY+"MM2Theme-Output/")

def main():
	for fileName in os.listdir(DIRECTORY+"BYML-Input/"):
		if not fileName.endswith(".byml"): continue
		with open(DIRECTORY+"BYML-Input/"+fileName, "rb") as bymlFile:
			for theme_dict in oead.byml.from_binary(bymlFile.read()):
				Theme = None
				if (fileName[8:-5] == "MyWorld"): Theme = MyWorld_Theme.from_byml_dict(theme_dict)
				elif (fileName[0:2] == "M1"): Theme = SMB1_Theme.from_byml_dict(theme_dict)
				elif (fileName[0:2] == "M3"): Theme = SMB3_Theme.from_byml_dict(theme_dict)
				elif (fileName[0:2] == "MW"): Theme = SMW_Theme.from_byml_dict(theme_dict)
				elif (fileName[0:2] == "WU"): Theme = NSMBU_Theme.from_byml_dict(theme_dict)
				elif (fileName[0:2] == "3W"): Theme = SM3DW_Theme.from_byml_dict(theme_dict)
				else: raise Exception("BYML file does not match any recognised GameStyle.")
				
				if DEBUG_OUTPUT: Theme.print()
				with open(DIRECTORY+"MM2Theme-Output/"+Theme.Theme_Name+"."+Theme.Style.value+".MM2Theme", "wt") as jsonFile:
					json.dump(Theme.as_json_dict(), jsonFile)

if __name__ == "__main__":
	DEBUG_OUTPUT = True
	main()
