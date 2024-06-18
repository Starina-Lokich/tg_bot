from dataclasses import dataclass
from environs import Env


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

    
def load_config(path: str | None = None) -> Config:
    
    env: Env = Env()    # Создаем экземляр класса Env    
    env.read_env(path)      # Добавляем в переменные окружения данные, прочитанные из файла .env

    # Создаем экземпляр класса Config и наполняем его данными из переменного окружения
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS')))
        ),
        db=DataBaseConfig(
            database=env('DATABASE'),
            db_host=env('DB_HOST'),
            db_password=env('DB_PASSWORD'),
            db_user=env('DB_USER')
        )
    )
