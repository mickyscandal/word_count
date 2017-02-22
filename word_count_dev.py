#!/usr/bin/python

# Word Count
# Written by: Micky Scandal
# Email       mickyscandal@gmail.com
# VERSION: __DEV__ (0.2)
#
# CHANGELOG:
#   - change __init__ input var to not open/split the input file and let each function do it as needed.
#   - need to change search function to say where it found the match(s), how many, and a few words before and after the occurance.
#       * maybe even take it a step further and add options for just the first result, specify which result, go to that spot in the document etc...
#   - ABANDON THIS FILE AND RESTRUCTURE WITH 'revamp.py'. WITH A BETTER CLASS HIERARCHY.



from collections import Counter
import argparse
import time


# TEXTDATA CLASS CAN BECOME IT'S OWN FILE
class TextData(object):
    """class for working with and possing data extracted from text files../

    capabilities are(will), but not limited to: counting words (including
    instances of words. searching a text document, and writing any and/or
    all data to an external file.)"""

    def __init__(self, txt_file):
        """Open text file for TextData class to work with. opens in various
        formats to cut down on code in the following functions."""
        self.timestamp = "Generated on: %s" % time.asctime(time.localtime(time.time()))
        self.txt_name = txt_file
        self.txt_file = open(txt_file).read().split()
        self.text_file = open(txt_file)

    def basic_count(self):
        """basic count of all and uniqe words.

        basic option with no additional arguments. simply displays total words
        as well as uniq words."""
        with open(self.txt_name) as f:
            data = f.read().split()
            return "%s: %s words, %s unique words" % (self.txt_name, len(data), self.uniq_count())


    def uniq_word_count(self):
        """Returns a dictionary of every word appearing and how many instances of each
        .
        -c or --count flag. this simply returns a dictionary of all the words/counts,
        but not in a printable format. feed this function to either 'display_word_count'
        or write_word_count from with write_data."""
        with open(self.txt_name) as f:
            return Counter(f.read().split())

    def display_word_count(self):
        """prints the output of uniq_word_count() to the screen if --count is called"""
        counts = self.uniq_word_count()
        for k, v in counts.iteritems():
            print "%s: %s" % (k, str(v))


    def uniq_count(self):
        """a count of all unique words

        no argument flag. gets called along with basic_count. this method should
        not be called by itself"""
        with open(self.txt_name) as f:
            data = f.read().split()
            uniq_count = []
            for word in data:
                if word not in uniq_count:
                    uniq_count.append(word)
            return str(len(uniq_count))


    def search(self, word):
        """ check to see if the file contains a certain word

        uses the -s / --search flag followed by the word to search for. Future
        versions will also give the amount of times it appears as well as the
        location and possibly a few words before and after."""
        self.word = word
        with open(self.txt_name) as f:
            data = f.readlines()
            self.found = False
            for line in data:
                if word in line:
                    self.found = True
                    break
            return "'%s':  %s" % (self.word, self.found)

    def display_search(self):
        # WRITE DOCSTRING AND MAKE THIS RUN IF SEARCH RETURNS TRUE
        with open(self.txt_name) as f:
            data = f.readlines()
            for line in data:
                if self.word in line:
                    print line

    def write_data(self, search=None):
        """write specified data to an output file

         The file will be named <filename>_output.txt, and is saved in the same
         folder as the original input file. uses -w or --write flag. only writes
          the data you chose to appear on screen"""
        # Update for with/as statement to guarentee close for both in and out files
        out_file = open("%s_output.txt" % self.txt_name[0:-4], 'w')
        out_file.write(self.basic_count() + "\n")
        if args.count:
            counts = self.uniq_word_count()
            for k, v in counts.iteritems():
                out_file.write("%s: %s\n" % (k, str(v)))
        if search != None:
            out_file.write(self.search(search) + "\n")
            data = open(self.txt_name).readlines()
            for line in data:
                if self.word in line:
                    out_file.write(line)

        out_file.write(self.timestamp + "\n")

### END TEXTDATA ##############################################################



# DISPLAY CLASS CAN BE ITS OWN FILE
class Display(object):

    def __init__(self):
        pass

### END DISPLAY ###############################################################

# WRITE CLASS IN ITS OWN FILE
class Write(object):

    def __init__(self):
        pass

## END WRITE ##################################################################



# ADD TO DISPLAY CLASS???
def parseArguments():
    # make help statements variables so i can keep the lines shorter?
    """reads and parses all possible arguments entered at the command line

    args are --search(-s), --write(-w), --count(-c), --help(-h) and --version"""
    parser = argparse.ArgumentParser()
    # positional manditory Arguments
    parser.add_argument("fileName", help="File name", type=str)
    # optional Arguments
    parser.add_argument("-s", "--search", help="word search", type=str)
    parser.add_argument("-w", "--write", help="write output to file", action="store_true")
    parser.add_argument("-c", "--count", help="prints a list of all words and how many times they appear", action="store_true")
    parser.add_argument("--version", action="version", version="%(prog)s - Version 0.2 Written by: Micky Scandal, Email: mickyscandal@gmail.com")

    return parser.parse_args()





# RUNNER CODE,  BUT MOST OF THIS SHOULD BE FUNCTIONS IN THE DISPLAY CLASS
if __name__ == '__main__':
    args = parseArguments()
    infile = TextData(args.fileName)

    # Basic output, shows with no arguments
    print infile.basic_count()

    # -c / --count
    if args.count:
        infile.display_word_count()

    # -s / --search
    if args.search:
        print infile.search(args.search)
        infile.display_search()
    # -w / --write
    if args.write:
        if args.search:
            infile.write_data(args.search)
        else:
            infile.write_data()

    # Timestamp that appears at the bottom of every run and output file
    print infile.timestamp
