
<body>
	<h1>Projeto c137 Prompt-to-Shell</h1>
	<p>Este é um projeto que usa a API da c137 para gerar comandos shell a partir de prompts em linguagem natural.</p>
	<h2>Chave de API</h2>
	<p>Antes de começar a usar o shell_helper, você precisa ter uma chave API, gerada no site da c137".</p>
	<p>Ao executar o arquivo pela primeira vez, ele pedirá a chave da API. Após fornecê-la, na próxima vez que for usá-lo, não será mais necessário informá-la. </p>
	<h2>Como usar</h2>
<h2>Executando o shell_helper sem precisar especificar o caminho completo</h2>
<p>É possível executar um arquivo Python apenas digitando o nome do arquivo, sem precisar especificar o caminho completo. Para fazer isso, é necessário adicionar o diretório onde o arquivo Python está localizado ao PATH do sistema. O PATH é uma variável de ambiente que contém uma lista de diretórios onde o sistema procura por programas executáveis.</p>
<p>Pelo terminal vá até o diretório onde esta o shell_helper.py e utilize o comando  <code>pwd</code> para saber o caminho até o diretório onde o arquivo shell_assistant está localizado.</p>
<p>Para adicionar um diretório ao PATH no Linux ou macOS, abra o arquivo <code>~/.bashrc</code> ou <code>~/.bash_profile</code> (dependendo da distribuição) e adicione a seguinte linha ao final do arquivo:</p>
<pre><code>export PATH=$PATH:/caminho/para/o/diretório</code></pre>
<p>Substitua <code>/caminho/para/o/diretório</code> pelo caminho para o diretório onde o arquivo shell_assistant está localizado. Salve o arquivo e feche-o.</p>
<p>Estando no mesmo diretório do shell_assistant.py ative no terminal a permissão de execução  <code>chmod +x shell_helper.py</code> </p>
<p>No Windows, o diretório pode ser adicionado ao PATH usando o Painel de Controle. Siga estas etapas:</p>
<ol>
  <li>Abra o Painel de Controle e clique em "Sistema e Segurança".</li>
  <li>Clique em "Sistema".</li>
  <li>Clique em "Configurações avançadas do sistema".</li>
  <li>Clique em "Variáveis de ambiente".</li>
  <li>Na seção "Variáveis do sistema", selecione a variável "PATH" e clique em "Editar".</li>
  <li>Na janela "Editar variável de ambiente", clique em "Novo" e adicione o caminho para o diretório onde o arquivo Python está localizado.</li>
  <li>Clique em "OK" em todas as janelas para salvar as alterações.</li>
</ol>
<p>Após adicionar o diretório ao PATH e seguir os outros passos, o arquivo shell_helper.py pode ser executado apenas digitando o nome do arquivo no terminal, em qualquer diretório que você esteja.</p>
<h2>Utilização</h2>
<p>Para utilizar a aplicação, após seguir os passos anteriores, basta digitar no terminal o <code>shell_helper.py</code> e em seguida digitar um prompt em linguagem natural quando solicitado. A aplicação irá gerar um comando shell correspondente ao prompt inserido e lhe perguntará  se deseja executar o comando na sua máquina ou obter uma descrição detalhada do que o comando faz.</p>



<h2>Requisitos</h2>
<p>Para rodar a aplicação, é necessário ter a key do c137 Para consegui-la, basta acessar a documentação e seguir a orientação em: <a> https://docs.c137.belini.shop/get-started/get-a-key</a> </p>
</body>
</html>
