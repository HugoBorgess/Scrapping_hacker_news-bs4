# HackerNews Scraper

Este script em Python permite extrair notícias da página HackerNews e salvar as informações em arquivos de texto para cada página.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Bibliotecas Python: requests, beautifulsoup4

## Como usar

1. Clone o repositório ou faça o download do código-fonte.

2. No terminal, navegue até o diretório do projeto.

3. Execute o seguinte comando para instalar as dependências necessárias:

   ```
   pip install requests beautifulsoup4
   ```

4. Execute o script usando o seguinte comando:

   ```
   python hackernews_scraper.py
   ```

5. Siga as instruções no prompt de comando para fornecer o número de páginas que deseja extrair e se deseja ver uma saída detalhada (verbose).

6. Os resultados serão salvos no diretório `HackerNews` em arquivos de texto separados para cada página.

   - O formato do nome do arquivo será `NewsPageX.txt`, onde `X` representa o número da página.

7. Após a conclusão da execução do script, você poderá encontrar os arquivos de texto com as notícias da HackerNews.

## Observações

- O número máximo de páginas que podem ser extraídas é 20.

- Certifique-se de ter uma conexão de internet ativa ao executar o script.

- Se ocorrer algum erro de conexão ao extrair uma página específica, uma mensagem de erro será exibida no console e o processo continuará com as páginas restantes.

- Para exibir uma saída mais detalhada durante a execução do script, digite 'y' quando solicitado a opção verbose.

Aproveite a exploração das notícias da HackerNews com este script de coleta!
