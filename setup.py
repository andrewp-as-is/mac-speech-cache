import setuptools

setuptools.setup(
    name='mac-speech-cache',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/speech-cache']
)
