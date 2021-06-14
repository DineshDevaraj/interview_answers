
function prodapt_accounting_test {
    for x in {1..3}; do
        python prodapt_accounting.py --bank-name bank$x --input-filepath input_files/bank$x.csv;
        echo
    done;
}

prodapt_accounting_test
