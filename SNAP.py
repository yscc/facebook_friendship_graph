# coding=utf-8
import random
from flask import Flask, jsonify, render_template
from py2neo import Graph, authenticate

f1 = open('node.txt','wb')
f2 = open('edge.txt','wb')
authenticate("localhost:7474", "neo4j", "123456")
app = Flask(__name__)
graph = Graph()

def buildNodes(node):
	data = {"id": node['n']['name'], "label": ''}
	# data = {"id": node['n']['name'], "label": list(node['n'].labels())}
	data.update(node['n'].properties)
	f1.write(node['n']['name']+'\n')
	return {"data": data}


def buildEdges(relation):
	data = {"source": relation['r'].start_node()['name'],
			"target": relation['r'].end_node()['name'],
			"relationship": relation['r'].relationships()[0].type()}
	f2.write(relation['r'].start_node()['name']+' '+relation['r'].end_node()['name']+'\n')
	return {"data": data}


def buidRandom(R, N, random_tag):
	Nl = len(N)
	# N_set节点集合
	N_set=[]
	for n in N:
		N_set.append(n['data']['name'])
	# 去掉重复的边，和R中节点在N中没有的边
	print 'remove error edge'
	R1=[]
	for r in R:
		if r['data']['source'] in N_set and r['data']['target'] in N_set:
			flag=True
			for r1 in R1:
				if r1['data']['source']==r['data']['target'] and r1['data']['target']== r['data']['source']:
					flag=False
			if flag:
				R1.append(r)

	i = 0
	tag1_list = []
	# 随机标记random_tag个tag1
	print 'put tag1'
	while i < random_tag:
		k = random.randint(0, Nl - 1)
		if 'tag1' not in N[k]['data']['label']:
			tag1_list.append(k)
			N[k]['data']['label'] = 'tag1'
			i += 1
	#根据random_tag个tag1的relation来标记tag2
	print 'put tag2'
	for tag1 in tag1_list:
		for r in R1:
			if r['data']['source'] == str(tag1):
				if int(r['data']['target']) <len(N):
					if 'tag1' != N[int(r['data']['target'])]['data']['label']:
						N[int(r['data']['target'])]['data']['label'] = 'tag2'
			elif r['data']['target'] == str(tag1):
				if int(r['data']['source']) <len(N):
					if 'tag1' != N[int(r['data']['source'])]['data']['label']:
						N[int(r['data']['source'])]['data']['label'] = 'tag2'
	print 'end buildRandom'
	return jsonify(elements={"nodes": N, "edges": R1})


@app.route('/')
def hello_world():
	return 'Hello World!'


@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/graph')
def get_graph():
	f1 = open('node.txt','wb')
	f2 = open('edge.txt','wb')
	node_num = 500
	random_tag = 20
	print 'match nodes'
	# 查询 node_num个节点
	N = graph.data('MATCH (n) RETURN n limit ' + str(node_num))
	# 格式化字符串
	print 'build nodes'
	nodes = map(buildNodes, N)

	E = []
	print 'match relation'
	# 只查询node_num个节点的一跳关系
	for n in N:
		name = n['n']['name']
		E += graph.data('MATCH (a)-[r]->()where id(a)=' + name + ' RETURN r')
		#E += graph.data('MATCH ()-[r]->(a)where id(a)=' + name + ' RETURN r')
	print 'build edges'
	edges = map(buildEdges, E)
	# edges = map(buildEdges, graph.data('MATCH ()-[r]->() RETURN r'))
	print 'buildRandom'
	f1.flush()
	f2.flush()
	return buidRandom(edges, nodes, random_tag)


if __name__ == '__main__':
	app.run()
