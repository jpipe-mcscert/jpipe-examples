#! /usr/bin/env bash

for file in *.dot
do
    dot -Tpdf < $file > $(basename $file '.dot').pdf
    dot -Tsvg < $file > $(basename $file '.dot').svg
done    