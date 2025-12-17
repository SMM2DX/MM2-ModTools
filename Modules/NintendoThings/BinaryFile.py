import numpy
from Modules.HelperUtils import print2, print2_in, print2_out, stringAtOffset, bytesFromSpan

class BinaryFile():
	Magic: str
	Version: str
	ByteOrderMark: numpy.uint16
	Alignment: numpy.uint64
	Unknown1: numpy.uint8
	FileNameOffset: numpy.uint32
	IsRelocated: numpy.uint16
	BinaryBlockOffset: numpy.uint16
	RelocationTableOffset: numpy.uint32
	FileSize: numpy.uint32

	def __init__(self, data: bytes):
		self.Magic = bytesFromSpan(data, 0x00, 0x08)[::-1].decode()
		self.Version = "v"+str(int.from_bytes(bytesFromSpan(data, 0x0A, 0x02)))+"."+str(int.from_bytes(bytesFromSpan(data, 0x09, 0x01)))+"."+str(int.from_bytes(bytesFromSpan(data, 0x08, 0x01)))
		self.ByteOrderMark = int.from_bytes(bytesFromSpan(data, 0x0C, 0x02))
		self.Alignment = 1 << int.from_bytes(bytesFromSpan(data, 0x0E, 0x01))
		self.Unknown1 = int.from_bytes(bytesFromSpan(data, 0x0F, 0x01))
		self.FileNameOffset = int.from_bytes(bytesFromSpan(data, 0x10, 0x04))
		self.IsRelocated = int.from_bytes(bytesFromSpan(data, 0x14, 0x02))
		self.BinaryBlockOffset = int.from_bytes(bytesFromSpan(data, 0x16, 0x02))
		self.RelocationTableOffset = int.from_bytes(bytesFromSpan(data, 0x18, 0x04))
		self.FileSize = int.from_bytes(bytesFromSpan(data, 0x1C, 0x04))
		if not (self.ByteOrderMark == 0xFEFF): raise SyntaxError()
	def print(self):
		print2("Magic", self.Magic)
		print2("Version", self.Version)
		print2("Byte Order Mark", hex(self.ByteOrderMark))
		print2("Alignment", str(self.Alignment))
		print2("Unknown", hex(self.Unknown1))
		print2("File Name Offset", hex(self.FileNameOffset))
		print2("Is Relocated", hex(self.IsRelocated))
		print2("Binary Block Offset", hex(self.BinaryBlockOffset))
		print2("Relocation Table Offset", hex(self.RelocationTableOffset))
		print2("File Size", hex(self.FileSize))