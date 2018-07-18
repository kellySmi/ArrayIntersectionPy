from pydash import uniq_by, mapcat, intersection
import sys
import requests
wsurl = "https://s3.amazonaws.com/challenge.getcrossbeam.com/public/";
rs1 = requests.get(wsurl +sys.argv[1]+".json")
data1 = rs1.json()
names1 =  uniq_by(data1['companies'],lambda r: r['domain']);
n1Ar = mapcat(names1, lambda n: n['domain']);
rs2 = requests.get(wsurl+sys.argv[2]+".json")
data2 = rs2.json()
names2 =  uniq_by(data2['companies'],lambda r: r['domain']);
n2Ar = mapcat(names2, lambda n: n['domain']);
names3 = intersection(n1Ar, n2Ar)
print(repr(len(names1)) + " "+repr(len(names2))+" "+repr(len(names3)))
