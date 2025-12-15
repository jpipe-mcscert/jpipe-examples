#! /usr/bin/env bash

for file in *.svg
do
    rsvg-convert -f pdf -o $(basename $file '.svg').pdf $file
done    