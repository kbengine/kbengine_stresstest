#!/bin/sh

export KBE_ROOT="/datas/kbengine"
export KBE_RES_PATH="$KBE_ROOT/kbe/res/:/datas/kbengine/kbengine_stresstest/mmorpg/server_assets:/datas/kbengine/kbengine_stresstest/mmorpg/server_assets/res:/datas/kbengine/kbengine_stresstest/mmorpg/server_assets/scripts/"
export KBE_BIN_PATH="$KBE_ROOT/kbe/bin/server/"

python watchlog.py&
