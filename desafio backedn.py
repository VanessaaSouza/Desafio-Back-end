import requests
from googletrans import Translator
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import system

def piadaChuck():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    data = response.json()
    return (data["value"])

#Coleta de dados
pvendas = requests.get('https://dummyjson.com/products')
dados = pvendas.json()
cont, soma = 0, 0

for i in dados['products']:
    if i['category'] == 'smartphones':
        soma += int(i['price'])
        cont += 1
media = soma/cont

#Integração com Banco de Dados
engine = create_engine("sqlite:///products.db")
Base = declarative_base()

class User(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    title = Column(String(30))
    category = Column(String(20))
    price = Column(Integer)

Base.metadata.create_all(engine)

#Conectar sessão
Sessao = sessionmaker(bind=engine)
section = Sessao()

#Criando Instância
for item in dados['products']:
    usuario_existente = section.query(User).filter_by(id=item['id']).first()
    
    if usuario_existente is None:
        usuario = User(id = item['id'], title = item['title'], category = item['category'], price = item['price'])
        section.add(usuario)
   
section.commit()

#Piada Chuck Norris
tradutor = Translator()
texto = piadaChuck()
traducao = tradutor.translate(texto, src='en', dest='pt')

#Resultados
system('cls')
print('## Resultado da coleta de dados ##')
print(f'Preço médio dos {cont} smartphones: $ {media:.2f}')
print('==============Momento Piada===============')
print(traducao.text)
