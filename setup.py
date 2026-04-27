from setuptools import setup, find_packages

setup(
    name="tf-iam",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "tf-iam=tf_iam.tf_runner:main",
        ],
    },
)
