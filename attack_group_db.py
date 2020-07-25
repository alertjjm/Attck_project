from selenium import webdriver
import os
browser=webdriver.Chrome()
dirname="groupdb"
if not os.path.isdir(dirname):
    os.mkdir(dirname)
for i in range(94):
    browser.get("https://attack.mitre.org/versions/v6/groups/")
    browser.implicitly_wait(1)
    cursor = browser.find_element_by_css_selector("#v-attckmatrix > div.row > div > div > div > div > table > tbody > tr:nth-child("+str(i+1)+") > td:nth-child(1) > a")
    cursor.click()
    a=browser.current_url
    a=a.split("/")
    a=a[6]
    try:
        browser.get("https://attack.mitre.org/versions/v6/groups/"+a+"/"+a+"-enterprise-layer.json")
        b=browser.find_element_by_css_selector("body > pre").text
        f=open(dirname+"/"+a+".json",'w')
        f.write(b)
        f.close()
        print(str(i + 1) + ". " + a)
    except:
        print(str(i + 1) + ". " +"404 error")
    browser.implicitly_wait(1)