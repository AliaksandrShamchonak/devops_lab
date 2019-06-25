import sys
import platform
import subprocess
import site
import json
import yaml

sver = platform.python_version()
print("Version", sver)
spref = sys.prefix
print("Virtual environment", spref)
sbpref = sys.base_exec_prefix
print("Python executable location", sys.base_exec_prefix)
subrun = subprocess.run(['which', 'pip'], stdout=subprocess.PIPE)
subrun = subrun.stdout.decode('utf-8').split('\n')[0]
print("PIP location", subrun)
spath = sys.path
print("PYTHONPATH", spath)
sinst = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)
sinst = sinst.stdout.decode('utf-8').split('\n')
print("Installed packages", sinst)
spack = site.getsitepackages()
print("Site-packages location", spack)

jsondata = {
    "Version": sver,
    "Virtual environment": spref,
    "Python executable location": sbpref,
    "PIP location": subrun,
    "PYTHONPATH": spath,
    "Installed packages": sinst,
    "Site-packages location": spack
}
with open('output.json', 'w') as f:
    f.write(json.dumps(jsondata, indent=4))

yamldata = {
    "Version": sver,
    "Virtual environment": spref,
    "Python executable location": sbpref,
    "PIP location": subrun,
    "PYTHONPATH": spath,
    "Installed packages": sinst,
    "Site-packages location": spack
}
with open('output.yml', 'w') as f:
    yaml.dump(yamldata, f)
