import digitalocean
import argparse

from decouple import config

droplet = digitalocean.Droplet(token='token',
name='name',
region='region',
image='image',
size_slug='size_slug',
backups='backups')

droplet.create()
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

