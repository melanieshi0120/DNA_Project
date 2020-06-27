python /home/sunysh/12Cancer/bin/ROC/Roc_prepare.py A B C
less A|awk '{print $2}'|sort -u> standard
python /home/sunysh/12Cancer/bin/ROC/Roc_point.py C standard point
less point|sort -k1n -k2nr>point.sort
python /home/sunysh/12Cancer/bin/ROC/AUC.py point.sort >AUC.result
