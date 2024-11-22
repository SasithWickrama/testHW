import re
import requests
import xml.etree.ElementTree as ET

proxies = {
    "http": None,
    "https": None,
}


xmlfile = open('/opt/test/lst_vlan_huawei.xml', 'r')
data = xmlfile.read()

#print(data)


response = requests.request("POST", "http://huaweincefanoss.intranet.slt.com.lk:30102/wsdl",data=data, proxies=proxies)

#print(response.request.body)
print("Response : =================================")
#print(response.text)

data = {}
root = ET.fromstring(response.text)
print(root)

ResultCode=re.findall("<os:errCode>(.*?)</os:errCode>", str(response.content))
ResultDescr=re.findall("<os:errDesc>(.*?)</os:errDesc>", str(response.content))
print(ResultCode,ResultDescr)

ulable = re.findall("<USERLABEL>(.*?)</USERLABEL>", str(response.content))
vlan = re.findall("<VLANID>(.*?)</VLANID>", str(response.content))

for i in range(len(ulable)):
    if ulable[i] == 'VOBB':
        print(i, ulable[i])
        print(vlan[i])

    if ulable[i] == 'Entree':
        print(i, ulable[i])
        print(vlan[i])

    if ulable[i] == 'SVLAN':
        print(i, ulable[i])
        print(vlan[i])
        
    if ulable[i] == 'IPTV_SVLAN':
        print(i, ulable[i])
        print(vlan[i])