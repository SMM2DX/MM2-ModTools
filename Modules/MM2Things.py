from enum import Enum

class GameStyle(Enum):
	Unknown	= '??'
	MyWorld	= 'MyWorld'
	SMB1	= 'M1'
	SMB3	= 'M3'
	SMW		= 'MW'
	NSMBU	= 'WU'
	SM3DW	= '3W'

class Theme():
	Style: GameStyle = GameStyle.Unknown
	Theme_Name: str
	def print(self):
		pass
	def from_json_dict(dict):
		pass
	def from_byml_dict(dict):
		pass
	def as_json_dict(self) -> dict:
		pass
	def as_byml_dict(self) -> dict:
		pass

class MyWorld_Theme(Theme):
	Style = GameStyle.MyWorld
	Background_Model: str
	Tileset_Model: str
	Editor_Grid: list[float] # Vec4
	WIP_Mask: list[float] # Vec5
	WIP_NothingAreaAttr: str
	WIP_RoadModel: str

	def print(self):
		print(self.Style.name+": "+self.Theme_Name+"\n"
			"> Background_Model:			"+str(self.Background_Model)+"\n"+
			"> Tileset_Model:			"+str(self.Tileset_Model)+"\n"+
			"> Editor_Grid:				"+str(self.Editor_Grid)+"\n"+
			"> WIP_Mask:				"+str(self.WIP_Mask)+"\n"+
			"> WIP_NothingAreaAttr:			"+str(self.WIP_NothingAreaAttr)+"\n"+
			"> WIP_RoadModel:			"+str(self.WIP_RoadModel)+"\n"
		)
	def from_json_dict(dict):
		self = MyWorld_Theme()
		return self
	def from_byml_dict(dict):
		self = MyWorld_Theme()
		self.Theme_Name = dict["FieldModel"][14:]
		self.Background_Model = dict["DVModel"]
		self.Tileset_Model = dict["FieldModel"]
		self.Editor_Grid = [
			float(dict["Grid_R"]).__round__(5),
			float(dict["Grid_G"]).__round__(5),
			float(dict["Grid_B"]).__round__(5),
			float(dict["Grid_A"]).__round__(5),
		]
		self.WIP_Mask = [
			float(dict["Mask_R"]).__round__(5),
			float(dict["Mask_G"]).__round__(5),
			float(dict["Mask_B"]).__round__(5),
			float(dict["Mask_A0"]).__round__(5),
			float(dict["Mask_A1"]).__round__(5),
		]
		self.WIP_NothingAreaAttr = dict["NothingAreaAttr"]
		self.WIP_RoadModel = dict["RoadModel"]
		return self
	def as_json_dict(self) -> dict:
		pass
	def as_byml_dict(self) -> dict:
		pass

class SMB1_Theme(Theme):
	Style = GameStyle.SMB1
	Tileset_Model: str
	Lighting: str
	Background_Model: str
	Background_Lighting: str
	Vertical_Background_Lighting: str
	Vertical_Background_Anchor_Type: str
	CustomScroll_Inside: list[float] # Vec4
	CustomScroll_Outside: list[float] # Vec4
	Editor_Grid: list[float] # Vec4
	Tileset_Model_Animation_Type: str
	Enemy_Variant: str
	Shadow_Color: list[float] # Vec4
	Shadow_Offset: float

	def print(self):
		print(self.Style.name+": "+self.Theme_Name+"\n"
			"> Background_Model:			"+str(self.Background_Model)+"\n"+
			"> Tileset_Model:			"+str(self.Tileset_Model)+"\n"+
			"> Editor_Grid:				"+str(self.Editor_Grid)+"\n"
		)
	def from_json_dict(dict):
		self = SMB1_Theme()
		return self
	def from_byml_dict(dict):
		self = SMB1_Theme()
		self.Theme_Name = dict["FieldModel"][9:]
		self.Background_Model = dict["DVModel"]
		self.Tileset_Model = dict["FieldModel"]
		self.Editor_Grid = [
			float(dict["Grid_R"]).__round__(5),
			float(dict["Grid_G"]).__round__(5),
			float(dict["Grid_B"]).__round__(5),
			float(dict["Grid_A"]).__round__(5),
		]
		return self
	def as_json_dict(self) -> dict:
		pass
	def as_byml_dict(self) -> dict:
		pass

