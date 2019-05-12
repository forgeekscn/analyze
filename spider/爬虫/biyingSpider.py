import requests
import re
import time

local = time.strftime("%Y.%m.%d")
url = 'http://data.sports.sohu.com/nba/nba_team_info.php?teamid=20'
con = requests.get(url)
content = con.text
# print(content)

# f2=open('demo.xml', 'r', encoding='utf-8')
# content = f2.read()
# f2.close()

reg = r"href=.*?[jpg,png]"
a = re.findall(reg, content, re.S)
print(a)


# read = requests.get(picUrl)

# f = open('%s.jpg' % local, 'wb')
# f.write(read.content)
# f.close()
