# Text-Based Browser
This repo contains a simple text-based browser that reads online documentation or finds something on the Internet from the command line or terminal

- The program requires one command-line argument which is a directory for saved tabs. For example, if the argument is `directory`, the program will create a folder with the name `directory` and will save all the web pages that the user downloads in this folder.
- The program shows the previous web page saved to a file if the user types `back`.
## Sample usage
**Input:**
```
>>> python main.py folder
>>> https://docs.python.org
```
**Output:**
```
index
modules
Python
Documentation
Python 3.7.4 documentation
Welcome! This is the documentation for Python 3.7.4.
Parts of the documentation:
What's new in Python 3.7? or all "What's new" documents since 2.0
Tutorial start here
Library Reference keep this under your pillow
Language Reference describes syntax and language elements
Python Setup and Usage how to use Python on different platforms
Python HOWTOs in-depth documents on specific topics
Installing Python Modules installing from the Python Package Index & other sources
Distributing Python Modules publishing modules for installation by others
Extending and Embedding tutorial for C/C++ programmers
Python/C API reference for C/C++ programmers
FAQs frequently asked questions (with answers!)
Indices and tables:
Global Module Index quick access to all modules
General Index all functions, classes, terms
Glossary the most important terms explained
Search page search this documentation
Complete Table of Contents lists all sections and subsections
Meta information:
Reporting bugs
About the documentation
History and License of Python
Copyright
```