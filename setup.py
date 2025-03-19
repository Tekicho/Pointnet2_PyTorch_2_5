import os.path as osp

from setuptools import find_packages, setup

requirements = ["hydra-core==0.11.3", "pytorch-lightning==0.7.1"]
installable_packages= find_packages()
print(f"Packages to be installed: {installable_packages}")

exec(open(osp.join("pointnet2", "_version.py")).read())

setup(
    name="pointnet2_ops_lib",
    version=__version__,
    author="Erik Wijmans",
    packages=find_packages(),
    install_requires=requirements,
)
