from setuptools import setup, find_packages

setup(
    name="uwudu",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click", "prettytable"],
    entry_points={
        "console_scripts": [
            "uwudu = uwudu.cli:cli",
        ],
    },
)
