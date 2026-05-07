import os

import json

def configurar_sistema():
  
  if not os.path.exists("uploads_projetos"):

   os.makedirs("uploads_projetos")

   def listar_projetos():
     
    arquivos = [f for f in os.listdir("uploads_projetos") if f.endswith(".json")]

    print ('\n'+'='*40)

    print ('PROJETOS CADASTRADOS')

    print ('='*40)

    if not arquivos

    print ("Nenhum projeto encontrado.")

    return []
   
   for i,arquivo in enumerate (arquivos,1):

    nome_exibicao = arquivo.replace("projeto_","").replace(".json","").replace("_"," ")

    print ("{f"{i}.{nome_exibicao.title()}"}")

    
    return arquivos
   
def gerencia_projeto():
 
 arquivos = listar_projetos()

 if not arquivos:return



try:
 
 escolha = int(input("\n Escolha o número do projeto para gerenciar(ou 0 para volatr)"))

