# politics



## Dependencies
Installation procedure:

  1. Install python3.

NO dependencies necessary for main script.  For additional functionalities, install:
  * pytest (only if you want to run the unit tests)
  * wget (only if you want to automate downloading the government data files)
  * zipfile (only if you want to automate downloading the government data files)
  * colorlog (only if you want to use the record_elapsed_time timers)



## Run instructions

Make sure you have 'python3' in your PATH and that this 'python3' points to your python3 installation.  Navigate to the root of the repo and execute:

    sh ./run.sh

*Note that a few liberties were taken in interpreting whether a value was valid or not.  For example, I decided that a transaction with an amount of 0 or less was invalid, and so my program discards those records.  See `src/lib/helpers.py > row_string_to_row` for the code pertaining to record validation.



## Approach

Firstly, to simulate a streaming scenario, I created the module `src/lib/stream.py`.  This module reads the lines of an input file one at a time, executes some function, and writes the output of that function to a separate file in append mode.

Now, to keep track of the data, two objects were implemented in `src/lib/data_container.py`.  The first object, `Donors`, keeps a record of all donors.  It can also tell which donors are repeat donors.  The second object, `Contributions`, keeps a record of all 'repeat contributions'.  It stores the amount of each 'repeat contribution' along with its year, zip code, and recipient.  Both of these objects are implemented as dictionaries because reading and writing to dictionaries is extremely fast.  (This is because dictionaries are implemented with hash tables that make key-lookup very fast.)

The program starts with the execution of the `src/lib/main.py > main` function which sets up the donor and contribution lists.  Those two lists persist throughout the program.  Then the function `src/lib/main.py > process_line` is run repeatedly, once on each line of the input file `itcont.txt`.  Therefore, `process_line` is the algorithm glueing everything together and is the most important piece of code to look at...

Here is a summary of how `process_line` works.  It first validates the input record, discarding it if the input is bad.  If the record has valid data, it adds the donor to the list of donors.  It then detects if the donor is a repeat contributor.  If the donor is a repeat contributor, it adds the contribution to the list of repeat contributions and then retrieves the appropriate output (recipient, zip code, year, percentile amount, total repeat contribution amount, and number of repeat contributions).  But I recommend taking a look at the code yourself!

Thanks for taking a look at my project!  :)



## Supplementary information

If you want to run the unit tests, then
  1. install pytest
  2. execute `py.test` at the root of the repo

*Note that the tests `insight_testsuite/tests/test_7` and `insight_testsuite/tests/test_9` are ommitted from the GitHub repository because the size of the input files is too large.

