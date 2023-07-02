#!/usr/bin/python3

import sys
import subprocess
import re

objfile = sys.argv[1]

"""
$>readelf --headers A.o
ELF 头：
  Magic：   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00
  类别:                              ELF64
  数据:                              2 补码，小端序 (little endian)
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI 版本:                          0
  类型:                              REL (可重定位文件)
  系统架构:                          Advanced Micro Devices X86-64
  版本:                              0x1
  入口点地址：               0x0
  程序头起点：          0 (bytes into file)
  Start of section headers:          156072 (bytes into file)
  标志：             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           0 (bytes)
  Number of program headers:         0
  Size of section headers:           64 (bytes)
  Number of section headers:         39
  Section header string table index: 38

节头：
  [号] 名称              类型             地址              偏移量
       大小              全体大小          旗标   链接   信息   对齐
  [ 0]                   NULL             0000000000000000  00000000
  0000000000000000  0000000000000000           0     0     0
  [ 1] .group            GROUP            0000000000000000  00000040
  000000000000000c  0000000000000004          36    34     4
  [ 2] .group            GROUP            0000000000000000  0000004c
  0000000000000008  0000000000000004          36    36     4
  [ 3] .group            GROUP            0000000000000000  00000054
  0000000000000008  0000000000000004          36    39     4
...

"""

proc = subprocess.Popen(["readelf", "--headers", objfile], env={"LANG" : "C"}, stdout=subprocess.PIPE)

read_info = True
read_section = False
read_next = False
begin_section_re = re.compile("\[[ \t]+0\]")

name = ""
size = 0

headers = {} # name, [cnt, size]

for line in proc.stdout.readlines():
  line = line.decode("utf-8")[:-1]
  #print(line)

  if begin_section_re.search(line):
    read_info = False
    read_section = True
    continue

  if read_info:
    if "Section Headers:" in line:
      read_info = False
      continue
    print(line)
    continue

  if read_section:
    try:
      if "[" in line:
        name = line.split("]")[1].split()[0]
        read_next = True
        continue

      if read_next:
        size = int(line.split()[1], 16)
        read_next = False
        shortname = ".".join(name.split(".")[:-1])
        if shortname == "":
          shortname = name
        #print(name, size)
        if shortname not in headers:
          headers[shortname] = [1, size]
        else:
          headers[shortname][0] += 1
          headers[shortname][1] += size
        continue
    except IndexError:
      break

totalsize = 0
for k, v in sorted(headers.items(), key=lambda v: v[1][1]):
  print("{:24s} x{:2d} {:8.2f}MB".format(k, v[0], v[1]/1024/1024))
  totalsize += v[1]
print("====================")
print("total size {:8.2f}MB".format(totalsize/1024/1024))
