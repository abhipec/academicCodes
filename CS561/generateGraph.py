# this is used to visualize graph
# it will generate a graph.dot file
# that can be converted to png by
#dot -Tpng graph.dot -o graph.png

png = open('graph.dot','w')
png.write('graph { \n')
png.write('splines=true;\nsep="+25,25";\noverlap=scalexy;\nnodesep=0.6;\n')

with open('graph.txt','r') as dataFile:
    lines = filter(None,dataFile.read().split('\n'))
    for vertex1, value in enumerate(lines):
        nodes = filter(None,value.split('\t'))
        for vertex2, node in enumerate(nodes):
            if node !='0' :
                if vertex1 > vertex2:
                    png.write(str(vertex1 + 1) + ' -- ' + str(vertex2 + 1) + '[label=' + str(node) + '];\n')

png.write('}')
png.close()