class SMB3_Theme(Theme):
	Style = GameStyle.SMB3
	Tileset_Model: str
	Lighting: str
	Background_Model: str
	Background_Lighting: str
	Vertical_Background_Lighting: str
	Vertical_Background_Anchor_Type: str
	CustomScroll_Inside: list[float] # Vec4
	CustomScroll_Outside: list[float] # Vec4
	Editor_Grid: list[float] # Vec4
	Tileset_Model_Animation_Type: str
	Enemy_Variant: str
	Shadow_Color: list[float] # Vec4
	Shadow_Offset: float

	def print(self):
		print(self.Style.name+": "+self.Theme_Name+"\n"
			"> Background_Model:			"+str(self.Background_Model)+"\n"+
			"> Tileset_Model:			"+str(self.Tileset_Model)+"\n"+
			"> Editor_Grid:				"+str(self.Editor_Grid)+"\n"
		)
	def from_json_dict(dict):
		self = SMB3_Theme()
		return self
	def from_byml_dict(dict):
		self = SMB3_Theme()
		self.Theme_Name = dict["FieldModel"][9:]
		self.Background_Model = dict["DVModel"]
		self.Tileset_Model = dict["FieldModel"]
		self.Editor_Grid = [
			float(dict["Grid_R"]).__round__(5),
			float(dict["Grid_G"]).__round__(5),
			float(dict["Grid_B"]).__round__(5),
			float(dict["Grid_A"]).__round__(5),
		]
		return self
	def as_json_dict(self) -> dict:
		pass
	def as_byml_dict(self) -> dict:
		pass

class SMW_Theme(Theme):
	Style = GameStyle.SMW
	Tileset_Model: str
	Lighting: str
	Background_Model: str
	Background_Lighting: str
	Vertical_Background_Lighting: str
	Vertical_Background_Anchor_Type: str
	CustomScroll_Inside: list[float] # Vec4
	CustomScroll_Outside: list[float] # Vec4
	Editor_Grid: list[float] # Vec4
	Tileset_Model_Animation_Type: str
	Enemy_Variant: str
	Shadow_Color: list[float] # Vec4
	Shadow_Offset: float

	def print(self):
		print(self.Style.name+": "+self.Theme_Name+"\n"
			"> Background_Model:			"+str(self.Background_Model)+"\n"+
			"> Tileset_Model:			"+str(self.Tileset_Model)+"\n"+
			"> Editor_Grid:				"+str(self.Editor_Grid)+"\n"
		)
	def from_json_dict(dict):
		self = SMW_Theme()
		return self
	def from_byml_dict(dict):
		self = SMW_Theme()
		self.Theme_Name = dict["FieldModel"][9:]
		self.Background_Model = dict["DVModel"]
		self.Tileset_Model = dict["FieldModel"]
		self.Editor_Grid = [
			float(dict["Grid_R"]).__round__(5),
			float(dict["Grid_G"]).__round__(5),
			float(dict["Grid_B"]).__round__(5),
			float(dict["Grid_A"]).__round__(5),
		]
		return self
	def as_json_dict(self) -> dict:
		pass
	def as_byml_dict(self) -> dict:
		pass

