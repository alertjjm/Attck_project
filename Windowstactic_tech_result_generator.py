import json
from collections import OrderedDict
from selenium import webdriver
browser=webdriver.Chrome()
file_data=OrderedDict()
f=open("result_windows.json",'r')
jsonobj=json.load(f)
for i in jsonobj:
    li=[]
    browser.get("https://attack.mitre.org/versions/v6/techniques/"+i+"/")
    try:
        tactics=""
        tactics=browser.find_element_by_xpath('''//*[@id="v-attckmatrix"]/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]''').text
        tactics=tactics.replace("Tactic: ","")
        li=tactics.split(", ")
        print(li)
        for j in li:
            try:
                file_data[j].append(i+":"+str(jsonobj[i]["count"]))
            except:
                file_data[j]=[]
                file_data[j].append(i+":"+str(jsonobj[i]["count"]))
    except:
        print("no tactics found")
for i in file_data:
    file_data[i].sort(key=lambda k:jsonobj[k.split(":")[0]]["count"],reverse=True)
f.close()
f=open("windows_tactics.json",'w',encoding='utf-8')
json.dump(file_data,f,ensure_ascii=False,indent='\t')