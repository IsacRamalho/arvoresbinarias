class Node: #cada nó terá duas ramificações
    def __init__(self, data): #metodo de inicialização que recebe um dado a ser armazenado
#
        self.data = data
        self.left = None #left e right porque as arvores binárias possuem sempre dois filhos para nós
        self.right = None

    def __str__(self):
        return str(self.data) #converte o dado recebido em string

#Abaixo, se um valor for passado no parâmetro data, um novo nó é criado usando a classe Node e é definido como a raiz da árvore (self.root).
class BinaryTree: #a ideia é que a árvore contém nós, que são um dos atributos da árvore, e os nós provém da classe Node
    def __init__(self, data=None): #data faz com que o usuário possa inserir um elemento como a raiz da árvore #none representa o vazio, vai ser um valor padrão usado para dizer que o método por ser chamado sem nenhum dado
        if data: #se o dado existir...
            node = Node(data) #cria-se um nó a partir do dado recebido na classe Node
            self.root = node #define-se um nó como a raiz
        else: #se o dado não existir
            self.root = None
    def simetric_traversal(self, node=None): #é uma operação para percorrer a árvore - percurso em ordem simétrica
        if node is None:
            node = self.root #diz para percorrer a partir da raiz
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node, end='') # esse print exibe quem está no meio #o end faz com que tudo apareça na mesma linha
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')
'''aqui acima, ele printa o filho à esquerda, depois a si mesmo (meio) e depois à direita;
porém, se o nó à direita possui um filho à esquerda, antes mesmo dele ser impresso, o método simetric
será chamado recursivamente para visitar primeiro esse filho à esquerda. MAIS DETALHES: confrir'''


'''if __name__ == "__main__": #TESTE
    tree = BinaryTree(7) #o nó que contém o 7 é a raiz da árvore
    tree.root.left = Node(18) #nó que fica à esquerda de tree, que é a raiz
    tree.root.right = Node(14)

    print(tree.root) #print do nó "tree"
    print(tree.root.left)
    print(tree.root.right)''' #as linhas 30 a 37 são de outro exemplo, mais básico

#nesse caso, estamos definindo os valores para os nós, construindo a árvore manualmente, o que na prática real depois será visto que não precisa

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
#definindo onde cada nó se posiciona na árvore
    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2

    tree.simetric_traversal()
    print('\n')

