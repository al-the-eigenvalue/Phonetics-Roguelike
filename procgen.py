from __future__ import annotations

import random
from typing import Iterator, List, Tuple
import tcod

from game_map import GameMap
import tile_types
from entity import Entity

DEPTH = 6
MIN_SIZE = 5
map_width = 80
map_height = 50
used = set()

rooms: List[RectangularRoom] = []

map = GameMap(map_width, map_height)


class RectangularRoom:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center(self) -> Tuple[int, int]:
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    @property
    def inner(self) -> Tuple[slice, slice]:
        """Return the inner area of this room as a 2D array index."""
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)


def tunnel_between(
    x1, x2, y1, y2
) -> Iterator[Tuple[int, int]]:
    """Return an L-shaped tunnel between these two points."""
    if random.random() < 0.5:  # 50% chance.
        # Move horizontally, then vertically.
        corner_x, corner_y = x2, y1
    else:
        # Move vertically, then horizontally.
        corner_x, corner_y = x1, y2

    # Generate the coordinates for this tunnel.
    for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
        yield x, y
    for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
        yield x, y


def traverse_node(node):

    # Create rooms
    if not node.children:
        minx = node.x + 1
        maxx = node.x + node.w - 1
        miny = node.y + 1
        maxy = node.y + node.h - 1

        if maxx == map_width - 1:
            maxx -= 1
        if maxy == map_width - 1:
            maxy -= 1

        # If it's False the rooms sizes are random, else the rooms are filled to the node's size
        minx = random.randint(minx, maxx - MIN_SIZE + 1)
        miny = random.randint(miny, maxy - MIN_SIZE + 1)
        maxx = random.randint(minx + MIN_SIZE - 2, maxx)
        maxy = random.randint(miny + MIN_SIZE - 2, maxy)

        node.x = minx
        node.y = miny
        node.w = maxx - minx + 1
        node.h = maxy - miny + 1

        new_room = RectangularRoom(x=minx, y=miny, width=maxx - minx + 1, height=maxy - miny + 1)
        map.tiles[new_room.inner] = tile_types.floor
        rooms.append(new_room)


    # Create corridors
    else:

        left = node.children[0]

        right = node.children[1]

        rand = random.randint(0, 1)

        if node.level % 2 == 0:

            node.x = right.x
            node.y = right.y
            node.w = right.w
            node.h = right.h
        else:
            node.x = left.x
            node.y = left.y
            node.w = left.w
            node.h = left.h

        left_center_x = int(left.w / 2) + left.x
        left_center_y = int(left.h / 2) + left.y
        right_center_x = int(right.w / 2) + right.x
        right_center_y = int(right.h / 2) + right.y

        tunnel = tunnel_between(left_center_x, right_center_x, left_center_y, right_center_y)
        log = str(left_center_x) + str(left_center_y) + str(right_center_x) + str(right_center_y)
        if log not in used:
            for x, y in tunnel:
                map.tiles[x, y] = tile_types.floor
        used.update(log)



def generate_dungeon(
    map_width: int,
    map_height: int,
    entities,
    player: Entity
    ) -> GameMap:

    # New root node
    bsp = tcod.bsp.BSP(0, 0, map_width - 3, map_height - 3)

    # Split into nodes
    bsp.split_recursive(DEPTH, MIN_SIZE + 1, MIN_SIZE + 1, 1.5, 1.5)

    # Traverse the nodes and create rooms
    order = bsp.inverted_level_order()
    for node in order:
        traverse_node(node)

    player_room = random.choice(rooms)
    player.x = player_room.center[0]
    player.y = player_room.center[1]
    return map