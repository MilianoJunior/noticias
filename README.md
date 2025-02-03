# 🤖 NewsBot - Monitor de Notícias

## 📋 Descrição
NewsBot é um robô em Python que monitora automaticamente as últimas notícias sobre tópicos específicos. Ele busca notícias no Google News, salva em um arquivo CSV e mostra apenas as notícias novas a cada atualização.

## ✨ Funcionalidades
- 🔍 Busca notícias sobre múltiplos assuntos simultaneamente
- 💾 Armazena as notícias em um arquivo CSV
- 🔄 Atualiza automaticamente a cada 30 segundos
- 🆕 Mostra apenas notícias novas (não mostradas anteriormente)
- 📊 Mantém um histórico completo das notícias encontradas

## 📦 Requisitos
- Python 3.x
- Biblioteca `requests`
- Biblioteca `beautifulsoup4`
- Biblioteca `pandas`


## 🚀 Como Usar

1. Clone o repositório ou baixe os arquivos
2. Instale as dependências:

```bash
pip install requests beautifulsoup4 pandas
```

3. Execute o script:

```bash
python news_bot.py
```

## ⚙️ Configuração
Para modificar os tópicos de busca, edite as seguintes linhas no final do arquivo `news_bot.py`:

```python
assuntos = ['Inteligência Artificial', 'IA']  # Adicione ou modifique os assuntos
quantidade = 10  # Modifique a quantidade de notícias por assunto
```

## 📄 Formato das Notícias
Cada notícia contém:
- Título
- Fonte
- Data de publicação
- Link para a notícia completa

## 💾 Armazenamento
- As notícias são salvas no arquivo `noticias.csv`
- O CSV mantém um histórico de todas as notícias encontradas
- Evita duplicação de notícias já mostradas

## 🔄 Ciclo de Atualização
1. Busca notícias dos assuntos configurados
2. Compara com as notícias já salvas
3. Mostra apenas as notícias novas
4. Salva as novas notícias no CSV
5. Aguarda 30 segundos
6. Repete o processo

## 📝 Notas
- O bot utiliza o Google News como fonte de notícias
- As notícias são mostradas em português
- O arquivo CSV pode ser aberto em qualquer editor de planilhas

## 🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação
- Enviar pull requests








