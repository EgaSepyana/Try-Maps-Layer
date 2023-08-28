from fastapi import APIRouter
from src.util.db.pyMongo.mopy import MongoConnection
from geojson2vt.geojson2vt import geojson2vt
from mercantile import Tile
from fastapi import Depends
from .util import tile_params
from .util import response_to_geojson
from vt2pbf import vt2pbf
from fastapi.responses import Response

class NewGeojsonController():
    
    def __init__(self):
        self.__router = APIRouter(prefix="/api/v1/geojson", tags=["Geojson"])
        self._con:MongoConnection = MongoConnection.NewMongoConnectionLocal("indonesian-prov")

    def GetRouter(self) -> APIRouter:

        
        @self.__router.get("/get-province")
        def Generate_province_geojson(province:str):
           query = {"provice_name" : province} 
           return response_to_geojson(self._con.FindWitoutPagging( query ))

        @self.__router.get("/get-province-as-mvt/{z}/{x}/{y}/")
        def Generate_province_as_mvt(
            tile: Tile = Depends(tile_params)
        ):
            tile_index = geojson2vt(response_to_geojson(self._con.FindWitoutPagging()) , {})

            vt = tile_index.get_tile(tile.z , tile.x , tile.y)

            return Response(bytes(vt2pbf(vt)) , media_type="application/x-protobuf")

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