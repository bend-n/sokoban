#!/bin/bash

release_path=~/sokoban/exports

release -e sokoban "$release_path/linux" "$release_path/windows" "$release_path/mac" "$release_path/html" $1
