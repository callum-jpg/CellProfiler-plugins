from setuptools import setup
import setuptools

install_deps = [
    "cellprofiler",
    "cellprofiler-core",
            ]

cellpose_deps = [
    "cellpose>=1.0.2"
]

omnipose_deps = [
    "omnipose",
    "ncolor"
]

stardist_deps = [
    "tensorflow",
    "stardist"
]

setup(
    name="cellprofiler_plugins",
    packages=setuptools.find_packages(),
    install_requires = install_deps,
    extras_require = {
      "cellpose": cellpose_deps,
      "omnipose": omnipose_deps,
      "stardist": stardist_deps,
    }
)