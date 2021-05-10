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
        rand = random.random()

        if dungeon.level == 1:
            if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
                if rand < 0.2:
                    entity_factories.glottal_stop.spawn(dungeon, x, y)
                elif rand < 0.4:
                    entity_factories.voiceless_glottal_fricative.spawn(dungeon, x, y)
                elif rand < 0.6:
                    entity_factories.voiced_glottal_fricative.spawn(dungeon, x, y)
                elif rand < 0.8:
                    entity_factories.voiceless_pharyngeal_fricative.spawn(dungeon, x, y)
                else:
                    entity_factories.voiced_pharyngeal_fricative.spawn(dungeon, x, y)

        elif dungeon.level == 2:
            if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
                if rand < 0.1667:
                    entity_factories.voiced_uvular_stop.spawn(dungeon, x, y)
                elif rand < 0.3333:
                    entity_factories.voiced_uvular_stop.spawn(dungeon, x, y)
                elif rand < 0.5:
                    entity_factories.voiced_uvular_nasal.spawn(dungeon, x, y)
                elif rand < 0.6667:
                    entity_factories.voiced_uvular_trill.spawn(dungeon, x, y)
                elif rand < 0.8333:
                    entity_factories.voiceless_uvular_fricative.spawn(dungeon, x, y)
                else:
                    entity_factories.voiced_uvular_fricative.spawn(dungeon, x, y)

        elif dungeon.level == 3:
            if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
                if rand < 0.1428:
                    entity_factories.voiceless_velar_stop.spawn(dungeon, x, y)
                elif rand < 0.2857:
                    entity_factories.voiced_velar_stop.spawn(dungeon, x, y)
                elif rand < 0.4286:
                    entity_factories.voiced_velar_nasal.spawn(dungeon, x, y)
                elif rand < 0.5714:
                    entity_factories.voiceless_velar_fricative.spawn(dungeon, x, y)
                elif rand < 0.7142:
                    entity_factories.voiced_velar_fricative.spawn(dungeon, x, y)
                elif rand < 0.8571:
                    entity_factories.voiced_velar_approximant.spawn(dungeon, x, y)
                else:
                    entity_factories.voiced_velar_lateral_approximant.spawn(dungeon, x, y)

        elif dungeon.level == 4:
            if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
                if rand < 0.1428:
                    entity_factories.voiceless_palatal_stop.spawn(dungeon, x, y)
                elif rand < 0.2857:
                    entity_factories.voiced_palatal_stop.spawn(dungeon, x, y)
                elif rand < 0.4286:
                    entity_factories.voiced_palatal_nasal.spawn(dungeon, x, y)
                elif rand < 0.5714:
                    entity_factories.voiceless_palatal_fricative.spawn(dungeon, x, y)
                elif rand < 0.7142:
                    entity_factories.voiced_palatal_fricative.spawn(dungeon, x, y)
                elif rand < 0.8571:
                    entity_factories.voiced_palatal_approximant.spawn(dungeon, x, y)
                else:
                    entity_factories.voiced_palatal_lateral_approximant.spawn(dungeon, x, y)

        elif dungeon.level == 5:
            if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
                if rand < 0.125:
                    entity_factories.voiceless_retroflex_stop.spawn(dungeon, x, y)
                elif rand < 0.25:
                    entity_factories.voiced_retroflex_stop.spawn(dungeon, x, y)
                elif rand < 0.375:
                    entity_factories.voiced_retroflex_nasal.spawn(dungeon, x, y)
                elif rand < 0.5:
                    entity_factories.voiced_retroflex_flap.spawn(dungeon, x, y)
                elif rand < 0.625:
                    entity_factories.voiceless_retroflex_fricative.spawn(dungeon, x, y)
                elif rand < 0.75:
                    entity_factories.voiced_retroflex_fricative.spawn(dungeon, x, y)
                elif rand < 0.875:
                    entity_factories.voiced_retroflex_approximant.spawn(dungeon, x, y)
                else:
                    entity_factories.voiced_retroflex_lateral_approximant.spawn(dungeon, x, y)

        elif dungeon.level == 6:
            if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
                if rand < 0.0667:
                    entity_factories.voiceless_alveolar_stop.spawn(dungeon, x, y)
                elif rand < 0.1333:
                    entity_factories.voiced_alveolar_stop.spawn(dungeon, x, y)
                elif rand < 0.2:
                    entity_factories.voiced_alveolar_nasal.spawn(dungeon, x, y)
                elif rand < 0.2667:
                    entity_factories.voiced_alveolar_trill.spawn(dungeon, x, y)
                elif rand < 0.3333:
                    entity_factories.voiced_alveolar_flap.spawn(dungeon, x, y)
                elif rand < 0.4:
                    entity_factories.voiceless_dental_fricative.spawn(dungeon, x, y)
                elif rand < 0.4667:
                    entity_factories.voiced_dental_fricative.spawn(dungeon, x, y)
                elif rand < 0.5333:
                    entity_factories.voiceless_alveolar_fricative.spawn(dungeon, x, y)
                elif rand < 0.6:
                    entity_factories.voiced_alveolar_fricative.spawn(dungeon, x, y)
                elif rand < 0.6667:
                    entity_factories.voiceless_postalveolar_fricative.spawn(dungeon, x, y)
                elif rand < 0.7333:
                    entity_factories.voiced_postalveolar_fricative.spawn(dungeon, x, y)
                elif rand < 0.8:
                    entity_factories.voiceless_alveolar_lateral_fricative.spawn(dungeon, x, y)
                elif rand < 0.8667:
                    entity_factories.voiced_alveolar_lateral_fricative.spawn(dungeon, x, y)
                elif rand < 0.9333:
                    entity_factories.voiced_alveolar_approximant.spawn(dungeon, x, y)
                else:
                    entity_factories.voiced_alveolar_lateral_approximant.spawn(dungeon, x, y)

        if dungeon.level == 7:
            if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
                if rand < 0.2:
                    entity_factories.voiced_labiodental_nasal.spawn(dungeon, x, y)
                elif rand < 0.4:
                    entity_factories.voiced_labiodental_flap.spawn(dungeon, x, y)
                elif rand < 0.6:
                    entity_factories.voiceless_labiodental_fricative.spawn(dungeon, x, y)
                elif rand < 0.8:
                    entity_factories.voiced_labiodental_fricative.spawn(dungeon, x, y)
                else:
                    entity_factories.voiced_labiodental_approximant.spawn(dungeon, x, y)

        elif dungeon.level == 8:
            if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
                if rand < 0.1667:
                    entity_factories.voiceless_bilabial_stop.spawn(dungeon, x, y)
                elif rand < 0.3333:
                    entity_factories.voiced_bilabial_stop.spawn(dungeon, x, y)
                elif rand < 0.5:
                    entity_factories.voiced_bilabial_nasal.spawn(dungeon, x, y)
                elif rand < 0.6667:
                    entity_factories.voiced_bilabial_trill.spawn(dungeon, x, y)
                elif rand < 0.8333:
                    entity_factories.voiceless_bilabial_fricative.spawn(dungeon, x, y)
                else:
                    entity_factories.voiced_bilabial_fricative.spawn(dungeon, x, y)

    for i in range(number_of_items):
        x = random.randint(room.x1 + 1, room.x2 - 1)
        y = random.randint(room.y1 + 1, room.y2 - 1)

        if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
            rand_potion = random.random()
            if dungeon.level == 1 or dungeon.level == 2:
                if rand_potion < 0.5:
                    entity_factories.open_front_unrounded_vowel.spawn(dungeon, x, y)
                else:
                    entity_factories.open_back_unrounded_vowel.spawn(dungeon, x, y)
            elif dungeon.level == 3 or dungeon.level == 4:
                if rand_potion < 0.5:
                    entity_factories.open_mid_front_unrounded_vowel.spawn(dungeon, x, y)
                else:
                    entity_factories.open_mid_back_unrounded_vowel.spawn(dungeon, x, y)
            elif dungeon.level == 5 or dungeon.level == 6:
                if rand_potion < 0.5:
                    entity_factories.close_mid_front_unrounded_vowel.spawn(dungeon, x, y)
                else:
                    entity_factories.close_mid_back_unrounded_vowel.spawn(dungeon, x, y)
            else:
                if rand_potion < 0.5:
                    entity_factories.close_front_unrounded_vowel.spawn(dungeon, x, y)
                else:
                    entity_factories.close_back_unrounded_vowel.spawn(dungeon, x, y)


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
    level,
    map_width: int,
    map_height: int,
    max_monsters_per_room: int,
    max_items_per_room: int,
    engine: Engine,
    ) -> GameMap:

    rooms: List[RectangularRoom] = []

    center_of_last_room = (0, 0)

    player = engine.player
    dungeon = GameMap(level, engine, map_width, map_height, entities=[player])

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
    last_room = random.choice(rooms)
    max_distance = abs(last_room.center[0] - player.x) + abs(last_room.center[1] - player.y)

    for room in rooms:
        if room != player_room:
            place_entities(room, dungeon, max_monsters_per_room, max_items_per_room)
            distance = abs(room.center[0] - player.x) + abs(room.center[1] - player.y)
            if distance > max_distance:
                last_room = room
                max_distance = distance

    center_of_last_room = last_room.center
    dungeon.tiles[center_of_last_room] = tile_types.down_stairs
    dungeon.downstairs_location = center_of_last_room

    return dungeon