import tcod

import traceback

import exceptions
import input_handlers
import color
import setup_game


def save_game(handler: input_handlers.BaseEventHandler, filename: str) -> None:
    """If the current event handler has an active Engine then save it."""
    if isinstance(handler, input_handlers.EventHandler):
        handler.engine.save_as(filename)
        print("Game saved.")


def main() -> None:
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "tiles.png", 32, 15, tcod.tileset.CHARMAP_TCOD
    )

    tileset.remap(0x2591, 0, 5)
    tileset.remap(0x2592, 1, 5)
    tileset.remap(0x2593, 2, 5)
    tileset.remap(0xC7, 3, 5)
    tileset.remap(0xFC, 4, 5)

    tileset.remap(0xE9, 0, 6)
    tileset.remap(0xE2, 1, 6)
    tileset.remap(0xE4, 2, 6)
    tileset.remap(0xE0, 3, 6)
    tileset.remap(0xE5, 4, 6)
    tileset.remap(0xE7, 5, 6)
    tileset.remap(0xEA, 6, 6)

    tileset.remap(0xEB, 0, 7)
    tileset.remap(0xE8, 1, 7)
    tileset.remap(0xEF, 2, 7)
    tileset.remap(0xEE, 3, 7)
    tileset.remap(0xEC, 4, 7)
    tileset.remap(0xC4, 5, 7)

    tileset.remap(0xC5, 0, 8)
    tileset.remap(0xC9, 1, 8)
    tileset.remap(0xE6, 2, 8)
    tileset.remap(0xC6, 3, 8)
    tileset.remap(0xF4, 4, 8)
    tileset.remap(0xF6, 5, 8)
    tileset.remap(0xF2, 6, 8)

    tileset.remap(0xFB, 0, 9)
    tileset.remap(0xF9, 1, 9)
    tileset.remap(0xFF, 2, 9)
    tileset.remap(0xD6, 3, 9)
    tileset.remap(0xDC, 4, 9)
    tileset.remap(0xA2, 5, 9)
    tileset.remap(0xA3, 6, 9)
    tileset.remap(0xA5, 7, 9)

    tileset.remap(0x20A7, 0, 10)
    tileset.remap(0x0192, 1, 10)
    tileset.remap(0xE1, 2, 10)
    tileset.remap(0xED, 3, 10)
    tileset.remap(0xF3, 4, 10)
    tileset.remap(0xFA, 5, 10)
    tileset.remap(0xF1, 6, 10)
    tileset.remap(0xD1, 7, 10)
    tileset.remap(0xAA, 8, 10)
    tileset.remap(0xBA, 9, 10)
    tileset.remap(0xBF, 10, 10)
    tileset.remap(0xB5, 11, 10)
    tileset.remap(0x03C4, 12, 10)
    tileset.remap(0x03A6, 13, 10)
    tileset.remap(0x0398, 14, 10)

    tileset.remap(0x2310, 0, 11)
    tileset.remap(0xAC, 1, 11)
    tileset.remap(0xBD, 2, 11)
    tileset.remap(0xBC, 3, 11)
    tileset.remap(0xA1, 4, 11)

    tileset.remap(0x03B1, 0, 12)
    tileset.remap(0xDF, 1, 12)
    tileset.remap(0x0393, 2, 12)
    tileset.remap(0x03C0, 3, 12)
    tileset.remap(0x03A3, 4, 12)
    tileset.remap(0x03C3, 5, 12)

    handler: input_handlers.BaseEventHandler = setup_game.MainMenu()

    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title="Phonetics Roguelike",
            renderer=tcod.RENDERER_SDL2,
            vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        try:
            while True:
                root_console.clear()
                handler.on_render(console=root_console)
                context.present(root_console)

                try:
                    for event in tcod.event.wait():
                        context.convert_event(event)
                        handler = handler.handle_events(event)
                except Exception:  # Handle exceptions in game.
                    traceback.print_exc()  # Print error to stderr.
                    # Then print the error to the message log.
                    if isinstance(handler, input_handlers.EventHandler):
                        handler.engine.message_log.add_message(
                            traceback.format_exc(), color.error
                        )
        except exceptions.QuitWithoutSaving:
            raise
        except SystemExit:  # Save and quit.
            save_game(handler, "savegame.sav")
            raise
        except BaseException:  # Save on any other unexpected exception.
            save_game(handler, "savegame.sav")
            raise


if __name__ == "__main__":
    main()
