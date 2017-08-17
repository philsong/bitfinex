from setuptools import setup

version = '0.3.0'

# Runtime dependencies. See requirements.txt for development dependencies.
dependencies = [
    'requests',
    'httpretty'
]

setup(name='bitfinex',
    version=version,
    description = 'Python client for the Bitfinex API',
    author = 'Scott Barr',
    author_email = 'songbohr@gmail.com',
    url = 'https://github.com/philsong/bitfinex',
    license = 'MIT',
    packages=['bitfinex'],
    scripts=['scripts/bitfinex-poll-orderbook'],
    install_requires=dependencies,
    download_url='https://github.com/philsong/bitfinex/tarball/%s' % version,
    keywords=['bitcoin', 'btc'],
    classifiers=[],
    zip_safe=True)
