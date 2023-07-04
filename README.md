# Descrição do Projeto

O escopo deste projeto é elaborar um sistema de chat utilizando o framework Django, escrito em Python, utilizando o protocolo de WebSocket.

## WebSocket

**WebSocket** é um protocolo de comunicação bidirecional baseado em TCP que permite a troca de mensagens entre um cliente e um servidor de forma contínua e em tempo real. Diferentemente do protocolo HTTP, que é baseado em requisições e respostas, o WebSocket estabelece uma conexão persistente e permite a comunicação em tempo real entre o cliente e o servidor.

O protocolo WebSocket foi desenvolvido para superar as limitações do HTTP, que é orientado a requisições e respostas - unidirecional. Com o WebSocket, uma vez estabelecida a conexão, o cliente e o servidor podem trocar mensagens instantaneamente, sem a necessidade de uma nova requisição a cada interação, se tornando bidirecional.

O WebSocket é amplamente utilizado em aplicações web que exigem atualizações em tempo real, como bate-papo em tempo real, notificações em tempo real, jogos multiplayer, colaboração em tempo real e streaming de dados. Ele oferece uma alternativa eficiente e escalável para técnicas anteriores, como polling ou long polling, que exigiam a realização repetida de requisições ao servidor para obter atualizações.

Ao estabelecer uma conexão WebSocket, o cliente e o servidor podem enviar mensagens em formato binário ou texto, permitindo a comunicação flexível e personalizada. O protocolo WebSocket também suporta recursos de segurança, como criptografia por SSL/TLS para proteger a comunicação entre cliente e servidor.

Em resumo, o WebSocket é um protocolo que permite a comunicação em tempo real entre um cliente e um servidor, facilitando a criação de aplicações web interativas e dinâmicas.

## ASGI vs WSGI

**ASGI** (Asynchronous Server Gateway Interface) e **WSGI** (Web Server Gateway Interface) são duas especificações para interfaces de aplicativos web em **Python**. Embora ambos sejam usados para conectar aplicativos web Python a servidores web, existem algumas diferenças significativas entre eles.

Paradigma de programação:

WSGI: O WSGI segue um modelo de programação síncrono, o que significa que cada solicitação é tratada sequencialmente. O servidor aguarda a resposta antes de processar a próxima solicitação.
ASGI: O ASGI adota um modelo de programação assíncrono, onde as solicitações são tratadas de forma não bloqueante. O servidor pode lidar com várias solicitações simultaneamente, sem precisar esperar por uma resposta antes de continuar.
Capacidade de processamento assíncrono:

WSGI: O WSGI não suporta diretamente operações assíncronas. Se um aplicativo WSGI precisar realizar operações assíncronas, ele deve usar bibliotecas externas ou técnicas de programação específicas para lidar com isso.
ASGI: O ASGI foi projetado especificamente para lidar com operações assíncronas. Ele suporta nativamente operações assíncronas e pode se comunicar com outros servidores assíncronos, como servidores de mensagens ou bancos de dados assíncronos.
Ecossistema e compatibilidade:

WSGI: O WSGI é uma especificação mais antiga e amplamente adotada na comunidade Python. A maioria dos frameworks e servidores web Python existentes foi projetada para trabalhar com o WSGI.
ASGI: O ASGI é uma especificação relativamente nova e está ganhando popularidade gradualmente. Embora existam frameworks e servidores web que suportem ASGI, o ecossistema em torno do WSGI é mais maduro e possui mais opções disponíveis.
Recursos avançados:

ASGI: Devido à natureza assíncrona do ASGI, ele permite recursos avançados, como streaming de resposta em tempo real, comunicação bidirecional (usando WebSockets) e suporte a eventos assíncronos.
WSGI: O WSGI é mais limitado em termos de recursos avançados. Embora seja possível implementar alguns desses recursos em um aplicativo WSGI, eles requerem soluções personalizadas e podem não ser tão eficientes quanto no ASGI.
Em resumo, o WSGI é uma especificação mais antiga e amplamente adotada, adequada para a maioria dos aplicativos web Python convencionais. O ASGI, por outro lado, é uma especificação mais moderna e flexível, mais adequada para aplicativos que requerem recursos assíncronos avançados ou comunicação em tempo real.

## Channels

