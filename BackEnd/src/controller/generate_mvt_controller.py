from fastapi import APIRouter
from mercantile import Tile
from src.util.helper.generate import generate_envelope
from fastapi import Depends
from .util import tile_params
from fastapi.responses import Response
from src.util.db.sqlpy.sqlpy import sesion

class NewMvtController():
    def __init__(self):
        self.__router = APIRouter(prefix="/api/v1/mvt", tags=["Mvt"])

    def GetRouter(self) -> APIRouter:
        
        @self.__router.get("/get-all-province/{z}/{x}/{y}/")
        def Get_MVT(
                tile: Tile = Depends(tile_params),  # FastAPI magic: receives x/y/z
        ):
            
            envelope = generate_envelope(tile.x , tile.y , tile.z)


            bound = f'ST_Segmentize(ST_MakeEnvelope({envelope.get("x_min")}, {envelope.get("y_min")}, 'f'{envelope.get("x_max")}, {envelope.get("y_max")}, 3857),' \
                        f'{(envelope.get("x_max") - envelope.get("x_min")) / 4})'
            
            query_tmp = f'''
                WITH 
                    bounds AS (
                        SELECT 
                            {bound} AS geom,
                            {bound}::box2d AS b2d
                    ),
                    datas AS (
                        SELECT
                            *
                        FROM
                            indonesia_prov
                    ),
                    mvtgeom AS (
                        SELECT 
                            ST_AsMVTGeom(ST_Transform(datas.geometry , 3857) , bounds.b2d) AS geom, 
                            datas.*
                        FROM
                            bounds,
                            datas
                        WHERE
                            datas.geometry && ST_Transform(bounds.geom, 4326)
                    )
                SELECT 
                    ST_AsMVT(mvtgeom.*, 'geojsonLayer')
                FROM 
                    mvtgeom
            ''' 

            # print(query_tmp)
            # print(bound)

            res = sesion.execute(query_tmp).first()

            return Response(bytes(res[0]) , media_type="application/x-protobuf")
            
        @self.__router.get("/get-province/{z}/{x}/{y}/")
        def Get_MVT(
                province : str,
                layer_name: str,
                tile: Tile = Depends(tile_params),  # FastAPI magic: receives x/y/z
        ):
            envelope = generate_envelope(tile.x , tile.y , tile.z)
            bound = f'ST_Segmentize(ST_MakeEnvelope({envelope.get("x_min")}, {envelope.get("y_min")}, 'f'{envelope.get("x_max")}, {envelope.get("y_max")}, 3857),' \
                        f'{(envelope.get("x_max") - envelope.get("x_min")) / 4})'
            
            query_tmp = f'''
                WITH 
                    bounds AS (
                        SELECT 
                            {bound} AS geom,
                            {bound}::box2d AS b2d
                    ),
                    datas AS (
                        SELECT
                            *
                        FROM
                            indonesia_prov
                        WHERE
                            propinsi='{province}'
                    ),
                    mvtgeom AS (
                        SELECT 
                                ST_AsMVTGeom(ST_Transform(datas.geometry , 3857) , bounds.b2d) AS geom, 
                                datas.*
                        FROM
                            bounds,
                            datas
                        WHERE
                            datas.geometry && ST_Transform(bounds.geom, 4326)
                    )
                SELECT 
                    ST_AsMVT(mvtgeom.*, '{layer_name}')
                FROM 
                    mvtgeom
            ''' 

            # print(query_tmp)
            # print(bound)

            res = sesion.execute(query_tmp).first()

            return Response(bytes(res[0]) , media_type="application/x-protobuf")


        @self.__router.get("/color-province/")
        def Get_Color_province():
            req = sesion.execute("SELECT propinsi FROM indonesia_prov").fetchall()

            colors = [
                "#FF5733", "#C70039", "#900C3F", "#581845",
                "#4CAF50", "#8BC34A", "#FFC107", "#FF9800",
                "#2196F3", "#3F51B5", "#9C27B0", "#673AB7",
                "#E91E63", "#F44336", "#795548", "#607D8B",
                "#00BCD4", "#03A9F4", "#FF5722", "#9E9E9E",
                "#8E44AD", "#2ECC71", "#3498DB", "#E74C3C",
                "#F39C12", "#D35400", "#16A085", "#2980B9",
                "#1ABC9C", "#34495E", "#27AE60", "#E67E22"
            ]

            province_with_color = []

            for i in range(len(colors)):
                province_with_color.append({
                    "province" : req[i][0],
                    "color" : colors[i]
                })

            return province_with_color

        return self.__router
    