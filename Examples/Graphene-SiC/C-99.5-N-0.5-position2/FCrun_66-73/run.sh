#!/bin/csh 
#$ -cwd  
#$ -V -S /bin/bash 
#$ -N PHrun-VCA 
#$ -o stdout 
#$ -e stdout 
#$ -pe smp 24  
mpirun  /home/emi/siesta/siesta-4.1-b2/Obj_Transiesta/transiesta   < ./RUN.fdf > ./RUN.out  
