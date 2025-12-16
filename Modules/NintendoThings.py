import numpy
from math import ceil

def stringAtOffset(data: bytes, offset: int) -> str:
	result: str = ""
	for byte in data[offset:]:
		if byte == 0: break
		result += chr(byte)
	return result

class RelocationTableEntry():
        FileRegionOffset: numpy.uint32
        ArrayCount: numpy.uint16
        PerArrayPointerCount: numpy.uint8
        ArrayStride: numpy.uint8

        def __init__(self, data: bytes):
         self.FileRegionOffset = int.from_bytes(data[0x00:0x04][::-1])
         self.ArrayCount = int.from_bytes(data[0x04:0x06][::-1])
         self.PerArrayPointerCount = int.from_bytes(data[0x06:0x07][::-1])
         self.ArrayStride = int.from_bytes(data[0x07:0x08][::-1])
        def debugPrint(self):
         print("			File Region Offset:		"+hex(self.FileRegionOffset))
         print("			Array Count:			"+hex(self.ArrayCount))
         print("			Per Array Pointer Count:	"+hex(self.PerArrayPointerCount))
         print("			Array Stride:			"+hex(self.ArrayStride))

class RelocationTableSection():
        Base: numpy.uint64
        FileRegionOffset: numpy.uint32
        FileRegionSize: numpy.uint32
        BaseEntryIndex: numpy.uint32
        EntryCount: numpy.uint32
        Entries: list[RelocationTableEntry]

        def __init__(self, data: bytes, dataEntries: bytes):
         self.Base = int.from_bytes(data[0x00:0x08][::-1])
         self.FileRegionOffset = int.from_bytes(data[0x08:0x0C][::-1])
         self.FileRegionSize = int.from_bytes(data[0x0C:0x10][::-1])
         self.BaseEntryIndex = int.from_bytes(data[0x10:0x14][::-1])
         self.EntryCount = int.from_bytes(data[0x14:0x18][::-1])
         self.Entries = list()
         for i in range(self.EntryCount):
            self.Entries.append(RelocationTableEntry(dataEntries[0x00+i*0x08:]))
        def debugPrint(self):
         print("		Base:				"+hex(self.Base))
         print("		File Region Offset:		"+hex(self.FileRegionOffset))
         print("		File Region Size:		"+hex(self.FileRegionSize))
         print("		Base Entry Index:		"+hex(self.BaseEntryIndex))
         print("		Entry Count:			"+hex(self.EntryCount))
         print("		Entries:")
         for x in self.Entries: x.debugPrint()

class RelocationTable():
        Magic: str
        OffsetFromHeader: numpy.uint32
        SectionCount: numpy.uint32
        Sections: list[RelocationTableSection]

        def __init__(self, data: bytes):
         self.Magic = data[0x00:0x04].decode()
         self.OffsetFromHeader = int.from_bytes(data[0x04:0x08][::-1])
         self.SectionCount = int.from_bytes(data[0x08:0x0C][::-1])
         self.Sections = list()
         for i in range(self.SectionCount):
          self.Sections.append(RelocationTableSection(data[0x10+i*0x18:], data[0x10+self.SectionCount*0x18:]))
        def debugPrint(self):
         print("	Magic:				"+self.Magic)
         print("	Offset From Header:		"+hex(self.OffsetFromHeader))
         print("	Section Count:			"+hex(self.SectionCount))
         print("	Blocks:")
         for x in self.Sections: x.debugPrint()

class BinaryBlock():
        Magic: str
        NextBinaryBlockOffset: numpy.uint32
        Size: numpy.uint32

        def __init__(self, data: bytes):
         self.Magic = data[0x00:0x04].decode()
         self.NextBinaryBlockOffset = int.from_bytes(data[0x04:0x08][::-1])
         self.Size = int.from_bytes(data[0x08:0x0C][::-1])
        def debugPrint(self):
         print("	Magic:				"+self.Magic)
         print("	Next Binary Block Offset:	"+hex(self.NextBinaryBlockOffset))
         print("	Size:				"+hex(self.Size))

class StringPool(BinaryBlock):
        StringCount: numpy.uint32
        Strings: list[str]
        
        def __init__(self, data: bytes):
         super().__init__(data)
         self.StringCount = int.from_bytes(data[0x10:0x14][::-1])
         self.Strings = list()
         offset = 0x18
         for i in range(self.StringCount):
          self.Strings.append(stringAtOffset(data, offset+0x02))
          stringLength = int.from_bytes(data[offset:offset+0x02][::-1])
          offset += 0x03+stringLength
          offset = 2 * ceil(offset/2)
          
        def debugPrint(self):
         super().debugPrint()
         print("	StringCount:			"+str(self.StringCount))
         print("	Strings:")
         for i in range(self.StringCount):
          print("		"+self.Strings[i])

