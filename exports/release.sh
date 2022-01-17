#!/bin/bash

release_path=~/sokoban/exports

export PATH="$HOME/.local/bin:$PATH"

release sokoban "$release_path/linux" "$release_path/windows" "$release_path/mac" "$release_path/html" $1
