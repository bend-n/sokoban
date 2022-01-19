#!/bin/bash

release_path=~/sokoban/exports

if [ "$1" == "-y" ]; then
    yes | release -e sokoban "$release_path/linux" "$release_path/windows" "$release_path/mac" "$release_path/html" $1
else
    release -e sokoban "$release_path/linux" "$release_path/windows" "$release_path/mac" "$release_path/html" $1
fi
