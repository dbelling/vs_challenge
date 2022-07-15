# Sensor Analytics

Included is a python script for analyzing sensor statistics with the [pandas package](https://pandas.pydata.org/) and dataframes.

## Setup

To setup this project, first install the dependencies described in the `requirements.txt` file, with [pip](https://pypi.org/project/pip/). If you don't yet have pip, find a suitable [installer](https://pip.pypa.io/en/stable/installation/) for your particular operating system. 

After you've setup pip - python packages can be installed as:

```python
pip install -r requirements.txt
```

## Usage

After you've run through setup, the included `main.py` script can be invoked as:

```python
python main.py -i file_name.csv
```

## Results

| Sensor Identifier | Num Entities    |
| ----------------- | --------------- |
| Sensor 1          | 4               |
| Sensor 2          | 10              |
| Sensor 3          | 18              |
| Sensor 4          | 100000000000000 |

## Test files
Included are some test files for an empty dataset, an inconclusive dataset, and a minimal dataset for sanity checking the validity of this implementation.