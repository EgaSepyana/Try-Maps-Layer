from src.util.db.pyMongo.mopy import MongoConnection

con = MongoConnection.NewMongoConnectionLocal("indonesian-prov")
 
import json
f = open ('indonesia-province-simple.json', "r")
data :dict = json.loads(f.read())
for i in data.get("features"):
    data = {}
    data['provice_name'] = i["properties"]["Propinsi"]
    data['description'] = "provice geometry"
    del i['properties']['ID']
    # del i['geometry']

    data['geom'] = i

    error , upsertId = con.InsertData(data)
    print(f"Succes Upsert Data With Id  : {upsertId}")
    
f.close()