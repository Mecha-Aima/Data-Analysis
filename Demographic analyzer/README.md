
# Demographic Data Analyzer

A Python project using pandas for data analysis and visualization of demographic data.

## Overview


This project provides a comprehensive analysis of demographic data using pandas, a powerful data analysis library in Python. The project includes a Python module `demographic_data_analyzer` that contains functions to calculate useful statistics about the demographic data.

## Features


*   Reads demographic data from a CSV file
*   Provides insights into demographic characteristics such as age, education, and occupation
*   Analyzes the relationship between demographic characteristics and income

## Requirements


*   Python 3.x
*   pandas
*   numpy

## Installation


1.  Clone the repository: `git clone https://github.com/your-username/demographic-data-analyzer.git`
2.  Install the required libraries: `pip install pandas numpy matplotlib`
3.  Run the project: `python main.py`

## Usage


### Running the Project

To run the project, simply execute the `main.py` file using Python:

```bash
python main.py
```

This will calculate and print the demographic data.

----------

### Calculating Demographic Data

The `calculate_demographic_data` function calculates demographic data from a CSV file. You can call this function by passing the path to your CSV file as an argument:

```python
from demographic_data_analyzer import calculate_demographic_data

data = calculate_demographic_data('path/to/your/data.csv')
```
------------

## Testing


The project includes a test module `test_module.py` that uses the `unittest` framework to run tests on the code. The tests can be run by executing the `test_module.py` file using Python:

```bash
python test_module.py
```

The tests cover the following functionality:

*   Test that the `calculate_demographic_data` function returns the correct data

------------

## Main Module


The `main.py` module brings together the analyzer and the tests. It imports the `demographic_data_analyzer` module and the `test_module` module, and runs the tests and the analyzer.

------------

## Data

The project uses a CSV file containing demographic data. A few of these columns are:

*   `age`: The age of the individual
*   `education`: The education level of the individual (e.g., high school, college, etc.)
*   `occupation`: The occupation of the individual
*   `salary`: The income of the individual
*   `race`: The race of the individual
*   `native-country`: The individual's native country, etc.

You can replace the sample data with your own data by modifying the `adult.data.csv` file.

------------

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

------------

## Acknowledgments

*   This project is part of the "Data Anlysis with Python" certification by freecodecamp: https://www.freecodecamp.org/
*   I wrote the code for the project, while the data file is owned by freecodecamp
