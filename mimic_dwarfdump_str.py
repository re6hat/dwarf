#!/usr/bin/python3

import sys
import subprocess

def get_strs(objfile):

  """
  readelf --debug-dump=str A.o

  .debug_str 节的内容:

    0x00000000 5f5a4e53 7431346e 756d6572 69635f6c _ZNSt14numeric_l
    0x00000010 696d6974 73497345 37657073 696c6f6e imitsIsE7epsilon
    0x00000020 4576005f 5a4e4b53 74313762 61736963 Ev._ZNKSt17basic
    0x00000030 5f737472 696e675f 76696577 49635374 _string_viewIcSt
    0x00000040 31316368 61725f74 72616974 73496345 11char_traitsIcE
    0x00000050 4535656d 70747945 76006c6f 6e67206c E5emptyEv.long l
    0x00000060 6f6e6720 696e7400 5f5a4e53 7431346e ong int._ZNSt14n
    ...

  """

  proc = subprocess.Popen(["readelf", "--debug-dump=str", objfile], stdout=subprocess.PIPE)

  all_chars = []
  for line in proc.stdout.readlines():
    line = line.decode("utf-8")[:-1]
    if "0x" in line:
      array_of_chars = line.split()[1:5]
      chars = "".join(array_of_chars)
      all_chars += chars

  idx = 0
  cnt = len(all_chars)
  strings = []
  chars = []
  while idx < cnt:
    try:
      number = int(all_chars[idx], 16) * 16 + int(all_chars[idx+1], 16)
      char = chr(number)
      if char == '\0':
        strings.append("".join(chars))
        chars = []
      else:
        chars.append(char)
    except ValueError:
      break
    idx += 2

  return strings

def run():

  objfile = sys.argv[1]
  strings = get_strs(objfile)
  for s in strings:
    print("{:6d} {}".format(len(s), s))

if __name__ == "__main__":
  run()
