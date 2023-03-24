import digitalocean
import argparse

def digital():
    droplet = digitalocean.Droplet(token="dop_v1_ba1850a51a5f9cc02a917f950e1376120dd957151d6541bb468f4979c5968ff5",
    name='Acunadroplet',
    region='nyc1',
    image='ubuntu-22-10-x64',
    size_slug='s-1vcpu-1gb',
    backups=True)

    droplet.create()

#if __name__ == '__main--':
digital()



##manager = digitalocean.Manager(token="dop_v1_ba1850a51a5f9cc02a917f950e1376120dd957151d6541bb468f4979c5968ff5")
##print(manager.get_all_droplets())



## 0. https://pypi.org/project/python-digitalocean/                   pip3 install -U python-digitalocean
## 1. https://docs.digitalocean.com/reference/doctl/how-to/install/   brew install doctl
## 2. https://docs.digitalocean.com/tutorials/build-deploy-first-image/

