



# Assets_NOC

Módulo para recuperação de assets do Rocketbot NOC.

*Read this in other languages: [English](Manual_assets_noc.md), [Português](Manual_assets_noc.pr.md), [Español](Manual_assets_noc.es.md)*

![banner](imgs/Banner_assets_noc.png)
## Como instalar este módulo

Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.


## Descrição do comando

### Login NOC

Faça login no NOC usando credenciais como e-mail e senha, chave de API e arquivo noc.ini.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL Servidor|URL do servidor para se conectar|https://roc.myrb.io/|
|Selecione um método para se conectar ao orquestrador|Opções para fazer login no R.O.C, você pode usar credenciais de usuário, chave de API ou selecionar o arquivo noc.ini||
|Ignorar SSL|Marque se deseja ignorar a verificação do certificado SSL||
|Atribuir resultado à variável|Variável onde será armazenado o estado da conexão, retorna True se for bem sucedida ou False caso contrário|Variable|

### Obter Asset específico

Obtém o ativo específico indicado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do Asset|Nome do asset a ser obtido|Teste|
|Token do processo|Token do processo|27FEXKIXFRFDUNVD|
|Key de Instância|Key de instância do processo|6241c3a1dd96f8f92f|
|Obter dados extras|Marque para obter dados extras dos Assets|True|
|Atribuir resultado a variável|Variável onde o resultado será salvo. Nome da variável sem chaves|Variável|

### Obter todos os Assets

Obtém todos os Assets e os atribui a variável correspondente
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribua resultado à Variável|Variável onde o resultado será salvo. Nome da variável sem chaves|Variável|
|Obter dados extras|Marque para obter dados extras dos Assets|True|

### Adicionar Asset

Adiciona um Asset ao seu Orquestrador
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do Asset|Nome do Asset a ser adicionado|NovoAsset|
|Token do processo|Token do processo ao qual o Asset será modificado|27FEXKIXFRFDUNVD|
|Key de Instância|Key da instância ao qual o Asset será adicionado|6241c3a1dd96f8f92f|
|Mails dos usuários|Lista de mails dos usuários aos quais o Asset será adicionado|[MailUsuario1, MailUsuario2, ...]|
|Tipo do Asset|Tipo do Asset a ser adicionado|Geral|
|Valor do Asset|Valor do Asset a ser adicionado|Um valor|
|Atribuir resultado a variável|Variável onde o resultado será salvo. Nome da variável sem chaves|Variável|

### Modifica o ativo específico

Modifica o ativo específico indicado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Id do Asset|Id do Asset a ser modificado|Id_Asset|
|Nome do Asset|Novo nome do Asset|NovoAsset|
|Token do processo|Token do processo ao qual o Asset será modificado|27FEXKIXFRFDUNVD|
|Key da instância|Key da instância ao qual o Asset será modificado|6241c3a1dd96f8f92f|
|Mails dos usuários|Lista de Mails dos usuários que terão o Asset|[MailUsuario1, MailUsuario2, ...]|
|Tipo do Asset|Tipo do Asset a ser modificado|Geral|
|Valor do Asset|Valor do Asset a ser modificado|Um valor|
|Atribuir resultado a variável|Variável onde o resultado será salvo. Nome da variável sem chaves|Variável|