class NSMBU_Theme(Theme):
	Style = GameStyle.NSMBU
	Tileset_Model: str
	Lighting: str
	Background_Model: str
	Background_Lighting: str
	Vertical_Background_Lighting: str
	Vertical_Background_Anchor_Type: str
	CustomScroll_Inside: list[float] # Vec4
	CustomScroll_Outside: list[float] # Vec4
	Editor_Grid: list[float] # Vec4
	Tileset_Model_Animation_Type: str
	Enemy_Variant: str
	Edge_Light_color: list[float] # Vec3
	Background_Position: list[float] # Vec2
	Vertical_Background_Position: list[float] # Vec2
	WIP_DV_CamMoveY: float
	WIP_DV_ProjMoveY: float
	WIP_DV_ProjOffsetY: float
	WIP_DV_V_CamMoveY: float
	WIP_DV_V_ProjMoveY: float
	WIP_DV_V_ProjOffsetY: float
	Play_Background_FOV: float

	def print(self):
		print(self.Style.name+": "+self.Theme_Name+"\n"
			"> Background_Model:			"+str(self.Background_Model)+"\n"+
			"> Tileset_Model:			"+str(self.Tileset_Model)+"\n"+
			"> Editor_Grid:				"+str(self.Editor_Grid)+"\n"
		)
	def from_json_dict(dict):
		self = NSMBU_Theme()
		return self
	def from_byml_dict(dict):
		self = NSMBU_Theme()
		self.Theme_Name = dict["FieldModel"][9:]
		self.Background_Model = dict["DVModel"]
		self.Tileset_Model = dict["FieldModel"]
		self.Editor_Grid = [
			float(dict["Grid_R"]).__round__(5),
			float(dict["Grid_G"]).__round__(5),
			float(dict["Grid_B"]).__round__(5),
			float(dict["Grid_A"]).__round__(5),
		]
		return self
	def as_json_dict(self) -> dict:
		pass
	def as_byml_dict(self) -> dict:
		pass

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
	Vertical_Background_Anchor_Type: str
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
	def from_json_dict(dict):
		self = SM3DW_Theme()
		return self
	def from_byml_dict(dict):
		self = SM3DW_Theme()
		self.Theme_Name = dict["FieldModel"][9:]
		self.CustomScroll_Inside = [
			float(dict["CSin_R"]).__round__(5),
			float(dict["CSin_G"]).__round__(5),
			float(dict["CSin_B"]).__round__(5),
			float(dict["CSin_A"]).__round__(5),
		]
		self.CustomScroll_Outside = [
			float(dict["CSout_R"]).__round__(5),
			float(dict["CSout_G"]).__round__(5),
			float(dict["CSout_B"]).__round__(5),
			float(dict["CSout_A"]).__round__(5),
		]
		self.Background_Model = dict["DVModel"]
		self.WIP_DV_CamMoveY = float(dict["DV_CamMoveY"]).__round__(5)
		self.Editor_Background_FOV = float(dict["DV_Edit_Fovy"]).__round__(5)
		self.Play_Background_FOV = float(dict["DV_Play_Fovy"]).__round__(5)
		self.WIP_DV_ProjMoveY = float(dict["DV_ProjMoveY"]).__round__(5)
		self.WIP_DV_ProjOffsetY = float(dict["DV_ProjOffsetY"]).__round__(5)
		self.WIP_DV_ScalePivot = float(dict["DV_ScalePivot"]).__round__(5)
		self.WIP_DV_V_CamMoveY = float(dict["DV_V_CamMoveY"]).__round__(5)
		self.Vertical_Background_Anchor_Type = "Top" if (dict["DV_V_OffsetType"] == "上基準") else "Bottom"
		self.WIP_DV_V_ProjMoveY = float(dict["DV_V_ProjMoveY"]).__round__(5)
		self.WIP_DV_V_ProjOffsetY = float(dict["DV_V_ProjOffsetY"]).__round__(5)
		self.Background_Lighting = dict["Env_DV"]
		self.Vertical_Background_Lighting = dict["Env_DV_V"]
		self.Lighting = dict["Env_Model"]
		self.Tileset_Model = dict["FieldModel"]
		self.Editor_Grid = [
			float(dict["Grid_R"]).__round__(5),
			float(dict["Grid_G"]).__round__(5),
			float(dict["Grid_B"]).__round__(5),
			float(dict["Grid_A"]).__round__(5),
		]
		return self
	def as_json_dict(self) -> dict:
		pass
	def as_byml_dict(self) -> dict:
		pass

