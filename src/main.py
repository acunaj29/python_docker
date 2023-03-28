#import digitalocean
#import argparse
from create import create_do
from status import status
from Delete import delete
from Shutdown import shutdown

if __name__ == "__main__":
    seleccion = (int(input("Seleccion tarea: \n 1. Crear \n 2. Delete \n 3. Status\n 4. Shutdown\n 5. Exit \n 6.website\n #:")))
    if seleccion == 1:
        create_do()
    elif seleccion == 2:
        delete()
    elif seleccion == 3:
        print(status())
    elif seleccion == 4:
        shutdown()
    elif seleccion == 5:
        exit()
    else:
        exit()

"""CRUD = create, read,update, delete.
CLICK"""
#digital()
##manager = digitalocean.Manager(token="dop_v1_ba1850a51a5f9cc02a917f950e1376120dd957151d6541bb468f4979c5968ff5")
##my_droplets = manager.get_all_droplets()
##for droplet in my_droplets:
##    droplet.shutdown()

##manager = digitalocean.Manager(token="dop_v1_ba1850a51a5f9cc02a917f950e1376120dd957151d6541bb468f4979c5968ff5")
##print(manager.get_all_droplets())

## 0. https://pypi.org/project/python-digitalocean/                   pip3 install -U python-digitalocean
## 1. https://docs.digitalocean.com/reference/doctl/how-to/install/   brew install doctl
## 2. https://docs.digitalocean.com/tutorials/build-deploy-first-image/
## 3. https://docs.docker.com/language/python/build-images/
## 4. .env https://www.youtube.com/watch?v=932A03KymK4