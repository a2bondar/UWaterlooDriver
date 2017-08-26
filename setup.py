from distutils.core import setup
setup(
  name = 'uwaterloodriver',
  packages = ['uwaterloodriver'],
  package_data = {'': ['LICENSE', 'README']},
  include_package_data = True,
  version = '0.9',
  description = 'A simple Python 3 wrapper for University of Waterloo\'s Open Data API (v2).',
  author = 'Anton Bondarenko',
  author_email = 'a2bondar@edu.uwaterloo.ca',
  url = 'https://github.com/a2bondar/UWaterlooDriver', 
  download_url = 'https://github.com/a2bondar/UWaterlooDriver/archive/0.9.tar.gz', 
  keywords = ['uwaterloo', 'uw', 'api', 'opendata', 'uwaterloodriver'],
  classifiers=(
   'Intended Audience :: Developers',
   "Operating System :: OS Independent",
  ),
  license='MIT',
  zip_safe = True,
)
