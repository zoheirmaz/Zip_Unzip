from Node import Node

te = ''
le = []


def tree(node2, node1):
    node = Node(node1.index + node2.index)
    if node1 < node2:
        node.left = node1
        node.right = node2
    else:
        node.left = node2
        node.right = node1
    return node


def read():
    None


def write():
    None


def write_binary(inp, file):
    ls = []
    while inp != '':
        if (len(inp) // 4 == 0) and (len(inp) % 4 != 0):
            result = ''
            for i in range(4 - (len(inp) % 4)):
                result += '0'
            result += inp
            inp = ''
        else:
            inp, result = inp[:-4], inp[-4:]
        temp = int(result[::-1], 2).to_bytes(4, 'big')
        ls.append(temp)
    ls.reverse()
    for byte in ls:
        file.write(byte)


def terav(no):
    global te
    global le
    if no is None:
        te += '0'
        return te
    else:
        te += '1'
        if no.value is not None:
            le.append(no.value)
        terav(no.left)
        terav(no.right)
        return te, le
