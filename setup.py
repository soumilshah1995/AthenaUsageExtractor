from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="athena-usage-metrics-extractor",
    version="1.2.0",
    description=""" Athena usage is simple python library that allows you to extract all usage information for given date range and for given workgroup """,
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/soumilshah1995/AppleStock",
    author="Soumil Nitin Shah",
    author_email="shahsoumil519@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["AthenaUsageExtractor"],
    include_package_data=True,
    install_requires=["dateparser", "boto3"]
)