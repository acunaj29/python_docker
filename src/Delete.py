import digitalocean
import environ
from dotenv import load_dotenv
from status import status

env_path = '../.env'
load_dotenv(dotenv_path=env_path)

env = environ.Env()
environ.Env.read_env()


def delete():
    list=(status())
    print(list)

    valor=(int(input("Id to Delete:")))

    manager = digitalocean.Manager(token=env.str('token'))

    droplet_name = valor
    droplet = manager.get_droplet(droplet_name)

    droplet.destroy()