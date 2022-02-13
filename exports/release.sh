#!/bin/bash

release_path=~/sokoban/exports

function download_and_push() {
    echo "Downloading $1"
    wget $1 -q -P $2
    butler push $2 $3:$4
    rm -rf "${2:?}/"*
}

owner=bendnuts
repository=sokoban

path="https://github.com/$owner/$repository/releases/latest/download"

itch_path=bendn/sokoban

download_and_push "$path/Linux.zip" "$release_path/linux" "$itch_path" linux
download_and_push "$path/HTML.zip" "$release_path/html" "$itch_path" html
download_and_push "$path/Windows.zip" "$release_path/windows" "$itch_path" windows
download_and_push "$path/Mac.zip" "$release_path/mac" "$itch_path" mac