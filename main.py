import requests
import os
from bs4 import BeautifulSoup, SoupStrainer

if not os.path.exists(os.path.join(os.getcwd(), 'HackerNews')):
    os.makedirs(os.path.join(os.getcwd(), 'HackerNews'))

def fetch(page_no, verbose=False):
    if page_no <= 0:
        raise ValueError('O numero de páginas tem que ser maior que zero')
    page_no = min(page_no, 20)
    i = page_no
    if verbose:
        print('Buscando páginas {}...'.format(i))
    try:
        res = requests.get('https://news.ycombinator.com/?p=' + str(i))
        only_td = SoupStrainer('td')
        soup = BeautifulSoup(res.content, 'html.parser', parse_only=only_td)
        tdtitle = soup.find_all('td', attrs={'class': 'title'})
        tdmetrics = soup.find_all('td', attrs={'class': 'subtext'})
        with open(os.path.join('HackerNews', 'NewsPage{}.txt'.format(i)), 'w+') as f:
            f.write('-' * 80)
            f.write('\n')
            f.write('Página {}'.format(i))
            tdtitle = soup.find_all('td', attrs={'class': 'title'})
            tdrank = soup.find_all(
                'td',
                attrs={
                    'class': 'title',
                    'align': 'right'})
            tdtitleonly = [t for t in tdtitle if t not in tdrank]
            tdmetrics = soup.find_all('td', attrs={'class': 'subtext'})
            tdt = tdtitleonly
            tdr = tdrank
            tdm = tdmetrics
            num_iter = min(len(tdr), len(tdt))
            for idx in range(num_iter):
                f.write('\n' + '-' * 80 + '\n')
                rank = tdr[idx].find('span', attrs={'class': 'rank'})
                titl = tdt[idx].find('a')
                if titl is not None:
                    url = titl['href'] if 'href' in titl and titl['href'].startswith('https') else 'https://news.ycombinator.com/' + (titl.get('href') or '')
                else:
                    url = ''
                site = tdt[idx].find('span', attrs={'class': 'sitestr'})
                score = tdm[idx].find('span', attrs={'class': 'score'})
                time = tdm[idx].find('span', attrs={'class': 'age'})
                author = tdm[idx].find('a', attrs={'class': 'hnuser'})
                f.write(
                    '\nNúmero do artigo: ' +
                    rank.text.replace(
                        '.',
                        '') if rank else '\nNúmero do artigo: Não foi possivel coletar Número do artigo')
                f.write(
                    '\nTítulo do Artigo: ' +
                    titl.text if titl else '\nTítulo do Artigo: Não foi possivel coletar Título do Artigo')
                f.write(
                    '\nSite Fonte: ' +
                    site.text if site else '\nSite Fonte: https://news.ycombinator.com')
                f.write(
                    '\nURL site: ' +
                    url if url else '\nURL site: Nenhum URL encontrado para este artigo')
                f.write(
                    '\nAutor do artigo: ' +
                    author.text if author else '\nAutor do artigo: Não foi possivel coletar autor do artigo')
                f.write(
                    '\nPontuação do artigo: ' +
                    score.text if score else '\nPontuação do artigo: Sem pontuação')
                f.write(
                    '\Postado: ' +
                    time.text if time else '\nPostado: Não foi possivel encontrar a data de publicação do artigo')
                f.write('\n' + '-' * 80 + '\n')
    except (requests.ConnectionError, requests.packages.urllib3.exceptions.ConnectionError) as e:
        print('Conexão perdida para a página {}'.format(i))
    except requests.RequestException as e:
        print("Ocorreu alguma exceção de solicitação ambígua. A exceção é " + str(e))


while(True):
    try:
        pages = int(
            input('Digite o número de páginas para as quais você deseja o HackerNews (máximo de 20): '))
        v = input('Deseja uma saída detalhada y/[n] ?')
        verbose = v.lower().startswith('y')
        if pages > 20:
            print('Um máximo de apenas 20 páginas pode ser buscado')
        pages = min(pages, 20)
        for page_no in range(1, pages + 1):
            fetch(page_no, verbose)
        print('Concluído')
        break
    except ValueError:
        print('\nEntrada inválida, provavelmente não é um número inteiro positivo\n')
        continue