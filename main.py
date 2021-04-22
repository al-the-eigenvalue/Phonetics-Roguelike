import tcod

from engine import Engine
from input_handlers import EventHandler
import copy
from procgen import generate_dungeon
import entity_factories


def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 50

    max_monsters_per_room = 2

    tileset = tcod.tileset.load_tilesheet(
        "tilestemporary.png", 32, 15, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = copy.deepcopy(entity_factories.player)

    game_map = generate_dungeon(
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        player=player
    )

    engine = Engine(event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title="Phonetics Roguelike",
            renderer=tcod.RENDERER_SDL2,
            vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()
