import numpy
from Modules.HelperUtils import print2, print2_in, print2_out, stringAtOffset, bytesFromSpan
from Modules.NintendoThings._DIC import ResourceDictionary
from Modules.NintendoThings._RLT import RelocationTable
from Modules.NintendoThings._STR import StringPool
from Modules.NintendoThings.BinaryBlock import BinaryBlock
from Modules.NintendoThings.BinaryFile import BinaryFile
from Modules.NintendoThings.FMDL import ResModel

def BinaryBlockHelper(data: bytes, offset: int):
	if bytesFromSpan(data, offset, 0x04).decode() == "_STR":
		return StringPool(data, offset)
	else:
		return BinaryBlock(data, offset)

class BinaryFileResource(BinaryFile):
	FileName: str
	ModelArray: ResModel = None
	ModelDictionary: ResourceDictionary = None
	SkeletalAnimationArray = None # TODO
	SkeletalAnimationDictionary: ResourceDictionary = None
	MaterialAnimationArray = None # TODO
	MaterialAnimationDictionary: ResourceDictionary = None
	BoneVisibilityAnimationArray = None # TODO
	BoneVisibilityAnimationDictionary: ResourceDictionary = None
	ShapeAnimationArray = None # TODO
	ShapeAnimationDictionary: ResourceDictionary = None
	SceneAnimationArray = None # TODO
	SceneAnimationDictionary: ResourceDictionary = None
	RuntimeMemoryPool = None # TODO
	MemoryPoolInfo = None # TODO
	EmbeddedFileArray = None # TODO
	EmbeddedFileDictionary: ResourceDictionary = None
	UserPointer = None # TODO
	Unknown2: str
	Unknown3: numpy.uint32
	ModelArrayCount: numpy.uint16
	Unknown4: numpy.uint16
	Unknown5: numpy.uint16
	SkeletalAnimationArrayCount: numpy.uint16
	MaterialAnimationArrayCount: numpy.uint16
	BoneVisibilityAnimationArrayCount: numpy.uint16
	ShapeAnimationArrayCount: numpy.uint16
	SceneAnimationArrayCount: numpy.uint16
	EmbeddedFileArrayCount: numpy.uint16
	Unknown6: numpy.uint16

	def __init__(self, data: bytes):
		super().__init__(data)
		self.FileName = stringAtOffset(data, int.from_bytes(bytesFromSpan(data, 0x20, 0x08))+0x02)
		tempPointer = int.from_bytes(bytesFromSpan(data, 0x28, 0x08))
		if not tempPointer == 0: self.ModelArray = ResModel(data, tempPointer)
		tempPointer = int.from_bytes(bytesFromSpan(data, 0x30, 0x08))
		if not tempPointer == 0: self.ModelDictionary = ResourceDictionary(data, tempPointer)
		tempPointer = int.from_bytes(bytesFromSpan(data, 0x60, 0x08))
		if not tempPointer == 0: self.SkeletalAnimationDictionary = ResourceDictionary(data, tempPointer)
		tempPointer = int.from_bytes(bytesFromSpan(data, 0x70, 0x08))
		if not tempPointer == 0: self.MaterialAnimationDictionary = ResourceDictionary(data, tempPointer)
		tempPointer = int.from_bytes(bytesFromSpan(data, 0x80, 0x08))
		if not tempPointer == 0: self.BoneVisibilityAnimationDictionary = ResourceDictionary(data, tempPointer)
		tempPointer = int.from_bytes(bytesFromSpan(data, 0x90, 0x08))
		if not tempPointer == 0: self.ShapeAnimationDictionary = ResourceDictionary(data, tempPointer)
		tempPointer = int.from_bytes(bytesFromSpan(data, 0xA0, 0x08))
		if not tempPointer == 0: self.SceneAnimationDictionary = ResourceDictionary(data, tempPointer)
		tempPointer = int.from_bytes(bytesFromSpan(data, 0xC0, 0x08))
		if not tempPointer == 0: self.EmbeddedFileDictionary = ResourceDictionary(data, tempPointer)
		
		self.Unknown2 = stringAtOffset(data, int.from_bytes(bytesFromSpan(data, 0xD0, 0x08))+0x02)
		self.Unknown3 = int.from_bytes(bytesFromSpan(data, 0xD8, 0x04))
		self.ModelArrayCount = int.from_bytes(bytesFromSpan(data, 0xDC, 0x02))
		self.Unknown4 = int.from_bytes(bytesFromSpan(data, 0xDE, 0x02))
		self.Unknown5 = int.from_bytes(bytesFromSpan(data, 0xE0, 0x02))
		self.SkeletalAnimationArrayCount = int.from_bytes(bytesFromSpan(data, 0xE2, 0x02))
		self.MaterialAnimationArrayCount = int.from_bytes(bytesFromSpan(data, 0xE4, 0x02))
		self.BoneVisibilityAnimationArrayCount = int.from_bytes(bytesFromSpan(data, 0xE6, 0x02))
		self.ShapeAnimationArrayCount = int.from_bytes(bytesFromSpan(data, 0xE8, 0x02))
		self.SceneAnimationArrayCount = int.from_bytes(bytesFromSpan(data, 0xEA, 0x02))
		self.EmbeddedFileArrayCount = int.from_bytes(bytesFromSpan(data, 0xEC, 0x02))
		self.Unknown6 = int.from_bytes(bytesFromSpan(data, 0xEE, 0x02))
	def print(self):
		super().print()
		print2("File Name", self.FileName)
		if self.ModelArray: 
			print2("Model Array")
			print2_in()
			self.ModelArray.print()
			print2_out()
		if self.ModelDictionary: 
			print2("Model Dictionary")
			print2_in()
			self.ModelDictionary.print()
			print2_out()
		if self.SkeletalAnimationDictionary:
			print2("Skeletal Animation Dictionary")
			print2_in()
			self.SkeletalAnimationDictionary.print()
			print2_out()
		if self.MaterialAnimationDictionary:
			print2("Material Animation Dictionary")
			print2_in()
			self.MaterialAnimationDictionary.print()
			print2_out()
		if self.BoneVisibilityAnimationDictionary:
			print2("Bone Visibility Animation Dictionary")
			print2_in()
			self.BoneVisibilityAnimationDictionary.print()
			print2_out()
		if self.ShapeAnimationDictionary:
			print2("Shape Animation Dictionary")
			print2_in()
			self.ShapeAnimationDictionary.print()
			print2_out()
		if self.SceneAnimationDictionary:
			print2("Scene Animation Dictionary")
			print2_in()
			self.SceneAnimationDictionary.print()
			print2_out()
		if self.EmbeddedFileDictionary:
			print2("Embedded File Dictionary")
			print2_in()
			self.EmbeddedFileDictionary.print()
			print2_out()

		print2("Unknown2", self.Unknown2)
		print2("Unknown3", hex(self.Unknown3))
		print2("ModelArrayCount", hex(self.ModelArrayCount))
		print2("Unknown4", hex(self.Unknown4))
		print2("Unknown5", hex(self.Unknown5))
		print2("SkeletalAnimationArrayCount", hex(self.SkeletalAnimationArrayCount))
		print2("MaterialAnimationArrayCount", hex(self.MaterialAnimationArrayCount))
		print2("BoneVisibilityAnimationArrayCount", hex(self.BoneVisibilityAnimationArrayCount))
		print2("ShapeAnimationArrayCount", hex(self.ShapeAnimationArrayCount))
		print2("SceneAnimationArrayCount", hex(self.SceneAnimationArrayCount))
		print2("EmbeddedFileArrayCount", hex(self.EmbeddedFileArrayCount))
		print2("Unknown6", hex(self.Unknown6))

