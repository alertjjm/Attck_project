import json
from collections import OrderedDict
from selenium import webdriver
browser=webdriver.Chrome()
file_data=OrderedDict()
f=open("result.json",'r')
jsonobj=json.load(f)
for i in jsonobj:
    j=1
    a={}
    li=[]
    browser.get("https://attack.mitre.org/versions/v6/techniques/"+i+"/")
    platform=browser.find_element_by_xpath('//*[@id="v-attckmatrix"]/div[2]/div/div/div/div[1]/div[2]/div/div/div[3]').text
    if('Linux' not in platform):
        print('it is not linux')
        continue
    while(1):
        try:
            strmi=""
            strmi=strmi+browser.find_element_by_xpath('//*[@id="v-attckmatrix"]/div[2]/div/div/div/table[2]/tbody/tr['+str(j)+']/td[1]/a').text+": "+browser.find_element_by_xpath('//*[@id="v-attckmatrix"]/div[2]/div/div/div/table[2]/tbody/tr['+str(j)+']/td[2]/p').text
            li.append(strmi)
            j=j+1
        except:
            break
    if(len(li)!=0):
        a['count']=jsonobj[i]
        a['mitigation']=li
        file_data[i]=a
        print(i+": ",end='')
        print(a)
    else:
        print(i+": no mitigations")
f.close()
print(json.dumps(file_data, ensure_ascii=False, indent="\t") )
f=open("result_linux.json",'w',encoding='utf-8')
json.dump(file_data,f,ensure_ascii=False,indent='\t')