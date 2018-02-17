# -*- coding: UTF-8 -*-
import datetime
def init():

  global chatGroups
  global vT
  global usersDict
  global admins 
  global ADMIN
  global previousDay

  chatGroups =[
  u'普渡二手交易群',
  u'普渡🚗汽车群',
  u'普渡租房群🏠',
  u'普渡拼车群🚗',
  u'普渡工作实习内推',
  u'北美信用',
  u'线上KTV',
  u'Chuck郭律师',
  u'2018 H1B 中中中',
  u'北美区块链技术交流总群',
  u'北美股市Trading技术交流总群1'
  ]
  save = [
  u'北美CPA',
  u'北美表情分享'
  ]

  v0= u"您好,Purdue普渡加群建群小助手为您服务:)\n"
  v00=u"每天只能加1个群哦;\n"
  v1= u"回复 0 普渡二手交易群;\n"
  v2= u"回复 1 普渡🚗汽车群;\n"
  v3= u"回复 2 普渡租房群🏠;\n"
  v4= u"回复 3 普渡拼车群🚗';\n"
  v5= u"回复 4 普渡工作实习内推总群;\n"
  v6= u"回复 5 北美信用卡爱好者总群;\n"
  v7= u"回复 6 加线上KTV开嗓🎙️北美总群;\n"
  v8= u"回复 7 加Chuck郭律师美帝绿卡讨论群;\n"
  v9= u"回复 8 加H1B中中中讨论群;\n"
  v10= u"回复 9 加北美区块链技术交流总群;\n"
  v11= u"回复 10 加北美股市Trading技术交流总群;\n"
  v12= u"回复 99 查看【北美加群小助手Jogchat.com】\n公众号二维码加纽约、硅谷、西雅图等群\n"
  vT =v0+v00+v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12
  
  
  #v8= u"回复 8 北美CPA,REG天天刷题群;\n"
  #v9= u"回复 9 加北美表情分享总群;\n"

  usersDict = {}
  admins = []
  ADMIN = u'@Purdue加群小助手'
  previousDay = datetime.datetime.now().day
 
