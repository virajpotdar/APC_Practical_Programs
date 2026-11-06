# APC Python Practical Programs

A collection of 29 simple Python practical programs for the Advanced Programming Concepts (APC) practical examination. Each experiment is kept in a separate file and uses beginner-friendly code.

## Experiments

| No. | Program | File |
|---:|---|---|
| 1 | read the contents of a text file and display them on the console | `01_read_file.py` |
| 2 | read the contents of one file and write them into another file | `02_copy_file.py` |
| 3 | demonstrate 10 directory and path handling functions using the os module | `03_directory_functions.py` |
| 4 | display a horizontal bar chart showing the popularity of programming languages | `04_horizontal_bar_chart.py` |
| 5 | create a pie chart showing the distribution of trip expenses by category | `05_pie_chart.py` |
| 6 | design a simple GUI using Tkinter with a label, entry box and button | `06_tkinter_gui.py` |
| 7 | demonstrate a class, object and constructor using student information | `07_class_object_constructor.py` |
| 8 | demonstrate method overloading using default arguments | `08_method_overloading.py` |
| 9 | demonstrate method overriding using parent and child classes | `09_method_overriding.py` |
| 10 | demonstrate single inheritance | `10_single_inheritance.py` |
| 11 | demonstrate multilevel inheritance | `11_multilevel_inheritance.py` |
| 12 | demonstrate multiple inheritance | `12_multiple_inheritance.py` |
| 13 | demonstrate hybrid inheritance | `13_hybrid_inheritance.py` |
| 14 | demonstrate hierarchical inheritance | `14_hierarchical_inheritance.py` |
| 15 | demonstrate 10 functions or operations of the array module | `15_array_functions.py` |
| 16 | demonstrate 10 list methods and functions | `16_list_functions.py` |
| 17 | demonstrate 10 dictionary methods and functions | `17_dictionary_functions.py` |
| 18 | demonstrate 10 string methods and functions | `18_string_functions.py` |
| 19 | demonstrate 10 useful tuple operations and built-in functions | `19_tuple_functions.py` |
| 20 | demonstrate 10 set methods and operations | `20_set_functions.py` |
| 21 | create and call a normal function and a lambda function | `21_function_lambda.py` |
| 22 | Create a Python package for addition and multiplication and use it in another program | `22_package/main.py` |
| 23 | apply stemming using NLTK PorterStemmer | `23_nltk_stemming.py` |
| 24 | demonstrate word tokenization using NLTK | `24_nltk_tokenization.py` |
| 25 | demonstrate NumPy array creation, properties and operations | `25_numpy_library.py` |
| 26 | Write a Python program using Pandas to read student records from a CSV file and display them in tabular format | `26_pandas_csv.py` |
| 27 | demonstrate an abstract class and abstract method | `27_abstract_class.py` |
| 28 | create and demonstrate a user-defined exception | `28_user_defined_exception.py` |
| 29 | demonstrate exception handling using try, except, else and finally | `29_exception_handling.py` |

## Requirements

- Python 3
- Matplotlib (Experiments 4 and 5)
- NumPy (Experiment 25)
- Pandas (Experiment 26)
- NLTK (Experiments 23 and 24)
- Tkinter (Experiment 6; normally included with standard Python installations)

Install the external libraries with:

```bash
pip install -r requirements.txt
```

## How to Run

Open a terminal in this folder and run the required file. For example:

```bash
python 01_read_file.py
```

Run each program from this project folder so the sample text and CSV files can be found. For the package experiment, run:

```bash
python 22_package/main.py
```

Experiment 6 opens a desktop window and needs a graphical desktop environment. Experiments 4 and 5 open Matplotlib chart windows. Experiment 24 uses NLTK wordpunct_tokenize() and does not need a separate tokenizer-data download.

## Files Included

- `sample.txt` — input file for file handling experiments.
- `student_records.csv` — sample student data for Pandas.
- `copy.txt` — created when Experiment 2 runs.
- `demo_folder/` — created and removed when Experiment 3 runs.
- `22_package/my_package/` — package used in Experiment 22.
- `PRACTICAL_NOTES.md` — problem statements, sample outputs, explanations and concepts for all experiments.

## Note

The examples use fixed sample values so they can be practised and explained easily in a practical examination.
