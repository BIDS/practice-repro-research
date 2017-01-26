To update the online Gitbook, ensure that the _repro-case-studies_ and _repro-case-private_ repositories are located in the file system as described in the script copy_chapters.py.

1.  Check out the most recent versions of the master branches of both repositories.
2.  Run copy_chapters.py from within the build-book directory.
3.  Edit the README.md file to bump the version history line at the bottom - include the SHA for the state of the the _repro-case-studies_ and _repro-case-private_ repositories when the contents of this repository were built.
4.  Commit all changes made to this repository, using the version history line from the bottom of README.md as the commit message.
5.  Push changes to this repository.
6.  Confirm that Gitbook built the new book successfully.

NOTE: There are several files that are used only in the Gitbook online book that must be kept manually in sync with other "main" files. These are:

1.  The file TOC.md (the tables of contents page), which must be manually edited to match SUMMARY.md (the sidebar).
2.  The several html table files in the _repro-case-studies_ repository, which were generated using `pandoc` from the Markdown tables in several core and case study chapters. Basically, whenever any table is edited in any Markdown file, the corresponding html file must be edited to match.
