from py2neo import authenticate, Graph
from py2neo import Node, Relationship


# set up authentication parameters
authenticate("localhost:7474", "neo4j", "123456")

# connect to authenticated graph database
#sgraph = Graph("http://localhost:7474/db/data/")
graph = Graph()

#graph.delete_all()

i = 0
person = []

while i <= 4038:
    temp_str = '%d' %i
    temp_node = Node("Person", name = temp_str)
    person.append(temp_node)
    graph.create(person[i])
    i = i + 1
#print person[282].labels
print "end1\n"

f10 = open("./facebook/0.edges", "r")
while True:
    line = f10.readline()
    if line:
        line = line.strip()
        p = line.rfind(' ')
        q = len(line)
        a_str = line[0 : p]
        b_str = line[p + 1 : q + 1]
        a = int(a_str)
        b = int(b_str)
        friendship = Relationship(person[a], "FRIEND", person[b])
        graph.create(friendship)

    else:
        break

print "f10 end!\n"

f11 = open("./facebook/107.edges", "r")
while True:
    line = f11.readline()
    if line:
        line = line.strip()
        p = line.rfind(' ')
        q = len(line)
        a_str = line[0 : p]
        b_str = line[p + 1 : q + 1]
        a = int(a_str)
        b = int(b_str)
        friendship = Relationship(person[a], "FRIEND", person[b])
        graph.create(friendship)

    else:
        break

print "f11 end!\n"

f12 = open("./facebook/348.edges", "r")
while True:
    line = f12.readline()
    if line:
        line = line.strip()
        p = line.rfind(' ')
        q = len(line)
        a_str = line[0 : p]
        b_str = line[p + 1 : q + 1]
        a = int(a_str)
        b = int(b_str)
        friendship = Relationship(person[a], "FRIEND", person[b])
        graph.create(friendship)

    else:
        break

print "f12 end!\n"

f13 = open("./facebook/414.edges", "r")
while True:
    line = f13.readline()
    if line:
        line = line.strip()
        p = line.rfind(' ')
        q = len(line)
        a_str = line[0 : p]
        b_str = line[p + 1 : q + 1]
        a = int(a_str)
        b = int(b_str)
        friendship = Relationship(person[a], "FRIEND", person[b])
        graph.create(friendship)

    else:
        break

print "f13 end!\n"

f14 = open("./facebook/686.edges", "r")
while True:
    line = f14.readline()
    if line:
        line = line.strip()
        p = line.rfind(' ')
        q = len(line)
        a_str = line[0 : p]
        b_str = line[p + 1 : q + 1]
        a = int(a_str)
        b = int(b_str)
        friendship = Relationship(person[a], "FRIEND", person[b])
        graph.create(friendship)

    else:
        break

print "f14 end!\n"

f15 = open("./facebook/698.edges", "r")
while True:
    line = f15.readline()
    if line:
        line = line.strip()
        p = line.rfind(' ')
        q = len(line)
        a_str = line[0 : p]
        b_str = line[p + 1 : q + 1]
        a = int(a_str)
        b = int(b_str)
        friendship = Relationship(person[a], "FRIEND", person[b])
        graph.create(friendship)

    else:
        break

print "f15 end!\n"

f16 = open("./facebook/1684.edges", "r")
while True:
    line = f16.readline()
    if line:
        line = line.strip()
        p = line.rfind(' ')
        q = len(line)
        a_str = line[0 : p]
        b_str = line[p + 1 : q + 1]
        a = int(a_str)
        b = int(b_str)
        friendship = Relationship(person[a], "FRIEND", person[b])
        graph.create(friendship)

    else:
        break

print "f16 end!\n"

f17 = open("./facebook/1912.edges", "r")
while True:
    line = f17.readline()
    if line:
        line = line.strip()
        p = line.rfind(' ')
        q = len(line)
        a_str = line[0 : p]
        b_str = line[p + 1 : q + 1]
        a = int(a_str)
        b = int(b_str)
        friendship = Relationship(person[a], "FRIEND", person[b])
        graph.create(friendship)

    else:
        break

print "f17 end!\n"