'''Certamente, vou detalhar a lógica do código passo a passo, especialmente a impressão de cada nó.

Classe Node:
O método __init__(self, data) é o construtor da classe Node, que recebe um parâmetro data contendo o valor a ser armazenado no nó.
Dentro do construtor, três atributos são inicializados:
self.data: armazena o valor recebido no parâmetro data.
self.left: inicializado como None, representa o nó filho à esquerda.
self.right: inicializado como None, representa o nó filho à direita.
O método __str__(self) retorna uma string contendo o valor armazenado no nó.
Classe BinaryTree:
O método __init__(self, data=None) é o construtor da classe BinaryTree.
Se um valor for passado no parâmetro data, um novo nó é criado usando a classe Node e é definido como a raiz da árvore (self.root).
Caso contrário, self.root é inicializado como None, indicando que a árvore está vazia.
Método simetric_traversal(self, node=None):
Esse método implementa o percurso em ordem simétrica (ou in-order) da árvore binária.
Primeiro, verifica-se se o parâmetro node é None. Caso seja, o valor de self.root é atribuído a node, indicando que o percurso deve começar a partir da raiz da árvore.
Em seguida, verifica-se se o nó à esquerda (node.left) existe. Se existir, é impresso um parêntese de abertura ( e então é chamado recursivamente o método simetric_traversal passando o nó à esquerda como argumento.
Após a recursão à esquerda, o valor do nó atual (node) é impresso.
Então, verifica-se se o nó à direita (node.right) existe. Se existir, o método simetric_traversal é chamado recursivamente passando o nó à direita como argumento, e após a recursão, é impresso um parêntese de fechamento ).
Essa sequência de impressões (esquerda, nó, direita) representa o percurso em ordem simétrica da árvore binária.
No exemplo fornecido, o código cria manualmente uma árvore binária com a seguinte estrutura:

Copiar
    +
   / \
  a   *
     / \
    b   -
       / \
      /   \
     /     \
    c       d
           /
          e
Ao chamar o método simetric_traversal(), a saída será:

Copiar
(a+(b*(c/d)-(e)))
Essa saída corresponde ao percurso em ordem simétrica da árvore binária, imprimindo os nós na seguinte ordem: esquerda, nó atual, direita.

por que e como o "*" é impresso depois de "b"?

Imagem do bot para Assistant
Assistant

Poe
Boa pergunta! Vamos entender melhor o porquê e como o "*" é impresso depois de "b" no percurso em ordem simétrica.

Lembre-se da estrutura da árvore binária:

Copiar
    +
   / \
  a   *
     / \
    b   -
       / \
      /   \
     /     \
    c       d
           /
          e
No percurso em ordem simétrica, a ordem de impressão dos nós é: esquerda, nó atual, direita.

Vamos acompanhar o passo a passo da execução do método simetric_traversal():

O método é chamado com tree.root, que é o nó +.
Como +.left (nó a) existe, o método é chamado recursivamente com +.left. Então, a é impresso.
Depois, o nó atual + é impresso.
Então, o método verifica +.right, que é o nó *.
Como *.left (nó b) existe, o método é chamado recursivamente com *.left. Então, b é impresso.
Agora, o nó atual * é impresso.
Em seguida, o método verifica *.right, que é o nó -.
Como -.left (nó /) existe, o método é chamado recursivamente com -.left. Então, / é impresso.
O nó atual - é impresso.
Finalmente, o método verifica -.right (nó d), que existe. O método é chamado recursivamente com -.right. Então, d é impresso.
Portanto, a impressão do "" após "b" ocorre porque o nó "" é o nó atual após a recursão do nó "b" à esquerda. Essa é a lógica do percurso em ordem simétrica, imprimindo os nós na ordem: esquerda, nó atual, direita.

Como *.left (nó b) existe, o método é chamado recursivamente com *.left. Então, b é impresso. Isso ocorre por conta do mecanismo do simetric_traversal?

Imagem do bot para Assistant
Assistant

Poe
Sim, isso ocorre devido ao mecanismo do método simetric_traversal().

Vamos relembrar os passos da execução:

O método é chamado com tree.root, que é o nó +.
Como +.left (nó a) existe, o método é chamado recursivamente com +.left. Então, a é impresso.
Depois, o nó atual + é impresso.
Então, o método verifica +.right, que é o nó *.
Como *.left (nó b) existe, o método é chamado recursivamente com *.left. Então, b é impresso.
Essa chamada recursiva com *.left é a chave para a impressão do nó b no percurso em ordem simétrica.

A lógica do percurso em ordem simétrica é:

Visitar o nó à esquerda (recursivamente)
Visitar o nó atual
Visitar o nó à direita (recursivamente)
Portanto, quando o método chega no nó *, ele segue essa lógica: primeiro visita o nó à esquerda (b), depois visita o nó atual (*) e então visita o nó à direita (se houver).

Então, sim, a impressão de b após o nó * ocorre por conta desse mecanismo do método simetric_traversal() seguir a ordem simétrica de visita dos nós.

o que quer dizer recursivamente?

Imagem do bot para Assistant
Assistant

Poe
Ótima pergunta! O termo "recursivamente" se refere a uma técnica de programação onde uma função (ou método) chama a si mesma para resolver um problema.

Na árvore binária, a implementação do percurso em ordem simétrica utiliza a recursão para visitar os nós da árvore. Vamos entender melhor como isso funciona:

Quando o método simetric_traversal() é chamado, ele verifica se o nó atual possui um filho à esquerda. Se sim, ele chama o próprio método simetric_traversal(), mas dessa vez passando o filho esquerdo como argumento.

Isso faz com que o método seja chamado recursivamente, ou seja, a função chama a si mesma para processar o filho esquerdo. Esse processo se repete até que não haja mais filhos à esquerda.

Então, após visitar todos os nós à esquerda de forma recursiva, o método imprime o nó atual. Em seguida, ele verifica se há um filho à direita e, se houver, chama recursivamente o método simetric_traversal() passando o filho direito.

Essa chamada recursiva permite que o método visite todos os nós da árvore binária na ordem simétrica (esquerda, nó atual, direita).

Então, quando dizemos que o método é chamado "recursivamente", significa que ele chama a si mesmo para resolver uma parte do problema (visitar um subconjunto de nós da árvore), até que todo o problema (toda a árvore) seja resolvido.

Espero que essa explicação tenha ajudado a entender melhor o conceito de recursão no contexto da implementação do percurso em ordem simétrica em árvores binárias. Deixe-me saber se você tiver mais alguma dúvida!

Então quando o código passa para "if node.right:", mesmo antes de imprimir o elemento à direta, se esse elemento possui um filho à esquerda, o codigo o chama?!

Imagem do bot para Assistant
Assistant

Poe

Exatamente isso! Você entendeu perfeitamente o funcionamento da recursão no percurso em ordem simétrica.

Quando o método simetric_traversal() chega no nó atual e verifica se há um filho à direita (node.right), ele segue a mesma lógica que seguiu para o filho à esquerda:

Se o filho à direita existir, o método é chamado recursivamente, passando esse filho à direita como argumento.
Isso faz com que o método "desça" pela árvore, visitando primeiro todos os nós à esquerda desse filho à direita, antes de imprimir o próprio filho à direita.
Só depois de visitar todos os nós à esquerda do filho à direita, o método imprime o filho à direita.
E então, continua percorrendo a árvore, visitando os nós à direita desse filho.
Então, você está completamente certo. Mesmo antes de imprimir o elemento à direita, se esse elemento possuir um filho à esquerda, o método será chamado recursivamente para visitar primeiro esse filho à esquerda, seguindo a lógica do percurso em ordem simétrica (esquerda, nó atual, direita).

Essa chamada recursiva é a essência da implementação do percurso em ordem simétrica, permitindo que o método visite todos os nós da árvore na ordem correta.'''
