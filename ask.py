from bs4 import BeautifulSoup
from googlesearch import search
# import search_google.api
import requests,webbrowser

def quiz():
    l_question=[]
    l_answer=[]
    while True:
        with open('bot.txt','r+') as b:
            b.seek(0)
            for i in b.readlines():
                if not i.split("-")[0] in l_question:
                    l_question.append(i.split("-")[0])
                    l_answer.append(i.split("-")[1])
                
            ask_question=input("Sualiniz: ")
            if ask_question=="exit":
                break
            for i in range (len(l_question)):
                if l_question[i]==ask_question:
                    print(f"Cavabiniz: {l_answer[i]}")
            if not ask_question in l_question:
                user_answer=input("Bu suala cavab yoxdur.Cavab vermek isteyirsiniz (beli): ")
                if user_answer=="beli":
                    user_question_answer=input("Cavabiniz: ")
                    b.write(f"\n{ask_question}-{user_question_answer}")
                else:
                    continue

def news():
    response= requests.get('https://oxu.az/')
    soup=BeautifulSoup(response.text, features="html.parser")
    title = soup.findAll('div',{'class':'title'})
    print(title)
    link = soup.findAll("a",{"class":"news-i-inner"})
    for i in range(len(title)):
        print(f"{title[i].text} - https://oxu.az/{link[i]['href']}")


def rates():
    response=requests.get("https://api.exchangeratesapi.io/latest").json()
    # print(response)
    for i in response['rates']:
        print(f"{response['rates'][i]}--{i}") 

def weather():
    response=requests.get('http://api.openweathermap.org/data/2.5/weather?appid=2b94272e8df26b0abdf7fc3a4beee70b&q=Baku').json()
    print(f"Country-{response['sys']['country']}")
    print(f"City-{response['name']}")

    for i in response['weather']:
        for key,values in i.items():
            print(f"{key}-{values}")

    print(f"wind-speed-{response['wind']['speed']}")
    for key,values in response['main'].items():
        print(f"{key}-{values}")

def google():
    search=input("Axtardiginizi daxil edin:")
    response=requests.get(f"https://www.google.com/search?q={search}")
    soup=BeautifulSoup(response.text,features="html.parser")
    search_title=soup.select('.vvjwJb')
    search_link=soup.select('.UPmit')
    for i in range(len(search_link)):
        link=search_link[i].text.replace('›','/').replace(" ","").split(",")[0]
        print(f"{search_title[i].text} -- link -> {link}")
while True:
    choose=input("Menu:1-Quiz 2-News 3-Rates 4-Weather 5-Google-search 6-Exit\nChoose number: ")
    while not choose.isdigit() or not choose in ['1','2','3','4','5','6'] :
        choose=input("Menu:1-Quiz 2-News 3-Rates 4-Weather 5-Google-search\nChoose number: ")
    if choose=='1':
        quiz() 
    if choose=='2':
        news()
    if choose=='3':
        rates()
    if choose=='4':
        weather()
    if choose=='5':
        google()
    if choose=='6':
        exit()


 
