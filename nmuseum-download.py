#!/usr/bin/python

import os
import subprocess
import sys

if len(sys.argv) != 3:
      sys.exit("two numbers required")

for i in range(int(sys.argv[1]), int(sys.argv[2])):
      out= subprocess.check_output(["/usr/bin/wget", "-qO-", "http://www.museum.go.kr/site/main/relic/search/view?relicId="+str(i)+""])
      pos1=out.find("<h4>")
      if(pos1>-1):
            pos2=out.find("</h4>",pos1)
            print i, out[pos1+4:pos2],

            out= subprocess.check_output(["/usr/bin/wget", "--content-disposition",
                                          "http://www.museum.go.kr/site/main/relic/download/file/get?relicId="+str(i)+"&imgpathno=1"],
                                         stderr=subprocess.STDOUT)
            print out

            pos1=out.find("Saving to: '")
            if(pos1>-1):
                  pos2=out.find("\n", pos1+2)
                  print out[pos1+12:pos2-1],
      print ""

sys.exit("done")
