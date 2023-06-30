<body>
  <h2>Versão 1: Sistema bancário simples:</h2>

  <p>A ideia é bem simples. Quando você executa o programa, ele mostra algumas opções para você escolher: depositar, sacar, ver o extrato ou sair.</p>

  <p>Se você escolher a opção de depósito, pode digitar o valor que deseja depositar. O programa adiciona esse valor ao seu saldo e registra a transação no histórico.</p>

  <p>Se preferir sacar dinheiro, é só escolher essa opção e digitar o valor desejado. Mas existem algumas regras: você só pode fazer até 3 saques por dia, e cada saque não pode ser maior que R$500. Além disso, a soma total dos saques do dia não pode ultrapassar R$1500. Se você atingir esses limites ou não tiver saldo suficiente, o programa avisa e não permite o saque.</p>

  <p>Por fim, se você quiser ver o extrato da sua conta, é só escolher essa opção. O programa mostra o saldo atual e exibe o histórico de todas as transações que você fez.</p>

  <p>Ah, e se você quiser sair do programa, basta escolher a opção de sair. Assim, ele é encerrado.</p>
</body>


<body>
  <h2>Versão 2: Adicionando funcionalidades ao sistema bancário:</h2>

  <p>Este é um código em Python que implementa um programa simples de banco, permitindo a realização de depósitos, saques, criação de contas e usuários, além de exibir extratos e listar as contas existentes.</p>

  <h3>Funcionalidades</h3>

  <ul>
    <li>Depósito: Permite realizar um depósito na conta, adicionando o valor especificado ao saldo.</li>
    <li>Saque: Permite realizar um saque da conta, subtraindo o valor especificado do saldo, desde que respeite as regras de limite diário de saques e saldo disponível.</li>
    <li>Extrato: Exibe as informações do extrato da conta, mostrando a quantidade de saques realizados, o total de saques efetuados e o saldo atual.</li>
    <li>Nova conta: Cria uma nova conta associada a um usuário existente, utilizando o CPF como identificador.</li>
    <li>Listar contas: Exibe a lista de contas cadastradas, mostrando o número da conta e o nome do titular.</li>
    <li>Novo usuário: Cria um novo usuário, solicitando informações como CPF, nome completo, data de nascimento e endereço.</li>
    <li>Sair: Encerra o programa.</li>
  </ul>

  <h3>Como utilizar</h3>

  <p>Execute o código em um ambiente Python. O programa exibirá um menu com opções numeradas. Escolha a opção desejada digitando o número correspondente e pressione Enter. Siga as instruções e forneça as informações solicitadas pelo programa. O programa executará a ação escolhida e exibirá o resultado. Repita o processo até escolher a opção de sair.</p>

  <p><strong>Observação:</strong> Certifique-se de ter a biblioteca Python instalada corretamente antes de executar o código.</p>

  <h3>Requisitos</h3>

  <p>Python 3.x</p>

  <h3>Notas</h3>

  <p>Este código é uma implementação simplificada de um sistema bancário e não deve ser utilizado para fins comerciais ou de produção sem uma análise mais aprofundada e aprimoramentos adicionais. É fornecido apenas para fins educacionais e demonstrativos.</p>
</body>
