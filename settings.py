# -*- coding: UTF-8 -*-
def init():

  global chatGroups
  global vT
  global usersDict
  global admins 

  chatGroups =[
  u'纽约拼车',
  u'天天刷题',
  u'纽约租房',
  u'NYU纽约校友',
  u'纽约美食',
  u'纽约二手',
  u'北美CPA',
  u'北美妈妈',
  u'圣约翰租房',
  u'北美信用',
  u'线上KTV',
  u'北美表情分享'
  ]

  v0= u"您好,NYU纽约加群建群小助手为您服务:)\n"
  v00=u"每天只能加3个群哦;\n"
  v1= u"回复 0 加纽约拼车群;\n"
  v2= u"回复 1 加北美CS刷题竞赛面试总群;\n"
  v3= u"回复 2 加纽约租房群;\n"
  v4= u"回复 3 加NYU纽约校友群;\n"
  v5= u"回复 4 加纽约美食约饭群;\n"
  v6= u"回复 5 加纽约二手货群;\n"
  v7= u"回复 6 加北美CPA,REG天天刷题群;\n"
  v8= u"回复 7 加北美妈妈母婴总群;\n"
  v9= u"回复 8 加圣约翰租房叫车玩乐全攻略群;\n"
  v10= u"回复 9 北美信用卡爱好者总群;\n"
  v11= u"回复 10 加线上KTV开嗓🎙️北美总群;\n"
  v12= u"回复 11 加北美表情分享总群;\n"
  vT =v0+v00+v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12
  
  usersDict = {}
  admins = []
