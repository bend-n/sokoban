#!/usr/bin/python3

import re
from glob import iglob
import json
import os

used = set()
unused = set()

re_dest_files = re.compile(r'^dest_files=(\[.*\])$')

# for all *.import files in project:
for path in iglob("**/*.import", recursive=True):
    with open(path, 'r') as f:
        # find the dest_files line in the [deps] section
        deps = False
        found = False
        for line in f:
            if not deps:
                deps = (line == '[deps]\n')
                continue
            else:
                if line[0] == '[':
                    # new section encountered, somehow there's no dest_files
                    break

                # extract the imported file path(s)
                match = re_dest_files.match(line)
                if match:
                    paths_str = match.group(1)
                    paths = json.loads(paths_str)
                    md5s = set()
                    for i, p in enumerate(paths):
                        # remove 'res://'
                        paths[i] = p[6:]
                        md5s.add(os.path.splitext(paths[i])[0] + '.md5')

                    used |= set(paths)
                    used |= md5s
                    found = True
                    break

        if not found:
            print(f"warning: {path}: no deps.dest_files")

# find every file in .import/ that isn't referenced in a *.import file
for path in iglob('.import/*'):
    if path not in used:
        unused.add(path)

# do this alphabetically for nicer terminal output
unused = list(unused)
unused.sort()
n = 0

for path in unused:
    print(path)
    os.remove(path)
    n += 1

print('---')
print(f'removed {n} files from .import/')
