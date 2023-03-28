import digitalocean
import environ
from dotenv import load_dotenv

env_path = '../.env'
load_dotenv(dotenv_path=env_path)

env = environ.Env()
environ.Env.read_env()

def create_do():
    droplet = digitalocean.Droplet(token=env.str('token'),
        name=env.str('name'),
        region=env.str('region'),
        image=env.str('image'),
        size_slug=env.str('size_slug'),
        backups=env.str('backups'))
    droplet.create()


#if __name__ == "__main__":
#    create()