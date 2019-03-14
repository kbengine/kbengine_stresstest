#!/bin/sh

currPath=$(pwd)
keyStr="/kbengine/"

bcontain=`echo $currPath|grep $keyStr|wc -l`


if [ $bcontain = 0 ]
then
	export KBE_ROOT="$(cd ../; pwd)"
else
	export KBE_ROOT="$(pwd | awk -F "/kbengine/" '{print $1}')/kbengine"
fi



export KBE_RES_PATH="$KBE_ROOT/kbe/res/:$(pwd):$(pwd)/res:$(pwd)/scripts/"
export KBE_BIN_PATH="$KBE_ROOT/kbe/bin/server/"
	
echo KBE_ROOT = \"${KBE_ROOT}\"
echo KBE_RES_PATH = \"${KBE_RES_PATH}\"
echo KBE_BIN_PATH = \"${KBE_BIN_PATH}\"

"$KBE_BIN_PATH/bots" --cid=100000000&
"$KBE_BIN_PATH/bots" --cid=110000000&
"$KBE_BIN_PATH/bots" --cid=120000000&
"$KBE_BIN_PATH/bots" --cid=130000000&
"$KBE_BIN_PATH/bots" --cid=140000000&
"$KBE_BIN_PATH/bots" --cid=150000000&
"$KBE_BIN_PATH/bots" --cid=160000000&
"$KBE_BIN_PATH/bots" --cid=170000000&
"$KBE_BIN_PATH/bots" --cid=180000000&
"$KBE_BIN_PATH/bots" --cid=190000000&
"$KBE_BIN_PATH/bots" --cid=200000000&
"$KBE_BIN_PATH/bots" --cid=210000000&
"$KBE_BIN_PATH/bots" --cid=220000000&
"$KBE_BIN_PATH/bots" --cid=230000000&
"$KBE_BIN_PATH/bots" --cid=240000000&
"$KBE_BIN_PATH/bots" --cid=250000000&
"$KBE_BIN_PATH/bots" --cid=260000000&
"$KBE_BIN_PATH/bots" --cid=270000000&
"$KBE_BIN_PATH/bots" --cid=280000000&
"$KBE_BIN_PATH/bots" --cid=290000000&

