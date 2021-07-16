#!/usr/bin/python

import sys, getopt

usage = 'usage:\n  boost.py -v <vocabfile> -o <outfile> -w <word> -b <boost>'
words_to_match = 80000

def main(argv):
   vocabfile = ''
   outfile = ''
   word = ''
   boost = 0
   try:
      opts, args = getopt.getopt(argv,"hv:o:w:b:",["vfile=","ofile=","word=","boost="])
   except getopt.GetoptError:
      print(usage)
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print(usage)
         sys.exit()
      elif opt in ("-v", "--vfile"):
         vocabfile = arg
      elif opt in ("-o", "--ofile"):
         outfile = arg
      elif opt in ("-w", "--word"):
         word = arg
      elif opt in ("-b", "--boost"):
          boost = int(arg)

   print( 'Vocab file is ', vocabfile )
   print( 'Out file is ', outfile )
   print( 'Word to boost is ', word )
   print( 'Boost value is ', boost)

   vocabulary = []
   with open(vocabfile) as file:
     for i in range(words_to_match):
       str = file.readline()
       str = str.replace('\n', '')
       vocabulary.append(str)

   # Construct our list of synthetic sentences
   print('Constructing ', words_to_match * 2 * boost, 'sentences')
   sentences = []
   for vocab_word in vocabulary:
     # vocab : key
     for i in range(boost):
       sentences.append( ' '.join( (vocab_word,word) ) )
     # key : vocab
     for i in range(boost):
       sentences.append( ' '.join( (word,vocab_word) ) )

   print('Writing to file: ', outfile)
   with open(outfile, 'w') as file:
     for sentence in sentences:
       file.write(sentence + '\n')

if __name__ == "__main__":
   main(sys.argv[1:])
