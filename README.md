# UWaterlooDriver
A simple Python 3 wrapper for University of Waterloo's Open Data API (v2). Documentation can be found at: https://api.uwaterloo.ca

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
v0.8 - Updated testing suite for /courses/ to use new methods.  
v0.7 - Added support for /blogs/ endpoint, small changes to code base for consistency.  
v0.6 - Full support for all /wireless/, /api/, /server/, /directory/ endpoints.  
v0.5 - Full support for all /poi/, /transit/, and /parking/ endpoints.  
v0.4 - Full support for all /weather/, /news/, and /opportunities/, /services/ endpoints.  
v0.3 - Full support for all /awards/, /events/, /terms/, /buildings/, /codes/, and /resources/ endpoints.  
v0.2 - Full support for all /FEDS/ and /courses/ endpoints added.  
v0.1 - Full support for all /foodservices/ endpoints added.  
