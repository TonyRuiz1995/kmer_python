#!/bin/sh
#python3 kmer.py 3 &
#python3 kmer.py 4 &
#python3 kmer.py 6 &
#python3 kmer.py 8 &
#python3 kmer.py 10 
#echo examining kmer $1 >>dat2.txt
start=$(date +%s%N | cut -b1-13)
start_generator=$(date +%s%N | cut -b1-13)
python3 generator.py $2 
end_generator=$(date +%s%N | cut -b1-13)
total_generator=$(echo "$end_generator - $start_generator"|bc)
echo TOTAL GENERATOR TIME: $total_generator  >> dat2.txt

start_kmer=$(date +%s%N | cut -b1-13)
python3 kmer.py $1
end_kmer=$(date +%s%N | cut -b1-13)
total_kmer=$(echo "$end_kmer - $start_kmer"|bc)
echo TOTAL KMER TIME: $total_kmer  >> dat2.txt

end=$(date +%s%N | cut -b1-13)
echo "$start"
echo "$end"
total=$(echo "$end - $start"|bc)
echo TOTAL TIME: $total  >> dat2.txt

