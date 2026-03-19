# Teste de perfil
## Programa para computar respostas de um teste comportamental
O arquivo "teste_de_perfil_comportamental.py" computa as respostas dadas a uma avaliação comportamental com perfis pré-definidos.

## Objetivo
A avaliação original, disponível no arquivo "avaliação_de_perfil.pdf" visa entender o comportamento dos respondentes, por meio de perguntas que simulam situações reais de trabalhos em grupo.

Para respodê-la alguns colegas registraram suas opções escolhidas em arquivos de texto e enviaram ao avaliador, Rafael, pelo WhatsApp. As mensagens tinham diferentes formatos, todas com uma resposta por linha, porém algumas com mais de uma opção escolhida por resposta, além de diferentes caracteres separadores, como "/", "e", ou ")".

O programa, então, procura facilitar a computação das respostas, lendo as opções escolhidas pelos respondentes (que podem ser simplesmente copiadas das mensagens de WhatsApp e coladas ao terminal) e atribuindo-lhes notas sobre os seus perfis comportamentais.

Visto que os respondentes já haviam registrado as suas escolhas, o objetivo do programa não era fazer um "quiz", mas apenas ler e calcular os perfis disponíveis. O relatório final pode ser encontrado no arquivo "relatorio_perfis.txt" .

## Funcionalidades
O Menu conta com as seguintes opções:
- Teste: dá acesso à avaliação, permitindo que diferentes respondentes possam ser registrados.
- Visualização Geral: mostra todas as respostas de diferentes respondentes.
- Salvamento: gera um arquivo txt com o relatório geral das respostas.
- Exclusão: permite excluir registros de acordo com o nome dos respondentes.
- Finalização: finaliza a execução do programa.

## Observações
- Nessa situação específica, optei por receber apenas as respostas como entrada, devido ao cenário particular em que a avaliação se enconta, mas pretendo, futuramente, implementar a funcionalidade "Quiz", que facilitaria outras avaliações.
- O programa é bastante simples, e calcula apenas a incidência de determinadas respostas sobre o total de opções computadas. Com o tempo pretendo melhorar o código, dificultando a sua quebra.
- Importante ressaltar que o programa comete um erro GRAVÍSSIMO de estatística, fazendo com que as freqências relativas nem sempre resultem em 100% (hehe~~). Mas o importante é que dá pra ter uma ideia do perfil de cada respondente e já ajuda, de certa forma~~ (vou tentar ajeitar isso, desculpa TwT)

