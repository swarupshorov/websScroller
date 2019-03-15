#============== include library ============#
import requests
from bs4 import BeautifulSoup
import csv
import schedule
import time
import random

#==============================================================
# function name: divide_chunks
# argument : 1st argument -> list item, 2nd argument-> number of slice
# return: 2d list
# ======================= divide_chunks (START) ==============#
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]
# ======================= divide_chunks (End) ==============#


#==============================================================
# function name: folldinfo
# argument :
# return: parse site data and write in a file
# ======================= floodInfo (START) ==============#


def floodInfo():
    #=============== site information =====================#
    r = requests.get('http://www.ffwc.gov.bd/') # site link
    soup = BeautifulSoup(r.text, 'html.parser')# parse site information
    results = soup.find_all('div', attrs={'id':'map'})# class name where get infomation

    #---------------  declear necessary list item ------------------#

    desp = []
    url = []
    coordinate = []
    print(results)
    #================ parse html data ===================
    for result in results:

       #------ parse river coordinate value -----------#
        for element  in result.find_all('a'): # parse  link data
            for stat in element.find_all("div"): # parse a tag inner html
                coordinate.append(stat["data-coords"])

        #-------- parse all model image ------------#
        for place in result.find_all('a'):
            url.append(place['href'])

        #--------- parse river all information ------#
        for data in result.find_all('strong'):
            action = data.next_sibling
            desp.append(action)


    fileRow = [["Station Name","River Name","Division","District","Upazilla","Union","Water Level","Highest Water Level","Danger Level","Url"]] #csv file top row element for title
    dInfo = list(divide_chunks(desp, 9))#split a list and convert it 2d list item which content 9 data
    k = 0
    #====================== append url in a list ====================
    for pDin in dInfo:
        pDin.append(url[k])
        k+=1

    allData = fileRow + dInfo #append / concate row title and all information


    #================== specify multi list data =====================

    filename=str(random.random()) # create dynamic name for set file name

    #===============  file write operation (start) ===============#
    with open(filename+".csv", 'w') as csvFile: #open csv file for import data
        writer = csv.writer(csvFile)
        writer.writerows(allData)
    csvFile.close()
    # ===============  file write operation (end) ===============#


# ======================= floodInfo (END) ==============#



# ========================= schedular  =================#
# call schdedular function in specific time
#=======================================================#
schedule.every(5).seconds.do(floodInfo)

while 1:
    schedule.run_pending()
    time.sleep(1)


