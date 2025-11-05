import oead
from enum import Enum

# Enums
class GameStyle(Enum):
	SMB1	= 'M1', 'M1_SceneDB'
	SMB3	= 'M3', 'M3_SceneDB'
	SMW		= 'MW', 'MW_SceneDB'
	NSMBU	= 'WU', 'WU_SceneDB'
	SM3DW	= '3W', '3W_SceneDB'
	MyWorld	= 'MyWorld', 'SceneDB_MyWorld'

class Vertical_Background_Anchor_Enum(Enum):
	Top		= '上基準'
	Bottom	= '下基準'

# Theme Classes
class Theme():
	Style: GameStyle
	Theme_Name: str
	Is_Night: bool = False
	def print(self):
		pass
	def from_json_dict(json: dict):
		pass
	def from_byml_dict(byml: dict):
		pass
	def as_json_dict(self) -> dict:
		pass
	def as_byml_dict(self) -> dict:
		pass

class SMB1_Theme(Theme):
	Style = GameStyle.SMB1
	CustomScroll_Inside: list[float] # Vec4
	CustomScroll_Outside: list[float] # Vec4
	Background_Model: str
	Vertical_Background_Anchor_Type: Vertical_Background_Anchor_Enum
	Enemy_Variant: str
	Background_Lighting: str
	Vertical_Background_Lighting: str
	Lighting: str
	Tileset_Model_Animation_Type: str
	Tileset_Model: str
	Editor_Grid: list[float] # Vec4
	Shadow_Color: list[float] # Vec4
	Shadow_Offset: float

	def print(self):
		print(self.Style.name+": "+self.Theme_Name+"\n"+
			"> CustomScroll_Inside:			"+str(self.CustomScroll_Inside)+"\n"+
			"> CustomScroll_Outside:			"+str(self.CustomScroll_Outside)+"\n"+
			"> Background_Model:			"+str(self.Background_Model)+"\n"+
			"> Vertical_Background_Anchor_Type:	"+str(self.Vertical_Background_Anchor_Type)+"\n"+
			"> Enemy_Variant:			"+str(self.Enemy_Variant)+"\n"+
			"> Background_Lighting:			"+str(self.Background_Lighting)+"\n"+
			"> Vertical_Background_Lighting:		"+str(self.Vertical_Background_Lighting)+"\n"+
			"> Lighting:				"+str(self.Lighting)+"\n"+
			"> Tileset_Model_Animation_Type:		"+str(self.Tileset_Model_Animation_Type)+"\n"+
			"> Tileset_Model:			"+str(self.Tileset_Model)+"\n"+
			"> Editor_Grid:				"+str(self.Editor_Grid)+"\n"+
			"> Shadow_Color:				"+str(self.Shadow_Color)+"\n"+
			"> Shadow_Offset:			"+str(self.Shadow_Offset)+"\n"
		)
	def from_json_dict(json: dict) -> Theme:
		self = SMB1_Theme()
		self.Theme_Name = json["Theme_Name"]
		self.CustomScroll_Inside = [
			float(json["CustomScroll_Inside"][0]).__round__(5),
			float(json["CustomScroll_Inside"][1]).__round__(5),
			float(json["CustomScroll_Inside"][2]).__round__(5),
			float(json["CustomScroll_Inside"][3]).__round__(5),
		]
		self.CustomScroll_Outside = [
			float(json["CustomScroll_Outside"][0]).__round__(5),
			float(json["CustomScroll_Outside"][1]).__round__(5),
			float(json["CustomScroll_Outside"][2]).__round__(5),
			float(json["CustomScroll_Outside"][3]).__round__(5),
		]
		self.Background_Model = json["Background_Model"]
		self.Vertical_Background_Anchor_Type = Vertical_Background_Anchor_Enum[json["Vertical_Background_Anchor_Type"]]
		self.Enemy_Variant = json["Enemy_Variant"]
		self.Background_Lighting = json["Background_Lighting"]
		self.Vertical_Background_Lighting = json["Vertical_Background_Lighting"]
		self.Lighting = json["Lighting"]
		self.Tileset_Model_Animation_Type = json["Tileset_Model_Animation_Type"]
		self.Tileset_Model = json["Tileset_Model"]
		self.Editor_Grid = [
			float(json["Editor_Grid"][0]).__round__(5),
			float(json["Editor_Grid"][1]).__round__(5),
			float(json["Editor_Grid"][2]).__round__(5),
			float(json["Editor_Grid"][3]).__round__(5),
		]
		self.Shadow_Color = [
			float(json["Shadow_Color"][0]).__round__(5),
			float(json["Shadow_Color"][1]).__round__(5),
			float(json["Shadow_Color"][2]).__round__(5),
			float(json["Shadow_Color"][3]).__round__(5),
		]
		self.Shadow_Offset = float(json["Shadow_Offset"]).__round__(5)
		return self
	def from_byml_dict(byml: dict) -> Theme:
		self = SMB1_Theme()
		self.Theme_Name = byml["FieldModel"][9:]
		if (self.Theme_Name[-2:] == "_D"):
			self.Theme_Name = self.Theme_Name[:-2]
			self.Is_Night = True
		self.CustomScroll_Inside = [
			float(byml["CSin_R"]).__round__(5),
			float(byml["CSin_G"]).__round__(5),
			float(byml["CSin_B"]).__round__(5),
			float(byml["CSin_A"]).__round__(5),
		]
		self.CustomScroll_Outside = [
			float(byml["CSout_R"]).__round__(5),
			float(byml["CSout_G"]).__round__(5),
			float(byml["CSout_B"]).__round__(5),
			float(byml["CSout_A"]).__round__(5),
		]
		self.Background_Model = byml["DVModel"]
		self.Vertical_Background_Anchor_Type = Vertical_Background_Anchor_Enum(byml["DV_V_OffsetType"])
		self.Enemy_Variant = byml["Enemy"]
		self.Background_Lighting = byml["Env_DV"]
		self.Vertical_Background_Lighting = byml["Env_DV_V"]
		self.Lighting = byml["Env_Model"]
		self.Tileset_Model_Animation_Type = byml["FieldAnime"]
		self.Tileset_Model = byml["FieldModel"]
		self.Editor_Grid = [
			float(byml["Grid_R"]).__round__(5),
			float(byml["Grid_G"]).__round__(5),
			float(byml["Grid_B"]).__round__(5),
			float(byml["Grid_A"]).__round__(5),
		]
		self.Shadow_Color = [
			float(byml["Shadow_R"]).__round__(5),
			float(byml["Shadow_G"]).__round__(5),
			float(byml["Shadow_B"]).__round__(5),
			float(byml["Shadow_A"]).__round__(5),
		]
		self.Shadow_Offset = float(byml["Shadow_Offset"]).__round__(5)
		return self
	def as_json_dict(self) -> dict:
		return {
			"Theme_Name": self.Theme_Name,
			"CustomScroll_Inside": self.CustomScroll_Inside,
			"CustomScroll_Outside": self.CustomScroll_Outside,
			"Background_Model": self.Background_Model,
			"Vertical_Background_Anchor_Type": self.Vertical_Background_Anchor_Type.name,
			"Enemy_Variant": self.Enemy_Variant,
			"Background_Lighting": self.Background_Lighting,
			"Vertical_Background_Lighting": self.Vertical_Background_Lighting,
			"Lighting": self.Lighting,
			"Tileset_Model_Animation_Type": self.Tileset_Model_Animation_Type,
			"Tileset_Model": self.Tileset_Model,
			"Editor_Grid": self.Editor_Grid,
			"Shadow_Color": self.Shadow_Color,
			"Shadow_Offset": self.Shadow_Offset,
		}
	def as_byml_dict(self) -> dict:
		return {
			"CSin_R": oead.F32(self.CustomScroll_Inside[0]),
			"CSin_G": oead.F32(self.CustomScroll_Inside[1]),
			"CSin_B": oead.F32(self.CustomScroll_Inside[2]),
			"CSin_A": oead.F32(self.CustomScroll_Inside[3]),
			"CSout_R": oead.F32(self.CustomScroll_Outside[0]),
			"CSout_G": oead.F32(self.CustomScroll_Outside[1]),
			"CSout_B": oead.F32(self.CustomScroll_Outside[2]),
			"CSout_A": oead.F32(self.CustomScroll_Outside[3]),
			"DVModel": self.Background_Model,
			"DV_V_OffsetType": self.Vertical_Background_Anchor_Type.value,
			"Enemy": self.Enemy_Variant,
			"Env_DV": self.Background_Lighting,
			"Env_DV_V": self.Vertical_Background_Lighting,
			"Env_Model": self.Lighting,
			"FieldAnime": self.Tileset_Model_Animation_Type,
			"FieldModel": self.Tileset_Model,
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

class SMB3_Theme(Theme):
	Style = GameStyle.SMB3
	CustomScroll_Inside: list[float] # Vec4
	CustomScroll_Outside: list[float] # Vec4
	Background_Model: str
	Vertical_Background_Anchor_Type: Vertical_Background_Anchor_Enum
	Enemy_Variant: str
	Background_Lighting: str
	Vertical_Background_Lighting: str
	Lighting: str
	Tileset_Model_Animation_Type: str
	Tileset_Model: str
	Editor_Grid: list[float] # Vec4
	Shadow_Color: list[float] # Vec4
	Shadow_Offset: float

	def print(self):
		print(self.Style.name+": "+self.Theme_Name+"\n"+
			"> CustomScroll_Inside:			"+str(self.CustomScroll_Inside)+"\n"+
			"> CustomScroll_Outside:			"+str(self.CustomScroll_Outside)+"\n"+
			"> Background_Model:			"+str(self.Background_Model)+"\n"+
			"> Vertical_Background_Anchor_Type:	"+str(self.Vertical_Background_Anchor_Type)+"\n"+
			"> Enemy_Variant:			"+str(self.Enemy_Variant)+"\n"+
			"> Background_Lighting:			"+str(self.Background_Lighting)+"\n"+
			"> Vertical_Background_Lighting:		"+str(self.Vertical_Background_Lighting)+"\n"+
			"> Lighting:				"+str(self.Lighting)+"\n"+
			"> Tileset_Model_Animation_Type:		"+str(self.Tileset_Model_Animation_Type)+"\n"+
			"> Tileset_Model:			"+str(self.Tileset_Model)+"\n"+
			"> Editor_Grid:				"+str(self.Editor_Grid)+"\n"+
			"> Shadow_Color:				"+str(self.Shadow_Color)+"\n"+
			"> Shadow_Offset:			"+str(self.Shadow_Offset)+"\n"
		)
	def from_json_dict(json: dict) -> Theme:
		self = SMB3_Theme()
		self.Theme_Name = json["Theme_Name"]
		self.CustomScroll_Inside = [
			float(json["CustomScroll_Inside"][0]).__round__(5),
			float(json["CustomScroll_Inside"][1]).__round__(5),
			float(json["CustomScroll_Inside"][2]).__round__(5),
			float(json["CustomScroll_Inside"][3]).__round__(5),
		]
		self.CustomScroll_Outside = [
			float(json["CustomScroll_Outside"][0]).__round__(5),
			float(json["CustomScroll_Outside"][1]).__round__(5),
			float(json["CustomScroll_Outside"][2]).__round__(5),
			float(json["CustomScroll_Outside"][3]).__round__(5),
		]
		self.Background_Model = json["Background_Model"]
		self.Vertical_Background_Anchor_Type = Vertical_Background_Anchor_Enum[json["Vertical_Background_Anchor_Type"]]
		self.Enemy_Variant = json["Enemy_Variant"]
		self.Background_Lighting = json["Background_Lighting"]
		self.Vertical_Background_Lighting = json["Vertical_Background_Lighting"]
		self.Lighting = json["Lighting"]
		self.Tileset_Model_Animation_Type = json["Tileset_Model_Animation_Type"]
		self.Tileset_Model = json["Tileset_Model"]
		self.Editor_Grid = [
			float(json["Editor_Grid"][0]).__round__(5),
			float(json["Editor_Grid"][1]).__round__(5),
			float(json["Editor_Grid"][2]).__round__(5),
			float(json["Editor_Grid"][3]).__round__(5),
		]
		self.Shadow_Color = [
			float(json["Shadow_Color"][0]).__round__(5),
			float(json["Shadow_Color"][1]).__round__(5),
			float(json["Shadow_Color"][2]).__round__(5),
			float(json["Shadow_Color"][3]).__round__(5),
		]
		self.Shadow_Offset = float(json["Shadow_Offset"]).__round__(5)
		return self
	def from_byml_dict(byml: dict) -> Theme:
		self = SMB3_Theme()
		self.Theme_Name = byml["FieldModel"][9:]
		if (self.Theme_Name[-2:] == "_D"):
			self.Theme_Name = self.Theme_Name[:-2]
			self.Is_Night = True
		self.CustomScroll_Inside = [
			float(byml["CSin_R"]).__round__(5),
			float(byml["CSin_G"]).__round__(5),
			float(byml["CSin_B"]).__round__(5),
			float(byml["CSin_A"]).__round__(5),
		]
		self.CustomScroll_Outside = [
			float(byml["CSout_R"]).__round__(5),
			float(byml["CSout_G"]).__round__(5),
			float(byml["CSout_B"]).__round__(5),
			float(byml["CSout_A"]).__round__(5),
		]
		self.Background_Model = byml["DVModel"]
		self.Vertical_Background_Anchor_Type = Vertical_Background_Anchor_Enum(byml["DV_V_OffsetType"])
		self.Enemy_Variant = byml["Enemy"]
		self.Background_Lighting = byml["Env_DV"]
		self.Vertical_Background_Lighting = byml["Env_DV_V"]
		self.Lighting = byml["Env_Model"]
		self.Tileset_Model_Animation_Type = byml["FieldAnime"]
		self.Tileset_Model = byml["FieldModel"]
		self.Editor_Grid = [
			float(byml["Grid_R"]).__round__(5),
			float(byml["Grid_G"]).__round__(5),
			float(byml["Grid_B"]).__round__(5),
			float(byml["Grid_A"]).__round__(5),
		]
		self.Shadow_Color = [
			float(byml["Shadow_R"]).__round__(5),
			float(byml["Shadow_G"]).__round__(5),
			float(byml["Shadow_B"]).__round__(5),
			float(byml["Shadow_A"]).__round__(5),
		]
		self.Shadow_Offset = float(byml["Shadow_Offset"]).__round__(5)
		return self
	def as_json_dict(self) -> dict:
		return {
			"Theme_Name": self.Theme_Name,
			"CustomScroll_Inside": self.CustomScroll_Inside,
			"CustomScroll_Outside": self.CustomScroll_Outside,
			"Background_Model": self.Background_Model,
			"Vertical_Background_Anchor_Type": self.Vertical_Background_Anchor_Type.name,
			"Enemy_Variant": self.Enemy_Variant,
			"Background_Lighting": self.Background_Lighting,
			"Vertical_Background_Lighting": self.Vertical_Background_Lighting,
			"Lighting": self.Lighting,
			"Tileset_Model_Animation_Type": self.Tileset_Model_Animation_Type,
			"Tileset_Model": self.Tileset_Model,
			"Editor_Grid": self.Editor_Grid,
			"Shadow_Color": self.Shadow_Color,
			"Shadow_Offset": self.Shadow_Offset,
		}
	def as_byml_dict(self) -> dict:
		return {
			"CSin_R": oead.F32(self.CustomScroll_Inside[0]),
			"CSin_G": oead.F32(self.CustomScroll_Inside[1]),
			"CSin_B": oead.F32(self.CustomScroll_Inside[2]),
			"CSin_A": oead.F32(self.CustomScroll_Inside[3]),
			"CSout_R": oead.F32(self.CustomScroll_Outside[0]),
			"CSout_G": oead.F32(self.CustomScroll_Outside[1]),
			"CSout_B": oead.F32(self.CustomScroll_Outside[2]),
			"CSout_A": oead.F32(self.CustomScroll_Outside[3]),
			"DVModel": self.Background_Model,
			"DV_V_OffsetType": self.Vertical_Background_Anchor_Type.value,
			"Enemy": self.Enemy_Variant,
			"Env_DV": self.Background_Lighting,
			"Env_DV_V": self.Vertical_Background_Lighting,
			"Env_Model": self.Lighting,
			"FieldAnime": self.Tileset_Model_Animation_Type,
			"FieldModel": self.Tileset_Model,
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

class SMW_Theme(Theme):
	Style = GameStyle.SMW
	CustomScroll_Inside: list[float] # Vec4
	CustomScroll_Outside: list[float] # Vec4
	Background_Model: str
	Vertical_Background_Anchor_Type: Vertical_Background_Anchor_Enum
	Enemy_Variant: str
	Background_Lighting: str
	Vertical_Background_Lighting: str
	Lighting: str
	Tileset_Model_Animation_Type: str
	Tileset_Model: str
	Editor_Grid: list[float] # Vec4
	Shadow_Color: list[float] # Vec4
	Shadow_Offset: float

	def print(self):
		print(self.Style.name+": "+self.Theme_Name+"\n"+
			"> CustomScroll_Inside:			"+str(self.CustomScroll_Inside)+"\n"+
			"> CustomScroll_Outside:			"+str(self.CustomScroll_Outside)+"\n"+
			"> Background_Model:			"+str(self.Background_Model)+"\n"+
			"> Vertical_Background_Anchor_Type:	"+str(self.Vertical_Background_Anchor_Type)+"\n"+
			"> Enemy_Variant:			"+str(self.Enemy_Variant)+"\n"+
			"> Background_Lighting:			"+str(self.Background_Lighting)+"\n"+
			"> Vertical_Background_Lighting:		"+str(self.Vertical_Background_Lighting)+"\n"+
			"> Lighting:				"+str(self.Lighting)+"\n"+
			"> Tileset_Model_Animation_Type:		"+str(self.Tileset_Model_Animation_Type)+"\n"+
			"> Tileset_Model:			"+str(self.Tileset_Model)+"\n"+
			"> Editor_Grid:				"+str(self.Editor_Grid)+"\n"+
			"> Shadow_Color:				"+str(self.Shadow_Color)+"\n"+
			"> Shadow_Offset:			"+str(self.Shadow_Offset)+"\n"
		)
	def from_json_dict(json: dict) -> Theme:
		self = SMW_Theme()
		self.Theme_Name = json["Theme_Name"]
		self.CustomScroll_Inside = [
			float(json["CustomScroll_Inside"][0]).__round__(5),
			float(json["CustomScroll_Inside"][1]).__round__(5),
			float(json["CustomScroll_Inside"][2]).__round__(5),
			float(json["CustomScroll_Inside"][3]).__round__(5),
		]
		self.CustomScroll_Outside = [
			float(json["CustomScroll_Outside"][0]).__round__(5),
			float(json["CustomScroll_Outside"][1]).__round__(5),
			float(json["CustomScroll_Outside"][2]).__round__(5),
			float(json["CustomScroll_Outside"][3]).__round__(5),
		]
		self.Background_Model = json["Background_Model"]
		self.Vertical_Background_Anchor_Type = Vertical_Background_Anchor_Enum[json["Vertical_Background_Anchor_Type"]]
		self.Enemy_Variant = json["Enemy_Variant"]
		self.Background_Lighting = json["Background_Lighting"]
		self.Vertical_Background_Lighting = json["Vertical_Background_Lighting"]
		self.Lighting = json["Lighting"]
		self.Tileset_Model_Animation_Type = json["Tileset_Model_Animation_Type"]
		self.Tileset_Model = json["Tileset_Model"]
		self.Editor_Grid = [
			float(json["Editor_Grid"][0]).__round__(5),
			float(json["Editor_Grid"][1]).__round__(5),
			float(json["Editor_Grid"][2]).__round__(5),
			float(json["Editor_Grid"][3]).__round__(5),
		]
		self.Shadow_Color = [
			float(json["Shadow_Color"][0]).__round__(5),
			float(json["Shadow_Color"][1]).__round__(5),
			float(json["Shadow_Color"][2]).__round__(5),
			float(json["Shadow_Color"][3]).__round__(5),
		]
		self.Shadow_Offset = float(json["Shadow_Offset"]).__round__(5)
		return self
	def from_byml_dict(byml: dict) -> Theme:
		self = SMW_Theme()
		self.Theme_Name = byml["FieldModel"][9:]
		if (self.Theme_Name[-2:] == "_D"):
			self.Theme_Name = self.Theme_Name[:-2]
			self.Is_Night = True
		self.CustomScroll_Inside = [
			float(byml["CSin_R"]).__round__(5),
			float(byml["CSin_G"]).__round__(5),
			float(byml["CSin_B"]).__round__(5),
			float(byml["CSin_A"]).__round__(5),
		]
		self.CustomScroll_Outside = [
			float(byml["CSout_R"]).__round__(5),
			float(byml["CSout_G"]).__round__(5),
			float(byml["CSout_B"]).__round__(5),
			float(byml["CSout_A"]).__round__(5),
		]
		self.Background_Model = byml["DVModel"]
		self.Vertical_Background_Anchor_Type = Vertical_Background_Anchor_Enum(byml["DV_V_OffsetType"])
		self.Enemy_Variant = byml["Enemy"]
		self.Background_Lighting = byml["Env_DV"]
		self.Vertical_Background_Lighting = byml["Env_DV_V"]
		self.Lighting = byml["Env_Model"]
		self.Tileset_Model_Animation_Type = byml["FieldAnime"]
		self.Tileset_Model = byml["FieldModel"]
		self.Editor_Grid = [
			float(byml["Grid_R"]).__round__(5),
			float(byml["Grid_G"]).__round__(5),
			float(byml["Grid_B"]).__round__(5),
			float(byml["Grid_A"]).__round__(5),
		]
		self.Shadow_Color = [
			float(byml["Shadow_R"]).__round__(5),
			float(byml["Shadow_G"]).__round__(5),
			float(byml["Shadow_B"]).__round__(5),
			float(byml["Shadow_A"]).__round__(5),
		]
		self.Shadow_Offset = float(byml["Shadow_Offset"]).__round__(5)
		return self
	def as_json_dict(self) -> dict:
		return {
			"Theme_Name": self.Theme_Name,
			"CustomScroll_Inside": self.CustomScroll_Inside,
			"CustomScroll_Outside": self.CustomScroll_Outside,
			"Background_Model": self.Background_Model,
			"Vertical_Background_Anchor_Type": self.Vertical_Background_Anchor_Type.name,
			"Enemy_Variant": self.Enemy_Variant,
			"Background_Lighting": self.Background_Lighting,
			"Vertical_Background_Lighting": self.Vertical_Background_Lighting,
			"Lighting": self.Lighting,
			"Tileset_Model_Animation_Type": self.Tileset_Model_Animation_Type,
			"Tileset_Model": self.Tileset_Model,
			"Editor_Grid": self.Editor_Grid,
			"Shadow_Color": self.Shadow_Color,
			"Shadow_Offset": self.Shadow_Offset,
		}
	def as_byml_dict(self) -> dict:
		return {
			"CSin_R": oead.F32(self.CustomScroll_Inside[0]),
			"CSin_G": oead.F32(self.CustomScroll_Inside[1]),
			"CSin_B": oead.F32(self.CustomScroll_Inside[2]),
			"CSin_A": oead.F32(self.CustomScroll_Inside[3]),
			"CSout_R": oead.F32(self.CustomScroll_Outside[0]),
			"CSout_G": oead.F32(self.CustomScroll_Outside[1]),
			"CSout_B": oead.F32(self.CustomScroll_Outside[2]),
			"CSout_A": oead.F32(self.CustomScroll_Outside[3]),
			"DVModel": self.Background_Model,
			"DV_V_OffsetType": self.Vertical_Background_Anchor_Type.value,
			"Enemy": self.Enemy_Variant,
			"Env_DV": self.Background_Lighting,
			"Env_DV_V": self.Vertical_Background_Lighting,
			"Env_Model": self.Lighting,
			"FieldAnime": self.Tileset_Model_Animation_Type,
			"FieldModel": self.Tileset_Model,
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

class NSMBU_Theme(Theme):
	Style = GameStyle.NSMBU
	CustomScroll_Inside: list[float] # Vec4
	CustomScroll_Outside: list[float] # Vec4
	Background_Model: str
	WIP_DV_CamMoveY: float
	Play_Background_FOV: float
	WIP_DV_ProjMoveY: float
	WIP_DV_ProjOffsetY: float
	WIP_DV_V_CamMoveY: float
	Vertical_Background_Anchor_Type: Vertical_Background_Anchor_Enum
	WIP_DV_V_ProjMoveY: float
	WIP_DV_V_ProjOffsetY: float
	Vertical_Background_Position: list[float] # Vec2
	Background_Position: list[float] # Vec2
	Edge_Light_Color: list[float] # Vec3
	Enemy_Variant: str
	Background_Lighting: str
	Vertical_Background_Lighting: str
	Lighting: str
	Tileset_Model_Animation_Type: str
	Tileset_Model: str
	Editor_Grid: list[float] # Vec4

	def print(self):
		print(self.Style.name+": "+self.Theme_Name+"\n"+
			"> CustomScroll_Inside:			"+str(self.CustomScroll_Inside)+"\n"+
			"> CustomScroll_Outside:			"+str(self.CustomScroll_Outside)+"\n"+
			"> Background_Model:			"+str(self.Background_Model)+"\n"+
			"> WIP_DV_CamMoveY:			"+str(self.WIP_DV_CamMoveY)+"\n"+
			"> Play_Background_FOV:			"+str(self.Play_Background_FOV)+"\n"+
			"> WIP_DV_ProjMoveY:			"+str(self.WIP_DV_ProjMoveY)+"\n"+
			"> WIP_DV_ProjOffsetY:			"+str(self.WIP_DV_ProjOffsetY)+"\n"+
			"> WIP_DV_V_CamMoveY:			"+str(self.WIP_DV_V_CamMoveY)+"\n"+
			"> Vertical_Background_Anchor_Type:	"+str(self.Vertical_Background_Anchor_Type)+"\n"+
			"> WIP_DV_V_ProjMoveY:			"+str(self.WIP_DV_V_ProjMoveY)+"\n"+
			"> WIP_DV_V_ProjOffsetY:			"+str(self.WIP_DV_V_ProjOffsetY)+"\n"+
			"> Vertical_Background_Position:		"+str(self.Vertical_Background_Position)+"\n"+
			"> Background_Position:			"+str(self.Background_Position)+"\n"+
			"> Edge_Light_Color:			"+str(self.Edge_Light_Color)+"\n"+
			"> Enemy_Variant:			"+str(self.Enemy_Variant)+"\n"+
			"> Background_Lighting:			"+str(self.Background_Lighting)+"\n"+
			"> Vertical_Background_Lighting:		"+str(self.Vertical_Background_Lighting)+"\n"+
			"> Lighting:				"+str(self.Lighting)+"\n"+
			"> Tileset_Model_Animation_Type:		"+str(self.Tileset_Model_Animation_Type)+"\n"+
			"> Tileset_Model:			"+str(self.Tileset_Model)+"\n"+
			"> Editor_Grid:				"+str(self.Editor_Grid)+"\n"
		)
	def from_json_dict(json: dict) -> Theme:
		self = NSMBU_Theme()
		self.Theme_Name = json["Theme_Name"]
		self.CustomScroll_Inside = [
			float(json["CustomScroll_Inside"][0]).__round__(5),
			float(json["CustomScroll_Inside"][1]).__round__(5),
			float(json["CustomScroll_Inside"][2]).__round__(5),
			float(json["CustomScroll_Inside"][3]).__round__(5),
		]
		self.CustomScroll_Outside = [
			float(json["CustomScroll_Outside"][0]).__round__(5),
			float(json["CustomScroll_Outside"][1]).__round__(5),
			float(json["CustomScroll_Outside"][2]).__round__(5),
			float(json["CustomScroll_Outside"][3]).__round__(5),
		]
		self.Background_Model = json["Background_Model"]
		self.WIP_DV_CamMoveY = float(json["WIP_DV_CamMoveY"]).__round__(5)
		self.Play_Background_FOV = float(json["Play_Background_FOV"]).__round__(5)
		self.WIP_DV_ProjMoveY = float(json["WIP_DV_ProjMoveY"]).__round__(5)
		self.WIP_DV_ProjOffsetY = float(json["WIP_DV_ProjOffsetY"]).__round__(5)
		self.WIP_DV_V_CamMoveY = float(json["WIP_DV_V_CamMoveY"]).__round__(5)
		self.Vertical_Background_Anchor_Type = Vertical_Background_Anchor_Enum[json["Vertical_Background_Anchor_Type"]]
		self.WIP_DV_V_ProjMoveY = float(json["WIP_DV_V_ProjMoveY"]).__round__(5)
		self.WIP_DV_V_ProjOffsetY = float(json["WIP_DV_V_ProjOffsetY"]).__round__(5)
		self.Vertical_Background_Position = [
			float(json["Vertical_Background_Position"][0]).__round__(5),
			float(json["Vertical_Background_Position"][1]).__round__(5),
		]
		self.Background_Position = [
			float(json["Background_Position"][0]).__round__(5),
			float(json["Background_Position"][1]).__round__(5),
		]
		self.Edge_Light_Color = [
			float(json["Edge_Light_Color"][0]).__round__(5),
			float(json["Edge_Light_Color"][1]).__round__(5),
			float(json["Edge_Light_Color"][2]).__round__(5),
		]
		self.Enemy_Variant = json["Enemy_Variant"]
		self.Background_Lighting = json["Background_Lighting"]
		self.Vertical_Background_Lighting = json["Vertical_Background_Lighting"]
		self.Lighting = json["Lighting"]
		self.Tileset_Model_Animation_Type = json["Tileset_Model_Animation_Type"]
		self.Tileset_Model = json["Tileset_Model"]
		self.Editor_Grid = [
			float(json["Editor_Grid"][0]).__round__(5),
			float(json["Editor_Grid"][1]).__round__(5),
			float(json["Editor_Grid"][2]).__round__(5),
			float(json["Editor_Grid"][3]).__round__(5),
		]
		return self
	def from_byml_dict(byml: dict) -> Theme:
		self = NSMBU_Theme()
		self.Theme_Name = byml["FieldModel"][9:]
		if (self.Theme_Name[-2:] == "_D"):
			self.Theme_Name = self.Theme_Name[:-2]
			self.Is_Night = True
		self.CustomScroll_Inside = [
			float(byml["CSin_R"]).__round__(5),
			float(byml["CSin_G"]).__round__(5),
			float(byml["CSin_B"]).__round__(5),
			float(byml["CSin_A"]).__round__(5),
		]
		self.CustomScroll_Outside = [
			float(byml["CSout_R"]).__round__(5),
			float(byml["CSout_G"]).__round__(5),
			float(byml["CSout_B"]).__round__(5),
			float(byml["CSout_A"]).__round__(5),
		]
		self.Background_Model = byml["DVModel"]
		self.WIP_DV_CamMoveY = float(byml["DV_CamMoveY"]).__round__(5)
		self.Play_Background_FOV = float(byml["DV_Play_Fovy"]).__round__(5)
		self.WIP_DV_ProjMoveY = float(byml["DV_ProjMoveY"]).__round__(5)
		self.WIP_DV_ProjOffsetY = float(byml["DV_ProjOffsetY"]).__round__(5)
		self.WIP_DV_V_CamMoveY = float(byml["DV_V_CamMoveY"]).__round__(5)
		self.Vertical_Background_Anchor_Type = Vertical_Background_Anchor_Enum(byml["DV_V_OffsetType"])
		self.WIP_DV_V_ProjMoveY = float(byml["DV_V_ProjMoveY"]).__round__(5)
		self.WIP_DV_V_ProjOffsetY = float(byml["DV_V_ProjOffsetY"]).__round__(5)
		self.Vertical_Background_Position = [
			float(byml["DV_V_pos_x"]).__round__(5),
			float(byml["DV_V_pos_y"]).__round__(5),
		]
		self.Background_Position = [
			float(byml["DV_pos_x"]).__round__(5),
			float(byml["DV_pos_y"]).__round__(5),
		]
		self.Edge_Light_Color = [
			float(byml["EdgeLightColor_R"]).__round__(5),
			float(byml["EdgeLightColor_G"]).__round__(5),
			float(byml["EdgeLightColor_B"]).__round__(5),
		]
		self.Enemy_Variant = byml["Enemy"]
		self.Background_Lighting = byml["Env_DV"]
		self.Vertical_Background_Lighting = byml["Env_DV_V"]
		self.Lighting = byml["Env_Model"]
		self.Tileset_Model_Animation_Type = byml["FieldAnime"]
		self.Tileset_Model = byml["FieldModel"]
		self.Editor_Grid = [
			float(byml["Grid_R"]).__round__(5),
			float(byml["Grid_G"]).__round__(5),
			float(byml["Grid_B"]).__round__(5),
			float(byml["Grid_A"]).__round__(5),
		]
		return self
	def as_json_dict(self) -> dict:
		return {
			"Theme_Name": self.Theme_Name,
			"CustomScroll_Inside": self.CustomScroll_Inside,
			"CustomScroll_Outside": self.CustomScroll_Outside,
			"Background_Model": self.Background_Model,
			"WIP_DV_CamMoveY": self.WIP_DV_CamMoveY,
			"Play_Background_FOV": self.Play_Background_FOV,
			"WIP_DV_ProjMoveY": self.WIP_DV_ProjMoveY,
			"WIP_DV_ProjOffsetY": self.WIP_DV_ProjOffsetY,
			"WIP_DV_V_CamMoveY": self.WIP_DV_V_CamMoveY,
			"Vertical_Background_Anchor_Type": self.Vertical_Background_Anchor_Type.name,
			"WIP_DV_V_ProjMoveY": self.WIP_DV_V_ProjMoveY,
			"WIP_DV_V_ProjOffsetY": self.WIP_DV_V_ProjOffsetY,
			"Vertical_Background_Position": self.Vertical_Background_Position,
			"Background_Position": self.Background_Position,
			"Edge_Light_Color": self.Edge_Light_Color,
			"Enemy_Variant": self.Enemy_Variant,
			"Background_Lighting": self.Background_Lighting,
			"Vertical_Background_Lighting": self.Vertical_Background_Lighting,
			"Lighting": self.Lighting,
			"Tileset_Model_Animation_Type": self.Tileset_Model_Animation_Type,
			"Tileset_Model": self.Tileset_Model,
			"Editor_Grid": self.Editor_Grid,
		}
	def as_byml_dict(self) -> dict:
		return {
			"CSin_R": oead.F32(self.CustomScroll_Inside[0]),
			"CSin_G": oead.F32(self.CustomScroll_Inside[1]),
			"CSin_B": oead.F32(self.CustomScroll_Inside[2]),
			"CSin_A": oead.F32(self.CustomScroll_Inside[3]),
			"CSout_R": oead.F32(self.CustomScroll_Outside[0]),
			"CSout_G": oead.F32(self.CustomScroll_Outside[1]),
			"CSout_B": oead.F32(self.CustomScroll_Outside[2]),
			"CSout_A": oead.F32(self.CustomScroll_Outside[3]),
			"DVModel": self.Background_Model,
			"DV_CamMoveY": oead.F32(self.WIP_DV_CamMoveY),
			"DV_Play_Fovy": oead.F32(self.Play_Background_FOV),
			"DV_ProjMoveY": oead.F32(self.WIP_DV_ProjMoveY),
			"DV_ProjOffsetY": oead.F32(self.WIP_DV_ProjOffsetY),
			"DV_V_CamMoveY": oead.F32(self.WIP_DV_V_CamMoveY),
			"DV_V_OffsetType": self.Vertical_Background_Anchor_Type.value,
			"DV_V_ProjMoveY": oead.F32(self.WIP_DV_V_ProjMoveY),
			"DV_V_ProjOffsetY": oead.F32(self.WIP_DV_V_ProjOffsetY),
			"DV_V_pos_x": oead.F32(self.Vertical_Background_Position[0]),
			"DV_V_pos_y": oead.F32(self.Vertical_Background_Position[1]),
			"DV_pos_x": oead.F32(self.Background_Position[0]),
			"DV_pos_y": oead.F32(self.Background_Position[1]),
			"EdgeLightColor_R": oead.F32(self.Edge_Light_Color[0]),
			"EdgeLightColor_G": oead.F32(self.Edge_Light_Color[1]),
			"EdgeLightColor_B": oead.F32(self.Edge_Light_Color[2]),
			"Enemy": self.Enemy_Variant,
			"Env_DV": self.Background_Lighting,
			"Env_DV_V": self.Vertical_Background_Lighting,
			"Env_Model": self.Lighting,
			"FieldAnime": self.Tileset_Model_Animation_Type,
			"FieldModel": self.Tileset_Model,
			"Grid_R": oead.F32(self.Editor_Grid[0]),
			"Grid_G": oead.F32(self.Editor_Grid[1]),
			"Grid_B": oead.F32(self.Editor_Grid[2]),
			"Grid_A": oead.F32(self.Editor_Grid[3]),
		}

class SM3DW_Theme(Theme):
	Style = GameStyle.SM3DW
	CustomScroll_Inside: list[float] # Vec4
	CustomScroll_Outside: list[float] # Vec4
	Background_Model: str
	WIP_DV_CamMoveY: float
	Editor_Background_FOV: float
	Play_Background_FOV: float
	WIP_DV_ProjMoveY: float
	WIP_DV_ProjOffsetY: float
	WIP_DV_ScalePivot: float
	WIP_DV_V_CamMoveY: float
	Vertical_Background_Anchor_Type: Vertical_Background_Anchor_Enum
	WIP_DV_V_ProjMoveY: float
	WIP_DV_V_ProjOffsetY: float
	Background_Lighting: str
	Vertical_Background_Lighting: str
	Lighting: str
	Tileset_Model: str
	Editor_Grid: list[float] # Vec4

	def print(self):
		print(self.Style.name+": "+self.Theme_Name+"\n"
			"> CustomScroll_Inside:			"+str(self.CustomScroll_Inside)+"\n"+
			"> CustomScroll_Outside:			"+str(self.CustomScroll_Outside)+"\n"+
			"> Background_Model:			"+str(self.Background_Model)+"\n"+
			"> WIP_DV_CamMoveY:			"+str(self.WIP_DV_CamMoveY)+"\n"+
			"> Editor_Background_FOV:		"+str(self.Editor_Background_FOV)+"\n"+
			"> Play_Background_FOV:			"+str(self.Play_Background_FOV)+"\n"+
			"> WIP_DV_ProjMoveY:			"+str(self.WIP_DV_ProjMoveY)+"\n"+
			"> WIP_DV_ProjOffsetY:			"+str(self.WIP_DV_ProjOffsetY)+"\n"+
			"> WIP_DV_ScalePivot:			"+str(self.WIP_DV_ScalePivot)+"\n"+
			"> WIP_DV_V_CamMoveY:			"+str(self.WIP_DV_V_CamMoveY)+"\n"+
			"> Vertical_Background_Anchor_Type:	"+str(self.Vertical_Background_Anchor_Type)+"\n"+
			"> WIP_DV_V_ProjMoveY:			"+str(self.WIP_DV_V_ProjMoveY)+"\n"+
			"> WIP_DV_V_ProjOffsetY:			"+str(self.WIP_DV_V_ProjOffsetY)+"\n"+
			"> Background_Lighting:			"+str(self.Background_Lighting)+"\n"+
			"> Vertical_Background_Lighting:		"+str(self.Vertical_Background_Lighting)+"\n"+
			"> Lighting:				"+str(self.Lighting)+"\n"+
			"> Tileset_Model:			"+str(self.Tileset_Model)+"\n"+
			"> Editor_Grid:				"+str(self.Editor_Grid)+"\n"
		)
	def from_json_dict(json: dict) -> Theme:
		self = SM3DW_Theme()
		self.Theme_Name = json["Theme_Name"]
		self.CustomScroll_Inside = [
			float(json["CustomScroll_Inside"][0]).__round__(5),
			float(json["CustomScroll_Inside"][1]).__round__(5),
			float(json["CustomScroll_Inside"][2]).__round__(5),
			float(json["CustomScroll_Inside"][3]).__round__(5),
		]
		self.CustomScroll_Outside = [
			float(json["CustomScroll_Outside"][0]).__round__(5),
			float(json["CustomScroll_Outside"][1]).__round__(5),
			float(json["CustomScroll_Outside"][2]).__round__(5),
			float(json["CustomScroll_Outside"][3]).__round__(5),
		]
		self.Background_Model = json["Background_Model"]
		self.WIP_DV_CamMoveY = float(json["WIP_DV_CamMoveY"]).__round__(5)
		self.Editor_Background_FOV = float(json["Editor_Background_FOV"]).__round__(5)
		self.Play_Background_FOV = float(json["Play_Background_FOV"]).__round__(5)
		self.WIP_DV_ProjMoveY = float(json["WIP_DV_ProjMoveY"]).__round__(5)
		self.WIP_DV_ProjOffsetY = float(json["WIP_DV_ProjOffsetY"]).__round__(5)
		self.WIP_DV_ScalePivot = float(json["WIP_DV_ScalePivot"]).__round__(5)
		self.WIP_DV_V_CamMoveY = float(json["WIP_DV_V_CamMoveY"]).__round__(5)
		self.Vertical_Background_Anchor_Type = Vertical_Background_Anchor_Enum[json["Vertical_Background_Anchor_Type"]]
		self.WIP_DV_V_ProjMoveY = float(json["WIP_DV_V_ProjMoveY"]).__round__(5)
		self.WIP_DV_V_ProjOffsetY = float(json["WIP_DV_V_ProjOffsetY"]).__round__(5)
		self.Background_Lighting = json["Background_Lighting"]
		self.Vertical_Background_Lighting = json["Vertical_Background_Lighting"]
		self.Lighting = json["Lighting"]
		self.Tileset_Model = json["Tileset_Model"]
		self.Editor_Grid = [
			float(json["Editor_Grid"][0]).__round__(5),
			float(json["Editor_Grid"][1]).__round__(5),
			float(json["Editor_Grid"][2]).__round__(5),
			float(json["Editor_Grid"][3]).__round__(5),
		]
		return self
	def from_byml_dict(byml: dict) -> Theme:
		self = SM3DW_Theme()
		self.Theme_Name = byml["FieldModel"][9:]
		if (self.Theme_Name[-2:] == "_D"):
			self.Theme_Name = self.Theme_Name[:-2]
			self.Is_Night = True
		self.CustomScroll_Inside = [
			float(byml["CSin_R"]).__round__(5),
			float(byml["CSin_G"]).__round__(5),
			float(byml["CSin_B"]).__round__(5),
			float(byml["CSin_A"]).__round__(5),
		]
		self.CustomScroll_Outside = [
			float(byml["CSout_R"]).__round__(5),
			float(byml["CSout_G"]).__round__(5),
			float(byml["CSout_B"]).__round__(5),
			float(byml["CSout_A"]).__round__(5),
		]
		self.Background_Model = byml["DVModel"]
		self.WIP_DV_CamMoveY = float(byml["DV_CamMoveY"]).__round__(5)
		self.Editor_Background_FOV = float(byml["DV_Edit_Fovy"]).__round__(5)
		self.Play_Background_FOV = float(byml["DV_Play_Fovy"]).__round__(5)
		self.WIP_DV_ProjMoveY = float(byml["DV_ProjMoveY"]).__round__(5)
		self.WIP_DV_ProjOffsetY = float(byml["DV_ProjOffsetY"]).__round__(5)
		self.WIP_DV_ScalePivot = float(byml["DV_ScalePivot"]).__round__(5)
		self.WIP_DV_V_CamMoveY = float(byml["DV_V_CamMoveY"]).__round__(5)
		self.Vertical_Background_Anchor_Type = Vertical_Background_Anchor_Enum(byml["DV_V_OffsetType"])
		self.WIP_DV_V_ProjMoveY = float(byml["DV_V_ProjMoveY"]).__round__(5)
		self.WIP_DV_V_ProjOffsetY = float(byml["DV_V_ProjOffsetY"]).__round__(5)
		self.Background_Lighting = byml["Env_DV"]
		self.Vertical_Background_Lighting = byml["Env_DV_V"]
		self.Lighting = byml["Env_Model"]
		self.Tileset_Model = byml["FieldModel"]
		self.Editor_Grid = [
			float(byml["Grid_R"]).__round__(5),
			float(byml["Grid_G"]).__round__(5),
			float(byml["Grid_B"]).__round__(5),
			float(byml["Grid_A"]).__round__(5),
		]
		return self
	def as_json_dict(self) -> dict:
		return {
			"Theme_Name": self.Theme_Name,
			"CustomScroll_Inside": self.CustomScroll_Inside,
			"CustomScroll_Outside": self.CustomScroll_Outside,
			"Background_Model": self.Background_Model,
			"WIP_DV_CamMoveY": self.WIP_DV_CamMoveY,
			"Editor_Background_FOV": self.Editor_Background_FOV,
			"Play_Background_FOV": self.Play_Background_FOV,
			"WIP_DV_ProjMoveY": self.WIP_DV_ProjMoveY,
			"WIP_DV_ProjOffsetY": self.WIP_DV_ProjOffsetY,
			"WIP_DV_ScalePivot": self.WIP_DV_ScalePivot,
			"WIP_DV_V_CamMoveY": self.WIP_DV_V_CamMoveY,
			"Vertical_Background_Anchor_Type": self.Vertical_Background_Anchor_Type.name,
			"WIP_DV_V_ProjMoveY": self.WIP_DV_V_ProjMoveY,
			"WIP_DV_V_ProjOffsetY": self.WIP_DV_V_ProjOffsetY,
			"Background_Lighting": self.Background_Lighting,
			"Vertical_Background_Lighting": self.Vertical_Background_Lighting,
			"Lighting": self.Lighting,
			"Tileset_Model": self.Tileset_Model,
			"Editor_Grid": self.Editor_Grid,
		}
	def as_byml_dict(self) -> dict:
		return {
			"CSin_R": oead.F32(self.CustomScroll_Inside[0]),
			"CSin_G": oead.F32(self.CustomScroll_Inside[1]),
			"CSin_B": oead.F32(self.CustomScroll_Inside[2]),
			"CSin_A": oead.F32(self.CustomScroll_Inside[3]),
			"CSout_R": oead.F32(self.CustomScroll_Outside[0]),
			"CSout_G": oead.F32(self.CustomScroll_Outside[1]),
			"CSout_B": oead.F32(self.CustomScroll_Outside[2]),
			"CSout_A": oead.F32(self.CustomScroll_Outside[3]),
			"DVModel": self.Background_Model,
			"DV_CamMoveY": oead.F32(self.WIP_DV_CamMoveY),
			"DV_Edit_Fovy": oead.F32(self.Editor_Background_FOV),
			"DV_Play_Fovy": oead.F32(self.Play_Background_FOV),
			"DV_ProjMoveY": oead.F32(self.WIP_DV_ProjMoveY),
			"DV_ProjOffsetY": oead.F32(self.WIP_DV_ProjOffsetY),
			"DV_ScalePivot": oead.F32(self.WIP_DV_ScalePivot),
			"DV_V_CamMoveY": oead.F32(self.WIP_DV_V_CamMoveY),
			"DV_V_OffsetType": self.Vertical_Background_Anchor_Type.value,
			"DV_V_ProjMoveY": oead.F32(self.WIP_DV_V_ProjMoveY),
			"DV_V_ProjOffsetY": oead.F32(self.WIP_DV_V_ProjOffsetY),
			"Env_DV": self.Background_Lighting,
			"Env_DV_V": self.Vertical_Background_Lighting,
			"Env_Model": self.Lighting,
			"FieldModel": self.Tileset_Model,
			"Grid_R": oead.F32(self.Editor_Grid[0]),
			"Grid_G": oead.F32(self.Editor_Grid[1]),
			"Grid_B": oead.F32(self.Editor_Grid[2]),
			"Grid_A": oead.F32(self.Editor_Grid[3]),
		}

class MyWorld_Theme(Theme):
	Style = GameStyle.MyWorld
	Background_Model: str
	Tileset_Model: str
	Editor_Grid: list[float] # Vec4
	WIP_Mask: list[float] # Vec5
	WIP_NothingAreaAttr: str
	WIP_RoadModel: str

	def print(self):
		print(self.Style.name+": "+self.Theme_Name+"\n"+
			"> Background_Model:			"+str(self.Background_Model)+"\n"+
			"> Tileset_Model:			"+str(self.Tileset_Model)+"\n"+
			"> Editor_Grid:				"+str(self.Editor_Grid)+"\n"+
			"> WIP_Mask:				"+str(self.WIP_Mask)+"\n"+
			"> WIP_NothingAreaAttr:			"+str(self.WIP_NothingAreaAttr)+"\n"+
			"> WIP_RoadModel:			"+str(self.WIP_RoadModel)+"\n"
		)
	def from_json_dict(json: dict) -> Theme:
		self = MyWorld_Theme()
		self.Theme_Name = json["Theme_Name"]
		self.Background_Model = json["Background_Model"]
		self.Tileset_Model = json["Tileset_Model"]
		self.Editor_Grid = [
			float(json["Editor_Grid"][0]).__round__(5),
			float(json["Editor_Grid"][1]).__round__(5),
			float(json["Editor_Grid"][2]).__round__(5),
			float(json["Editor_Grid"][3]).__round__(5),
		]
		self.WIP_Mask = [
			float(json["WIP_Mask"][0]).__round__(5),
			float(json["WIP_Mask"][1]).__round__(5),
			float(json["WIP_Mask"][2]).__round__(5),
			float(json["WIP_Mask"][3]).__round__(5),
			float(json["WIP_Mask"][4]).__round__(5),
		]
		self.WIP_NothingAreaAttr = json["WIP_NothingAreaAttr"]
		self.WIP_RoadModel = json["WIP_RoadModel"]
		return self
	def from_byml_dict(byml: dict) -> Theme:
		self = MyWorld_Theme()
		self.Theme_Name = byml["FieldModel"][14:]
		self.Background_Model = byml["DVModel"]
		self.Tileset_Model = byml["FieldModel"]
		self.Editor_Grid = [
			float(byml["Grid_R"]).__round__(5),
			float(byml["Grid_G"]).__round__(5),
			float(byml["Grid_B"]).__round__(5),
			float(byml["Grid_A"]).__round__(5),
		]
		self.WIP_Mask = [
			float(byml["Mask_R"]).__round__(5),
			float(byml["Mask_G"]).__round__(5),
			float(byml["Mask_B"]).__round__(5),
			float(byml["Mask_A0"]).__round__(5),
			float(byml["Mask_A1"]).__round__(5),
		]
		self.WIP_NothingAreaAttr = byml["NothingAreaAttr"]
		self.WIP_RoadModel = byml["RoadModel"]
		return self
	def as_json_dict(self) -> dict:
		return {
			"Theme_Name": self.Theme_Name,
			"Background_Model": self.Background_Model,
			"Tileset_Model": self.Tileset_Model,
			"Editor_Grid": self.Editor_Grid,
			"WIP_Mask": self.WIP_Mask,
			"WIP_NothingAreaAttr": self.WIP_NothingAreaAttr,
			"WIP_RoadModel": self.WIP_RoadModel,
		}
	def as_byml_dict(self) -> dict:
		return {
			"DVModel": self.Background_Model,
			"FieldModel": self.Tileset_Model,
			"Grid_R": oead.F32(self.Editor_Grid[0]),
			"Grid_G": oead.F32(self.Editor_Grid[1]),
			"Grid_B": oead.F32(self.Editor_Grid[2]),
			"Grid_A": oead.F32(self.Editor_Grid[3]),
			"Mask_R": oead.F32(self.WIP_Mask[0]),
			"Mask_G": oead.F32(self.WIP_Mask[1]),
			"Mask_B": oead.F32(self.WIP_Mask[2]),
			"Mask_A0": oead.F32(self.WIP_Mask[3]),
			"Mask_A1": oead.F32(self.WIP_Mask[4]),
			"NothingAreaAttr": self.WIP_NothingAreaAttr,
			"RoadModel": self.WIP_RoadModel,
		}

