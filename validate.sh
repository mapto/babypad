#!/bin/sh -e

echo '>>> Cleaning cache'
# rm -rf extractor/__pycache__
rm -rf __pycache__

echo '>>> Skipping Pylint'
# pylint -E extractor
# pylint -E selenium/

echo '>>> Running Mypy'
# mypy extractor
mypy .

echo '>>> Skipping Pytest'
# pytest -vv --doctest-modules -s . # --disable-warnings
# pytest -vv --doctest-modules -s selenium # --disable-warnings

echo '>>> Running Black'
# black extractor
black .
