import digitalocean
import argparse
import environ

env = environ.Env()
environ.Env.read_env()

#DEBUG = env.bool('DEBUG', default=False)
def main():
    droplet = digitalocean.Droplet(token=env.str('token'),
        name=env.str('name'),
        region=env.str('region'),
        image=env.str('image'),
        size_slug=env.str('size_slug'),
        backups=env.str('backups'))
    droplet.create()

if __name__ == "__main__":
    main()

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