f18 = open("./facebook/3437.edges", "r")
while True:
    line = f18.readline()
    if line:
        line = line.strip()
        p = line.rfind(' ')
        q = len(line)
        a_str = line[0 : p]
        b_str = line[p + 1 : q + 1]
        a = int(a_str)
        b = int(b_str)
        friendship = Relationship(person[a], "FRIEND", person[b])
        graph.create(friendship)

    else:
        break

print "f18 end!\n"

f19 = open("./facebook/3980.edges", "r")
while True:
    line = f19.readline()
    if line:
        line = line.strip()
        p = line.rfind(' ')
        q = len(line)
        a_str = line[0 : p]
        b_str = line[p + 1 : q + 1]
        a = int(a_str)
        b = int(b_str)
        friendship = Relationship(person[a], "FRIEND", person[b])
        graph.create(friendship)

    else:
        break

print "f19 end!\n"

f20 = open("./facebook/0.circles", "r")
node_s = 0
while True:
    line = f20.readline()
    if line:
        line = line.strip()
        q = len(line)
        p = line.find('\t', 0, q)

        circle_ID = '0_' + line[0 : p]
        person[node_s].add_label(circle_ID)
        graph.push(person[node_s])
        while p < q:
            tmp = p
            p = line.find('\t', tmp + 1, q)
            if p == -1:
                p = q
            node_i = int(line[tmp + 1 : p + 1])
            print node_i
            friendship = Relationship(person[node_s], "FRIEND", person[node_i])
            graph.create(friendship)
            friendship = Relationship(person[node_i], "FRIEND", person[node_s])
            graph.create(friendship)
            print person[node_i].labels
            person[node_i].add_label(circle_ID)
            print person[node_i].labels
            graph.push(person[node_i])
    else:
        break

print "f20 end!\n"

f21 = open("./facebook/107.circles", "r")
node_s = 107
while True:
    line = f21.readline()
    if line:
        line = line.strip()
        q = len(line)
        p = line.find('\t', 0, q)

        circle_ID = '1_' +  line[0: p]
        person[node_s].add_label(circle_ID)
        graph.push(person[node_s])
        while p < q:
            tmp = p
            p = line.find('\t', tmp + 1, q)
            if p == -1:
                p = q
            node_i = int(line[tmp + 1: p + 1])
            print node_i
            friendship = Relationship(person[node_s], "FRIEND", person[node_i])
            graph.create(friendship)
            friendship = Relationship(person[node_i], "FRIEND", person[node_s])
            graph.create(friendship)
            print person[node_i].labels
            person[node_i].add_label(circle_ID)
            print person[node_i].labels
            graph.push(person[node_i])
    else:
        break

print "f21 end!\n"

f22 = open("./facebook/348.circles", "r")
node_s = 348
while True:
    line = f22.readline()
    if line:
        line = line.strip()
        q = len(line)
        p = line.find('\t', 0, q)

        circle_ID =  '2_' + line[0: p]
        person[node_s].add_label(circle_ID)
        graph.push(person[node_s])
        while p < q:
            tmp = p
            p = line.find('\t', tmp + 1, q)
            if p == -1:
                p = q
            node_i = int(line[tmp + 1: p + 1])
            print node_i
            friendship = Relationship(person[node_s], "FRIEND", person[node_i])
            graph.create(friendship)
            friendship = Relationship(person[node_i], "FRIEND", person[node_s])
            graph.create(friendship)
            print person[node_i].labels
            person[node_i].add_label(circle_ID)
            print person[node_i].labels
            graph.push(person[node_i])
    else:
        break

print "f22 end!\n"

f23 = open("./facebook/414.circles", "r")
node_s = 414
while True:
    line = f23.readline()
    if line:
        line = line.strip()
        q = len(line)
        p = line.find('\t', 0, q)

        circle_ID =  '3_' + line[0: p]
        person[node_s].add_label(circle_ID)
        graph.push(person[node_s])
        while p < q:
            tmp = p
            p = line.find('\t', tmp + 1, q)
            if p == -1:
                p = q
            node_i = int(line[tmp + 1: p + 1])
            print node_i
            friendship = Relationship(person[node_s], "FRIEND", person[node_i])
            graph.create(friendship)
            friendship = Relationship(person[node_i], "FRIEND", person[node_s])
            graph.create(friendship)
            print person[node_i].labels
            person[node_i].add_label(circle_ID)
            print person[node_i].labels
            graph.push(person[node_i])
    else:
        break

