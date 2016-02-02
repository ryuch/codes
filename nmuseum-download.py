#!/usr/bin/python

import os
import subprocess
import sys
import time

#wget_cmd = "/usr/bin/wget"
wget_cmd = "/usr/local/bin/wget"


if len(sys.argv) != 3:
        sys.exit("two numbers required")

for i in range(int(sys.argv[1]), int(sys.argv[2])):
        out= subprocess.check_output([wget_cmd, "-qO-", "http://www.museum.go.kr/site/main/relic/search/view?relicId="+str(i)+""])
        if out < 0 : continue
        pos1=out.find("<h4>")
        if(pos1>-1):
                pos2=out.find("</h4>",pos1)
                print i, out[pos1+4:pos2],

                # ex) http://www.museum.go.kr/site/main/relic/download/file/get?relicId=329&imgPathNo=1
                out= subprocess.check_output([wget_cmd, "--content-disposition",
                                                                                          "http://www.museum.go.kr/site/main/relic/download/file/get?relicId="+str(i)+"&imgPathNo=1"],
                                                                                         stderr=subprocess.STDOUT)
                if out < 0 : continue

                pos1=out.find("Saving to: ")
                if(pos1>-1):
                        pos2=out.find("\n", pos1+2)
                        print out[pos1+12:pos2-1],

                print ""
                sys.stdout.flush()
		time.sleep(3)

sys.exit("done")
