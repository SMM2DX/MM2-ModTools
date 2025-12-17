import numpy
from Modules.HelperUtils import print2, print2_in, print2_out, stringAtOffset, bytesFromSpan

class RelocationTableEntry():
	FileRegionOffset: numpy.uint32
	ArrayCount: numpy.uint16
	PerArrayPointerCount: numpy.uint8
	ArrayStride: numpy.uint8

	def __init__(self, data: bytes, offset: int):
		self.FileRegionOffset = int.from_bytes(bytesFromSpan(data, offset + 0x00, 0x04))
		self.ArrayCount = int.from_bytes(bytesFromSpan(data, offset + 0x04, 0x02))
		self.PerArrayPointerCount = int.from_bytes(bytesFromSpan(data, offset + 0x06, 0x01))
		self.ArrayStride = int.from_bytes(bytesFromSpan(data, offset + 0x07, 0x01))
	def print(self):
		print2("File Region Offset", hex(self.FileRegionOffset))
		print2("Array Count", str(self.ArrayCount))
		print2("Per Array Pointer Count", hex(self.PerArrayPointerCount))
		print2("Array Stride", hex(self.ArrayStride))

class RelocationTableSection():
	Base: numpy.uint64
	FileRegionOffset: numpy.uint32
	FileRegionSize: numpy.uint32
	BaseEntryIndex: numpy.uint32
	EntryCount: numpy.uint32
	Entries: list[RelocationTableEntry]

	def __init__(self, data: bytes, offset: int, entriesOffset: int):
		self.Base = int.from_bytes(bytesFromSpan(data, offset + 0x00, 0x08))
		self.FileRegionOffset = int.from_bytes(bytesFromSpan(data, offset + 0x08, 0x04))
		self.FileRegionSize = int.from_bytes(bytesFromSpan(data, offset + 0x0C, 0x04))
		self.BaseEntryIndex = int.from_bytes(bytesFromSpan(data, offset + 0x10, 0x04))
		self.EntryCount = int.from_bytes(bytesFromSpan(data, offset + 0x14, 0x04))
		self.Entries = list()
		for i in range(self.EntryCount):
			self.Entries.append(RelocationTableEntry(data, entriesOffset + i * 0x08))
	def print(self):
		print2("Base", hex(self.Base))
		print2("File Region Offset", hex(self.FileRegionOffset))
		print2("File Region Size", hex(self.FileRegionSize))
		print2("Base Entry Index", hex(self.BaseEntryIndex))
		print2("Entry Count", str(self.EntryCount))
		print2("Entries")
		print2_in()
		for x in self.Entries:
			x.print()
		print2_out()

class RelocationTable():
	Magic: str
	OffsetFromHeader: numpy.uint32
	SectionCount: numpy.uint32
	Sections: list[RelocationTableSection]

	def __init__(self, data: bytes, offset: int):
		self.Magic = bytesFromSpan(data, offset + 0x00, 0x04)[::-1].decode()
		self.OffsetFromHeader = int.from_bytes(bytesFromSpan(data, offset + 0x04, 0x04))
		self.SectionCount = int.from_bytes(bytesFromSpan(data, offset + 0x08, 0x04))
		self.Sections = list()
		for i in range(self.SectionCount):
			self.Sections.append(RelocationTableSection(data, 0x10 + i * 0x18, 0x10 + self.SectionCount * 0x18))
	def print(self):
		print2("Magic", self.Magic)
		print2("Offset From Header", hex(self.OffsetFromHeader))
		print2("Section Count", str(self.SectionCount))
		print2("Sections")
		print2_in()
		for x in self.Sections:
			x.print()
		print2_out()
