import oead
import json
import os

class MM2Theme():
	Tileset_Model: str
	Lighting: str
	Background_Model: str
	Background_Lighting: str
	Vertical_Background_Lighting: str
	Vertical_Background_Anchor_Type: str
	CustomScroll_Inside: list[float]
	CustomScroll_Outside: list[float]
	Editor_Grid: list[float]

	def __init__(self, info):
		self.Tileset_Model						= info["Tileset_Model"]
		self.Lighting							= info["Lighting"]
		self.Background_Model					= info["Background_Model"]
		self.Background_Lighting				= info["Background_Lighting"]
		self.Vertical_Background_Lighting		= info["Vertical_Background_Lighting"]
		self.Vertical_Background_Anchor_Type	= info["Vertical_Background_Anchor_Type"]
		self.CustomScroll_Inside				= [info["CustomScroll_Inside"][0], info["CustomScroll_Inside"][1], info["CustomScroll_Inside"][2], info["CustomScroll_Inside"][3]]
		self.CustomScroll_Outside				= [info["CustomScroll_Outside"][0], info["CustomScroll_Outside"][1], info["CustomScroll_Outside"][2], info["CustomScroll_Outside"][3]]
		self.Editor_Grid						= [info["Editor_Grid"][0], info["Editor_Grid"][1], info["Editor_Grid"][2], info["Editor_Grid"][3]]
	def print(self):
		pass
	def as_byml_dict(self):
		pass

class MM2Theme_M1(MM2Theme):
	Tileset_Model_Animation_Type: str
	Enemy_Variant: str
	Shadow_Color: list[float]
	Shadow_Offset: float

	def __init__(self, info):
		super().__init__(info)
		self.Tileset_Model_Animation_Type		= info["Tileset_Model_Animation_Type"]
		self.Enemy_Variant						= info["Enemy_Variant"]
		self.Shadow_Color						= [info["Shadow_Color"][0], info["Shadow_Color"][1], info["Shadow_Color"][2], info["Shadow_Color"][3]]
		self.Shadow_Offset						= info["Shadow_Offset"]
	def print(self):
		print("Tileset_Model:				"+str(self.Tileset_Model)+
			"\nTileset_Model_Animation_Type:		"+str(self.Tileset_Model_Animation_Type)+
			"\nLighting:				"+str(self.Lighting)+
			"\nEnemy_Variant:				"+str(self.Enemy_Variant)+
			"\nBackground_Model:			"+str(self.Background_Model)+
			"\nBackground_Lighting:			"+str(self.Background_Lighting)+
			"\nVertical_Background_Lighting:		"+str(self.Vertical_Background_Lighting)+
			"\nVertical_Background_Anchor_Type:	"+str(self.Vertical_Background_Anchor_Type)+
			"\nCustomScroll_Inside:			"+str(self.CustomScroll_Inside)+
			"\nCustomScroll_Outside:			"+str(self.CustomScroll_Outside)+
			"\nEditor_Grid:				"+str(self.Editor_Grid)+
			"\nShadow_Color:				"+str(self.Shadow_Color)+
			"\nShadow_Offset:				"+str(self.Shadow_Offset)+"\n")
	def as_byml_dict(self):
		return {
			"FieldModel": self.Tileset_Model,
			"FieldAnime": self.Tileset_Model_Animation_Type,
			"Env_Model": self.Lighting,
			"Enemy": self.Enemy_Variant,
			"DVModel": self.Background_Model,
			"Env_DV": self.Background_Lighting,
			"Env_DV_V": self.Vertical_Background_Lighting,
			"DV_V_OffsetType": "上基準" if (self.Vertical_Background_Anchor_Type == "Top") else "下基準", # Default to "Lower Benchmark"
			"CSin_R": oead.F32(self.CustomScroll_Inside[0]),
			"CSin_G": oead.F32(self.CustomScroll_Inside[1]),
			"CSin_B": oead.F32(self.CustomScroll_Inside[2]),
			"CSin_A": oead.F32(self.CustomScroll_Inside[3]),
			"CSout_R": oead.F32(self.CustomScroll_Outside[0]),
			"CSout_G": oead.F32(self.CustomScroll_Outside[1]),
			"CSout_B": oead.F32(self.CustomScroll_Outside[2]),
			"CSout_A": oead.F32(self.CustomScroll_Outside[3]),
			"Grid_R": oead.F32(self.Editor_Grid[0]),
			"Grid_G": oead.F32(self.Editor_Grid[1]),
			"Grid_B": oead.F32(self.Editor_Grid[2]),
			"Grid_A": oead.F32(self.Editor_Grid[3]),
			"Shadow_R": oead.F32(self.Shadow_Color[0]),
			"Shadow_G": oead.F32(self.Shadow_Color[1]),
			"Shadow_B": oead.F32(self.Shadow_Color[2]),
			"Shadow_A": oead.F32(self.Shadow_Color[3]),
			"Shadow_Offset": oead.F32(self.Shadow_Offset),
		}

