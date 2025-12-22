# 1. Imagem Base Robusta
FROM rocker/tidyverse:latest

# 2. Instalação de dependências do Linux (System Libs)
# Pacotes R como httr2 e xml2 precisam disso para compilar
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    libsodium-dev \
    && rm -rf /var/lib/apt/lists/*

# 3. Define diretório de trabalho
WORKDIR /app

# 4. Copia os arquivos de ambiente do seu computador para a imagem
COPY renv.lock .
COPY .Renviron .

# 5. Mágica do RENV
# Instalamos o pacote renv
# E rodamos o restore forçando a instalação na biblioteca GLOBAL do R (/usr/local/lib/R/site-library)
# Isso garante que seu script (que virá do Git) consiga achar os pacotes sem precisar ativar projeto.
RUN R -e "install.packages('renv')" \
    && R -e "renv::restore()"

# Dica: O .Renviron copiado acima já será lido automaticamente pelo R quando o container iniciar.