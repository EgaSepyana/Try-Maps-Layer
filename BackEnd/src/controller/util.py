from mercantile import Tile
from fastapi import Path

def tile_params(
        z: int = Path(..., ge=0, le=25,),
        x: int = Path(...),
        y: int = Path(...),
    ) -> Tile:
        """Tile parameters."""
        return Tile(x, y, z)

def response_to_geojson(data: list):
    feature = []
    
    for i in data:
          if i.get("geom"):
                feature.append(i['geom'])
            
    return {
          "type" : "FeatureCollection",
          "features" : feature
    }