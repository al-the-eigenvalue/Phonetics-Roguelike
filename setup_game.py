"""Handle the loading and initialization of game sessions."""
from __future__ import annotations

import copy
import lzma
import pickle
import traceback
from typing import Optional

import tcod

import color
import new_game
from engine import Engine
import input_handlers


# Load the background image and remove the alpha channel.
background_image = tcod.image.load("background.png")[:, :, :3]


def load_game(filename: str) -> Engine:
    """Load an Engine instance from a file."""
    with open(filename, "rb") as f:
        engine = pickle.loads(lzma.decompress(f.read()))
    assert isinstance(engine, Engine)
    return engine


class MainMenu(input_handlers.BaseEventHandler):
    """Handle the main menu rendering and input."""

    def on_render(self, console: tcod.Console) -> None:
        """Render the main menu on a background image."""
        console.draw_semigraphics(background_image, 0, 0)

        console.print(
            console.width // 2,
            console.height // 2 - 4,
            "PHONETICS ROGUELIKE",
            fg=color.menu_title,
            bg=color.black,
            alignment=tcod.CENTER,
            bg_blend=tcod.BKGND_ALPHA(64),
        )
        console.print(
            console.width // 2,
            console.height - 2,
            "By @entrapolarity, @chenopodiumlang, and @esil-11",
            fg=color.menu_title,
            bg=color.black,
            alignment=tcod.CENTER,
            bg_blend=tcod.BKGND_ALPHA(64),
        )

        menu_width = 24
        for i, text in enumerate(
            ["(N) Play a new game", "(C) Continue last game", "(H) Help", "(Q) Quit"]
        ):
            console.print(
                console.width // 2,
                console.height // 2 - 2 + i,
                text.ljust(menu_width),
                fg=color.menu_text,
                bg=color.black,
                alignment=tcod.CENTER,
                bg_blend=tcod.BKGND_ALPHA(64),
            )

    def ev_keydown(
        self, event: tcod.event.KeyDown
    ) -> Optional[input_handlers.BaseEventHandler]:
        if event.sym in (tcod.event.K_q, tcod.event.K_ESCAPE):
            raise SystemExit()
        elif event.sym == tcod.event.K_c:
            try:
                return input_handlers.MainGameEventHandler(load_game("savegame.sav"))
            except FileNotFoundError:
                return input_handlers.PopupMessage(self, "No saved game to load.")
            except Exception as exc:
                traceback.print_exc()  # Print to stderr.
                return input_handlers.PopupMessage(self, f"Failed to load save:\n{exc}")
            pass
        elif event.sym == tcod.event.K_h:
            return input_handlers.PopupMessage(self, "Welcome to Phonetics Roguelike!\n\nIn this game, you need to "
                                                     "find your way out of a human`s oral cavity.\nConsonants will "
                                                     "try to hinder you, and vowels will help you.\n\nControls:\n[Y]["
                                                     "K][U]                                   \n[H]   [L] - movements "
                                                     "(arrow keys also work!)\n[B][J][N]                              "
                                                     "     \n[Q] - open this menu\n[C] - show character info\n[G] - "
                                                     "grab item\n[D] - drop item\n[I] - open inventory\n[V] - show "
                                                     "message history\n[Shift] + [.] (i.e. [>]) - move to next "
                                                     "level\n\nGood luck!\n\n", 18)
        elif event.sym == tcod.event.K_n:
            return input_handlers.MainGameEventHandler(new_game.start())

        return None