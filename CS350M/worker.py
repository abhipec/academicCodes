import time
import socket
def worker(tree, name, data):
    
    # This condition will be satisfied for root node only
    if not tree.getParent(name):
        print("This is root", name)
        # create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind socket port to its name after converting to integer
        s.bind(('', int(name)))
        # get its children
        children = tree.getChildren(name)
        # limit maximun number of clent connection based on number of children
        s.listen(len(children))
        # start listining
        objects = {}
        for child in children:
            objects[child], _ = s.accept()
        # wait for date received from children
        array = {}
        for i in range(len(children)):
            array[str(i)] = objects[children[i]].recv(10000)
        # concatenate result send by all children
        result = []
        for d in array.values():
            result = result + [int(x) for x in d.split(',')]
        # write result to file after sorting
        f = open('output.txt','w')
        for i in sorted(result):
            f.write(str(i) + '\n')
        f.close()
        # close all conections
        for child in children:
            objects[child].close()

    # This condition will be satisfied for leaf node only
    elif not tree.getChildren(name):
        print("This is leaf", name, "its parent is", tree.getParent(name))
        # small delay so that all intermediate nodes start listining
        time.sleep(0.1)
        # initialize socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect to its parent
        s.connect(('', int(tree.getParent(name))))
        # sort data and send it to parent
        data = ','.join(str(x) for x in sorted(data))
        s.sendall(data)
        # close connection
        s.close()

    # This condition will be run on all other nodes that are not root or leaf node
    else :
        print("This is intermideate", name, "its parent is", tree.getParent(name))
        # create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind socket port to its name after converting to integer
        s.bind(('', int(name)))
        # get its children
        children = tree.getChildren(name)
        # limit maximun number of clent connection based on number of children
        s.listen(len(children))
        # start listining
        objects = {}
        for child in children:
            objects[child], _ = s.accept()
        # wait for data received from children
        array = {}
        for i in range(len(children)):
            array[str(i)] = objects[children[i]].recv(10000)
        # concatenate result send by all children
        result = []
        for d in array.values():
            result = result + [int(x) for x in d.split(',')]
        # close the connection
        for child in children:
            objects[child].close()

        # create new socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect to parent node
        s.connect(('', int(tree.getParent(name))))
        # send the sorted data to parent
        data = ','.join(str(x) for x in sorted(result))
        s.sendall(data)
        # close connection
        s.close()
