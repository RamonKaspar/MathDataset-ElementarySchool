# Translation to German Using DeepL API

This directory contains scripts for translating selected datasets from English to German using the DeepL API.

## Overview

The translation utilizes the DeepL API, which is free to use for up to 500,000 characters per month. The datasets included for translation are subsets of arithmetic problems and word problems.

## Datasets

The following datasets have been translated:

- `arithmetic_100.csv` and `arithmetic_1000.csv`
- `wordProblems_100.csv` and `wordProblems_1000.csv`
- `geometry_100.csv` and `geometry_1000.csv`

The complete datasets (`arithmetic_complete`, `wordProblems_complete` and `geometry_complete`) are not included due to their large size, which exceeds the free translation limit.

## Getting Started

To use these scripts, you must first create a DeepL API key. Register at [www.deepl.com](https://www.deepl.com/pro?utm_source=github&utm_medium=github-python-readme#developer) to obtain your key. Once you have your API key, follow these steps:

1. Create a `.env` file in this directory.
2. Add the following line to the `.env` file:
   ```
   DEEPL_API_KEY=your_api_key_here
   ```
3. Install the necessary Python package by running:
   ```bash
   pip install --upgrade deepl
   ```

For more information and advanced configurations, visit the DeepL Python library documentation on GitHub: [DeepL Python](https://github.com/DeepLcom/deepl-python?tab=readme-ov-file).

## Usage

Run the Python scripts to translate the datasets and convert them to JSON format. The scripts read CSV files, perform the translation, and output the translated data as JSON files.
