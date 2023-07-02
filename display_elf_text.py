#!/usr/bin/python3

import sys
import subprocess
import re

def get_functions(objfile):

  section_functions = {}
  all_functions = set()
  callees = set()

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

  functions = []
  section_name = ""
  for line in proc.stdout.readlines():
    line = line.decode("utf-8")[:-1]

    if line.startswith("Disassembly of section"):
      if section_name != "":
        section_functions[section_name] = functions
        all_functions.update(functions)

      section_name = line
      functions = []
      continue

    if line.startswith("0000"):
      functions.append(line.split()[1].replace("<", "").replace(">", "").replace(":", ""))
      continue

    if "call" in line:
      callee = line.split()[-1]
      if "<" in callee:
        callee = callee.replace("<", "").replace(">", "")
        if "+" in callee:
          callee = callee.split("+")[0]
        if "@" in callee:
          if "@plt" not in callee:
            callee = callee.split("@")[0]
        callees.add(callee)

  if section_name != "":
    section_functions[section_name] = functions
    all_functions.update(functions)

  return section_functions, all_functions, callees - all_functions

def run():
  objfile = sys.argv[1]
  section_functions, all_functions, callees = get_functions(objfile)
  for section, functions in section_functions.items():
    print(section)
    for f in sorted(functions):
      print("    {}".format(f))
  print("\n\nneeds:\n\n")
  for callee in callees:
    print("{}".format(callee))
if __name__ == "__main__":
  run()
