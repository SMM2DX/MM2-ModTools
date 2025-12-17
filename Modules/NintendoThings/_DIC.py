import numpy
from Modules.HelperUtils import print2, print2_in, print2_out, stringAtOffset, bytesFromSpan

class ResourceDictionaryNode():
	RefBit: numpy.uint32
	RightShift: int
	Length: int
	LeftNodeIndex: numpy.uint16
	RightNodeIndex: numpy.uint16
	StringKey: str

	def __init__(self, data: bytes, offset: int):
		self.RefBit = int.from_bytes(bytesFromSpan(data, offset + 0x00, 0x04))
		self.RightShift = self.RefBit >> 30
		self.Length = self.RefBit >> 2
		self.LeftNodeIndex = int.from_bytes(bytesFromSpan(data, offset + 0x04, 0x02))
		self.RightNodeIndex = int.from_bytes(bytesFromSpan(data, offset + 0x06, 0x02))
		self.StringKey = stringAtOffset(data, offset + 0x08)
	def print(self):
		print2("Ref Bit", hex(self.RefBit))
		print2("Right Shift", hex(self.RightShift))
		print2("Length", hex(self.Length))
		print2("Left Node Index", hex(self.LeftNodeIndex))
		print2("Right Node Index", hex(self.RightNodeIndex))
		print2("String Key", str(self.StringKey.encode()))

class ResourceDictionary():
	Magic: str
	NodeCount: numpy.uint32
	Nodes: list[ResourceDictionaryNode]

	def __init__(self, data: bytes, offset: int):
		self.Magic = bytesFromSpan(data, offset + 0x00, 0x04)[::-1].decode()
		self.NodeCount = int.from_bytes(bytesFromSpan(data, offset + 0x04, 0x04))+1
		self.Nodes = list()
		for i in range(self.NodeCount):
			self.Nodes.append(ResourceDictionaryNode(data, offset + 0x08 + i * 0x10))
	def print(self):
		print2("Magic", self.Magic)
		print2("NodeCount", str(self.NodeCount))
		print2("Nodes")
		print2_in()
		for x in self.Nodes:
			x.print()
		print2_out()
