from pprint import pprint

from Node import Node
from fuctions import tree

coding_list = []


def code(node, s):
    if (node.left is None) and (node.right is None):
        coding_list.append((node.value, s))
    else:
        code(node.left, s + '1')
        code(node.right, s + '0')


if __name__ == '__main__':

    # f = fileinput.input(files='index.png')

    # f = open('index.png', encoding='latin1')
    f = open('index.png', mode='rb')
    # a = f.read()
    x = []
    # print(a)
    # for i in a:
    #     hex_int = int()
    #     new_int = hex_int + 0x200
    #     print(hex(new_int)[2:])
    # print(' '.join(format(ord(x), 'b') for x in a))

    b = None

    while b != b'':
        b = f.read(1)
        if b is not None:
            x.append(b)
            print(b)
        else:
            break

    f.close()

    # print(f.encoding)
    # data="UTF-8 DATA"
    # udata=a.decode("utf-8").encode("ascii","ignore")
    # a=udata.encode("ascii","ignore")

    # b = binascii.a2b_base64(a)
    # print(a, b)

    distinct_list = list(set(x))
    # print(x)
    # print(distinct_list)
    counter_list = []

    for item in distinct_list:
        cnt = x.count(item)
        counter_list.append((cnt, item))

    # pprint([item for item in x if item == ''])
    # counter_list.sort()
    # counter_list.reverse()

    # pprint(counter_list)
    # print(x)
    # print(x.count('.'))

    # Create tree
    counterTree_list = []

    for v in counter_list:
        t = Node(v[0], v[1])
        counterTree_list.append(t)

    # counterTree_list.sort(key=operator.attrgetter('index'))
    counterTree_list.sort()

    # for i in counterTree_list:
    #     print(i.value, ' ', i.index)

    while counterTree_list.__len__() > 1:
        t = tree(counterTree_list.pop(1), counterTree_list.pop(0))
        counterTree_list.append(t)
        counterTree_list.sort()

    # print(counterTree_list)

    # create a list of codes
    code(counterTree_list[0], '')
    pprint(coding_list)

    coding_list = dict(coding_list)

    # print(coding_list['s'])
    text = ''
    # with open('spam.txt', encoding='latin1') as f:
    with open('a.png', mode='rb') as k:
        b = None

        while b != b'':
            b = k.read(1)
            if b == b'':
                break
            else:
                char_code = coding_list[b]
                # print(char_code, ' ', b)
                text += char_code


        print(text)

        # with open('spam.txt', mode='wb') as f:
        #     f.write(text)
