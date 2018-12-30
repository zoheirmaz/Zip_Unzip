from binarytree import tree, Node
from bitstring import BitArray


te = ''
lst = None




def reverse(string):
    string = string[::-1]
    return string


def terav(no):
    global te
    if no is None:
        te += '-1 '
        return te
    te += str(no.value) + ' '
    terav(no.left)
    terav(no.right)
    return te


def getList(ls):
    text = ''
    cursor = ''
    if ls.__len__() != 0:
        cursor = ls.pop()
        # text += cursor

    while (cursor != ' ') and (ls.__len__() != 0):
        text += cursor
        cursor = ls.pop()

    if text == '':
        # print('None')
        return None
    else:
        # print(text)
        return int(text)


def cre():
    x = getList(lst)
    if x == -1:
        return None
    node = Node(x)
    node.left = cre()
    node.right = cre()
    return node

def get4(inp):
    inp, result = inp[:-4], inp[-4:]
    return inp,result

if __name__ == '__main__':
    # node1 = tree(4)
    #
    # print(node1)
    # lst = terav(node1)
    # print(lst)
    # s = ''
    # lst = list(lst)
    # lst.reverse()
    #
    # print(cre())
    print(get4('0123456789'))

