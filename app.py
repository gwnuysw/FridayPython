from flask import Flask, escape, request
import json, usefulMethods
from usefulMethods import getSysNumber, responseHandler
from tinydb import TinyDB, Query
import sortfunc

app = Flask(__name__)
db = TinyDB('./questionFlow.json')
TREE = Query()

@app.route('/', methods=['POST'])
def watsonInput():
	# 데이터 베이스에서 트리정보를 가져옴
	trees = db.search(TREE.type == "json")[0]['trees']
	print(trees)
	#json 형식의 데이터를 dictionary 형식으로 바꿔줌
	data = json.loads(request.data)
	#새로 만들어진 크리가 아닌 경우
	if data['treeName'] in trees:
		#처음 실행하는 노드인 경우 실행횟수 1을 리스트에  추가한다.
		if len(trees[data['treeName']]) <= int(data['currentNode']):
			trees[data['treeName']].append(1)
		#처음 실행하는게 아니면 해당 노드에 +1해준다.
		else:
			trees[data['treeName']][int(data['currentNode'])] += 1
	#새로 만들어진 트리인 경우 트리를 만든다
	else:
		trees[data['treeName']] = []
		trees[data['treeName']].append(1)
	db.update({'trees':trees}, TREE.type=="json")
	#현재 노드가 트리의 마지막 노드인 경우실행
	if len(trees[data['treeName']]) - 1 == int(data['currentNode']):
		#중간 이탈이 가장 많은 트리를 찾는다.
		'''
		hard = {}
		for key in trees:
			big = 0
			small = 10
			for key2 in range(len(trees[key])):
				if big < trees[key][key2]:
					big = trees[key][key2]
				if small > trees[key][key2]:
					small = trees[key][key2]
			hard[key] = big - small
		'''
		#가장 많이 검색한 트리를 찾는다.
		'''
		many = ''
		temp = 0
		for key in trees:
			if temp < trees[key][0]:
				temp = trees[key][0]
				many = key
		hardest = max(hard, key=hard.get)
		print('hardest one',hardest)
		print('many ', many)
		'''
		hardest = ''
		many = ''
		sortedAbortTree = sorted(trees.items(), key = sortfunc.treeGetAbort, reverse = True)
		sortedManyTree = sorted(trees.items(), key = sortfunc.manySearch, reverse = True)
		if data['treeName'] == sortedAbortTree[0][0]:
			hardest = sortedAbortTree[1][0]
		else:
			hardest = sortedAbortTree[0][0]
		if data['treeName'] == sortedManyTree[0][0]:
			many = sortedManyTree[1][0]
		else:
			many = sortedManyTree[0][0]
		#데이터 베이스 업데이트
		j = json.dumps({'hardest':hardest,'manyask':many})
		print(j)
		print('what tha fack')
		return json.loads(j)
	else:
		return {}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
