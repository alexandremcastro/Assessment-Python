# [Assessment] Lógica de programação com Python

### Faça um programa que leia um arquivo texto de contas corrente (contas.txt) de pessoas físicas (PF). As contas devem ser armazenadas em uma lista na memória principal. A conta da PF tem como informações: o número da conta (inteiro maior que zero), nome do correntista (string) e saldo (real).

O programa deve exibir um menu com as seguintes opções: inclusão de conta, alteração de saldo, exclusão de conta, relatórios gerenciais e saída do programa. Ao término, o programa deverá gravar os dados atualizados da lista no mesmo arquivo em disco.

- No caso de inclusão, o programa deverá evitar que seja criada uma conta com um número que já exista, caso contrário deverá enviar uma mensagem de erro. Além disso, o nome deve ter, pelo menos, dois nomes e o saldo inicial um valor maior ou igual a zero;
- Nos casos de alteração e exclusão, o programa deverá garantir que a conta exista, caso contrário deverá enviar uma mensagem de erro. 
- No caso específico da exclusão, o saldo da conta corrente deverá ser igual a zero, caso contrário deverá enviar uma mensagem de erro.
- No caso específico da alteração, apenas o saldo poderá ser alterado, podendo ser um crédito ou um débito, sempre numérico e maior que zero. 
- No caso da opção de relatórios gerenciais, serão oferecidas as seguintes opções: listar clientes com saldo negativo, listar os clientes que têm saldo acima de um determinado valor e listar todas as contas.
- Nos casos de exclusão, alteração e consulta, o programa deverá verificar se a lista de contas está vazia e exibir uma mensagem para o usuário.

O programa deve implementar variáveis locais, passagem de parâmetros, tratador de exceção (try/except), lista, funções e todas as boas práticas apresentadas durante o curso como, por exemplo, evitar funções que realizam mais de uma operação.

O programa deverá ser apresentado pessoalmente para o professor antes de ser enviado no Moodle. Caso contrário, o trabalho não será avaliado e o aluno reprovado.

**Dicas:**

*Utilize funções para cada operação (incluir, alterar, excluir e consultar);*
*Utilize funções para os menus, pesquisa de conta, entrada de dados e leitura e gravação do arquivo;*
*Faça a validação dos dados utilizando funções para número da conta, nome e saldo;*
*Leia o arquivo no início do programa, antes do loop principal, armazene em uma lista e depois grava a lista em arquivo no final do programa.*
