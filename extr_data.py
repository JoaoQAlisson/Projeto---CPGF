## Extração de dados da transparência Gov.BR
#bibs
import requests
import time
import pandas as pd

#Dados do headers de requisição deve ser o documentado pela instituição
headers = {
    "chave-api-dados": "SUA CHAVE AQUI" 
}

url = 'https://api.portaldatransparencia.gov.br/api-de-dados/cartoes'
param = {"pagina" : 1, 
         "mesExtratoInicio" : "01/2025",
         "mesExtratoFim": "01/2026"}
pagina = 1
dados = []
infos ={}
while pagina <= 100000:
    param["pagina"] = pagina
    response = requests.get(url, headers=headers, params=param)
    if response.status_code == 200:
        dados_pagina = response.json()

        if not dados_pagina:
            break
        
        df = pd.json_normalize(dados_pagina)
        dados.append(df)
        print(f"Página {pagina} extraída...")
        pagina += 1

    else:
        print(f"Erro: {response.status_code}")
    
else: 
    print("Limite de Paginas Atingido")
df_final = pd.concat(dados, ignore_index=True)
df_final.to_csv('dados_2025.csv')
