#!/usr/bin/python3

import sys
import subprocess

objfile = sys.argv[1]

"""
readelf --debug-dump=info A.o

Contents of the .debug_info section:

Compilation Unit @ offset 0x0:
  Length:        0x9661 (32-bit)
  Version:       4
  Abbrev Offset: 0x0
  Pointer Size:  8

<0><b>: Abbrev Number: 96 (DW_TAG_compile_unit)
   <c>   DW_AT_producer    : (indirect string, offset: 0x1447): GNU C++17 8.4.0 -mtune=generic -march=x86-64 -g -O0 -std=c++17 -fasynchronous-unwind-tables -fstack-protector-strong -fstack-clash-protection -fcf-protection
   <10>   DW_AT_language    : 4        (C++)
   <11>   DW_AT_name        : A.C
   <15>   DW_AT_comp_dir    : (indirect string, offset: 0x6654): /home/tj/Development/github/dwarf
   <19>   DW_AT_ranges      : 0x0
   <1d>   DW_AT_low_pc      : 0x0
   <25>   DW_AT_stmt_list   : 0x0
<1><29>: Abbrev Number: 97 (DW_TAG_namespace)
   <2a>   DW_AT_name        : std
   <2e>   DW_AT_decl_file   : 29
   <2f>   DW_AT_decl_line   : 0
   <30>   DW_AT_sibling     : <0x66d3>
<2><34>: Abbrev Number: 51 (DW_TAG_namespace)
   <35>   DW_AT_name        : (indirect string, offset: 0x141b): __cxx11
   <39>   DW_AT_decl_file   : 12
   <3a>   DW_AT_decl_line   : 260
   <3c>   DW_AT_decl_column : 65
   <3d>   DW_AT_export_symbols: 1
...

"""

proc = subprocess.Popen(["readelf", "--debug-dump=info", objfile], stdout=subprocess.PIPE)

read_body = False
tag = ""
indent = 0
name = ""
for line in proc.stdout.readlines():
  line = line.decode("utf-8")[:-1]

  if read_body:
    if "DW_AT_name" in line:
      name = " ".join(line.split()[3:])
      print("{}[{}] {} {}".format(indent * "    ", indent, tag, name))
      tag = ""
      indent = 0
      name = ""
      read_body = False
      continue

  if "><" in line and "DW_TAG_" in line:
    tag = line.split()[-1].replace("(", "").replace(")", "")
    indent = int(line.split(">")[0].replace("<", ""))
    read_body = True
