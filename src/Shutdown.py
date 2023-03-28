import digitalocean
import environ
from dotenv import load_dotenv

env_path = '../.env'
load_dotenv(dotenv_path=env_path)

env = environ.Env()
environ.Env.read_env()

def shutdown():
    manager = digitalocean.Manager(token=env.str('token'))
    my_droplets = manager.get_all_droplets()
    for droplet in my_droplets:
        droplet.shutdown()