O Channels é uma biblioteca do Django que adiciona suporte para comunicação assíncrona, como WebSockets, no framework. O Channels é baseado no protocolo ASGI (Asynchronous Server Gateway Interface) e permite que você crie aplicativos em tempo real e assíncronos com o Django.

O Channels possui várias camadas que trabalham juntas para fornecer funcionalidades avançadas. Aqui estão as principais camadas do Channels:

1. Protocolo ASGI (ASGI Protocol): A camada de protocolo ASGI é a base do Channels. O ASGI define como os servidores, aplicativos e frameworks interagem entre si. Ele fornece uma interface entre os servidores web e os aplicativos, permitindo que as solicitações sejam tratadas de forma assíncrona e facilitando a comunicação bidirecional.

2. Servidor (Server): A camada do servidor é responsável por receber e enviar solicitações usando o protocolo ASGI. O servidor ASGI pode ser um servidor web compatível com ASGI, como o **Daphne**, ou um servidor WSGI com suporte a ASGI. O servidor é responsável por rotear as solicitações para os manipuladores apropriados.

3. Roteador (Router): A camada do roteador é responsável por direcionar as solicitações recebidas pelo servidor para os canais apropriados. O roteador examina as informações da solicitação, como o caminho do URL, para determinar qual canal deve lidar com a solicitação.

4. Canal (Channel): Os canais são a principal abstração fornecida pelo Channels. Um canal representa uma conexão bidirecional entre o servidor e o cliente. Os canais podem ser usados para várias finalidades, como lidar com solicitações HTTP tradicionais, comunicação em tempo real por WebSockets, notificações push, processamento de tarefas assíncronas e muito mais. Cada canal tem um identificador único e pode ser usado para enviar e receber mensagens assíncronas.

5. Consumidor (Consumer): Um consumidor é uma função ou classe que processa mensagens em um canal específico. Ele recebe as mensagens recebidas em um canal e executa a lógica necessária para processar essas mensagens. Os consumidores são responsáveis por determinar como as mensagens são manipuladas e quais ações devem ser executadas em resposta a elas.

6. Message Layer Backend: A camada de mensagens é responsável por armazenar e enviar mensagens entre os consumidores e os canais. O Channels oferece suporte a vários backends de camada de mensagens, como Redis, database e outros, para lidar com a persistência e a entrega de mensagens.

Essas são as principais camadas do Channels. Juntas, elas permitem que você crie aplicativos Django assíncronos e em tempo real, aproveitando recursos como WebSockets, notificações push e comunicação assíncrona.

### Message Layer Backend

O Message Layer Backend é uma parte essencial do Channels que lida com o armazenamento e envio de mensagens entre os consumidores e os canais. Quando uma mensagem é recebida em um canal, ela é encaminhada para o Message Layer Backend para que seja armazenada e entregue ao consumidor apropriado.

O Channels suporta diferentes backends de camada de mensagens, dependendo dos requisitos do seu aplicativo. Alguns exemplos de backends de camada de mensagens comumente usados incluem Redis, database (banco de dados), memória e outros.

Cada backend tem sua própria implementação específica para armazenar e enviar mensagens assíncronas. Por exemplo, se você estiver usando o Redis como Message Layer Backend, as mensagens podem ser armazenadas em filas específicas do Redis e os consumidores podem consultar essas filas para processar as mensagens pendentes. Outros backends podem usar abordagens diferentes para armazenar e entregar mensagens.

O uso de um Message Layer Backend fornece várias vantagens. Ele permite que as mensagens sejam armazenadas de forma segura e persistente até que sejam processadas pelos consumidores. Além disso, o Message Layer Backend pode fornecer recursos adicionais, como filas de mensagens, priorização de mensagens, distribuição de carga e escalabilidade.

Ao configurar o Channels, você precisa escolher o Message Layer Backend mais adequado para o seu caso de uso. Isso envolve a instalação e configuração do backend escolhido, além de ajustar as configurações do Channels para usar o backend correto.

Em resumo, o Message Layer Backend é uma parte crucial do Channels que gerencia o armazenamento e o envio de mensagens entre os consumidores e os canais, permitindo a comunicação assíncrona e em tempo real. A escolha do Message Layer Backend adequado depende das necessidades do seu aplicativo e dos recursos que você deseja aproveitar.