class MM2Theme_M3(MM2Theme):
	Tileset_Model_Animation_Type: str
	Enemy_Variant: str
	Shadow_Color: list[float]
	Shadow_Offset: float

	def __init__(self, info):
		super().__init__(info)
		self.Tileset_Model_Animation_Type		= info["Tileset_Model_Animation_Type"]
		self.Enemy_Variant						= info["Enemy_Variant"]
		self.Shadow_Color						= [info["Shadow_Color"][0], info["Shadow_Color"][1], info["Shadow_Color"][2], info["Shadow_Color"][3]]
		self.Shadow_Offset						= info["Shadow_Offset"]
	def print(self):
		print("Tileset_Model:				"+str(self.Tileset_Model)+
			"\nTileset_Model_Animation_Type:		"+str(self.Tileset_Model_Animation_Type)+
			"\nLighting:				"+str(self.Lighting)+
			"\nEnemy_Variant:				"+str(self.Enemy_Variant)+
			"\nBackground_Model:			"+str(self.Background_Model)+
			"\nBackground_Lighting:			"+str(self.Background_Lighting)+
			"\nVertical_Background_Lighting:		"+str(self.Vertical_Background_Lighting)+
			"\nVertical_Background_Anchor_Type:	"+str(self.Vertical_Background_Anchor_Type)+
			"\nCustomScroll_Inside:			"+str(self.CustomScroll_Inside)+
			"\nCustomScroll_Outside:			"+str(self.CustomScroll_Outside)+
			"\nEditor_Grid:				"+str(self.Editor_Grid)+
			"\nShadow_Color:				"+str(self.Shadow_Color)+
			"\nShadow_Offset:				"+str(self.Shadow_Offset)+"\n")
	def as_byml_dict(self):
		return {
			"FieldModel": self.Tileset_Model,
			"FieldAnime": self.Tileset_Model_Animation_Type,
			"Env_Model": self.Lighting,
			"Enemy": self.Enemy_Variant,
			"DVModel": self.Background_Model,
			"Env_DV": self.Background_Lighting,
			"Env_DV_V": self.Vertical_Background_Lighting,
			"DV_V_OffsetType": "上基準" if (self.Vertical_Background_Anchor_Type == "Top") else "下基準", # Default to "Lower Benchmark"
			"CSin_R": oead.F32(self.CustomScroll_Inside[0]),
			"CSin_G": oead.F32(self.CustomScroll_Inside[1]),
			"CSin_B": oead.F32(self.CustomScroll_Inside[2]),
			"CSin_A": oead.F32(self.CustomScroll_Inside[3]),
			"CSout_R": oead.F32(self.CustomScroll_Outside[0]),
			"CSout_G": oead.F32(self.CustomScroll_Outside[1]),
			"CSout_B": oead.F32(self.CustomScroll_Outside[2]),
			"CSout_A": oead.F32(self.CustomScroll_Outside[3]),
			"Grid_R": oead.F32(self.Editor_Grid[0]),
			"Grid_G": oead.F32(self.Editor_Grid[1]),
			"Grid_B": oead.F32(self.Editor_Grid[2]),
			"Grid_A": oead.F32(self.Editor_Grid[3]),
			"Shadow_R": oead.F32(self.Shadow_Color[0]),
			"Shadow_G": oead.F32(self.Shadow_Color[1]),
			"Shadow_B": oead.F32(self.Shadow_Color[2]),
			"Shadow_A": oead.F32(self.Shadow_Color[3]),
			"Shadow_Offset": oead.F32(self.Shadow_Offset),
		}

