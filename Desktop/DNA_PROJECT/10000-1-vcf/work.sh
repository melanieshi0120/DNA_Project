perl /home/sunysh/12Cancer/bin/filter.pl 10000-1.total.unique.Matrix 10000-1.total.unique.filter.Matrix
python /home/sunysh/12Cancer/bin/split.py 10000-1.total.unique.filter.Matrix /home/sunysh/12Cancer/BRCA/10000-1-vcf/
cat 2 3 4 5 > train.Matrix.1
cat 1 3 4 5 > train.Matrix.2
cat 1 2 4 5 > train.Matrix.3
cat 1 2 3 5 > train.Matrix.4
cat 1 2 3 4 > train.Matrix.5
mkdir part1 part2 part3 part4 part5
