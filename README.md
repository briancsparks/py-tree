# py-tree

A tree-like utility, but more how I want.

## Features

- Auto-magically ignore dirs and files that should always be ignored.
  - `.git/`
  - `node_modules/`
  - etc.
- Auto-magically go to the 'right' depth in each dir.
- Auto-magically put filenames left-to-right for leaf-dirs.
- Auto-magically show filenames left-to-right for certain file types
  like `.cpp` files.
- Colorful, the right way
  - Colorizing for execute is good
  - Colorizing for 0777 is horrible
- "Mark" files (color, symbols like '*', etc.)
  - Files/Dirs 'out of place' for a best-practice?
  - Files/Dirs 'verified' as following best-practice?
  - Dir is in $PATH?
  - `package.json` links to file (like `index.js`, or the `.../bin/` dir)?
  - Same for setup.py, et. al.


