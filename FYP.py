from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import re
import csv



url = "https://scrapinghub.com/privacy-policy"
#url = "https://www.apple.com/uk/legal/privacy/en-ww/"
#url = "https://www.monster.co.uk/inside/fullpolicy/inside2.aspx"
#url = 'https://www.bcu.ac.uk/about-us/corporate-information/policies-and-procedures/privacy-policy'

page = requests.get(url)
data = page.text
soup = BeautifulSoup(data,features="lxml")


def csvStorage(question, result):
    myData =  [url, question, result]
    myFile = open('PrivacyPolicy.csv', 'a', newline ='')  
    with myFile:  
       writer = csv.writer(myFile)
       writer.writerows([myData])
       
#find all email(@) under Contact Us section
question = " Contact email"
word =''  
email ='' 
heading = 'h2'
i=2         
result =''
while heading != 'h6' and result == '':
    for nextNode in soup.find_all(heading,text=re.compile('Contact') ):
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, NavigableString):
                word += nextNode.strip()
            if isinstance(nextNode, Tag):
                if nextNode.name == heading:
                    break
                word += nextNode.get_text(strip=True).strip() 
                email = re.findall(r'[\w]+@[\w]+', word)
                if email:
                    print(email)
    i = i+1
    heading = 'h' + str(i)
csvStorage(question,email)
    
if heading == 'h6' and email == '':
    print('No match result')
         
#Get paragraph with div class
question = "What information is collected"
heading = 'h2'
i=2
result=''
while heading != 'h6' and result =='':
    for nextNode in soup.find_all(heading,text=re.compile('(What|Information).*(collect|gather)') ):
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, NavigableString):
                result = nextNode.strip()
                print (result)
            if isinstance(nextNode, Tag):
                if nextNode.name == heading:
                    break
                result=nextNode.get_text(strip=True).strip()
                print (result) 

    i = i+1
    heading = 'h' + str(i)
csvStorage(question, result)

#Get paragraph with div class
question = "Third parties and cookies"
heading = 'h2'
i=2
result=''
third_party_policies=''
while heading != 'h6' and result =='':
    for nextNode in soup.find_all(heading,text=re.compile('cookies')): 
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, NavigableString):
                result = nextNode.strip()
                print (result)
            if isinstance(nextNode, Tag):
                if nextNode.name == heading:
                    break
                result=nextNode.get_text(strip=True).strip()
                print (result)
                global third_party_polices
                third_party_policies += result
    
    i = i+1
    heading = 'h' + str(i)
csvStorage(question, third_party_policies) 
    
#Term of condition may apply
       
   


