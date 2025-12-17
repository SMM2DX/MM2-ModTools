import numpy
from Modules.HelperUtils import print2, print2_in, print2_out, stringAtOffset, bytesFromSpan
from Modules.NintendoThings._DIC import ResourceDictionary
from Modules.NintendoThings.FVTX import ResVertex

class ResModel():
	Magic: str
	Unknown1: numpy.uint32
	ModelName: str
	Unknown2: str
	Skeleton = None # TODO
	VertexArray: ResVertex = None
	ShapeArray = None # TODO
	ShapeDictionary: ResourceDictionary = None
	MaterialArray = None # TODO
	MaterialDictionary: ResourceDictionary = None
	ShaderReflectionArray = None # TODO
	UserDataArray = None # TODO
	UserDataDictionary: ResourceDictionary = None
	RuntimeUserPointer = None # TODO
	VertexCount: numpy.uint16
	ShapeCount: numpy.uint16
	MaterialCount: numpy.uint16
	ShaderReflectionCount: numpy.uint16
	UserDataCount: numpy.uint16

	def __init__(self, data: bytes, offset: int):
		self.Magic = bytesFromSpan(data, offset+0x00, 0x04)[::-1].decode()
		self.Unknown1 = int.from_bytes(bytesFromSpan(data, offset+0x04, 0x04))
		self.ModelName = stringAtOffset(data, int.from_bytes(bytesFromSpan(data, offset+0x08, 0x08))+0x02)
		self.Unknown2 = stringAtOffset(data, int.from_bytes(bytesFromSpan(data, offset+0x10, 0x08))+0x02)
		tempPointer = int.from_bytes(bytesFromSpan(data, offset+0x20, 0x08))
		if not tempPointer == 0: self.VertexArray = ResVertex(data, tempPointer)
		tempPointer = int.from_bytes(bytesFromSpan(data, offset+0x30, 0x08))
		if not tempPointer == 0: self.ShapeDictionary = ResourceDictionary(data, tempPointer)
		tempPointer = int.from_bytes(bytesFromSpan(data, offset+0x40, 0x08))
		if not tempPointer == 0: self.MaterialDictionary = ResourceDictionary(data, tempPointer)
		tempPointer = int.from_bytes(bytesFromSpan(data, offset+0x58, 0x08))
		if not tempPointer == 0: self.UserDataDictionary = ResourceDictionary(data, tempPointer)
		self.VertexCount = int.from_bytes(bytesFromSpan(data, offset+0x68, 0x02))
		self.ShapeCount = int.from_bytes(bytesFromSpan(data, offset+0x6A, 0x02))
		self.MaterialCount = int.from_bytes(bytesFromSpan(data, offset+0x6C, 0x02))
		self.ShaderReflectionCount = int.from_bytes(bytesFromSpan(data, offset+0x6E, 0x02))
		self.UserDataCount = int.from_bytes(bytesFromSpan(data, offset+0x70, 0x02))
	def print(self):
		print2("Magic", self.Magic)
		print2("Unknown1", hex(self.Unknown1))
		print2("Model Name", self.ModelName)
		print2("Unknown2", self.Unknown2)
		if self.VertexArray:
			print2("Vertex Array")
			print2_in()
			self.VertexArray.print()
			print2_out()
		if self.ShapeDictionary:
			print2("Shape Dictionary")
			print2_in()
			self.ShapeDictionary.print()
			print2_out()
		if self.MaterialDictionary:
			print2("Material Dictionary")
			print2_in()
			self.MaterialDictionary.print()
			print2_out()
		if self.UserDataDictionary:
			print2("User Data Dictionary")
			print2_in()
			self.UserDataDictionary.print()
			print2_out()
		print2("Vertex Count", hex(self.VertexCount))
		print2("Shape Count", hex(self.ShapeCount))
		print2("Material Count", hex(self.MaterialCount))
		print2("Shader Reflection Count", hex(self.ShaderReflectionCount))
		print2("User Data Count", hex(self.UserDataCount))