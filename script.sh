#!/bin/bash

cd ~/Downloads/Imagens/
ls *.jpg | sed 's/^\(Cisto\|Lesao_Benigna\|Lesao_Maligna\|Sem_Lesao\)_\(.*\)/\1_\2,\L\1/'
# print(files)
