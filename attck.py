from selenium import webdriver
browser=webdriver.Chrome()
for i in range(94):
    browser.get("https://attack.mitre.org/groups/")
    browser.implicitly_wait(1)
    cursor = browser.find_element_by_css_selector("#v-attckmatrix > div.row > div > div > div > div > table > tbody > tr:nth-child("+str(i+1)+") > td:nth-child(1) > a")
    cursor.click()
    a=browser.current_url
    a=a.split("/")
    a=a[4]
    try:
        browser.get("https://attack.mitre.org/groups/"+a+"/"+a+"-enterprise-layer.json")
        b=browser.find_element_by_css_selector("body > pre").text
        f=open("C:/Users/windows10/Downloads/"+a+".json",'w')
        f.write(b)
        f.close()
        print(str(i + 1) + ". " + a)
    except:
        print(str(i + 1) + ". " +"404 error")
    browser.implicitly_wait(1)