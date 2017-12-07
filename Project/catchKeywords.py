# -*- coding: utf-8 -*-

import re

#if there are two str, firstStr is the str about time
def catchKeywords(firstStr, secStr = None):
	resultList = []

	#按空格将第一个字符串分割，并把空格删除
	firstStr = firstStr.replace('\n','')
	firstList = firstStr.split(' ')
	firstList.sort()
	for index in range(0, len(firstList)):
		if (firstList[0] == ''):
			firstList.pop(0)
		else:
			break

	#找到firstList中日期所在元素，放到结果中，并从firstList中删除
	dateMatch = False
	for term in firstList:
		date1 = re.findall(r'[0-9]+-[0-9]+-[0-9]+',term)
		if(len(date1) != 0):
			resultList.append(date1[0])
			firstList.remove(term)
			dateMatch = True
			break

		date2 = re.findall(r'[0-9]+/[0-9]+/[0-9]+', term)
		if (len(date2) != 0):
			subDate = re.findall(r'[0-9]+',date2[0])
			resultList.append(subDate[0]+'-'+subDate[1]+'-'+subDate[2])
			firstList.remove(term)
			dateMatch = True
			break

		date3 = re.findall(r'[0-9]+年[0-9]+月[0-9]+日', term)
		if (len(date3) != 0):
			subDate = re.findall(r'[0-9]+', date3[0])
			resultList.append(subDate[0] + '-' + subDate[1] + '-' + subDate[2])
			firstList.remove(term)
			dateMatch = True
			break

		date4 = re.findall(r'[0-9]+-[0-9]+', term)
		if (len(date4) != 0):
			resultList.append(date4[0])
			firstList.remove(term)
			dateMatch = True
			break

	if not dateMatch:
		resultList.append('无详细发布日期')

	#找到firstList中时间所在元素，放到结果中，并从firstList中删除
	timeMatch = False
	for term in firstList:
		time1 = re.findall(r'[0-9]+:[0-9]+:[0-9]+', term)
		if (len(time1) != 0):
			resultList.append(time1[0])
			firstList.remove(term)
			timeMatch = True
			break

		time2 = re.findall(r'[0-9]+:[0-9]+', term)
		if (len(time2) != 0):
			resultList.append(time2[0]+':00')
			firstList.remove(term)
			timeMatch = True
			break

	if not timeMatch:
		resultList.append('无详细发布时间')

	#依据是否有第二个str得到用于获取来源的secList
	secList = []
	if(secStr == None):
		secList = firstList
	else:
		secStr = secStr.replace('\n','')
		secList = secStr.split(' ')
		secList.sort()
		for index in range(0, len(secList)):
			if (secList[0] == ''):
				secList.pop(0)
			else:
				break

	#粗略处理来源部分，删掉已知无用部分 （可追加）
	uselessStr = ['发表于', '发布时间：', '来源：', '消息来源：', '发布时间:', '来源:', '消息来源:', '&nbsp&nbsp']
	for deleteStr in uselessStr:
		try:
			secList.remove(deleteStr)
		except:
			pass

	#将处理结果放入结果中
	origin = ''
	for term in secList:
		origin = origin + term + ' '
	if(len(origin) == 0):
		origin = '无详细来源'
	resultList.append(origin)

	return resultList

