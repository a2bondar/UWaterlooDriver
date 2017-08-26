from distutils.core import setup
setup(
  name = 'uwaterloodriver',
  packages = ['uwaterloodriver'],
  package_data = {'': ['LICENSE', 'README.rst']},
  include_package_data = True,
  version = '1.1',
  description = 'A simple Python 3 wrapper for University of Waterloo\'s Open Data API (v2).',
  author = 'Anton Bondarenko',
  author_email = 'a2bondar@edu.uwaterloo.ca',
  url = 'https://github.com/a2bondar/UWaterlooDriver', 
  download_url = 'https://github.com/a2bondar/UWaterlooDriver/archive/1.1.tar.gz', 
  keywords = ['uwaterloo', 'uw', 'api', 'opendata', 'uwaterloodriver'],
  classifiers=(
   'Intended Audience :: Developers',
   "Operating System :: OS Independent",
  ),
  license='MIT',
  zip_safe = True,
)
