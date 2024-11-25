# Integration tests with pytest
TODO
1. Integration with Qmetry
1. Unzip downloaded CLI


## Running pytest as a GHA
per https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python 
General reference - https://pytest-with-eric.com/integrations/pytest-github-actions/ 

API testing - https://laerciosantanna.medium.com/mastering-restful-api-testing-with-pytest-56d22460a9c4 

Cannot use these GHA as they are not verified:
- https://github.com/marketplace/actions/run-pytest 
- robinraju/release-downloader@v1 

## Pytest-html
https://pytest-with-eric.com/plugins/pytest-html/#Why-Create-HTML-Tests-Reports

## Pytest folder structure...
create a folder per application, CLI and API version
pytest.ini at root level (controls flags and logging)
requirements.txt (controls pip install of plugins during GitHub Action setup pytest), could alternatively add in pyproject.toml per https://packaging.python.org/en/latest/guides/writing-pyproject-toml/ 

Should evaluae if https://github.com/kvas-it/pytest-console-scripts/tree/master simplifies things

## .gitignore additions
__pycache__
*.pytest_cache
test/report/

## Pytest fixtures...
use for data structures, like headers
https://docs.pytest.org/en/stable/how-to/fixtures.html & https://www.tutorialspoint.com/pytest/pytest_fixtures.htm 

## Installing and running tests
pip install pytest
pip install pytest-html (can do as GHA)

Can specify folder as below
```
pytest .\test\integration\ --html=./test/report/report.html       
```

```
==================================================== test session starts ====================================================
platform win32 -- Python 3.12.2, pytest-8.2.2, pluggy-1.5.0
rootdir: C:\Users\loomis\Documents\GitHub\arch-sample-cli
plugins: html-4.1.1, metadata-3.1.1
collected 3 items

test\integration\api_test.py ..                                                                                        [ 66%]
test\integration\cli_test.py .                                                                                         [100%]

---------- Generated html report: file:///C:/Users/loomis/Documents/GitHub/arch-sample-cli/test/report/report.html ---------- 
==================================================== 3 passed in 40.02s ====================================================
```