print "f23 end!\n"

f24 = open("./facebook/686.circles", "r")
node_s = 686
while True:
    line = f24.readline()
    if line:
        line = line.strip()
        q = len(line)
        p = line.find('\t', 0, q)

        circle_ID =  '4_' + line[0: p]
        person[node_s].add_label(circle_ID)
        graph.push(person[node_s])
        while p < q:
            tmp = p
            p = line.find('\t', tmp + 1, q)
            if p == -1:
                p = q
            node_i = int(line[tmp + 1: p + 1])
            print node_i
            friendship = Relationship(person[node_s], "FRIEND", person[node_i])
            graph.create(friendship)
            friendship = Relationship(person[node_i], "FRIEND", person[node_s])
            graph.create(friendship)
            print person[node_i].labels
            person[node_i].add_label(circle_ID)
            print person[node_i].labels
            graph.push(person[node_i])
    else:
        break

print "f24 end!\n"

f25 = open("./facebook/698.circles", "r")
node_s = 698
while True:
    line = f25.readline()
    if line:
        line = line.strip()
        q = len(line)
        p = line.find('\t', 0, q)

        circle_ID = '5_' +  line[0: p]
        person[node_s].add_label(circle_ID)
        graph.push(person[node_s])
        while p < q:
            tmp = p
            p = line.find('\t', tmp + 1, q)
            if p == -1:
                p = q
            node_i = int(line[tmp + 1: p + 1])
            print node_i
            friendship = Relationship(person[node_s], "FRIEND", person[node_i])
            graph.create(friendship)
            friendship = Relationship(person[node_i], "FRIEND", person[node_s])
            graph.create(friendship)
            print person[node_i].labels
            person[node_i].add_label(circle_ID)
            print person[node_i].labels
            graph.push(person[node_i])
    else:
        break

print "f25 end!\n"

f26 = open("./facebook/1684.circles", "r")
node_s = 1684
while True:
    line = f26.readline()
    if line:
        line = line.strip()
        q = len(line)
        p = line.find('\t', 0, q)

        circle_ID = '6_' +  line[0: p]
        person[node_s].add_label(circle_ID)
        graph.push(person[node_s])
        while p < q:
            tmp = p
            p = line.find('\t', tmp + 1, q)
            if p == -1:
                p = q
            node_i = int(line[tmp + 1: p + 1])
            print node_i
            friendship = Relationship(person[node_s], "FRIEND", person[node_i])
            graph.create(friendship)
            friendship = Relationship(person[node_i], "FRIEND", person[node_s])
            graph.create(friendship)
            print person[node_i].labels
            person[node_i].add_label(circle_ID)
            print person[node_i].labels
            graph.push(person[node_i])
    else:
        break

print "f26 end!\n"

f27 = open("./facebook/1912.circles", "r")
node_s = 1912
while True:
    line = f27.readline()
    if line:
        line = line.strip()
        q = len(line)
        p = line.find('\t', 0, q)

        circle_ID = '7_' +  line[0: p]
        person[node_s].add_label(circle_ID)
        graph.push(person[node_s])
        while p < q:
            tmp = p
            p = line.find('\t', tmp + 1, q)
            if p == -1:
                p = q
            node_i = int(line[tmp + 1: p + 1])
            print node_i
            friendship = Relationship(person[node_s], "FRIEND", person[node_i])
            graph.create(friendship)
            friendship = Relationship(person[node_i], "FRIEND", person[node_s])
            graph.create(friendship)
            print person[node_i].labels
            person[node_i].add_label(circle_ID)
            print person[node_i].labels
            graph.push(person[node_i])
    else:
        break

print "f27 end!\n"

