from math import floor

def stringAtOffset(data: bytes, offset: int) -> str:
	result: str = ""
	for byte in data[offset:]:
		if byte == 0: break
		result += chr(byte)
	return result

def bytesFromSpan(data: bytes, offset: int, span: int) -> bytes:
	return data[offset:offset+span][::-1]

PRINT_DEPTH: int = 0

def print2_in():
	global PRINT_DEPTH
	PRINT_DEPTH += 1

def print2_out():
	global PRINT_DEPTH
	PRINT_DEPTH -= 1

def print2(name: str, value: str = None):
	global PRINT_DEPTH
	name += ":"
	if not value: value = ""
	tabCount = 5 - floor(name.__len__()/8)
	print("|	"*PRINT_DEPTH + name + "	"*tabCount + value)