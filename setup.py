import os
from setuptools import setup, find_packages

dir_path = os.path.dirname(os.path.realpath(__file__))

VERSION = open(os.path.join(dir_path, 'VERSION')).read()

setup(
  name = 'generic-encoders',
  packages = find_packages(),
  version = VERSION,
  description = '''
  A set of encoders which provide a simple string/byte based interface.
  ''',
  long_description=open(os.path.join(dir_path, 'README.md')).read(),
  long_description_content_type='text/markdown',
  author = 'Marco Montagna',
  author_email = 'marcojoemontagna@gmail.com',
  url = 'https://github.com/mmontagna/generic-encoders',
  keywords = ['encoders', 'gzip', 'compression', 'decompression'],
  classifiers=(
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Natural Language :: English',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
  ),
  data_files = [('', ['LICENSE', 'VERSION', 'README.md'])],
  include_package_data=True,
  python_requires=">=2.7",
  license=open(os.path.join(dir_path, 'LICENSE')).read(),
  install_requires=[
    "six>=1.9.0",
    "lz4~=1.0.0",
    "dill~=0.2.5",
    "msgpack~=0.5.6",
    "simplejson>=3.8.0",
  ],
  extras_require={
      'avro':  ["fastavro~=0.21.7"],
      'dev':  ["fastavro~=0.21.7"],
  },
  entry_points = {
  },
)