class MM2Theme_MW(MM2Theme):
	Tileset_Model_Animation_Type: str
	Enemy_Variant: str
	Shadow_Color: list[float]
	Shadow_Offset: float

	def __init__(self, info):
		super().__init__(info)
		self.Tileset_Model_Animation_Type		= info["Tileset_Model_Animation_Type"]
		self.Enemy_Variant						= info["Enemy_Variant"]
		self.Shadow_Color						= [info["Shadow_Color"][0], info["Shadow_Color"][1], info["Shadow_Color"][2], info["Shadow_Color"][3]]
		self.Shadow_Offset						= info["Shadow_Offset"]
	def print(self):
		print("Tileset_Model:				"+str(self.Tileset_Model)+
			"\nTileset_Model_Animation_Type:		"+str(self.Tileset_Model_Animation_Type)+
			"\nLighting:				"+str(self.Lighting)+
			"\nEnemy_Variant:				"+str(self.Enemy_Variant)+
			"\nBackground_Model:			"+str(self.Background_Model)+
			"\nBackground_Lighting:			"+str(self.Background_Lighting)+
			"\nVertical_Background_Lighting:		"+str(self.Vertical_Background_Lighting)+
			"\nVertical_Background_Anchor_Type:	"+str(self.Vertical_Background_Anchor_Type)+
			"\nCustomScroll_Inside:			"+str(self.CustomScroll_Inside)+
			"\nCustomScroll_Outside:			"+str(self.CustomScroll_Outside)+
			"\nEditor_Grid:				"+str(self.Editor_Grid)+
			"\nShadow_Color:				"+str(self.Shadow_Color)+
			"\nShadow_Offset:				"+str(self.Shadow_Offset)+"\n")
	def as_byml_dict(self):
		return {
			"FieldModel": self.Tileset_Model,
			"FieldAnime": self.Tileset_Model_Animation_Type,
			"Env_Model": self.Lighting,
			"Enemy": self.Enemy_Variant,
			"DVModel": self.Background_Model,
			"Env_DV": self.Background_Lighting,
			"Env_DV_V": self.Vertical_Background_Lighting,
			"DV_V_OffsetType": "上基準" if (self.Vertical_Background_Anchor_Type == "Top") else "下基準", # Default to "Lower Benchmark"
			"CSin_R": oead.F32(self.CustomScroll_Inside[0]),
			"CSin_G": oead.F32(self.CustomScroll_Inside[1]),
			"CSin_B": oead.F32(self.CustomScroll_Inside[2]),
			"CSin_A": oead.F32(self.CustomScroll_Inside[3]),
			"CSout_R": oead.F32(self.CustomScroll_Outside[0]),
			"CSout_G": oead.F32(self.CustomScroll_Outside[1]),
			"CSout_B": oead.F32(self.CustomScroll_Outside[2]),
			"CSout_A": oead.F32(self.CustomScroll_Outside[3]),
			"Grid_R": oead.F32(self.Editor_Grid[0]),
			"Grid_G": oead.F32(self.Editor_Grid[1]),
			"Grid_B": oead.F32(self.Editor_Grid[2]),
			"Grid_A": oead.F32(self.Editor_Grid[3]),
			"Shadow_R": oead.F32(self.Shadow_Color[0]),
			"Shadow_G": oead.F32(self.Shadow_Color[1]),
			"Shadow_B": oead.F32(self.Shadow_Color[2]),
			"Shadow_A": oead.F32(self.Shadow_Color[3]),
			"Shadow_Offset": oead.F32(self.Shadow_Offset),
		}

