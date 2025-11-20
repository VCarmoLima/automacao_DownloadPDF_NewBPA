import pandas as pd
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

CAMINHO_EXCEL = os.getenv("INPUT_FILE_PATH")
PASTA_DESTINO_BASE = os.getenv("OUTPUT_FOLDER")

def baixar_invoices():
    if not CAMINHO_EXCEL or not PASTA_DESTINO_BASE:
        print("ERRO: Variáveis de ambiente não configuradas. Verifique o arquivo .env")
        return

    if not os.path.exists(PASTA_DESTINO_BASE):
        os.makedirs(PASTA_DESTINO_BASE)

    print(f"Lendo arquivo: {CAMINHO_EXCEL}...")

    try:
        df = pd.read_excel(CAMINHO_EXCEL)

        df['due_date'] = pd.to_datetime(df['due_date'], errors='coerce')

        total_links = len(df)
        print(f"Encontradas {total_links} linhas. Iniciando processamento...\n")

        for index, row in df.iterrows():
            url = row['invoice_file']
            data_vencimento = row['due_date']

            if pd.isna(data_vencimento):
                print(f"[{index+1}/{total_links}] AVISO: Data inválida/vazia na linha {index+2}. Salvando em 'Sem_Data'.")
                nome_pasta_mes = "Sem_Data"
            else:
                nome_pasta_mes = data_vencimento.strftime('%Y-%m')

            if pd.isna(url):
                continue

            caminho_final_pasta = os.path.join(PASTA_DESTINO_BASE, nome_pasta_mes)

            if not os.path.exists(caminho_final_pasta):
                os.makedirs(caminho_final_pasta)

            nome_arquivo = str(url).split('/')[-1]
            if not nome_arquivo.lower().endswith('.pdf'):
                nome_arquivo = f"invoice_linha_{index+2}.pdf"

            nome_arquivo = "".join([c for c in nome_arquivo if c.isalnum() or c in (' ', '.', '_', '-')])
            caminho_arquivo = os.path.join(caminho_final_pasta, nome_arquivo)

            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    with open(caminho_arquivo, 'wb') as f:
                        f.write(response.content)
                    print(f"[{index+1}/{total_links}] Sucesso: {nome_pasta_mes}/{nome_arquivo}")
                else:
                    print(f"[{index+1}/{total_links}] Erro HTTP {response.status_code}: Linha {index+2}")
            except Exception as e:
                print(f"[{index+1}/{total_links}] Falha ao baixar linha {index+2}: {e}")

    except FileNotFoundError:
        print(f"Erro CRÍTICO: O arquivo não foi encontrado em: {CAMINHO_EXCEL}")
        print("Verifique se o caminho no arquivo .env está correto.")
    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")

if __name__ == "__main__":
    baixar_invoices()