# politics

## dependencies
Using python3 (3.6.1) on my system, not compatible with python2

python3
python3 modules:
  * pandas (for dataframe stuff)
  * numpy (only for the ceil function)
  * wget (if downloading data)
  * zipfile (if downloading data)
  * pytest (if running tests)

## run instructions

## approach

Consider running a linter at the end or addint git-lint to the git-commit but I think it's mostly red tape right now.

Need to know when values are 'malformed' so we can omit those rows, possibly on pandas input

remember to update the list of dependencies when you're finished

consider a 'database engine' or multithreading.

see https://stackoverflow.com/questions/34740592/skip-certain-lines-from-file-using-python-pandas#34741278 for performance differences depending on file size

---we need TOTAL_NUM_CONTRIBS to be PER recipient PER zip PER year, which is not what we are doing now

---create a correct_output.txt file in each test folder (or the small ones at least)
   make a new small one (say 15 entries) and calculate the correct_output.txt file yourself.
   then fix the thing above and then run the test

make the matrix just a single dictionary to see if it helps performance.

we might be able to go faster if we keep the donation amount lists sorted by simply inserting new values in the correct location

next thing to do:
  1. move file to a 'tmp' folder in input, unzip there, rename output file, move to appropriate dir.
  2. run pandas on that file and see what happens



