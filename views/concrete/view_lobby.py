import context
from config import config
from settings import settings
from views.concrete.view_base import ViewBase
from views.input_enum import Input
from views.view_enum import Views


class ViewLobby(ViewBase):
    def __init__(self):
        super().__init__()
        participant = context.GAME.lobby.get_local_participant()
        self.options = [
            ["READY", Views.LOBBY, lambda: context.GAME.toggle_ready_bc(), Input.SELECT],
            ["EXIT", Views.MENU, lambda: context.GAME.abandon_lobby(), Input.SELECT]
        ]

    def print_screen(self):
        self.print_text(context.GAME.lobby.address + ":" + str(context.GAME.lobby.port))

        players = context.GAME.lobby.participants
        for player in players:
            player_string = player.name + "[" + str(player.player_id) + "]"
            if player.ready:
                player_string += "[READY]"
            else:
                player_string += "[NOT READY]"

            print(player_string.center(settings["MAX_WIDTH"]))
        for i in range(config["MAX_PLAYERS"] - len(players)):
            print("free".center(settings["MAX_WIDTH"]))
        print("")
        self._print_options()
