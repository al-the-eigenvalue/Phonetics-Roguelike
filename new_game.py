from __future__ import annotations

import copy

import color
from engine import Engine
from game_map import GameWorld


def start() -> Engine:
    """Return a brand new game session as an Engine instance."""
    map_width = 80
    map_height = 45

    max_monsters_per_room = 2
    max_items_per_room = 2

    import entity_factories
    player = copy.deepcopy(entity_factories.player)

    engine = Engine(player=player)

    engine.game_world = GameWorld(
        engine=engine,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        max_items_per_room=max_items_per_room,
    )

    engine.game_world.generate_floor()
    engine.update_fov()

    engine.message_log.add_message(
        "Welcome to the phonetics course!", color.welcome_text
    )
    return engine
