#!/usr/bin/python3

import sys
import display_elf_text
import mimic_dwarfdump_str

def run():

  objfile = sys.argv[1]
  strings = set(mimic_dwarfdump_str.get_strs(objfile))
  _, functions, callees = display_elf_text.get_functions(objfile)

  in_debugstr_not_in_text = strings - (functions | callees)
  in_text_not_in_debugstr = (functions | callees) - strings

  print("========== in debugstr, not in text =========")
  for s in in_debugstr_not_in_text:
    print(s)
  print("\n\n")
  print("========== in text, not in debugstr =========")
  for s in in_text_not_in_debugstr:
    print(s)

if __name__ == "__main__":
  run()
