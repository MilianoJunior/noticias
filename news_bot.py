import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import pandas as pd
import os

class NewsBot:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.arquivo_csv = 'noticias.csv'
        self.criar_csv_se_nao_existe()

    def criar_csv_se_nao_existe(self):
        if not os.path.exists(self.arquivo_csv):
            df = pd.DataFrame(columns=['titulo', 'fonte', 'data', 'link'])
            df.to_csv(self.arquivo_csv, index=False)

    def carregar_noticias_existentes(self):
        try:
            return pd.read_csv(self.arquivo_csv)
        except:
            return pd.DataFrame(columns=['titulo', 'fonte', 'data', 'link'])

    def salvar_noticias(self, noticias):
        df_novo = pd.DataFrame(noticias)
        df_novo.to_csv(self.arquivo_csv, index=False)

    def filtrar_noticias_novas(self, noticias):
        df_existente = self.carregar_noticias_existentes()
        noticias_novas = []
        
        for noticia in noticias:
            # Verifica se a notícia já existe no CSV
            if not df_existente['link'].str.contains(noticia['link']).any():
                noticias_novas.append(noticia)
        
        # Adiciona as novas notícias ao CSV existente
        if noticias_novas:
            df_novas = pd.DataFrame(noticias_novas)
            df_atualizado = pd.concat([df_existente, df_novas], ignore_index=True)
            df_atualizado.to_csv(self.arquivo_csv, index=False)
        
        return noticias_novas

    def buscar_noticias(self, assunto, quantidade=5):
        # Formata o assunto para a URL
        assunto_formatado = assunto.replace(' ', '+')
        url = f'https://news.google.com/rss/search?q={assunto_formatado}&hl=pt-BR&gl=BR&ceid=BR:pt-419'

        try:
            # Faz a requisição
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()

            # Parse do XML
            soup = BeautifulSoup(response.content, 'xml')
            items = soup.find_all('item')

            noticias = []
            for item in items[:quantidade]:
                noticia = {
                    'titulo': item.title.text,
                    'link': item.link.text,
                    'data': item.pubDate.text,
                    'fonte': item.source.text
                }
                noticias.append(noticia)

            return noticias

        except Exception as e:
            print(f"Erro ao buscar notícias: {str(e)}")
            return []

    def mostrar_noticias(self, noticias):
        print("\n=== ÚLTIMAS NOTÍCIAS ===")
        print(f"Atualizado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        
        for i, noticia in enumerate(noticias, 1):
            print(f"{i}. {noticia['titulo']}")
            print(f"Fonte: {noticia['fonte']}")
            print(f"Data: {noticia['data']}")
            print(f"Link: {noticia['link']}")
            print("-" * 80 + "\n")

    def buscar_noticias_multiplos_assuntos(self, assuntos, quantidade=5):
        todas_noticias = []
        for assunto in assuntos:
            noticias = self.buscar_noticias(assunto, quantidade)
            todas_noticias.extend(noticias)
        
        # Filtra apenas as notícias novas
        noticias_novas = self.filtrar_noticias_novas(todas_noticias)
        return noticias_novas

def main(assuntos, quantidade):
    bot = NewsBot()
    
    while True:
        noticias = bot.buscar_noticias_multiplos_assuntos(assuntos, quantidade)
        
        if noticias:
            print("\nNovas notícias encontradas!")
            bot.mostrar_noticias(noticias)
        else:
            print("\nNenhuma notícia nova encontrada.")
        
        print("\nAguardando 3 minutos para próxima atualização...")
        time.sleep(30)  # Espera 3 minutos

if __name__ == "__main__":
    assuntos = ['Inteligência Artificial', 'IA']
    quantidade = 10
    main(assuntos, quantidade) 