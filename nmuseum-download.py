import os
import subprocess


for i in range(368, 10000):
#   out= subprocess.check_output(["/usr/local/bin/wget", "-qO-", "\"http://www.museum.go.kr/site/main/relic/search/view?relicId="+str(i)+"\""])
      out= subprocess.check_output(["/usr/local/bin/wget", "-qO-", "http://www.museum.go.kr/site/main/relic/search/view?relicId="+str(i)+""])
      pos1=out.find("<h4>")
      if(pos1>-1):
            pos2=out.find("</h4>",pos1)
            print i, out[pos1+4:pos2],

            out= subprocess.check_output(["/usr/local/bin/wget", "--content-disposition", "http://www.museum.go.kr/site/main/relic/download/file/get?relicId="+str(i)+
                                          "&imgPathNo=1"], stderr=subprocess.STDOUT)

            pos1=out.find("Saving to: '")
            if(pos1>-1):
                  pos2=out.find("\n", pos1+2)
                  print out[pos1+12:pos2-1]