class BinaryFileResource():
        Magic: str
        Version: str
        IsBigEndian: bool
        ByteOrderMark: numpy.uint16
        Alignment: numpy.uint64
        FileName: str
        FileNameOffset: numpy.uint32
        BinaryBlockOffset: numpy.uint16
        RelocationTableOffset: numpy.uint32
        FileSize: numpy.uint32
        Blocks: list[BinaryBlock]
        relocationTable: RelocationTable

        def __init__(self, data: bytes):
         self.IsBigEndian = not (int.from_bytes(data[0x0C:0x0E]) == 0xfffe)
         if self.IsBigEndian:
          # Header
          self.Magic = data[0x00:0x04].decode()
          self.Version = "v"+str(int.from_bytes(data[0x06:0x08]))+"."+str(int.from_bytes(data[0x05:0x06]))+"."+str(int.from_bytes(data[0x04:0x05]))
          self.ByteOrderMark = int.from_bytes(data[0x08:0x0A])
          #self.HeaderLength = int.from_bytes(fileData[0x0A:0x0C]) # Redundant.
          self.FileSize = int.from_bytes(data[0x0C:0x10])
          # Metadata
          self.Alignment = int.from_bytes(data[0x10:0x14])
          self.FileNameOffset = int.from_bytes(data[0x14:0x18])+0x14 # Relative
          self.FileName = stringAtOffset(data, self.FileNameOffset)
          
          #self.StringTableLength = int.from_bytes(fileData[0x18:0x1C])
          #self.StringTablePosition = int.from_bytes(fileData[0x1C:0x20])+0x1C # Relative
          #self.StringTableTemp = fileData[self.StringTablePosition:self.StringTablePosition+self.StringTableLength]
          #self.ModelDictionaryPosition = int.from_bytes(fileData[0x20:0x24])
          #if not self.ModelDictionaryPosition == 0: self.ModelDictionaryPosition += 0x20 # Relative
          #self.TextureDictionaryPosition = int.from_bytes(fileData[0x24:0x28])
          #if not self.TextureDictionaryPosition == 0: self.TextureDictionaryPosition += 0x24 # Relative
         else:
          # Header
          self.Magic = data[0x00:0x08].decode()
          self.Version = "v"+str(int.from_bytes(data[0x0A:0x0C][::-1]))+"."+str(int.from_bytes(data[0x09:0x0A]))+"."+str(int.from_bytes(data[0x08:0x09]))
          self.ByteOrderMark = int.from_bytes(data[0x0C:0x0E])
          self.Alignment = 1 << int.from_bytes(data[0x0E:0x0F][::-1])
          # 1 byte gap?
          self.FileNameOffset = int.from_bytes(data[0x10:0x14][::-1])
          self.FileName = stringAtOffset(data, self.FileNameOffset)
          self.BinaryBlockOffset = int.from_bytes(data[0x16:0x18][::-1])
          self.RelocationTableOffset = int.from_bytes(data[0x18:0x1C][::-1])
          self.FileSize = int.from_bytes(data[0x1C:0x20][::-1])
          self.Blocks = list()
          offset = self.BinaryBlockOffset
          while True:
           block: BinaryBlock
           if data[offset:offset+0x04].decode() == "_STR":
            block = StringPool(data[offset:])
           else:
            block = BinaryBlock(data[offset:])
           self.Blocks.append(block)
           if block.NextBinaryBlockOffset == 0: break
           offset += block.NextBinaryBlockOffset
          self.relocationTable = RelocationTable(data[self.RelocationTableOffset:])
        def debugPrint(self):
         print("Magic:				"+self.Magic)
         print("Version:			"+self.Version)
         print("Byte Order Mark:		"+hex(self.ByteOrderMark))
         print("Is Big Endian:			"+str(self.IsBigEndian))
         print("Alignment:			"+str(self.Alignment))
         print("File Name Offset:		"+hex(self.FileNameOffset))
         print("File Name:			"+self.FileName)
         print("Binary Block Offset:		"+hex(self.BinaryBlockOffset))
         print("Relocation Table Offset:	"+hex(self.RelocationTableOffset))
         print("File Size:			"+hex(self.FileSize))
         print("Blocks:")
         for x in self.Blocks: x.debugPrint()
         print("Relocation Table:")
         if self.relocationTable: self.relocationTable.debugPrint()
