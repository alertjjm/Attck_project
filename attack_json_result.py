import os
import json
from collections import OrderedDict
url="groupdb"
file_list=os.listdir(url)
file_list=file_list[1:]
print(file_list)
jsonlist=[]
file_data=OrderedDict()

for i in range(len(file_list)):
    f=open(url+"/"+file_list[i],'r')
    jsonobj=json.load(f)
    technique=jsonobj["techniques"]
    for i in technique:
        try:
            file_data[i["techniqueID"]] += 1
        except:
            file_data[i["techniqueID"]]=1
    f.close()
print(json.dumps(file_data, ensure_ascii=False, indent="\t") )
f=open("result.json",'w',encoding='utf-8')
json.dump(file_data,f,ensure_ascii=False,indent='\t')