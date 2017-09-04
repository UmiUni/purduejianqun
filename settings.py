# -*- coding: UTF-8 -*-
def init():

  global chatGroups
  global vT
  global usersDict
  global admins 
  global ADMIN

  chatGroups =[
  u'Purdue普渡拼车群',
  u'Purdue普渡二手车群'
  ]

  v0= u"您好,Purdue普渡加群建群小助手为您服务:)\n"
  v00=u"每天只能加3个群哦;\n"
  v1= u"回复 0 Purdue普渡拼车群;\n"
  v2= u"回复 1 Purdue普渡二手车群;\n"
  vT =v0+v00+v1+v2
  
  usersDict = {}
  admins = []
  ADMIN = u'@Purdue加群小助手'
