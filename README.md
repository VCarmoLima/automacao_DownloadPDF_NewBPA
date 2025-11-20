# Invoice Downloader Automation

Este projeto é um script de automação em Python desenvolvido para ler uma planilha Excel contendo links de faturas e datas de vencimento, fazer o download dos arquivos PDF e organizá-los automaticamente em pastas separadas por mês (Ano-Mês).

## 📋 Funcionalidades

- Leitura de planilhas Excel (.xlsx).
- Tratamento de erros de data (ex: datas digitadas incorretamente como ano 2925).
- Download automático de arquivos via URL.
- Organização automática de diretórios baseada na data de vencimento (`YYYY-MM`).
- Renomeação inteligente de arquivos genéricos.

## 🛠️ Pré-requisitos

- Python 3.8 ou superior
- Pip (Gerenciador de pacotes do Python)

## 🚀 Instalação

1. Clone o repositório:
   ```bash
   git clone [https://github.com/VCarmoLima/automacao_DownloadPDFs_NewBPA.git]
   cd invoice-downloader
   
2. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt

## ⚙️ Configuração (.env)

Antes de rodar, você deve criar um arquivo .env na raiz do projeto para configurar os caminhos locais. Você pode usar o arquivo de exemplo abaixo:

1. Crie um arquivo chamado .env.

2. Adicione as seguintes variáveis:
    ```bash
       # Caminho para o arquivo Excel de entrada
    INPUT_FILE_PATH= "C:\Caminho\Para\Seu\Arquivo\invoice_file.xlsx"
       # Pasta onde os downloads serão salvos
    OUTPUT_FOLDER="C:\Caminho\Para\Downloads\Invoices_Baixadas"
   
**Nota**: O arquivo .env não deve ser comitado no Git por questões de segurança.

## 📂 Estrutura da Planilha

O script espera um arquivo Excel com, no mínimo, as seguintes colunas (cabeçalhos):
invoice_file, due_date

## ▶️ Como usar

Basta executar o script principal:
```bash
    python main.py
```
O terminal mostrará o progresso linha a linha. Arquivos com datas inválidas serão salvos numa pasta chamada Sem_Data.

## 📄 Licença

[MIT](https://choosealicense.com/licenses/mit/)