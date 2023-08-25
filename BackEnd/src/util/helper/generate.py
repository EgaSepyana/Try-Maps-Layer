def generate_envelope(x: int, y: int, z: int) -> dict:
    world_max = 20037508.3427892
    world_min = -1 * world_max
    world_size = world_max - world_min
    world_tile_size = 2 ** z
    tile_size = world_size / world_tile_size
    return {
        'x_min': world_min + tile_size * x,
        'x_max': world_min + tile_size * (x + 1),
        'y_min': world_max - tile_size * (y + 1),
        'y_max': world_max - tile_size * y
    }

def get_color(province):
    pass