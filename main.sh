#!/bin/sh
#python3 kmer.py 3 &
#python3 kmer.py 4 &
#python3 kmer.py 6 &
#python3 kmer.py 8 &
#python3 kmer.py 10 

python3 generator.py $2 

start=$(date +%s%N | cut -b1-13)
python3 kmer.py $1
end=$(date +%s%N | cut -b1-13)
#echo "$start"
#echo "$end"
total=$(($end - $start))
echo $total >> dat1.txt
echo $total >> data_times.txt
