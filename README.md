# politics

Using python3 (3.6.1) on my system, but should make also compatible with python2 before submitting.

## dependencies
python3
python3 modules:
  * pandas
  * wget
  * zipfile



Consider running a linter at the end or addint git-lint to the git-commit but I think it's mostly red tape right now.

Need to know when values are 'malformed' so we can omit those rows, possibly on pandas input

remember to update the list of dependencies when you're finished

consider a 'database engine' or multithreading.

see https://stackoverflow.com/questions/34740592/skip-certain-lines-from-file-using-python-pandas#34741278 for performance differences depending on file size

next thing to do:
  1. move file to a 'tmp' folder in input, unzip there, rename output file, move to appropriate dir.
  2. run pandas on that file and see what happens


