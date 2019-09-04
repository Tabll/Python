from pip._internal.utils.misc import get_installed_distributions
from subprocess import call
for dist in get_installed_distributions():
    call("pip3.6 install --upgrade " + dist.project_name, shell=True)
