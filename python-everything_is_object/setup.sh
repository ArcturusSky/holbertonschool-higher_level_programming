#!/bin/bash

# File to create all the files (empty and executable) in one go 

for i in {0..28}; do
    touch "$i-answer.txt"
chmod u+x *-answer.txt
done