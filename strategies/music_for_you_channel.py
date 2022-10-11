import string

from config.daemon_config import DaemonConfig
from strategies.base import BaseChannelManager
from sanitize_filename import sanitize


class MusicForYouChannelStrategy(BaseChannelManager):

    def __init__(self, daemon_config: DaemonConfig):
        super().__init__(daemon_config)
        self._managed_channel: list[int] = [1449513897]

    def extract_folder_name(self, picture_message: string) -> string:
        print(f"Input message received: {picture_message}")
        print("Splitted output:")
        print(picture_message.splitlines())
        print(f"Resolved folder name: ", picture_message.splitlines()[1])
        return sanitize(picture_message.splitlines()[1])

    @property
    def managed_channel(self) -> list[int]:
        return self._managed_channel

