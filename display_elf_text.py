#!/usr/bin/python3

import sys
import subprocess
import re

objfile = sys.argv[1]

"""
$>objdump -d A.o
...
Disassembly of section .fini:

0000000000005d58 <_fini>:
    5d58:       f3 0f 1e fa             endbr64
    5d5c:       48 83 ec 08             sub    $0x8,%rsp
    5d60:       48 83 c4 08             add    $0x8,%rsp
    5d64:       c3                      retq
...

"""

proc = subprocess.Popen(["objdump", "-d", objfile], env={"LANG" : "C"}, stdout=subprocess.PIPE)

section_functions = []
section_name = ""
for line in proc.stdout.readlines():
  line = line.decode("utf-8")[:-1]

  if line.startswith("Disassembly of section"):
    if section_name != "":
      print(section_name)
      for f in sorted(section_functions):
        print("    {}".format(f))

    section_name = line
    section_functions = []
    continue

  if line.startswith("0000"):
    section_functions.append(line.split()[1].replace("<", "").replace(">", "").replace(":", ""))
    continue

if section_name != "":
  print(section_name)
  for f in sorted(section_functions):
    print("    {}".format(f))