class MM2Theme_WU(MM2Theme):
	Tileset_Model_Animation_Type: str
	Enemy_Variant: str
	Edge_Light_color: list[float]
	Background_Position: list[float]
	Vertical_Background_Position: list[float]
	WIP_DV_CamMoveY: float
	WIP_DV_ProjMoveY: float
	WIP_DV_ProjOffsetY: float
	WIP_DV_V_CamMoveY: float
	WIP_DV_V_ProjMoveY: float
	WIP_DV_V_ProjOffsetY: float
	Play_Background_FOV: float

	def __init__(self, info):
		super().__init__(info)
		self.Tileset_Model_Animation_Type		= info["Tileset_Model_Animation_Type"]
		self.Enemy_Variant						= info["Enemy_Variant"]
		self.Edge_Light_color					= [info["Edge_Light_color"][0], info["Edge_Light_color"][1], info["Edge_Light_color"][2]]
		self.Background_Position				= [info["Background_Position"][0], info["Background_Position"][1]]
		self.Vertical_Background_Position		= [info["Vertical_Background_Position"][0], info["Vertical_Background_Position"][1]]
		self.WIP_DV_CamMoveY					= info["WIP_DV_CamMoveY"]
		self.WIP_DV_ProjMoveY					= info["WIP_DV_ProjMoveY"]
		self.WIP_DV_ProjOffsetY					= info["WIP_DV_ProjOffsetY"]
		self.WIP_DV_V_CamMoveY					= info["WIP_DV_V_CamMoveY"]
		self.WIP_DV_V_ProjMoveY					= info["WIP_DV_V_ProjMoveY"]
		self.WIP_DV_V_ProjOffsetY				= info["WIP_DV_V_ProjOffsetY"]
		self.Play_Background_FOV				= info["Play_Background_FOV"]
	def print(self):
		print("Tileset_Model:				"+str(self.Tileset_Model)+
			"\nTileset_Model_Animation_Type:		"+str(self.Tileset_Model_Animation_Type)+
			"\nLighting:				"+str(self.Lighting)+
			"\nEnemy_Variant:				"+str(self.Enemy_Variant)+
			"\nBackground_Model:			"+str(self.Background_Model)+
			"\nBackground_Lighting:			"+str(self.Background_Lighting)+
			"\nVertical_Background_Lighting:		"+str(self.Vertical_Background_Lighting)+
			"\nVertical_Background_Anchor_Type:	"+str(self.Vertical_Background_Anchor_Type)+
			"\nCustomScroll_Inside:			"+str(self.CustomScroll_Inside)+
			"\nCustomScroll_Outside:			"+str(self.CustomScroll_Outside)+
			"\nEditor_Grid:				"+str(self.Editor_Grid)+
			"\nEdge_Light_color:			"+str(self.Edge_Light_color)+
			"\nBackground_Position:			"+str(self.Background_Position)+
			"\nVertical_Background_Position:		"+str(self.Vertical_Background_Position)+
			"\nWIP_DV_CamMoveY:			"+str(self.WIP_DV_CamMoveY)+
			"\nWIP_DV_ProjMoveY:			"+str(self.WIP_DV_ProjMoveY)+
			"\nWIP_DV_ProjOffsetY:			"+str(self.WIP_DV_ProjOffsetY)+
			"\nWIP_DV_V_CamMoveY:			"+str(self.WIP_DV_V_CamMoveY)+
			"\nWIP_DV_V_ProjMoveY:			"+str(self.WIP_DV_V_ProjMoveY)+
			"\nWIP_DV_V_ProjOffsetY:			"+str(self.WIP_DV_V_ProjOffsetY)+
			"\nPlay_Background_FOV:			"+str(self.Play_Background_FOV)+"\n")
	def as_byml_dict(self):
		return {
			"FieldModel": self.Tileset_Model,
			"FieldAnime": self.Tileset_Model_Animation_Type,
			"Env_Model": self.Lighting,
			"Enemy": self.Enemy_Variant,
			"DVModel": self.Background_Model,
			"Env_DV": self.Background_Lighting,
			"Env_DV_V": self.Vertical_Background_Lighting,
			"DV_V_OffsetType": "上基準" if (self.Vertical_Background_Anchor_Type == "Top") else "下基準", # Default to "Lower Benchmark"
			"CSin_R": oead.F32(self.CustomScroll_Inside[0]),
			"CSin_G": oead.F32(self.CustomScroll_Inside[1]),
			"CSin_B": oead.F32(self.CustomScroll_Inside[2]),
			"CSin_A": oead.F32(self.CustomScroll_Inside[3]),
			"CSout_R": oead.F32(self.CustomScroll_Outside[0]),
			"CSout_G": oead.F32(self.CustomScroll_Outside[1]),
			"CSout_B": oead.F32(self.CustomScroll_Outside[2]),
			"CSout_A": oead.F32(self.CustomScroll_Outside[3]),
			"Grid_R": oead.F32(self.Editor_Grid[0]),
			"Grid_G": oead.F32(self.Editor_Grid[1]),
			"Grid_B": oead.F32(self.Editor_Grid[2]),
			"Grid_A": oead.F32(self.Editor_Grid[3]),
			"EdgeLightColor_R": oead.F32(self.Edge_Light_color[0]),
			"EdgeLightColor_G": oead.F32(self.Edge_Light_color[1]),
			"EdgeLightColor_B": oead.F32(self.Edge_Light_color[2]),
			"DV_pos_x": oead.F32(self.Background_Position[0]),
			"DV_pos_y": oead.F32(self.Background_Position[1]),
			"DV_V_pos_x": oead.F32(self.Vertical_Background_Position[0]),
			"DV_V_pos_y": oead.F32(self.Vertical_Background_Position[1]),
			"DV_CamMoveY": oead.F32(self.WIP_DV_CamMoveY),
			"DV_ProjMoveY": oead.F32(self.WIP_DV_ProjMoveY),
			"DV_ProjOffsetY": oead.F32(self.WIP_DV_ProjOffsetY),
			"DV_V_CamMoveY": oead.F32(self.WIP_DV_V_CamMoveY),
			"DV_V_ProjMoveY": oead.F32(self.WIP_DV_V_ProjMoveY),
			"DV_V_ProjOffsetY": oead.F32(self.WIP_DV_V_ProjOffsetY),
			"DV_Play_Fovy": oead.F32(self.Play_Background_FOV),
		}

