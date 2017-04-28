# -*- coding: utf-8 -*-
import copy
import GlobalConst

datas={
1: {'entityType': 'SpaceCenter', 'name': '中心城', 'type': 1, 'resPath': 'spaces/center', 'spawnPos': (0, 1.5, 0), 'id': 1}, 
1001: {'entityType': 'Space', 'name': '游戏场景', 'type': 2, 'resPath': 'spaces/cell_sene', 'spawnPos': (-97.9299, 1.5, -158.922), 'id': 1001}, 
3001: {'entityType': 'SpaceDuplicate', 'name': '副本', 'type': 3, 'resPath': 'spaces/duplicate', 'spawnPos': (0.0, 1.5, 0.0), 'id': 3001}}

idx = 1001
cellspace = datas[idx]

for i in range(GlobalConst.MAX_STRESSTEST_CELL_SPACE):
	idx += 1
	datas[idx] = copy.deepcopy(cellspace)
	datas[idx]["id"] = idx
	datas[idx]['name'] += str(idx)

allDatas = {
	'场景表':datas,
}