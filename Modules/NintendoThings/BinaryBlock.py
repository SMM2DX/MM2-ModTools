import numpy
from Modules.HelperUtils import print2, print2_in, print2_out, stringAtOffset, bytesFromSpan

class BinaryBlock():
	Magic: str
	NextBinaryBlockOffset: numpy.uint32
	Size: numpy.uint32

	def __init__(self, data: bytes, offset: int):
		self.Magic = bytesFromSpan(data, offset+0x00, 0x04)[::-1].decode()
		self.NextBinaryBlockOffset = int.from_bytes(bytesFromSpan(data, offset+0x04, 0x04))
		self.Size = int.from_bytes(bytesFromSpan(data, offset+0x08, 0x04))
	def print(self):
		print2("Magic", self.Magic)
		print2("Next Binary Block Offset", hex(self.NextBinaryBlockOffset))
		print2("Size", hex(self.Size))