f28 = open("./facebook/3437.circles", "r")
node_s = 3437
while True:
    line = f28.readline()
    if line:
        line = line.strip()
        q = len(line)
        p = line.find('\t', 0, q)

        circle_ID = '8_' +  line[0: p]
        person[node_s].add_label(circle_ID)
        graph.push(person[node_s])
        while p < q:
            tmp = p
            p = line.find('\t', tmp + 1, q)
            if p == -1:
                p = q
            node_i = int(line[tmp + 1: p + 1])
            print node_i
            friendship = Relationship(person[node_s], "FRIEND", person[node_i])
            graph.create(friendship)
            friendship = Relationship(person[node_i], "FRIEND", person[node_s])
            graph.create(friendship)
            print person[node_i].labels
            person[node_i].add_label(circle_ID)
            print person[node_i].labels
            graph.push(person[node_i])
    else:
        break

print "f28 end!\n"

f29 = open("./facebook/3980.circles", "r")
node_s = 3980
while True:
    line = f29.readline()
    if line:
        line = line.strip()
        q = len(line)
        p = line.find('\t', 0, q)

        circle_ID = '9_' +  line[0: p]
        person[node_s].add_label(circle_ID)
        graph.push(person[node_s])
        while p < q:
            tmp = p
            p = line.find('\t', tmp + 1, q)
            if p == -1:
                p = q
            node_i = int(line[tmp + 1: p + 1])
            print node_i
            friendship = Relationship(person[node_s], "FRIEND", person[node_i])
            graph.create(friendship)
            friendship = Relationship(person[node_i], "FRIEND", person[node_s])
            graph.create(friendship)
            print person[node_i].labels
            person[node_i].add_label(circle_ID)
            print person[node_i].labels
            graph.push(person[node_i])
    else:
        break

print "f29 end!\n"

'''
while i <= 347:
    temp_str = '%d' %i
    temp_node = Node("Person", name = temp_str)
    person.append(temp_node)
#    graph.create(person[i])
    i = i + 1
#print person[282].labels
print "end1\n"

f2 = open("./facebook/0.circles", "r")

while True:
    line = f2.readline()
    if line:
        line = line.strip()
        q = len(line)
        p = line.find('\t', 0, q)

        circle_ID = line[0 : p]
        person[0].add_label(circle_ID)
        while p < q:
            tmp = p
            p = line.find('\t', tmp + 1, q)
            if p == -1:
                p = q
            node_i = int(line[tmp + 1 : p + 1])

            print person[node_i].labels
            person[node_i].add_label(circle_ID)
            print person[node_i].labels
            graph.push(person[node_i])

    else:
        break

'''
'''MATCH a-[:FRIEND]->follower,b-[:FRIEND]->follower WHERE a.name = '284' and b.name = '239' RETURN follower'''
f3 = open("./facebook/0.featnames", "r")
'''
featnames = []
while True:
    line = f3.readline()
    if line:
        tmpname = line.strip()
        featnames.append(tmpname)

    else:
        break
'''
'''
i = 0
while i < 224:
    tmp = featnames[i]
    print tmp
    i = i + 1
'''
'''
f4 = open("./facebook/0.egofeat", "r")
while True:
    line = f4.readline()
    if line:
        line = line.strip()
        q = len(line)
        p = -1
        i = 0
        while p < q:
            tmp = p
            p = line.find(' ', tmp + 1, q)
            if p == -1:
                p = q
            feature = int(line[tmp + 1: p + 1])
            tmpname = featnames[i]
            person[0].properties[featnames[i]] = feature
            i = i + 1
        print person[0].labels
#        print person[0].properties[featnames[9]]
    else:
        break

print "end4\n"
'''
'''
i = 0
while i <= 347:
    graph.create(person[i])
    i = i + 1
print "end2\n"

f1 = open("./facebook/0.edges", "r")
while True:
    line = f1.readline()
    if line:
        line = line.strip()
        p = line.rfind(' ')
        q = len(line)
        a_str = line[0 : p]
        b_str = line[p + 1 : q + 1]
        a = int(a_str)
        b = int(b_str)
        friendship = Relationship(person[a], "FRIEND", person[b])
        graph.create(friendship)

    else:
        break

print "end3\n"
'''

