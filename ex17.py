from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copy from %s to %s" % (from_file, to_file)

#we could do these two on one line, how to?
in_file = open(from_file)
in_data = open(from_file).read()
print in_data

print "The input file is %d bytes long." % len(in_data)

print "Does the out file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("-")

open(to_file, 'w').write(in_data)

txt = open(to_file).read()

print "lenth of out file: %d" % len(txt)
print txt

print "Alright, all done."
#out_file.close()
in_file.close()