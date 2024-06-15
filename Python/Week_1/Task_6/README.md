# Firelink - Open Websites with Firefox

This is a Python project that allows you to open specified websites using the Firefox browser through a simple command-line interface.

## Description

The project consists of two files: a module file (`firelink.py`) and a main file. The module file defines a dictionary of websites and a function to open these websites using Firefox. The main file provides a command-line interface for the user to select a website to open.

## Module File: `firelink.py`

```python
import webbrowser

websites = {"Facebook": "https://www.facebook.com/", "Youtube": "https://www.youtube.com/"}
urls = ["Facebook", "Youtube"]

def firefox(url):
    firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
    webbrowser.get('firefox').open(websites[urls[int(url) - 1]])