class MM2Theme_3W(MM2Theme):
	WIP_DV_CamMoveY: float
	WIP_DV_ProjMoveY: float
	WIP_DV_ProjOffsetY: float
	WIP_DV_V_CamMoveY: float
	WIP_DV_V_ProjMoveY: float
	WIP_DV_V_ProjOffsetY: float
	Editor_Background_FOV: float
	Play_Background_FOV: float
	WIP_DV_ScalePivot: float

	def __init__(self, info):
		super().__init__(info)
		self.WIP_DV_CamMoveY					= info["WIP_DV_CamMoveY"]
		self.WIP_DV_ProjMoveY					= info["WIP_DV_ProjMoveY"]
		self.WIP_DV_ProjOffsetY					= info["WIP_DV_ProjOffsetY"]
		self.WIP_DV_V_CamMoveY					= info["WIP_DV_V_CamMoveY"]
		self.WIP_DV_V_ProjMoveY					= info["WIP_DV_V_ProjMoveY"]
		self.WIP_DV_V_ProjOffsetY				= info["WIP_DV_V_ProjOffsetY"]
		self.Editor_Background_FOV				= info["Editor_Background_FOV"]
		self.Play_Background_FOV				= info["Play_Background_FOV"]
		self.WIP_DV_ScalePivot					= info["WIP_DV_ScalePivot"]
	def print(self):
		print("Tileset_Model:				"+str(self.Tileset_Model)+
			"\nLighting:				"+str(self.Lighting)+
			"\nBackground_Model:			"+str(self.Background_Model)+
			"\nBackground_Lighting:			"+str(self.Background_Lighting)+
			"\nVertical_Background_Lighting:		"+str(self.Vertical_Background_Lighting)+
			"\nVertical_Background_Anchor_Type:	"+str(self.Vertical_Background_Anchor_Type)+
			"\nCustomScroll_Inside:			"+str(self.CustomScroll_Inside)+
			"\nCustomScroll_Outside:			"+str(self.CustomScroll_Outside)+
			"\nEditor_Grid:				"+str(self.Editor_Grid)+
			"\nWIP_DV_CamMoveY:			"+str(self.WIP_DV_CamMoveY)+
			"\nWIP_DV_ProjMoveY:			"+str(self.WIP_DV_ProjMoveY)+
			"\nWIP_DV_ProjOffsetY:			"+str(self.WIP_DV_ProjOffsetY)+
			"\nWIP_DV_V_CamMoveY:			"+str(self.WIP_DV_V_CamMoveY)+
			"\nWIP_DV_V_ProjMoveY:			"+str(self.WIP_DV_V_ProjMoveY)+
			"\nWIP_DV_V_ProjOffsetY:			"+str(self.WIP_DV_V_ProjOffsetY)+
			"\nEditor_Background_FOV:			"+str(self.Editor_Background_FOV)+
			"\nPlay_Background_FOV:			"+str(self.Play_Background_FOV)+
			"\nWIP_DV_ScalePivot:			"+str(self.WIP_DV_ScalePivot)+"\n")
	def as_byml_dict(self):
		return {
			"FieldModel": self.Tileset_Model,
			"Env_Model": self.Lighting,
			"DVModel": self.Background_Model,
			"Env_DV": self.Background_Lighting,
			"Env_DV_V": self.Vertical_Background_Lighting,
			"DV_V_OffsetType": "上基準" if (self.Vertical_Background_Anchor_Type == "Top") else "下基準", # Default to "Lower Benchmark"
			"CSin_R": oead.F32(self.CustomScroll_Inside[0]),
			"CSin_G": oead.F32(self.CustomScroll_Inside[1]),
			"CSin_B": oead.F32(self.CustomScroll_Inside[2]),
			"CSin_A": oead.F32(self.CustomScroll_Inside[3]),
			"CSout_R": oead.F32(self.CustomScroll_Outside[0]),
			"CSout_G": oead.F32(self.CustomScroll_Outside[1]),
			"CSout_B": oead.F32(self.CustomScroll_Outside[2]),
			"CSout_A": oead.F32(self.CustomScroll_Outside[3]),
			"Grid_R": oead.F32(self.Editor_Grid[0]),
			"Grid_G": oead.F32(self.Editor_Grid[1]),
			"Grid_B": oead.F32(self.Editor_Grid[2]),
			"Grid_A": oead.F32(self.Editor_Grid[3]),
			"DV_CamMoveY": oead.F32(self.WIP_DV_CamMoveY),
			"DV_ProjMoveY": oead.F32(self.WIP_DV_ProjMoveY),
			"DV_ProjOffsetY": oead.F32(self.WIP_DV_ProjOffsetY),
			"DV_V_CamMoveY": oead.F32(self.WIP_DV_V_CamMoveY),
			"DV_V_ProjMoveY": oead.F32(self.WIP_DV_V_ProjMoveY),
			"DV_V_ProjOffsetY": oead.F32(self.WIP_DV_V_ProjOffsetY),
			"DV_Edit_Fovy": oead.F32(self.Editor_Background_FOV),
			"DV_Play_Fovy": oead.F32(self.Play_Background_FOV),
			"DV_ScalePivot": oead.F32(self.WIP_DV_ScalePivot),
		}

