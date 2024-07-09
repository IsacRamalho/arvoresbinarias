from arvorebinaria import BinaryTree, Node

#expressão matemática a ser representada em árvore

#            '+'
#           /   \
#          a     '*'
#               /   \
#              b    '-'
#                  /   \
#                '/'    e
#               /   \
#              c     d

#nesse caso, de baixo para cima, c é divido por d;
#depois, o resultado é subtraído por "e", e assim por diante.
# (a + (b * ((c/d) - e)))

if __name__ == "__main__":
    tree = BinaryTree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')
    n9 = Node('e')

    n6.left = n7
    n6.right = n8

