import digitalocean
import environ
from dotenv import load_dotenv

env_path = '../.env'
load_dotenv(dotenv_path=env_path)

env = environ.Env()
environ.Env.read_env()

def status():
    manager = digitalocean.Manager(token=env.str('token'))
    if manager.get_all_droplets() == []:
        return("No existen Droplets")
    else:
        #print(manager.get_all_droplets())
    
        return(manager.get_all_droplets())