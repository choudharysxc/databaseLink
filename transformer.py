import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

import sqlite3

x=input("Enter a URl :")
conn=sqlite3.connect("email.db")
c=conn.cursor()

#c.execute("CREATE TABLE email ( email text)")

lst=list()
final_lst=list()

def convert(x):
    link=urllib.request.urlopen(x)
    soup=BeautifulSoup(link,'html.parser')
    return soup


def Scraper(x):
    soup=convert(x)
    
    for link in soup.findAll('a'):
        lst.append(link.get('href'))
    
    for link in lst:
        i=0
        copy=link
        img=[]
        link=str(link)
        i=link.find('@')
        if i > 1:
            final_lst.append(copy)
    print(final_lst)        
 
Scraper(x)

for i in final_lst:
    img=[]
    img.append(i)
    c.execute("INSERT INTO email VALUES (?)", img)
    conn.commit()

c.execute("SELECT * FROM email ")
z=c.fetchall()
for i in z:
    print(i)
conn.commit()
conn.close()
