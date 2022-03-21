import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="playersMindset",
    version="0.0.1b",
    author="Bjorn Goriatcheff",
    author_email="bjorn.goriatcheff@gmail.com",
    description="A simplet yet effective program to search in a graph-like problem for the longuest set of connected components",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    package_data={'data':['data/default/*.txt'], },

    install_requires=['numpy'],
    python_requires=">=3.6",
)

