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