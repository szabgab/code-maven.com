---
title: "Error 718: Missing files cannot be found."
timestamp: 2016-05-27T18:00:01
tags:
  - error code
published: true
author: szabgab
archive: true
---


Once upon a time I worked at a company on an automated testing system. It had lots of "interesting" things in their
code-base, but one that stood out was one of the error messages:

## Error 718: Missing files cannot be found

Of course. If the file is missing, it cannot be found. What's the story?


## List of missing files

The system had a step checking if all the required files are present and it created a list of the files that were missing
and saved it in a file called `missing_files.txt`.

A later step then would read the content of `missing_files.txt` and report it it.

The question was, what to do if the file "missing_files.txt" did not exist? The rather unfortunate choice was to report
`Missing files cannot be found` with an obscure error number.

The problem was made worse as the 'missing_files.txt' file would only be created if there was at least one missing file.
In normal circumstances, when all the files were supplied, the 'missing_files.txt' was not created and this the error was reported.

Yes I know. This whole thing looks strange.

## Better solution?

A much better choice would have been an error message such as `The 'missing_files.txt' file could not be found.`
with possibly a link to a much more detailed explanation.

An even better solution would be probably to alway create the 'missing_files.txt' file, but leave it empty if
there are no missing file.


