UWaterlooDriver
===============

A simple Python 3 wrapper for University of Waterloo's Open Data API
(v2). Documentation can be found at: https://api.uwaterloo.ca

Usage
-----

Install:

   pip install uwaterloodriver

Basic usage:

.. code:: python

      >>> import os
      >>> os.environ['UW_API_KEY'] = 'YOUR_API_KEY_HERE'
      >>> from uwaterloodriver import UW_Driver
      >>> uw_driver = UW_Driver()
      >>> uw_driver.foodservices_diets()
    [{'diet_id': 2, 'diet_type': 'Non Vegetarian'}, {'diet_id': 5, 'diet_type': 'Vegan'}, {'diet_id': 6, 'diet_type': 'Vegetarian'}, {'diet_id': 7, 'diet_type': 'Halal'}]
      >>> uw_driver.courses_schedule(subject="CS", catalog_num=115)
    [{'campus': 'UW U', 'term': 1175, 'associated_class': 1, 'reserves': [], 'academic_level': 'undergraduate', 'section': 'LEC 001', 'class_number': 3723, 'catalog_number': '115', 'last_updated': '2017-08-24T11:00:42-04:00', 'subject': 'CS', 'enrollment_total': 85, 'note': 'Choose LAB section for Related 1.', 'units': 0.5, 'enrollment_capacity': 90, 'classes': [{'date': {'is_cancelled': False, 'start_date': None, 'end_time': '12:50', 'end_date': None, 'start_time': '11:30', 'weekdays': 'TTh', 'is_closed': False, 'is_tba': False}, 'instructors': ['Akinyemi,John Akinlabi'], 'location': {'room': '2054', 'building': 'MC'}}], 'waiting_total': 0, 'related_component_2': '201', 'held_with': [], 'waiting_capacity': 0, 'topic': None, 'related_component_1': None, 'title': 'Introduction to Computer Science 1'}, {'campus': 'UW U', 'term': 1175, 'associated_class': 2, 'reserves': [], 'academic_level': 'undergraduate', 'section': 'LEC 002', 'class_number': 3912, 'catalog_number': '115', 'last_updated': '2017-08-24T11:00:42-04:00', 'subject': 'CS', 'enrollment_total': 74, 'note': 'Choose LAB section for Related 1.', 'units': 0.5, 'enrollment_capacity': 90, 'classes': [{'date': {'is_cancelled': False, 'start_date': None, 'end_time': '15:50', 'end_date': None, 'start_time': '14:30', 'weekdays': 'TTh', 'is_closed': False, 'is_tba': False}, 'instructors': ['Akinyemi,John Akinlabi'], 'location': {'room': '235', 'building': 'PHY'}}], 'waiting_total': 0, 'related_component_2': '201', 'held_with': [], 'waiting_capacity': 0, 'topic': None, 'related_component_1': None, 'title': 'Introduction to Computer Science 1'}, {'campus': 'UW U', 'term': 1175, 'associated_class': 99, 'reserves': [], 'academic_level': 'undergraduate', 'section': 'LAB 101', 'class_number': 3724, 'catalog_number': '115', 'last_updated': '2017-08-24T11:00:42-04:00', 'subject': 'CS', 'enrollment_total': 59, 'note': 'Choose LAB section for Related 1.', 'units': 0.5, 'enrollment_capacity': 60, 'classes': [{'date': {'is_cancelled': False, 'start_date': None, 'end_time': '11:20', 'end_date': None, 'start_time': '10:00', 'weekdays': 'F', 'is_closed': False, 'is_tba': False}, 'instructors': [], 'location': {'room': '3003', 'building': 'MC'}}], 'waiting_total': 0, 'related_component_2': None, 'held_with': [], 'waiting_capacity': 0, 'topic': None, 'related_component_1': '99', 'title': 'Introduction to Computer Science 1'}, {'campus': 'UW U', 'term': 1175, 'associated_class': 99, 'reserves': [], 'academic_level': 'undergraduate', 'section': 'LAB 102', 'class_number': 3772, 'catalog_number': '115', 'last_updated': '2017-08-24T11:00:42-04:00', 'subject': 'CS', 'enrollment_total': 56, 'note': 'Choose LAB section for Related 1.', 'units': 0.5, 'enrollment_capacity': 60, 'classes': [{'date': {'is_cancelled': False, 'start_date': None, 'end_time': '12:50', 'end_date': None, 'start_time': '11:30', 'weekdays': 'F', 'is_closed': False, 'is_tba': False}, 'instructors': [], 'location': {'room': '3003', 'building': 'MC'}}], 'waiting_total': 0, 'related_component_2': None, 'held_with': [], 'waiting_capacity': 0, 'topic': None, 'related_component_1': '99', 'title': 'Introduction to Computer Science 1'}, {'campus': 'UW U', 'term': 1175, 'associated_class': 99, 'reserves': [], 'academic_level': 'undergraduate', 'section': 'LAB 103', 'class_number': 3930, 'catalog_number': '115', 'last_updated': '2017-08-24T11:00:42-04:00', 'subject': 'CS', 'enrollment_total': 44, 'note': 'Choose LAB section for Related 1.', 'units': 0.5, 'enrollment_capacity': 60, 'classes': [{'date': {'is_cancelled': False, 'start_date': None, 'end_time': '14:20', 'end_date': None, 'start_time': '13:00', 'weekdays': 'F', 'is_closed': False, 'is_tba': False}, 'instructors': [], 'location': {'room': '3003', 'building': 'MC'}}], 'waiting_total': 0, 'related_component_2': None, 'held_with': [], 'waiting_capacity': 0, 'topic': None, 'related_component_1': '99', 'title': 'Introduction to Computer Science 1'}, {'campus': 'UW U', 'term': 1175, 'associated_class': 99, 'reserves': [], 'academic_level': 'undergraduate', 'section': 'TST 201', 'class_number': 3725, 'catalog_number': '115', 'last_updated': '2017-08-24T11:00:42-04:00', 'subject': 'CS', 'enrollment_total': 159, 'note': 'Choose LAB section for Related 1.', 'units': 0.5, 'enrollment_capacity': 180, 'classes': [{'date': {'is_cancelled': False, 'start_date': '06/19', 'end_time': '20:50', 'end_date': '06/19', 'start_time': '19:00', 'weekdays': 'M', 'is_closed': False, 'is_tba': False}, 'instructors': ['Daly,Barbara'], 'location': {'room': None, 'building': None}}], 'waiting_total': 0, 'related_component_2': None, 'held_with': [], 'waiting_capacity': 0, 'topic': None, 'related_component_1': '99', 'title': 'Introduction to Computer Science 1'}]

By default each method returns a Python dictionary (JSON response
conversion), or a list of Python dictionaries.

Changelog:
----------

| v1.1 - Hotfix for setup.py
| v1.0 - Formatting fixes to be compliant with PyPi. Added install instructions.
| v0.9 - Uploaded to PyPi for easy install.
| v0.8 - Updated testing suite for /courses/ to use new methods.
| v0.7 - Added support for /blogs/ endpoint, small changes to code base for consistency.
| v0.6 - Full support for all /wireless/, /api/, /server/, /directory/ endpoints.
| v0.5 - Full support for all /poi/, /transit/, and /parking/ endpoints.
| v0.4 - Full support for all /weather/, /news/, /opportunities/, and /services/ endpoints.
| v0.3 - Full support for all /awards/, /events/, /terms/, /buildings/, /codes/, and /resources/ endpoints.
| v0.2 - Full support for all /FEDS/ and /courses/ endpoints added.
| v0.1 - Full support for all /foodservices/ endpoints added.
