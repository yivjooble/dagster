from setuptools import find_packages, setup

setup(
    name="dagster_multi_etl",
    packages=find_packages(exclude=["dagster_multi_etl_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
