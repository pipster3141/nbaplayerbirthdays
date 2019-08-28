#NBA Birthdate Web Scrape - Trevor J Dalton - 10/18/2018
#Intended to study athletic favoritism by birthdate

import bs4, urllib3, requests, lxml
urllib3.disable_warnings()
from urbanDictionaryDef import getHTML
import matplotlib.pyplot as plt
import numpy as np

def main():
    soup = getHTML('https://en.wikipedia.org/wiki/List_of_current_NBA_team_rosters')
    names = getNames(soup)
    birthDates = getBirthdates(soup)
    
    """
    for i in range(len(names)):
        print('Name: '+names[i])
        print('Birthdate: '+birthDates[i][0]+' '+birthDates[i][1]+' '+birthDates[i][2])
        print()
    """
    
    makeGraph(birthDates)
    return

def getNames(soup):
    names = []
    oneStep = soup.find_all('table')
    for table in oneStep:
        twoStep = table.find_all('tr')
        for tr in twoStep:
            threeStep = tr.find_all('td')
            if threeStep != []:
                try:
                    fourStep = threeStep[2]
                    text1 = fourStep.text
                    strip1 = text1.split('\n')
                    text2 = strip1[0]
                    strip2 = text2.split('\\xa')
                    text3 = strip2[0]
                    strip3 = text3.split()
                    if text3[0] != '7' and text3[0] != '5':
                        try:
                            text4 = strip3[0]+' '+strip3[1]
                        except:
                            text4 = strip3[0]
                        names.append(text4)
                except:
                    pass
    return names

def getBirthdates(soup):
    birthDates = []
    oneStep = soup.find_all('table')
    for table in oneStep:
        twoStep = table.find_all('tr')
        for tr in twoStep:
            threeStep = tr.find_all('td')
            if threeStep != []:
                try:
                    fourStep = threeStep[5]
                    text1 = fourStep.text
                    strip1 = text1.split('\n')
                    text2 = strip1[0]
                    if not 'kg' in text2:
                        birthDate = [text2[:4],text2[5:7],text2[8:]]
                        birthDates.append(birthDate)
                except:
                    pass
    return birthDates

def makeGraph(dates):
    monthsCounter = [0,0,0,0,0,0,0,0,0,0,0,0]
    months = ['Jan','Feb','Mar','April','May','June','July','Aug','Sept','Oct','Nov','Dec']
    for date in dates:
        monthsCounter[int(date[1])-1] += 1
    width = .35
    ind = np.arange(len(months))

    fig, ax = plt.subplots()
    rect = ax.bar( ind, monthsCounter, width, color='IndianRed')

    ax.set_ylabel('Birthdates')
    ax.set_title('Birthdates of Current NBA Players by Month')
    ax.set_xticks(ind)
    ax.set_xticklabels(months)
    ax.grid(axis='y', linewidth='.5')
    autoLabel(rect, monthsCounter)

    plt.show()

def autoLabel(rects, monthsCounter):
    for i in range(len(rects)):
        height = rects[i].get_height()
        plt.text(rects[i].get_x(), 1.01*height, str(monthsCounter[i]))

                

if __name__ == "__main__":
    main()
