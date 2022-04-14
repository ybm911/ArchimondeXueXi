#!/bin/bash
RUN_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )";
echo $RUN_DIR
CMD="python3 $RUN_DIR/main.py >> $RUN_DIR/run.log"
echo "5 9 * * 3   root    $CMD" > /etc/cron.d/ArchimondeXueXi;
/etc/init.d/cron reload;
