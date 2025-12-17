import numpy
from Modules.HelperUtils import print2, print2_in, print2_out, stringAtOffset, bytesFromSpan
from Modules.NintendoThings._DIC import ResourceDictionary

class ResVertexBufferStride():
	Stride: numpy.uint32
	Divisor: numpy.uint32
	Unknown1: numpy.uint32
	Unknown2: numpy.uint16

	def __init__(self, data: bytes, offset: int):
		self.Stride = int.from_bytes(bytesFromSpan(data, offset+0x00, 0x04))
		self.Divisor = int.from_bytes(bytesFromSpan(data, offset+0x04, 0x04))
		self.Unknown1 = int.from_bytes(bytesFromSpan(data, offset+0x08, 0x04))
		self.Unknown2 = int.from_bytes(bytesFromSpan(data, offset+0x0C, 0x04))
	def print(self):
		print2("Stride", hex(self.Stride))
		print2("Divisor", hex(self.Divisor))
		print2("Unknown1", hex(self.Unknown1))
		print2("Unknown2", hex(self.Unknown2))

class ResVertexAttribute():
	AttributeName: str
	AttributeFormat: numpy.uint32
	BufferOffset: numpy.uint16
	BufferIndex: numpy.uint8
	Dynamic: numpy.uint8

	def __init__(self, data: bytes, offset: int):
		self.AttributeName = stringAtOffset(data, int.from_bytes(bytesFromSpan(data, offset+0x00, 0x08))+0x02)
		self.AttributeFormat = int.from_bytes(bytesFromSpan(data, offset+0x08, 0x04))
		self.BufferOffset = int.from_bytes(bytesFromSpan(data, offset+0x0C, 0x02))
		self.BufferIndex = int.from_bytes(bytesFromSpan(data, offset+0x0E, 0x01))
		self.Dynamic = int.from_bytes(bytesFromSpan(data, offset+0x0F, 0x01))
	def print(self):
		print2("Attribute Name", self.AttributeName)
		print2("Attribute Format", hex(self.AttributeFormat))
		print2("Buffer Offset", hex(self.BufferOffset))
		print2("Buffer Index", hex(self.BufferIndex))
		print2("Dynamic?", hex(self.Dynamic))

class ResVertex():
	Magic: str
	Unknown1: numpy.uint32
	VertexAttributeArray: ResVertexAttribute = None
	VertexAttributeDictionary: ResourceDictionary = None
	RuntimeMemoryPoolPointer = None # TODO
	RuntimeVertexBufferArray = None # TODO
	RuntimeUserVertexBufferArray = None # TODO
	VertexBufferInfoArray = None # TODO
	VertexBufferStrideArray: ResVertexBufferStride = None
	RuntimeUserPointer = None # TODO
	VertexDataOffset: numpy.uint32
	VertexAttributeCount: numpy.uint8
	VertexBufferCount: numpy.uint8
	Index: numpy.uint16
	VertexCount: numpy.uint32
	Unknown2: numpy.uint16
	VertexBufferAlignment: numpy.uint16

	def __init__(self, data: bytes, offset: int):
		self.Magic = bytesFromSpan(data, offset+0x00, 0x04)[::-1].decode()
		self.Unknown1 = int.from_bytes(bytesFromSpan(data, offset+0x04, 0x04))
		tempPointer = int.from_bytes(bytesFromSpan(data, offset+0x08, 0x08))
		if not tempPointer == 0: self.VertexAttributeArray = ResVertexAttribute(data, tempPointer)
		tempPointer = int.from_bytes(bytesFromSpan(data, offset+0x10, 0x08))
		if not tempPointer == 0: self.VertexAttributeDictionary = ResourceDictionary(data, tempPointer)
		tempPointer = int.from_bytes(bytesFromSpan(data, offset+0x38, 0x08))
		if not tempPointer == 0: self.VertexBufferStrideArray = ResVertexBufferStride(data, tempPointer)
		
		self.VertexDataOffset = int.from_bytes(bytesFromSpan(data, offset+0x48, 0x04))
		self.VertexAttributeCount = int.from_bytes(bytesFromSpan(data, offset+0x4C, 0x01))
		self.VertexBufferCount = int.from_bytes(bytesFromSpan(data, offset+0x4D, 0x01))
		self.Index = int.from_bytes(bytesFromSpan(data, offset+0x4E, 0x02))
		self.VertexCount = int.from_bytes(bytesFromSpan(data, offset+0x50, 0x04))
		self.Unknown2 = int.from_bytes(bytesFromSpan(data, offset+0x54, 0x02))
		self.VertexBufferAlignment = int.from_bytes(bytesFromSpan(data, offset+0x56, 0x02))
	def print(self):
		print2("Magic", self.Magic)
		print2("Unknown1", hex(self.Unknown1))
		if self.VertexAttributeArray: 
			print2("Vertex Attribute Array")
			print2_in()
			self.VertexAttributeArray.print()
			print2_out()
		if self.VertexAttributeDictionary: 
			print2("Vertex Attribute Dictionary")
			print2_in()
			self.VertexAttributeDictionary.print()
			print2_out()
		if self.VertexBufferStrideArray: 
			print2("Vertex Buffer Stride Array")
			print2_in()
			self.VertexBufferStrideArray.print()
			print2_out()
		print2("Vertex Data Offset", hex(self.VertexDataOffset))
		print2("Vertex Attribute Count", hex(self.VertexAttributeCount))
		print2("Vertex Buffer Count", hex(self.VertexBufferCount))
		print2("Index", hex(self.Index))
		print2("Vertex Count", hex(self.VertexCount))
		print2("Unknown2", hex(self.Unknown2))
		print2("Vertex Buffer Alignment", hex(self.VertexBufferAlignment))