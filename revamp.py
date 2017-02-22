#!/usr/bin/python

# imports
import argparse
import time
from collections import Counter

class TextData(object):

    def __init__(self, nfile):
        self.nfile = nfile

    def basic_count(self):
        """basic count of all words and unique words"""
        with open(self.nfile) as f:
            data = f.read().split()
            return "%s: %s words, <fix> unique words" % (self.nfile, len(data))

    def uniq_count(self):
        """basic count of all unique words"""
        with open(self.nfile) as f:
            data = f.read().split
            print data
            self.uniq = []
            for word in data  :
                if word not in uniq:
                    uniq.append(word)
            return len(uniq)


    def uniq_word_count(self):
        """every word in file and a count of how many occurances --(c)ount"""
        with open(self.nfile) as f:
            return Counter(f.read().split())

    def search(self, pattern):
        """searches the file and returns bool weather true or false --(s)earch"""
        self.pattern = pattern
        with open(self.nfile) as f:
            self.searchDat = f.readlines()
            self.found = False
            for line in self.searchDat:
                if pattern in line:
                    self.found = True
                    break
        return self.found



class Argument(object):

    def __init__(self, textdata):
        self.parser = argparse.ArgumentParser()
        self.textdata = textdata

    def parseArguments(self):
        # positional argument
        self.parser.add_argument("filename", help="File name.", type=str)
        # optional arguments
        self.parser.add_argument("-s", "--search", help="search help", type=str)
        self.parser.add_argument("-c", "--count", help="count help", action="store_true")
        self.parser.add_argument("-w", "--write", help="write help", action="store_true")
        self.parser.add_argument("--version", action="version", version="%(prog)s - Version X.X")

        return self.parser.parse_args()



class Display(object):

    def __init__(self, textdata):
        self.textdata = textdata
        pass

    def basic_display(Self):
        print textdata.basic_count()

    def display_word_count(self):
        count = textdata.uniq_word_count()
        for k, v in count.iteritems():
            print "%s: %d" % (k,v)

    def display_search(self):
        if textdata.found:
            print "'%s' found: " % textdata.pattern
            for line in textdata.searchDat:
                if textdata.pattern in line:
                    print line

    def timestamp(self):
        print "Generated on: %s" % time.asctime(time.localtime(time.time()))




class Write(object):

    def __init__(self, textdata):
        self.textdata = textdata
        self.outfile = open("%s_output.txt" % textdata.nfile[0:-4], 'w')
        pass

    def basic_write(self):
        self.outfile.write(textdata.basic_count() + "\n")

    def write_word_count(self):
        count = textdata.uniq_word_count()
        for k, v in count.iteritems():
            self.outfile.write("%s: %d\n" % (k,v))

    def write_search(self):
        if textdata.found:
            self.outfile.write("'%s' found: \n" % textdata.pattern)
            for line in textdata.searchDat:
                if textdata.pattern in line:
                    self.outfile.write(line + "\n")

    def close_file(self):
        self.outfile.close()

    def timestamp(self):
        self.outfile.write("Generated on: %s\n" % time.asctime(time.localtime(time.time())))



if __name__ == "__main__":
    textdata = TextData('text.txt')
    display = Display(textdata)
    write = Write(textdata)

    textdata.search('fuck')

    # display outputs
    display.basic_display()
    display.display_word_count()
    display.display_search()
    display.timestamp()

    # write outputs
    write.basic_write()
    write.write_word_count()
    write.write_search()
    write.timestamp()
    write.close_file()
