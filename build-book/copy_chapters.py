#!/usr/bin/env python

"""
Python 3 script to copy chapters from repro-case-studies and 
repro-case-private repositories, and convert them into Gitbook-compatible
formats.

Both of these directories must be in the same parent directory, i.e.,

.
|-- repro-case-studies
|   |-- case-studies
|   |...
|-- repro-case-private
|   |-- book
|   |...
|-- practice-repro-research
|   |-- README.md
|   |-- build-book
|   |...

Ensure that the correct branches of repro-case-private and repro-case-studies 
are both checked out.

Recent versions of pandoc and imagemagick must be available on the path.
The pandoc-citeproc filter must also be installed.

This script must be executed with the cwd at the script path (i.e., using 
just `python copy_chapters.py`).

"""

import sys, os
import subprocess
import pandas as pd
from subprocess import call

cwd = os.getcwd()
cstud_dir = os.path.normpath(os.path.join(cwd,
            "../../repro-case-studies/case-studies/"))
cpriv_dir = os.path.normpath(os.path.join(cwd,
            "../../repro-case-private/book/"))

# Clear or create build directory and subdirs
call("rm -r ../case-studies; mkdir ../case-studies", shell=True)
call("rm -r ../core-chapters; mkdir ../core-chapters", shell=True)

# Read master chapter table
tab = pd.read_csv('chapt_table.csv')

# Loop through each row in table and process chapter files accordingly
for i in range(len(tab.index)):

    # if i not in [21]:
    #     continue

    # Check whether chapter is case study or other
    study = (tab.iloc[i]['dir'] == 'studies')

    # Determine files to read and write
    if study:
        inpath = ("../../repro-case-studies/case-studies/" +
                  tab.iloc[i]['path'] + ".md")
    else:
        inpath = ("../../repro-case-private/book/" +
                  tab.iloc[i]['path'] + "/main.md")

    outpath = "temp.md"  # Just put the temp file here for now

    # Write temporary markdown file, adjusting:
    # 1. Image syntax in case studies
    # 2. Chapter titles
    # 3. Header levels
    # 4. Tables
    with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:

        dash_line_count = 0
        in_table = False

        # Loop through each line in file
        for line in infile:

            # Handle grabbing title and author phrases
            if line[0:6] == "title:":
                title = line[7:]
                title = title.replace('"', '')  # Get rid of any quotes

            if line[0:7] == "author:":
                author = line[8:]

            # Handle writing title and author, given header entry/exit
            if dash_line_count == 2:  # Trips on line after exit header
                outfile.write("\n# " + title + "\n")
                outfile.write("\n## " + author + "\n\n")
                dash_line_count = 0

            if line == "---\n":
                dash_line_count += 1

            # Handle header levels (drop two levels to allow title, author)
            if line[0:2] == "# ":
                line = "##" + line

            # Handle image lines
            if line[0:2] == "![":

                line = line.replace('.pdf', '.png')  # Image extension
                line = line.split('{')[0]  # Drop width argument
                line = "@@@" + line[1:]  # False start so Word ignores

                # If it's a case study, convert and copy image
                # Non-case study images are handled manually later
                if study:
                    pdfpath = ("../../repro-case-studies/case-studies/" +
                                tab.iloc[i]['path'] + ".pdf ")
                    pngpath = ("../case-studies/" + tab.iloc[i]['path'] +
                                ".png ")
                    call("convert -density 400 " + pdfpath + 
                         "-resize 1200 " + pngpath, shell=True)

            # Handle table lines
            if line[1:6] == 'sttab':
                line = ""
                in_table = True
            elif line[1:6] == 'entab':
                line = "INSERTTABLEHERE\n\n"
                in_table = False
            elif in_table:
                line = ""

            # Write the (possibly modified) line
            outfile.write(line)

    # Start pandoc command
    cmd = "pandoc "

    # Add refs file if needed
    path = tab.iloc[i]["path"]

    if (not study) and "references.bib" in os.listdir(cpriv_dir + "/" + path):
        cmd += ("--filter pandoc-citeproc --bibliography=" +
                cpriv_dir + "/" + path +  "/references.bib --csl=apa.csl ")

    if study and (path +".bib") in os.listdir(cstud_dir):
         cmd += ("--filter pandoc-citeproc --bibliography=" + 
                cstud_dir + "/" + path + ".bib " + "--csl=apa.csl ")

    # Complete and run first pandoc command
    # We have to outsmart pandoc a bit
    # It won't run the citeproc filter if you convert md to md
    # We convert to docx then back to md, which seems to work
    cmd += "-o temp.docx temp.md"
    call(cmd, shell=True)

    # Now we just convert the temp.docx to the "real" md file
    if study:
        outpath = ("../case-studies/" + tab.iloc[i]["path"] + ".md ")
    else:
        outpath = ("../core-chapters/" + tab.iloc[i]["path"] + ".md ")

    call("pandoc --wrap=none -o " + outpath + "temp.docx", shell=True)

    # Fix the false starts (, now that back in md
    # Note that '' after -i is for Max OS X, as is space syntax
    refcmd = r"sed -i '' 's/@@@\[/!\[/g' " + outpath
    call(refcmd, shell=True)

    # Insert HTML version of tables
    tab_inpath = os.path.normpath(os.path.join(cwd,
            inpath[:-3] + "-table.html"))
    outpath = os.path.normpath(os.path.join(cwd, outpath))

    if os.path.isfile(tab_inpath):
        tabcmd = r'FILE2=$(<%s); FILE1=$(<%s); echo "${FILE2//INSERTTABLEHERE/$FILE1}" > %s' % (outpath, tab_inpath, outpath)
        call(tabcmd, shell=True)

    # Remove temp files
    call("rm temp.md", shell=True)
    call("rm temp.docx", shell=True)

