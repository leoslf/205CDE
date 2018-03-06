from setuptools import setup

setup(
    name="app",
    packages=["app"],
    include_package_data=True,
    install_requires=[
        "flask", "pymysql", "virtualenv",
    ],
    setup_requires=[
        "pytest-runner",
    ],
    tests_require=[
        "pytest",
    ],
)

