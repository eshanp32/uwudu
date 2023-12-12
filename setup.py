""" (U w U)_/××××××  setup file  ××××××\_(U w U) """

from setuptools import setup, find_packages

setup(
    name="uwudu",
    version="1.0.0",
    description="your cli todo list manager (U w U)",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click", "prettytable"],
    keywords=["cli", "todo", "uwu", "todo list", "python", "python cli"],
    entry_points={
        "console_scripts": [
            "uwudu = uwudu.cli:cli",
        ],
    },
)