# Special section for millman $ signs
# First change all $ to *, to just do italics (there's one subscript issue)
# Second, change four spaces then * back to $, that's a code block

call("sed -i '' 's/\$/\*/g' ../case-studies/millmanOttoboniStark.md", shell=True)
call("sed -i '' 's/^[[:space:]][[:space:]][[:space:]][[:space:]]\*/    \$/g' ../case-studies/millmanOttoboniStark.md", shell=True)

# Process the three non-case study images
imgpaths = [("4-casestudies/CaseStudies123.pdf", "4-fig-1.png"),
            ("7-lessons/plots/testing.eps", "5-fig-1.png"),
            ("7-lessons/plots/tools.eps", "5-fig-2.png")]

for inpath, outpath in imgpaths:
    inpath = os.path.normpath(os.path.join(cwd,
             "../../repro-case-private/book/", inpath))
    outpath = os.path.normpath(os.path.join(cwd,
              "../core-chapters/", outpath))

    call("convert -density 400 " + inpath +
         " -resize 1200 " + outpath, shell=True)

# Adjust text to point to new versions of images
imgtxt = [("4-casestudies", "\/CaseStudies123.png", "4-fig-1.png"),
          ("7-lessons", "\/plots\/testing.eps", "5-fig-1.png"),
          ("7-lessons", "\/plots\/tools.eps", "5-fig-2.png")]

for txtdir, oldtxt, newtxt in imgtxt:
    filepath = "../core-chapters/" + txtdir + ".md"
    txttoreplace = ".\/" + txtdir + oldtxt
    txtcmd = "sed -i '' 's/%s/%s/g' " % (txttoreplace, newtxt) + filepath
    call(txtcmd, shell=True)

# Change chapter numbers on last core chapters to match new org
call("mv ../core-chapters/7-lessons.md " +
     "../core-chapters/5-lessons.md", shell=True)
call("mv ../core-chapters/8-supporting.md " +
     "../core-chapters/6-future.md", shell=True)
call("mv ../core-chapters/9-glossary.md " +
     "../core-chapters/7-glossary.md", shell=True)
