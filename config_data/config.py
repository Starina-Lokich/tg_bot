from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str  # Telegram bot token


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    evn = Env()
    evn.read_env(path)
    return Config(tg_bot=TgBot(token=evn.get('BOT_TOKEN')))