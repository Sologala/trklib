from setuptools import setup, find_packages
import subprocess
# 调用子项目的 setup.py


subprocess.check_call(
    ["python", "setup.py", "build_ext", "--inplace"],
    cwd="./pyCFTrackers/lib/eco/features"
)
subprocess.check_call(
    ["python", "setup.py", "build_ext", "--inplace"],
    cwd="./pyCFTrackers/lib/pysot/utils"
)

setup(
    name='pyCFTrackers',
    version='0.0.1',
    install_requires=[
        "matplotlib",
        "mxnet",
        "numba",
        "scipy",
        "h5py",
        "colorama",
        "opencv_python",
        "Cython",
        "numpy",
        "tqdm",
        "Pillow",
        "scikit-image"
    ],
    packages=find_packages(
    ),
)
