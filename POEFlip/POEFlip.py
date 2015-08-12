__author__ = 'AureOc'

from bs4 import BeautifulSoup
import urllib.request
import re
import time


def runcheck():
    with open("Items.txt") as f:
        content = f.readlines()

    for lines in content:
        linesarray = lines.split(",")
        r = urllib.request.urlopen(linesarray[1]).read()
        soup = BeautifulSoup(r, "html.parser")

        table = soup.find_all('span', attrs={'class':'sortable'})

        for row in table:
            result = re.search('data-value="-(.*)"><span', str(row))
            if float(result.group(1)) <= float(linesarray[2]):
                print(linesarray[0]," found at price: ", result.group(1)," - ", linesarray[1])


    time.sleep(60*5)

while True:
    runcheck()