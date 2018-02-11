# politics

## dependencies
Installation procedure:

Install python3.

(Details: Tested with python3 (3.6.1) on my system, but should work with any version of python3.  download.py may fail for python 3.4 and earlier due to changes in the builtin subprocess module, but download.py is not currently used in the script anyway.  Not compatible with python2)

Install the following PyPI modules onto your python3 installation:
  * numpy (only for the ceil function)
  * pytest (if running tests)
  * wget (if using download.py)
  * zipfile (if using download.py)

## run instructions

Make sure you have 'python3' in your PATH and that this 'python3' points to your python3 installation.  Navigate to the root of the repo and execute

    sh ./run.sh

## approach

Consider running a linter at the end or addint git-lint to the git-commit but I think it's mostly red tape right now.

Need to know when values are 'malformed' so we can omit those rows, possibly on pandas input

remember to update the list of dependencies when you're finished

consider a 'database engine' or multithreading.

see https://stackoverflow.com/questions/34740592/skip-certain-lines-from-file-using-python-pandas#34741278 for performance differences depending on file size

---create a correct_output.txt file in each test folder (or the small ones at least)
   make a new small one (say 15 entries) and calculate the correct_output.txt file yourself.
   then fix the thing above and then run the test

the prompt says a donor 'in a prior calendar year' which suggests that a donor twice in the SAME year is NOT a repeat donor.....YES we DO have to change the way we detect REPEAT donors

If TRANSACTION_DT is an invalid date (e.g., empty, malformed)
If ZIP_CODE is an invalid zip code (i.e., empty, fewer than five digits)
If the NAME is an invalid name (e.g., empty, malformed)
If any lines in the input file contains empty cells in the CMTE_ID or TRANSACTION_AMT fields


