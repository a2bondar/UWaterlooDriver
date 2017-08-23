# UWaterlooDriver
A simple Python 3 wrapper for University of Waterloo's Open Data API (v2). Documentation can be found at: http://api.uwaterloo.ca

Usage
-----

Basic usage:
```python
  >>> import os
  >>> os.environ['UW_API_KEY'] = 'YOUR_API_KEY_HERE'
  >>> from uwaterloodriver import UW_Driver
  >>> uw_driver = UW_Driver()
  >>> uw_driver.diets()
{'diet_id': 2, 'diet_type': 'Non Vegetarian'}, {'diet_id': 5, 'diet_type': 'Vegan'}, {'diet_id': 6, 'diet_type': 'Vegetarian'}, {'diet_id': 7, 'diet_type': 'Halal'}
```

By default each method returns a Python dictionary (JSON response conversion), or a list of Python dictionaries.


Changelog:
----------
v0.1 - Full support for all /foodservices/ endpoints added.
