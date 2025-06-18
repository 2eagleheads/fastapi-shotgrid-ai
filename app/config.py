from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    shotgrid_url: str
    shotgrid_script_name: str
    shotgrid_script_key: str

    class Config:
        env_file = ".env"

settings = Settings()
