import numpy
from math import ceil
from Modules.HelperUtils import print2, print2_in, print2_out, stringAtOffset, bytesFromSpan
from Modules.NintendoThings.BinaryBlock import BinaryBlock

class StringPool(BinaryBlock):
	StringCount: numpy.uint32
	Strings: list[str]

	def __init__(self, data: bytes, offset: int):
		super().__init__(data, offset)
		self.StringCount = int.from_bytes(bytesFromSpan(data, offset + 0x0C, 0x04))
		self.Strings = list()
		curOff = 0x18
		for i in range(self.StringCount):
			stringLength = int.from_bytes(bytesFromSpan(data, offset + curOff, 0x02))
			self.Strings.append(stringAtOffset(data, offset + curOff + 0x02))
			curOff += stringLength + 0x03
			curOff = 2 * ceil(curOff/2)

	def print(self):
		super().print()
		print2("String Count:			"+str(self.StringCount))
		print2("Strings:")
		print2_in()
		for i in range(self.StringCount):
			print2("		"+self.Strings[i])
		print2_out()
