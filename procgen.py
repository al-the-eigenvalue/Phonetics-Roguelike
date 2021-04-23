from __future__ import annotations

import random
from typing import Iterator, List, Tuple
import tcod

import entity_factories
from game_map import GameMap
import tile_types
from engine import Engine

DEPTH = 6
MIN_SIZE = 5
map_width = 80
map_height = 50
used = set()


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


def place_entities(
    room: RectangularRoom, dungeon: GameMap, maximum_monsters: int, maximum_items: int
) -> None:
    number_of_monsters = random.randint(0, maximum_monsters)
    number_of_items = random.randint(0, maximum_items)

    for i in range(number_of_monsters):
        x = random.randint(room.x1 + 1, room.x2 - 1)
        y = random.randint(room.y1 + 1, room.y2 - 1)

        if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
            if random.random() < 0.2:
                entity_factories.glottal_stop.spawn(dungeon, x, y)
            elif random.random() < 0.4:
                entity_factories.voiceless_glottal_fricative.spawn(dungeon, x, y)
            elif random.random() < 0.6:
                entity_factories.voiced_glottal_fricative.spawn(dungeon, x, y)
            elif random.random() < 0.8:
                entity_factories.voiceless_pharyngeal_fricative.spawn(dungeon, x, y)
            else:
                entity_factories.voiced_pharyngeal_fricative.spawn(dungeon, x, y)

    for i in range(number_of_items):
        x = random.randint(room.x1 + 1, room.x2 - 1)
        y = random.randint(room.y1 + 1, room.y2 - 1)

        if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
            entity_factories.health_potion.spawn(dungeon, x, y)


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


def traverse_node(node, map, rooms):

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
    max_monsters_per_room: int,
    max_items_per_room: int,
    engine: Engine,
    ) -> GameMap:

    rooms: List[RectangularRoom] = []

    player = engine.player
    dungeon = GameMap(engine, map_width, map_height, entities=[player])

    # New root node
    bsp = tcod.bsp.BSP(0, 0, map_width - 3, map_height - 3)

    # Split into nodes
    bsp.split_recursive(DEPTH, MIN_SIZE + 1, MIN_SIZE + 1, 1.5, 1.5)

    # Traverse the nodes and create rooms
    order = bsp.inverted_level_order()
    for node in order:
        traverse_node(node, dungeon, rooms)

    player_room = random.choice(rooms)
    player.place(*player_room.center, dungeon)
    for room in rooms:
        if room != player_room:
            place_entities(room, dungeon, max_monsters_per_room, max_items_per_room)
    return dungeon