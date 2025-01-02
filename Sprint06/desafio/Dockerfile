# Versão do Python escolhida
FROM python:3.9-slim
# Diretório de trabalho
WORKDIR /app
# Cópia do txt de requerimentos para instalação de bibliotecas
COPY requirements.txt requirements.txt
# Executa a instalação das bibliotecas contidas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Cópia do script em python
COPY Script.py Script.py
# Cópia do arquivo movies para o container
COPY movies.csv movies.csv
# Cópia do arquivo series para o container
COPY series.csv series.csv
# Execução do script em pyhton
CMD ["python", "Script.py"]