class MM2ThemeSet():
	Day_M1: MM2Theme_M1
	Night_M1: MM2Theme_M1
	Day_M3: MM2Theme_M3
	Night_M3: MM2Theme_M3
	Day_MW: MM2Theme_MW
	Night_MW: MM2Theme_MW
	Day_WU: MM2Theme_WU
	Night_WU: MM2Theme_WU
	Day_3W: MM2Theme_3W
	Night_3W: MM2Theme_3W

	def __init__(self, ThemePrefix):
		with open("Input/"+ThemePrefix+".M1.MM2Theme", "rt") as file:
			self.Day_M1 = MM2Theme_M1(json.load(file))
			self.Day_M1.print()
		with open("Input/"+ThemePrefix+"_Night.M1.MM2Theme", "rt") as file:
			self.Night_M1 = MM2Theme_M1(json.load(file))
			self.Night_M1.print()

		with open("Input/"+ThemePrefix+".M3.MM2Theme", "rt") as file:
			self.Day_M3 = MM2Theme_M3(json.load(file))
			self.Day_M3.print()
		with open("Input/"+ThemePrefix+"_Night.M3.MM2Theme", "rt") as file:
			self.Night_M3 = MM2Theme_M3(json.load(file))
			self.Night_M3.print()

		with open("Input/"+ThemePrefix+".MW.MM2Theme", "rt") as file:
			self.Day_MW = MM2Theme_MW(json.load(file))
			self.Day_MW.print()
		with open("Input/"+ThemePrefix+"_Night.MW.MM2Theme", "rt") as file:
			self.Night_MW = MM2Theme_MW(json.load(file))
			self.Night_MW.print()

		with open("Input/"+ThemePrefix+".WU.MM2Theme", "rt") as file:
			self.Day_WU = MM2Theme_WU(json.load(file))
			self.Day_WU.print()
		with open("Input/"+ThemePrefix+"_Night.WU.MM2Theme", "rt") as file:
			self.Night_WU = MM2Theme_WU(json.load(file))
			self.Night_WU.print()

		with open("Input/"+ThemePrefix+".3W.MM2Theme", "rt") as file:
			self.Day_3W = MM2Theme_3W(json.load(file))
			self.Day_3W.print()
		with open("Input/"+ThemePrefix+"_Night.3W.MM2Theme", "rt") as file:
			self.Night_3W = MM2Theme_3W(json.load(file))
			self.Night_3W.print()
		

