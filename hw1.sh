#!/bin/bash

hw="homework"
fcont="homework/content.txt"

[[ -d $hw ]] && echo "$hw dir already exist" || mkdir ~/$hw
[[ -e ~/$fcont ]] && echo "~/$fcont already exist" || touch ~/$fcont

date >> ~/$fcont; cat ~/$fcont|wc -l 


