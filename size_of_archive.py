from bs4 import BeautifulSoup
import sys
import re
from subprocess import call

# generate url from item name
itemname = sys.argv[1]

url = "https://archive.org/download/" + itemname + "/" + itemname + "_files.xml"

# gorn get..

command = "wget -q " + url

call(command, shell=True)

filename = itemname + "_files.xml"

with open(filename) as f:
   content_list = f.readlines()

content_str =' '.join(content_list)

#print(content_str)

soup = BeautifulSoup(content_str,'html.parser')

sizes = soup("size")


result = 0
for item in sizes:
   stripped = re.sub('<[^<]+?>', '', str(item))
   print(stripped)
   result = result + int(stripped)

print()
#output = str(result) +
print(str(result) + " Bytes")
gigs = result / 1073741824
gibs = result / 1000000000
print(str(gigs) + " Gibbibytes or " + str(gibs) + " Gigabytes")
rmcommand = "rm " + filename
call(rmcommand, shell=True)
