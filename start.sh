SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
echo $SCRIPT_DIR
git -C $SCRIPT_DIR pull
python $SCRIPT_DIR/stock_printer.py