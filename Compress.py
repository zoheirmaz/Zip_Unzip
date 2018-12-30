from pprint import pprint

from Node import Node
from fuctions import tree, terav, write_binary

coding_list = []


def code(node, s):
    if (node.left is None) and (node.right is None):
        coding_list.append((node.value, s))
    else:
        code(node.left, s + '1')
        code(node.right, s + '0')


if __name__ == '__main__':

    # f = open('index.png', encoding='latin1')
    f = open('files/index.png', mode='rb')
    # a = f.read()

    x = []

    b = None

    while b != b'':
        b = f.read(1)
        if b != b'':
            x.append(b)
            print(b)
        else:
            break

    f.close()

    distinct_list = list(set(x))
    # print(x)
    # print(distinct_list)

    counter_list = []

    for item in distinct_list:
        cnt = x.count(item)
        counter_list.append((cnt, item))

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

    pprint(coding_list)

    tex = ''
    for i in x:
        tex += coding_list[i]

    # print(coding_list['s'])
    text = ''
    # y=None

    nnn = terav(counterTree_list[0])

    # with open('spam.txt', encoding='latin1') as f:
    with open('files/a.png', mode='wb') as k:
        # bits = "10111111111111111011110"
        bits = nnn[0]
        # bits = ''

        print(bits.__len__())

        write_binary(bits, k)

        # k.write(int(bits[::-1], 2).to_bytes(4, 'little'))
        # k.write(0)
        # b = None
        #
        # while b != b'':
        #     b = k.read(1)
        #     if b == b'':
        #         break
        #     else:
        #         char_code = coding_list[b]
        #         # print(char_code, ' ', b)
        #         text += char_code
        #         # y=b
        # for i in coding_list:
        #     k.write(i)
        # print(type(y))

        # with open('spam.txt', mode='wb') as f:
        #     f.write(text)
        k.close()





        # with open('files/a.png', mode='wb') as k:
        #     # b = None
        #     #
        #     # while b != b'':
        #     #     b = k.read(1)
        #     #     if b == b'':
        #     #         break
        #     #     else:
        #     #         char_code = coding_list[b]
        #     #         # print(char_code, ' ', b)
        #     #         text += char_code
        #     #         # y=b
        #     for i in coding_list:
        #         k.write(i)
        #     # print(type(y))
        #
        #     # with open('spam.txt', mode='wb') as f:
        #     #     f.write(text)
        #     k.close()
