import oead
import json
import os

DEBUG_OUTPUT = False
DIRECTORY = os.path.dirname(__file__)+"/"
if not os.path.exists(DIRECTORY+"BYML-Input/"):
	os.makedirs(DIRECTORY+"BYML-Input/")
if not os.path.exists(DIRECTORY+"MM2Theme-Output/"):
	os.makedirs(DIRECTORY+"MM2Theme-Output/")

def bymlToJson(byml):
	byml = dict(byml)
	json = {
		"Tileset_Model": byml["FieldModel"],
		"Lighting": byml["Env_Model"],
		"Background_Model": byml["DVModel"],
		"Background_Lighting": byml["Env_DV"],
		"Vertical_Background_Lighting": byml["Env_DV_V"],
		"Vertical_Background_Anchor_Type": "Top" if (byml["DV_V_OffsetType"] == "上基準") else "Bottom",

		"CustomScroll_Inside": [
			float(byml["CSin_R"]),
			float(byml["CSin_G"]),
			float(byml["CSin_B"]),
			float(byml["CSin_A"])
		],
		"CustomScroll_Outside": [
			float(byml["CSout_R"]),
			float(byml["CSout_G"]),
			float(byml["CSout_B"]),
			float(byml["CSout_A"])
		],
		"Editor_Grid": [
			float(byml["Grid_R"]),
			float(byml["Grid_G"]),
			float(byml["Grid_B"]),
			float(byml["Grid_A"])
		]
	}
	
	if ("Shadow_Offset" in byml):
		json["Tileset_Model_Animation_Type"] = byml["FieldAnime"]
		json["Enemy_Variant"] = byml["Enemy"]
		json["Shadow_Color"] = [
			float(byml["Shadow_R"]),
			float(byml["Shadow_G"]),
			float(byml["Shadow_B"]),
			float(byml["Shadow_A"])
		]
		json["Shadow_Offset"] = float(byml["Shadow_Offset"])
	if ("DV_pos_x" in byml):
		json["Tileset_Model_Animation_Type"] = byml["FieldAnime"]
		json["Enemy_Variant"] = byml["Enemy"]
		json["Edge_Light_color"] = [
			float(byml["EdgeLightColor_R"]),
			float(byml["EdgeLightColor_G"]),
			float(byml["EdgeLightColor_B"])
		]
		json["Background_Position"] = [
			float(byml["DV_pos_x"]),
			float(byml["DV_pos_y"])
		]
		json["Vertical_Background_Position"] = [
			float(byml["DV_V_pos_x"]),
			float(byml["DV_V_pos_y"])
		]
		json["WIP_DV_CamMoveY"] = float(byml["DV_CamMoveY"])
		json["WIP_DV_ProjMoveY"] = float(byml["DV_ProjMoveY"])
		json["WIP_DV_ProjOffsetY"] = float(byml["DV_ProjOffsetY"])
		json["WIP_DV_V_CamMoveY"] = float(byml["DV_V_CamMoveY"])
		json["WIP_DV_V_ProjMoveY"] = float(byml["DV_V_ProjMoveY"])
		json["WIP_DV_V_ProjOffsetY"] = float(byml["DV_V_ProjOffsetY"])
		json["Play_Background_FOV"] = float(byml["DV_Play_Fovy"])
	if ("DV_ScalePivot" in byml):
		json["WIP_DV_CamMoveY"] = float(byml["DV_CamMoveY"])
		json["WIP_DV_ProjMoveY"] = float(byml["DV_ProjMoveY"])
		json["WIP_DV_ProjOffsetY"] = float(byml["DV_ProjOffsetY"])
		json["WIP_DV_V_CamMoveY"] = float(byml["DV_V_CamMoveY"])
		json["WIP_DV_V_ProjMoveY"] = float(byml["DV_V_ProjMoveY"])
		json["WIP_DV_V_ProjOffsetY"] = float(byml["DV_V_ProjOffsetY"])
		json["Editor_Background_FOV"] = float(byml["DV_Edit_Fovy"])
		json["Play_Background_FOV"] = float(byml["DV_Play_Fovy"])
		json["WIP_DV_ScalePivot"] = float(byml["DV_ScalePivot"])

	return json

def main():
	for fileName in os.listdir(DIRECTORY+"BYML-Input/"):
		if not fileName.endswith(".byml"): continue
		with open(DIRECTORY+"BYML-Input/"+fileName, "rb") as bymlFile:
			for theme in oead.byml.from_binary(bymlFile.read()):
				themeJson = bymlToJson(theme)
				if DEBUG_OUTPUT: print(themeJson)
				with open(DIRECTORY+"MM2Theme-Output/"+theme["FieldModel"][9:]+"."+fileName[:2]+".MM2Theme", "wt") as jsonFile:
					json.dump(themeJson, jsonFile)

if __name__ == "__main__":
	DEBUG_OUTPUT = True
	main()
