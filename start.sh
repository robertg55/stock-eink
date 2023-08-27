HOME_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
USER=$(basename $HOME_DIR)
export PYTHONPATH=$HOME_DIR/stock-eink
git -C $HOME_DIR/stock-eink reset --hard HEAD
git -C $HOME_DIR/stock-eink pull
chown -R $USER:$USER $HOME_DIR/stock-eink/
python $HOME_DIR/stock-eink/stock_printer.py