def main():
	Plains = MM2ThemeSet("Plains")
	Underground = Plains
	Castle = Plains
	Airship = Plains
	Water = Plains
	GhostHouse = Plains
	Snow = Plains
	Desert = Plains
	Atheltic = Plains
	Woods = Plains

	Scenes_M1= [Plains.Day_M1.as_byml_dict(),		Plains.Night_M1.as_byml_dict(),
				Underground.Day_M1.as_byml_dict(),	Underground.Night_M1.as_byml_dict(),
				Castle.Day_M1.as_byml_dict(),		Castle.Night_M1.as_byml_dict(),
				Airship.Day_M1.as_byml_dict(),		Airship.Night_M1.as_byml_dict(),
				Water.Day_M1.as_byml_dict(),		Water.Night_M1.as_byml_dict(),
				GhostHouse.Day_M1.as_byml_dict(),	GhostHouse.Night_M1.as_byml_dict(),
				Snow.Day_M1.as_byml_dict(),			Snow.Night_M1.as_byml_dict(),
				Desert.Day_M1.as_byml_dict(),		Desert.Night_M1.as_byml_dict(),
				Atheltic.Day_M1.as_byml_dict(),		Atheltic.Night_M1.as_byml_dict(),
				Woods.Day_M1.as_byml_dict(),		Woods.Night_M1.as_byml_dict()]
	Scenes_M3= [Plains.Day_M3.as_byml_dict(),		Plains.Night_M3.as_byml_dict(),
				Underground.Day_M3.as_byml_dict(),	Underground.Night_M3.as_byml_dict(),
				Castle.Day_M3.as_byml_dict(),		Castle.Night_M3.as_byml_dict(),
				Airship.Day_M3.as_byml_dict(),		Airship.Night_M3.as_byml_dict(),
				Water.Day_M3.as_byml_dict(),		Water.Night_M3.as_byml_dict(),
				GhostHouse.Day_M3.as_byml_dict(),	GhostHouse.Night_M3.as_byml_dict(),
				Snow.Day_M3.as_byml_dict(),			Snow.Night_M3.as_byml_dict(),
				Desert.Day_M3.as_byml_dict(),		Desert.Night_M3.as_byml_dict(),
				Atheltic.Day_M3.as_byml_dict(),		Atheltic.Night_M3.as_byml_dict(),
				Woods.Day_M3.as_byml_dict(),		Woods.Night_M3.as_byml_dict()]
	Scenes_MW= [Plains.Day_MW.as_byml_dict(),		Plains.Night_MW.as_byml_dict(),
				Underground.Day_MW.as_byml_dict(),	Underground.Night_MW.as_byml_dict(),
				Castle.Day_MW.as_byml_dict(),		Castle.Night_MW.as_byml_dict(),
				Airship.Day_MW.as_byml_dict(),		Airship.Night_MW.as_byml_dict(),
				Water.Day_MW.as_byml_dict(),		Water.Night_MW.as_byml_dict(),
				GhostHouse.Day_MW.as_byml_dict(),	GhostHouse.Night_MW.as_byml_dict(),
				Snow.Day_MW.as_byml_dict(),			Snow.Night_MW.as_byml_dict(),
				Desert.Day_MW.as_byml_dict(),		Desert.Night_MW.as_byml_dict(),
				Atheltic.Day_MW.as_byml_dict(),		Atheltic.Night_MW.as_byml_dict(),
				Woods.Day_MW.as_byml_dict(),		Woods.Night_MW.as_byml_dict()]
	Scenes_WU= [Plains.Day_WU.as_byml_dict(),		Plains.Night_WU.as_byml_dict(),
				Underground.Day_WU.as_byml_dict(),	Underground.Night_WU.as_byml_dict(),
				Castle.Day_WU.as_byml_dict(),		Castle.Night_WU.as_byml_dict(),
				Airship.Day_WU.as_byml_dict(),		Airship.Night_WU.as_byml_dict(),
				Water.Day_WU.as_byml_dict(),		Water.Night_WU.as_byml_dict(),
				GhostHouse.Day_WU.as_byml_dict(),	GhostHouse.Night_WU.as_byml_dict(),
				Snow.Day_WU.as_byml_dict(),			Snow.Night_WU.as_byml_dict(),
				Desert.Day_WU.as_byml_dict(),		Desert.Night_WU.as_byml_dict(),
				Atheltic.Day_WU.as_byml_dict(),		Atheltic.Night_WU.as_byml_dict(),
				Woods.Day_WU.as_byml_dict(),		Woods.Night_WU.as_byml_dict()]
	Scenes_3W= [Plains.Day_3W.as_byml_dict(),		Plains.Night_3W.as_byml_dict(),
				Underground.Day_3W.as_byml_dict(),	Underground.Night_3W.as_byml_dict(),
				Castle.Day_3W.as_byml_dict(),		Castle.Night_3W.as_byml_dict(),
				Airship.Day_3W.as_byml_dict(),		Airship.Night_3W.as_byml_dict(),
				Water.Day_3W.as_byml_dict(),		Water.Night_3W.as_byml_dict(),
				GhostHouse.Day_3W.as_byml_dict(),	GhostHouse.Night_3W.as_byml_dict(),
				Snow.Day_3W.as_byml_dict(),			Snow.Night_3W.as_byml_dict(),
				Desert.Day_3W.as_byml_dict(),		Desert.Night_3W.as_byml_dict(),
				Atheltic.Day_3W.as_byml_dict(),		Atheltic.Night_3W.as_byml_dict(),
				Woods.Day_3W.as_byml_dict(),		Woods.Night_3W.as_byml_dict()]

	if not os.path.exists("Output/"):
		os.makedirs("Output/")

	with open("Output/M1_SceneDB.yaml", "wt") as file:
		file.write(oead.byml.to_text(Scenes_M1))
	with open("Output/M1_SceneDB.byml", "wb") as file:
		file.write(oead.byml.to_binary(Scenes_M1, False, 1))
	with open("Output/M3_SceneDB.yaml", "wt") as file:
		file.write(oead.byml.to_text(Scenes_M3))
	with open("Output/M3_SceneDB.byml", "wb") as file:
		file.write(oead.byml.to_binary(Scenes_M3, False, 1))
	with open("Output/MW_SceneDB.yaml", "wt") as file:
		file.write(oead.byml.to_text(Scenes_MW))
	with open("Output/MW_SceneDB.byml", "wb") as file:
		file.write(oead.byml.to_binary(Scenes_MW, False, 1))
	with open("Output/WU_SceneDB.yaml", "wt") as file:
		file.write(oead.byml.to_text(Scenes_WU))
	with open("Output/WU_SceneDB.byml", "wb") as file:
		file.write(oead.byml.to_binary(Scenes_WU, False, 1))
	with open("Output/3W_SceneDB.yaml", "wt") as file:
		file.write(oead.byml.to_text(Scenes_3W))
	with open("Output/3W_SceneDB.byml", "wb") as file:
		file.write(oead.byml.to_binary(Scenes_3W, False, 1))

main()
