from setuptools import setup


setup(
    name="mobcrush",
    version="0.1.0",
    description="Python Mobcrush API Wrapper",
    author="Jay Nagpaul",
    author_email="spieswithin@gmail.com",
    url="https://github.com/jaynagpaul/mobcrush",
    packages=["mobcrush"],
    install_requires=["requests"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    license="MIT"
)
