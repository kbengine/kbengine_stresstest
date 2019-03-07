# kbengine_stresstest

测试前要求

  1：必须使用Linux系统， 如unbuntu系统
  
  2: 系统默认的TCP和可建立的连接数都很小，执行kbengine\kbe\tools\server\linux\socket_optimization.sh优化系统后重启系统
  
  3：根据系统的核数配置适当的cellapp、baseapp进程的数量， 通常一核占用一个进程最好
  
  4: 启动服务器后等待服务器定时将所有场景创建完毕之后才可以进入游戏
  
  5: bots进程最好在另外一台机器上开启， 每个bots进程的虚拟客户端数量最好不要太多kbengine.xml->defaultAddBots->totalCount，例如配置为50， 需要测试多少人就缓慢多启动一点bots进程

  6: 条件满足的话dbmgr、cellappmgr、baseappmgr、logger以及mysql最好不要和baseapp、cellapp放在一台硬件上
  
  7：使用print_servers.sh输出服务器当前信息， clients代表当前客户端连接数。

--------------------------------------------------------------------------------------------

Video: http://v.youku.com/v_show/id_XMjgyMjM0MTYwNA==.html?spm=a2h3j.8428770.3416059.1
![screenshots1](https://github.com/kbengine/kbengine_stresstest/blob/master/screenshots/stresstest_mmorpg3.jpg)
