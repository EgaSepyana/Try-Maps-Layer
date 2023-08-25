from fastapi import APIRouter
from src.util.db.pyMongo.mopy import MongoConnection
from .util import response_to_geojson

class NewGeojsonController():
    
    def __init__(self):
        self.__router = APIRouter(prefix="/api/v1/geojson", tags=["Geojson"])
        self._con:MongoConnection = MongoConnection.NewMongoConnectionLocal("indonesian-prov")

    def GetRouter(self) -> APIRouter:

        
        @self.__router.get("/get-province")
        def Generate_province_geojson(province:str):
           query = {"provice_name" : province} 
           return response_to_geojson(self._con.FindWitoutPagging( query ))

        @self.__router.get("/get-province-as-mvt")
        def Generate_province_as_mvt():
            pass

        @self.__router.get("/get-color-province")
        def Get_color_province():
            colors = [
                "#FF5733", "#FFC300", "#36DBCA", "#FF85A1", "#FFAC81", "#FFD700", "#FF6347", "#FF3E96",
                "#FF69B4", "#FF1493", "#FF00FF", "#9400D3", "#8A2BE2", "#4B0082", "#0000FF", "#00BFFF",
                "#1E90FF", "#00CED1", "#20B2AA", "#32CD32", "#00FF00", "#7CFC00", "#FFFF00", "#FFD700",
                "#FFA500", "#FF8C00", "#FF4500", "#FF0000", "#DC143C", "#FF69B4", "#FF1493", "#C71585"
            ]

            data = self._con.FindWitoutPagging()


            province_with_color = []


            for i in range(len(colors)):
                province_with_color.append(
                    {
                        "province" : data[i]['provice_name'],
                        "color" : colors[i]
                    }
                )


            return province_with_color
        
 
        @self.__router.get("/get-all-province")
        def Get_color_province():
            return response_to_geojson(self._con.FindWitoutPagging())


        return self.__router