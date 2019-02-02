#!/usr/bin/env bash
# @Time  : 2019-01-30 11:55
# @Author: sunnnychan@gmail.com
# @File  : login.sh

SCRIPT_HOME="$(cd $(dirname $0) && pwd -P)"
WORK_HOME="${SCRIPT_HOME}/.."
SRC_DIR="${WORK_HOME}/src"

CONF_FILE="${WORK_HOME}/conf/login.input"

alias python="python3"

python "${SRC_DIR}/cmd-exe.py" ${CONF_FILE}