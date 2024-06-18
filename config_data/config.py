from dataclasses import dataclass

@dataclass
class DataBaseConfig:
    database: str           # Название БД
    db_host: str            # URL-адрес БД
    db_user: str            # Username пользователя БД
    db_password: str        # Пароль к БД


@dataclass
class TgBot:
    token: str              # Токен для доступа к телеграм-боту
    admin_ids: list[int]    # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DataBaseConfig 