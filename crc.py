#  by Oszau
#  crc calculate for line hex file
#  :1001B000 10001A0020001A001E001A001E001A00 6B
#  10+01+B0+00+10+00+1A+00+20+00+1A+00+1E+00+1A+00+1E+00+1A+00=0195
#  0195 Not = FE6A
#  FE6A+1=FE6B

string = '1001B00010001A0020001A001E001A001E001A00'
crc = 0
for num in range(0, len(string), 2):
  crc += int(string[num : num + 2],16)
crc = 0x10000 - crc
print(":" + string + "{:X}".format(crc)[2:])
