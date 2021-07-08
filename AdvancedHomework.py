'''
the crazy advanced homework. Create a textfile in a folder,
zip just the file, move it to new folder, unzip it,
read it, search for specific pattern and print it on screen.
'''

import zipfile
import os
import re
#make a file for the homework, will make it in the current working directory
filename = os.getcwd()
os.mkdir(filename+"/folderForZipFiles")
#create a text file, zip it, move it to the homework folder, unzip it and find
#the phone number 333-333-22-3333
text = '''
kkasd sg bdgb dfvdf vdf bd fb dbd bd gb dgbd
b etb et ge the t eth et eth ethe fsdfgsgs
sgsg sdS  S SFgsd gsdgS FgsFG dFgdgdFg DFGdgdfgd DFGH€T
dfGdfg dfghD dfg df3t gfb 535  354 235 25 2 4534534
 345345345345345345345dfgDFGDFGdfgdgdfg798dg787dfg79d
 fg98df7g987 333-333-22-333345345345345345345dfgDFGDFGdfgdg
 dfg798dg787dfg79dfg98df7g987ererge ertertert erte
 ete rt erddfg dfg dfg erertert  erte rt erte rt ert ert . dfg7
 er45gdf vrg 65 gfg fsds s ddfdf y ttyty dfde 54 dfdf4 efdf
  fddfdf dg gfgddf.
  kkasd sg bdgb dfvdf vdf bd fb dbd bd gb dgbd
  b etb et ge the t eth et eth ethe fsdfgsgs
  sgsg sdS  S SFgsd gsdgS FgsFG dFgdgdFg DFGdgdfgd DFGH€T
  dfGdfg dfghD dfg df3t gfb 535  354 235 25 2 4534534
   345345345345345345345dfgDFGDFGdfgdgdfg798dg787dfg79d
   fg98df7g987 333-333-22-333345345345345345345dfgDFGDFGdfgdg
   dfg798dg787dfg79dfg98df7g987ererge ertertert erte
   ete rt erddfg dfg dfg erertert  erte rt erte rt ert ert . dfg7
   er45gdf vrg 65 gfg fsds s ddfdf y ttyty dfde 54 dfdf4 efdf
    fddfdf dg gfgddf.
    kkasd sg bdgb dfvdf vdf bd fb dbd bd gb dgbd
    b etb et ge the t eth et eth ethe fsdfgsgs
    sgsg sdS  S SFgsd gsdgS FgsFG dFgdgdFg DFGdgdfgd DFGH€T
    dfGdfg dfghD dfg df3t gfb 535  354 235 25 2 4534534
     345345345345345345345dfgDFGDFGdfgdgdfg798dg787dfg79d
     fg98df7g987 333-333-22-333345345345345345345dfgDFGDFGdfgdg
     dfg798dg787dfg79dfg98df7g987ererge ertertert erte
     ete rt erddfg dfg dfg erertert  erte rt erte rt ert ert . dfg7
     er45gdf vrg 65 gfg fsds s ddfdf y ttyty dfde 54 dfdf4 efdf
      fddfdf dg gfgddf
'''

os.chdir(filename+"/folderForZipFiles")
f = open("textToZip.txt", "w+")
f.write(text)
f.close()

zipfile.ZipFile("textZipFile.zip", 'w').write("textToZip.txt",compress_type=zipfile.ZIP_DEFLATED)

openObject = zipfile.ZipFile("textZipFile.zip", 'r')

openObject.extractall("extracted_content")

#change directory to created

os.chdir(filename+"/folderForZipFiles/extracted_content")

pat = r'\d{3}-\d{3}-\d{2}-\d{4}'
textToSearch = open("textToZip.txt", 'r')
reader = textToSearch.read()

isMatch = re.search(pat, reader)

if isMatch:
    print("Found phonenumber {}".format(isMatch.group()))
else:
    print("no match found, shutting down")
