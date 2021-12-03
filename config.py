from pathlib import Path

Base_DIR = Path(__file__).parent
print(Base_DIR)


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' +str(Base_DIR.joinpath('db.sqlite'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False