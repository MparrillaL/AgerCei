# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [0.0.0] - 2023-12-20
- Added template.
- Added `patient.py` file with classes `Patient` and `ScalePatient`.
- Introduced `patient_charts.py` for graph-related functions.

## [0.1.0] - 2023-12-26
- Introducing a new feature: `patient_gestor.py` file.

## [0.2.0] - 2023-12-29
- Introduced a new feature: `form.py` file.
- Addressed circular dependency issues by renaming GUI components to Scalepatient, patient, and patient_chart..

## [0.3.0] - 2023-1-12
- Removed the files `patient_for_ui.py` and `patient_chart_for_ui.py`, which were specific to the interface.
- Consolidated all functionalities into the `form.py` file.
- Refocused the program on the form, with substantial improvements to the interface.

## [0.4.0] - 2023-1-15
- Added Numpy documentation to classes and methods.
- Added `csv_analysis.py` with 'medidas.csv' for patient dataframe analysis.

## [0.5.0] - 2023-1-20
- removed personalized exceptions on `patient.py` due to errors in collab.

## [0.6.0] - 2023-1-20
- changed from 'patient' to from '.patient' in `patient_charts` due to errors in collab.

## [0.7.0] - 2023-1-20
- fixed some import errors in `form.py`