from selenium import webdriver
from bs4 import BeautifulSoup

for x in range(11):
    

    link = 'https://steamcommunity.com/groups/csgolounge/members/?p=' + str(x)

    browser = webdriver.Firefox()
    browser.get(link)

    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')


    results = soup.find_all("div",{"id":"memberList"})
    with open('racxa.txt', 'a') as f:
        for result in results:
            dapr = result.find_all("div",{"class":"playerAvatar in-game"})
            f.write(dapr + '\n')


browser.close()
f.close()






