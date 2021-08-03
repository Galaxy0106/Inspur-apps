#!/bin/bash
path=~/Web/images/test2014_100
files=$(ls $path)
for filename in $files
do
   echo "${filename}"
   curl -F "file=@${path}/${filename};filename='${filename}'" http://localhost:8000/
done
