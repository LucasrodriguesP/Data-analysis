import csv

import json

# Ler o JSON do arquivo json.txt
##with open('json.txt', 'r') as file:
 #   json_data = json.load(file)

json_data = {
   "objectIdFieldName":"objectid",
   "globalIdFieldName":"",
   "geometryType":"esriGeometryPolyline",
   "spatialReference":{
      "wkid":4326,
      "latestWkid":4326
   },
   "fields":[
      {
         "name":"completo",
         "alias":"completo",
         "type":"esriFieldTypeString",
         "length":68
      },
      {
         "name":"nome",
         "alias":"nome",
         "type":"esriFieldTypeString",
         "length":50
      }
   ],
   "features":[
      {
         "attributes":{
            "completo":"Rua Compositor Ribamar",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Compositor Ribamar",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Compositor Ribamar",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Compositor Ribamar",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua João Batista",
            "nome":"Paciência"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Brasil",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Olga Paula de Souza",
            "nome":"Marechal Hermes"
         }
      },
      {
         "attributes":{
            "completo":"Rua Antônio Sales",
            "nome":"Cacuia"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Praça Guarda Amaral",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua União",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Monsenhor Távola",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua Mangara",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Presidente Antonio Carlos",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Buenos Aires",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Comércio",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Gustavo de Lacerda",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Rosário",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Primeiro de Março",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Largo dos Pracinhas",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Rosário",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Presidente Antonio Carlos",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Candelária",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Primeiro de Março",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Buenos Aires",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Praça Melvin Jones",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Primeiro de Março",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Candelária",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Luís de Camões",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Buenos Aires",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Debret",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Praça Monte Castelo",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Praça Cardeal Câmara",
            "nome":"Lapa"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Almirante Barroso",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Araújo Porto Alegre",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Presidente Antonio Carlos",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Presidente Antonio Carlos",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Erasmo Braga",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Buenos Aires",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Anfilofio de Carvalho",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Araújo Porto Alegre",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Presidente Antonio Carlos",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Santa Luzia",
            "nome":"Lapa"
         }
      },
      {
         "attributes":{
            "completo":"Rua Santa Luzia",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Primeiro de Março",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua da Conceição",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Beco do Rosário",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida General Justo",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Primeiro de Março",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Rosário",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Miguel Couto",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua dos Andradas",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Presidente Antonio Carlos",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua dos Andradas",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Debret",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Candelária",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Mem de Sá",
            "nome":"Lapa"
         }
      },
      {
         "attributes":{
            "completo":"Travessa do Paço",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Almirante Barroso",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Presidente Antonio Carlos",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Marechal Aguinaldo Caiado de Castro",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Beco do Rosário",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Marechal Floriano",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Praça Tiradentes",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Rosário",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Armando de Sales Oliveira",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Presidente Antonio Carlos",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Presidente Antonio Carlos",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Mercado",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Almirante Barroso",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Presidente Wilson",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Marechal Aguinaldo Caiado de Castro",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Buenos Aires",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Primeiro de Março",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Presidente Antonio Carlos",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida República do Chile",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Debret",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida República do Chile",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Araújo Porto Alegre",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Marechal Floriano",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Presidente Antonio Carlos",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Ramalho Ortigão",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Praça Embaixador Azeredo da Silveira",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Praça Procurador-Geral de Justiça Hermano Odilon dos Anjos",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Praça Comandante Alexandre Siqueira",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Bartolomeu de Gusmão",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida General Justo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Marechal Bitencourt",
            "nome":"Riachuelo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada 05 PAA 12767/PAL 49882",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada 05 PAA 12767/PAL 49882",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Marisa Letícia Lula da Silva",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Marisa Letícia Lula da Silva",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"Rua José Soares de Oliveira",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Décio Esteves",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Ursa Menor",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Octante",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Garapa",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Caingá",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Roxinho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Gonçalo-Alves",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Furriel",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Suindara",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Pintadinho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Visconde do Rio Branco",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Praça Tiradentes",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Aparicio Borges",
            "nome":"Laranjeiras"
         }
      },
      {
         "attributes":{
            "completo":"Rua da Vila PAL 28899",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Luís de Camões",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Ituverava",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"Escadaria da Ituverava",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Sertão",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"Rua Araticum",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"Rua Denise Dobbin Bauerfeldt",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Denise Dobbin Bauerfeldt",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Ponte Lágrimas de Diamante",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Santa Gertrudes",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Coração Divino",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Jardim Santa Matilde",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Modelo",
            "nome":"Anchieta"
         }
      },
      {
         "attributes":{
            "completo":"Rua Santo Antonio da Pedra",
            "nome":"Anchieta"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Prefeito Dulcídio Cardoso",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Sobral Pinto",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida A PAA 10090/PAL 37215",
            "nome":"Itanhangá"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Sobral Pinto",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Sobral Pinto",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Sobral Pinto",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Sobral Pinto",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Sobral Pinto",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Avenida A PAA 10090/PAL 37215",
            "nome":"Itanhangá"
         }
      },
      {
         "attributes":{
            "completo":"Rua Ernesto Carneiro Ribeiro",
            "nome":"Santíssimo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Ernesto Carneiro Ribeiro",
            "nome":"Santíssimo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Ernesto Carneiro Ribeiro",
            "nome":"Santíssimo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Evangelina de Lima Barreto",
            "nome":"Santíssimo"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Gilberto Marmorosch",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Suzana Amaral",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"Rua Maria José Deane",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Ernestina Barreiro",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Tambaqui",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Ayrton Senna",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Mato Alto",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Mato Alto",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Mato Alto",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua 1 PAA 6290/PAL 18986",
            "nome":"Pitangueiras"
         }
      },
      {
         "attributes":{
            "completo":"Rua 2 PAA 6290/PAL 18986",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Carlos Colla",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Stella Goulart Marinho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Anthero Monteiro de Azevedo",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Tarso de Castro",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua D PAA 11265/PAL 44546",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua E PAA 11265/PAL 44546",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua B PAA 11265 / PAL 44546",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua B PAA 11265 / PAL 44546",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Avenida A PAA 10090/PAL 37215",
            "nome":"Itanhangá"
         }
      },
      {
         "attributes":{
            "completo":"Avenida A PAA 10090/PAL 37215",
            "nome":"Itanhangá"
         }
      },
      {
         "attributes":{
            "completo":"Avenida A PAA 10090/PAL 37215",
            "nome":"Itanhangá"
         }
      },
      {
         "attributes":{
            "completo":"Avenida A PAA 10090/PAL 37215",
            "nome":"Itanhangá"
         }
      },
      {
         "attributes":{
            "completo":"Avenida A PAA 10090/PAL 37215",
            "nome":"Itanhangá"
         }
      },
      {
         "attributes":{
            "completo":"Avenida A PAA 10090/PAL 37215",
            "nome":"Itanhangá"
         }
      },
      {
         "attributes":{
            "completo":"Rua Joaquim Guimarães",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Beatriz Larragoiti Lucas",
            "nome":"Cidade Nova"
         }
      },
      {
         "attributes":{
            "completo":"Rua Madre Tereza de Calcutá",
            "nome":"Cidade Nova"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Presidente Vargas",
            "nome":"Cidade Nova"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Paulo de Frontin",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua D PAA 11663/PAL 45187",
            "nome":"Santíssimo"
         }
      },
      {
         "attributes":{
            "completo":"Rua D PAA 11663/PAL 45187",
            "nome":"Santíssimo"
         }
      },
      {
         "attributes":{
            "completo":"Rua E PAA 11663/PAL 45187",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua C PAA 11663/PAL 45187",
            "nome":"Santíssimo"
         }
      },
      {
         "attributes":{
            "completo":"Rua C PAA 11663/PAL 45187",
            "nome":"Santíssimo"
         }
      },
      {
         "attributes":{
            "completo":"Rua B PAA 11663/PAL 45187",
            "nome":"Santíssimo"
         }
      },
      {
         "attributes":{
            "completo":"Rua I PAA 11663/PAL 45187",
            "nome":"Santíssimo"
         }
      },
      {
         "attributes":{
            "completo":"Praça PAA 11663/PAL 45187",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Aldemir Martins",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Aldemir Martins",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Aluisio Palhano",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Ayrton Senna",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Oscar Niemeyer",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Aldemir Martins",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Aldemir Martins",
            "nome":"Recreio dos Bandeirantes"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Aldemir Martins",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Aldemir Martins",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida George Savalla",
            "nome":"Recreio dos Bandeirantes"
         }
      },
      {
         "attributes":{
            "completo":"Rua Vittorio Migliora",
            "nome":"Recreio dos Bandeirantes"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Aldemir Martins",
            "nome":"Recreio dos Bandeirantes"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Aldemir Martins",
            "nome":"Recreio dos Bandeirantes"
         }
      },
      {
         "attributes":{
            "completo":"Rua Fernando de Souza Barros (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Aldemir Martins",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Aldemir Martins",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 245621",
            "nome":"Recreio dos Bandeirantes"
         }
      },
      {
         "attributes":{
            "completo":"Rua Olavo Gama",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Geraldo Ireneo Joffily",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Edna Côrte Silveira",
            "nome":"Recreio dos Bandeirantes"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 338632",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Guianas",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida das Américas",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Paulo Humberto Pizziali",
            "nome":"Sepetiba"
         }
      },
      {
         "attributes":{
            "completo":"Rua Pellegrino Tolomei",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Peter Giuliano Pereira da Silva",
            "nome":"Sepetiba"
         }
      },
      {
         "attributes":{
            "completo":"Rua Jorgina Fernandes da Silva",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Mendanha",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua da Floresta",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 367722",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua do Bem Querer",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua do Bem Querer",
            "nome":"Anil"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Projetada 4 PAA 12559/PAL 49018",
            "nome":"Anil"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Bem Querer",
            "nome":"Anil"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Projetada 16 PAA 12559/PAL 49018",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Doutor Paulino Werneck",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Projetada 17 PAA 12559/PAL 49018",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Projetada 20 PAA 12559/PAL 49018",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 445791",
            "nome":"Rocinha"
         }
      },
      {
         "attributes":{
            "completo":"Rua Alcelino Vendas Rodrigues",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Alcelino Vendas Rodrigues",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada Marechal Alencastro",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua São José",
            "nome":"Parada de Lucas"
         }
      },
      {
         "attributes":{
            "completo":"Rua Antônio Barros de Castro (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Aloísio Teixeira (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Aloísio Teixeira (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Fernando de Souza Barros (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Fernando de Souza Barros (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Aloísio Teixeira (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Aloísio Teixeira (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Aloísio Teixeira (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Aloísio Teixeira (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Fernando de Souza Barros (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Athilio Brum",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada A PAA 12490/PAL 48650",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada B PAA 12490/PAL 48650",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada B PAA 12490/PAL 48650",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada A PAA 12490/PAL 48650",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada E PAA 12490/PAL 48650",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada A PAA 12490/PAL 48650",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada A PAA 12490/PAL 48650",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada E PAA 12490/PAL 48650",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada E PAA 12490/PAL 48650",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada A PAA 12490/PAL 48650",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada A PAA 12490/PAL 48650",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada E PAA 12490/PAL 48650",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada B PAA 12490/PAL 48650",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada B PAA 12490/PAL 48650",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 267187",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"Estrada Adhemar Bebiano",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada D PAA 12490/PAL 48650",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada D PAA 12490/PAL 48650",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada D PAA 12490/PAL 48650",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada E PAA 12490/PAL 48650",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada E PAA 12490/PAL 48650",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada E PAA 12490/PAL 48650",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada D PAA 12490/PAL 48650",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada D PAA 12490/PAL 48650",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome - CL 454074",
            "nome":"Paciência"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome - CL 454074",
            "nome":"Paciência"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome - CL 454074",
            "nome":"Paciência"
         }
      },
      {
         "attributes":{
            "completo":"Rua Vitória Régia (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Rua Vitória Régia (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Rua Flor-de-Lis (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Tulipas (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Margarida (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Rua Margarida (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Rua dos Cravos (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Roberto Dinamite",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Roberto Dinamite",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"Rua Pedro Calmon (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Rua Pedro Calmon (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Praça Samira Nashid Mesquita (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Praça Samira Nashid Mesquita (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Horácio de Macedo (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Horácio de Macedo (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Ponte do Saber (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Ponte do Saber (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Ponte do Saber (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Ponte do Saber (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Moniz de Aragão (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Rua Barão de São Felix",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Uruguai",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Pau da Fome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Athos da Silveira Ramos (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Athos da Silveira Ramos (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Praça Edson Abdalla Saad (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Praça Edson Abdalla Saad (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Horácio de Macedo (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Praça Edson Abdalla Saad (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Professor Rodolpho Paulo Rocco (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Rua Professor Rodolpho Paulo Rocco (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Rua César Pernetta (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Rua César Pernetta (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Praça Walter Baptist Mors (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Walter Baptist Mors (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Walter Baptist Mors (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Professor Rodolpho Paulo Rocco (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Professor Rodolpho Paulo Rocco (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Praça Edgar de Magalhães Gomes (N.R.)",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua César Pernetta (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Rua Maria Dolores Lins de Andrade (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"Rua Octávio Cantanhede (N.R.)",
            "nome":"Cidade Universitária"
         }
      },
      {
         "attributes":{
            "completo":"sem nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua C",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua C",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua C",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua O",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Estrada Adhemar Bebiano",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Fernão de Magalhães",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Fernão de Magalhães",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua D",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Neuza Amaral",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Neuza Amaral",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Neif Antônio Alem",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Neif Antônio Alem",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Neif Antônio Alem",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Neif Antônio Alem",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Neif Antônio Alem",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Lobo Junior",
            "nome":"Penha Circular"
         }
      },
      {
         "attributes":{
            "completo":"Avenida B PAA 10316/PAL 39026",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida B PAA 10316/PAL 39026",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida B PAA 10316/PAL 39026",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida B PAA 10316/PAL 39026",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Tamarindos da Península",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Eleone de Almeida",
            "nome":"Santa Teresa"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Ayrton Senna",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Ayrton Senna",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Ayrton Senna",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Ayrton Senna",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Praça Jose de Alencar",
            "nome":"Flamengo"
         }
      },
      {
         "attributes":{
            "completo":"Praça Jose de Alencar",
            "nome":"Flamengo"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Rei Pelé",
            "nome":"Maracanã"
         }
      },
      {
         "attributes":{
            "completo":"Rua Doutor Jose Thomaz",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua Tupassi",
            "nome":"Cosmos"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Gibeom",
            "nome":"Cidade de Deus"
         }
      },
      {
         "attributes":{
            "completo":"Rua Dois",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua Nambi",
            "nome":"Pitangueiras"
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Barro Vermelho",
            "nome":"Rocha Miranda"
         }
      },
      {
         "attributes":{
            "completo":"Rua C",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 378604",
            "nome":"Leme"
         }
      },
      {
         "attributes":{
            "completo":"Rua Coaraci Gentil Nunes",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Beco Francisco Alves",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Mozart",
            "nome":"Jardim América"
         }
      },
      {
         "attributes":{
            "completo":"Rua Guararema",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua Ana Maria Noronha",
            "nome":"Vidigal"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Ribeiro Dantas",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"Rua Beatriz Feitler",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Porena",
            "nome":"Ramos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Maestro Amaro Barreto",
            "nome":"Cordovil"
         }
      },
      {
         "attributes":{
            "completo":"Rua Martim Afonso",
            "nome":"Leme"
         }
      },
      {
         "attributes":{
            "completo":"Rua Patrocínio",
            "nome":"Guadalupe"
         }
      },
      {
         "attributes":{
            "completo":"Rua Vieira do Couto",
            "nome":"Rocha Miranda"
         }
      },
      {
         "attributes":{
            "completo":"Rua Oscar Lopes",
            "nome":"Anil"
         }
      },
      {
         "attributes":{
            "completo":"Rua Wilson Souza Pinheiro",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Três ",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Alfredo Balthazar da Silveira",
            "nome":"Recreio dos Bandeirantes"
         }
      },
      {
         "attributes":{
            "completo":"Rua Ana Teles",
            "nome":"Campinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua Frei Alexandre",
            "nome":"Irajá"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Brasil",
            "nome":"Ramos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Professor Carlos Chagas",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua General Correa e Castro",
            "nome":"Jardim América"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 429399",
            "nome":"Santa Teresa"
         }
      },
      {
         "attributes":{
            "completo":"Rua Teodoro Sampaio",
            "nome":"Jardim Sulacap"
         }
      },
      {
         "attributes":{
            "completo":"Rua Tales de Carvalho",
            "nome":"Jardim América"
         }
      },
      {
         "attributes":{
            "completo":"Rua Jorge Gomes",
            "nome":"Complexo do Alemão"
         }
      },
      {
         "attributes":{
            "completo":"Rua Tacaratu",
            "nome":"Marechal Hermes"
         }
      },
      {
         "attributes":{
            "completo":"Estrada da Água Grande",
            "nome":"Irajá"
         }
      },
      {
         "attributes":{
            "completo":"Avenida dos Italianos",
            "nome":"Rocha Miranda"
         }
      },
      {
         "attributes":{
            "completo":"Rua Nove",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Presidente Vargas",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Rio da Prata",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome - CL 453092",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua Rio Apa",
            "nome":"Cordovil"
         }
      },
      {
         "attributes":{
            "completo":"Rua Rio Apa",
            "nome":"Braz de Pina"
         }
      },
      {
         "attributes":{
            "completo":"Estrada da Água Grande",
            "nome":"Vista Alegre"
         }
      },
      {
         "attributes":{
            "completo":"Travessa D",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Limites",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Luzitânia",
            "nome":"Penha Circular"
         }
      },
      {
         "attributes":{
            "completo":"Rua Turvo",
            "nome":"Irajá"
         }
      },
      {
         "attributes":{
            "completo":"Rua Turvo",
            "nome":"Vicente de Carvalho"
         }
      },
      {
         "attributes":{
            "completo":"Rua São Gedeão",
            "nome":"Penha"
         }
      },
      {
         "attributes":{
            "completo":"Rua Ortivo Guedes",
            "nome":"Estácio"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Cidade de Lima",
            "nome":"Santo Cristo"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Canal",
            "nome":"Maré"
         }
      },
      {
         "attributes":{
            "completo":"Rua Bombaim",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"Rua Adelis Luis de Lima",
            "nome":"Anchieta"
         }
      },
      {
         "attributes":{
            "completo":"Rua Eduardo Ramos",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua General Caiado de Castro - P 39587",
            "nome":"Penha"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Brasil",
            "nome":"Caju"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 351924",
            "nome":"Laranjeiras"
         }
      },
      {
         "attributes":{
            "completo":"Rua Clarisse",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome - CL 470823",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Sauna",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 413278",
            "nome":"Cidade de Deus"
         }
      },
      {
         "attributes":{
            "completo":"Avenida dos Mananciais",
            "nome":"Taquara"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Carlos Sampaio Correa",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 280487",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Boa Vista PAA 10345/PAL 39463",
            "nome":"Barros Filho"
         }
      },
      {
         "attributes":{
            "completo":"Rua Sargento Marqueti",
            "nome":"Marechal Hermes"
         }
      },
      {
         "attributes":{
            "completo":"Rua Caripare",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Largo do Sapê",
            "nome":"Rocha Miranda"
         }
      },
      {
         "attributes":{
            "completo":"Viaduto Procurador José Alves de Moraes",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Beco da União",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Diber",
            "nome":"Gardênia Azul"
         }
      },
      {
         "attributes":{
            "completo":"Rua Maturaca",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua 13 Estrada do Galeão nº 2980",
            "nome":"Portuguesa"
         }
      },
      {
         "attributes":{
            "completo":"Praia José Bonifácio",
            "nome":"Paquetá"
         }
      },
      {
         "attributes":{
            "completo":"Avenida das Américas",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 238170",
            "nome":"Padre Miguel"
         }
      },
      {
         "attributes":{
            "completo":"Praça Belmonte",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"Rua Cesar do Rego Monteiro Filho",
            "nome":"Tomás Coelho"
         }
      },
      {
         "attributes":{
            "completo":"Rua Cesar do Rego Monteiro Filho",
            "nome":"Engenho da Rainha"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Meriti",
            "nome":"Parada de Lucas"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Meriti",
            "nome":"Cordovil"
         }
      },
      {
         "attributes":{
            "completo":"Rua Cisne",
            "nome":"Copacabana"
         }
      },
      {
         "attributes":{
            "completo":"Travessa do Trigo de Marcílio Dias",
            "nome":"Penha Circular"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 383497",
            "nome":"Copacabana"
         }
      },
      {
         "attributes":{
            "completo":"Rua Barão da Laguna",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Oaxaco",
            "nome":"Inhaúma"
         }
      },
      {
         "attributes":{
            "completo":"Rua Cinquenta e nove",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua Monte Amor Sagrado - PAL 40109",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua São Martiniano",
            "nome":"São Conrado"
         }
      },
      {
         "attributes":{
            "completo":"Rua Monte Rei",
            "nome":"Paciência"
         }
      },
      {
         "attributes":{
            "completo":"Rua Marinho Pessoa",
            "nome":"Irajá"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Pastor Martin Luther King Jr.",
            "nome":"Colégio"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Pastor Martin Luther King Jr.",
            "nome":"Irajá"
         }
      },
      {
         "attributes":{
            "completo":"Rua Maria do Carmo",
            "nome":"Rocinha"
         }
      },
      {
         "attributes":{
            "completo":"Rua João Romariz",
            "nome":"Ramos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 359570",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Bento Ribeiro Dantas",
            "nome":"Maré"
         }
      },
      {
         "attributes":{
            "completo":"Rua General Gustavo Cordeiro de Farias",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Professor Valadares",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Ayrton Senna",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Esperança",
            "nome":"Rocinha"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 280156",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua Senador Mozart Lago",
            "nome":"Coelho Neto"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Dom João VI",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Costa Carvalho",
            "nome":"Freguesia (Ilha)"
         }
      },
      {
         "attributes":{
            "completo":"Avenida A",
            "nome":"Paciência"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Brasil",
            "nome":"Vila Kennedy"
         }
      },
      {
         "attributes":{
            "completo":"Rua Pantoja",
            "nome":"Acari"
         }
      },
      {
         "attributes":{
            "completo":"Rua Saint Hilaire",
            "nome":"Bonsucesso"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 445668",
            "nome":"Rocinha"
         }
      },
      {
         "attributes":{
            "completo":"Rua Angelo Pimentel",
            "nome":"Bancários"
         }
      },
      {
         "attributes":{
            "completo":"Rua Dona Emília",
            "nome":"Inhaúma"
         }
      },
      {
         "attributes":{
            "completo":"Rua Aurea",
            "nome":"Santa Teresa"
         }
      },
      {
         "attributes":{
            "completo":"Rua General Bruce",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Armando Lombardi",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Angelo Agostini",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Estrada Rio-São Paulo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sergipe",
            "nome":"Vigário Geral"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 371211",
            "nome":"São Conrado"
         }
      },
      {
         "attributes":{
            "completo":"Rua Gonzaga Duque",
            "nome":"Ramos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Peruipe",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"Rua 41 PAA 6172/PAL 18529",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Pastor Martin Luther King Jr.",
            "nome":"Vicente de Carvalho"
         }
      },
      {
         "attributes":{
            "completo":"Rua Parapeuna",
            "nome":"Cosmos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Marechal Aguinaldo Caiado de Castro",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Trindade",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Dom Helder Camara",
            "nome":"Cachambi"
         }
      },
      {
         "attributes":{
            "completo":"Rua Servidão F",
            "nome":"Recreio dos Bandeirantes"
         }
      },
      {
         "attributes":{
            "completo":"Rua José Inácio",
            "nome":"Rocinha"
         }
      },
      {
         "attributes":{
            "completo":"Rua São Francisco",
            "nome":"Santa Teresa"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Alpiste",
            "nome":"Penha Circular"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 359398",
            "nome":"Tomás Coelho"
         }
      },
      {
         "attributes":{
            "completo":"Rua Ministro Raul Fernandes",
            "nome":"Botafogo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 446104",
            "nome":"Rocinha"
         }
      },
      {
         "attributes":{
            "completo":"Rua Dois de Maio",
            "nome":"Jacaré"
         }
      },
      {
         "attributes":{
            "completo":"Rua Engenheiro Jose Carvalho Salgado",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 359646",
            "nome":"Acari"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 356907",
            "nome":"Irajá"
         }
      },
      {
         "attributes":{
            "completo":"Rua Valdomiro Figueira Jorge",
            "nome":"Alto da Boa Vista"
         }
      },
      {
         "attributes":{
            "completo":"Rua Teixeira Franco",
            "nome":"Ramos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Engenheiro Mario Carvalho",
            "nome":"Vicente de Carvalho"
         }
      },
      {
         "attributes":{
            "completo":"Praça Oliveira Campos",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"Rua Couro de Chapéu",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Monte Amor Sagrado - PAL 40109",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua das Turmalinas",
            "nome":"Rocha Miranda"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Dom Helder Camara",
            "nome":"Cascadura"
         }
      },
      {
         "attributes":{
            "completo":"Rua Maestro Henrique Vogeler",
            "nome":"Braz de Pina"
         }
      },
      {
         "attributes":{
            "completo":"Rua Capitão Barbosa",
            "nome":"Cocotá"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 303032",
            "nome":"Inhoaíba"
         }
      },
      {
         "attributes":{
            "completo":"Rua Letícia",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada da Matriz",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Manuel Júlio",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua São João Gualberto",
            "nome":"Vila da Penha"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 333963",
            "nome":"Alto da Boa Vista"
         }
      },
      {
         "attributes":{
            "completo":"Rua Jorge Gonçalves de Araujo",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"Rua Jorge Gonçalves de Araujo",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"Rua Cinco",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua Ouro Verde",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":"Colégio"
         }
      },
      {
         "attributes":{
            "completo":"Rua Principal",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"Rua Principal",
            "nome":"Jacaré"
         }
      },
      {
         "attributes":{
            "completo":"Rua G",
            "nome":"Estácio"
         }
      },
      {
         "attributes":{
            "completo":"Rua Basílio de Magalhães",
            "nome":"Guadalupe"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 364083",
            "nome":"Vicente de Carvalho"
         }
      },
      {
         "attributes":{
            "completo":"Rua Guanabara",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Maracanã",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Carlos Sampaio Correa",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 406942",
            "nome":"Complexo do Alemão"
         }
      },
      {
         "attributes":{
            "completo":"Avenida das Américas",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Vila Oitenta e Seis",
            "nome":"Maré"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 351809",
            "nome":"Catete"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Andorinha",
            "nome":"Copacabana"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 250589",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Calatea",
            "nome":"Parque Anchieta"
         }
      },
      {
         "attributes":{
            "completo":"Rua Pedro Ivo",
            "nome":"Taquara"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 246025",
            "nome":"Vargem Pequena"
         }
      },
      {
         "attributes":{
            "completo":"Travessa sem nome",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Estrada da Paciência",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Dois",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa do Souza",
            "nome":"Barra de Guaratiba"
         }
      },
      {
         "attributes":{
            "completo":"Rua Cristalina",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 254904",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 252098",
            "nome":"Pedra de Guaratiba"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 368142",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"Ladeira Mendonça",
            "nome":"Santo Cristo"
         }
      },
      {
         "attributes":{
            "completo":"Beco do Aluguel",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 369751",
            "nome":"Braz de Pina"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 258368",
            "nome":"Braz de Pina"
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242925",
            "nome":"Rocha"
         }
      },
      {
         "attributes":{
            "completo":"Rua Padre Januário",
            "nome":"Inhaúma"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Doutor Andre Luiz",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Antonio Manoel de Oliveira",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Rio do Pau",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Praça Bela Cruz",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 231829",
            "nome":"Vaz Lobo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Onze",
            "nome":"Vista Alegre"
         }
      },
      {
         "attributes":{
            "completo":"Rua Antonio Pinto da Mota",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Praça Central do Caju",
            "nome":"Caju"
         }
      },
      {
         "attributes":{
            "completo":"Vila sem nome - CL 464370",
            "nome":"Paciência"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Marechal Fontenele",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 412320",
            "nome":"Cidade de Deus"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242529",
            "nome":"Cachambi"
         }
      },
      {
         "attributes":{
            "completo":"Estrada da Cachamorra",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Projetada Onze PAA 12396/PAL48172",
            "nome":"Anil"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Brasil",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada 4 - PAA 11519 / PAL 44874",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Adolfo Lemos",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada Bougainville",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"Praça Alberto Monteiro Filho",
            "nome":"Jacaré"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Antuérpia de Souza Santos",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 370064",
            "nome":"Bento Ribeiro"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Ipê do Jamelão",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua Dois",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"Rua Augusto",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Jacaré",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Mil novecentos e e noventa e três",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua 3",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"Estrada São Pedro de Alcantara",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"Caminho do Canal",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Praça Domingos Velasco",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 230078",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Florianópolis",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Ladeira Felipe Neri",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365817",
            "nome":"Quintino Bocaiúva"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"Rua Professora Maria Carlota",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 375295",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Luiz Carlos Tourinho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida das Américas",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça dos Salmos",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"Caminho Carioca",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida das Américas",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua A",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua A",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"Vila sem nome - CL 466227",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Licínio Cardoso",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua São Pedro",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"Rua F - PAA 10810/ PAL 42840",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Igara",
            "nome":"Cosmos"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Alfredo Balthazar da Silveira",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 382531",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 341891",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Largo João da Baiana",
            "nome":"Saúde"
         }
      },
      {
         "attributes":{
            "completo":"Beco São Pedro",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"Estrada Boiuna",
            "nome":"Taquara"
         }
      },
      {
         "attributes":{
            "completo":"Estrada da Matriz",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 346403",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Doutor Bernardino",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Vila Trezentos e sessenta e dois",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Rua da Candelária",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365775",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Ladislau Neto",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Almirante Calheiros da Graça",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Jose Atanázio Filho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Osvaldo Neves Sena",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Botelho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Agenor",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365817",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 238980",
            "nome":"Curicica"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Central",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 245753",
            "nome":"Vargem Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 241810",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"Rua Carlos Xavier",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada Professor Brant Hora",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Vila Rejane",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Mario Calderaro",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Brasil",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Santo Antônio",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 249870",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 412627",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 260919",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 240291",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Praça Alegria do Sossego",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"Vila Goiás",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"Rua Barreto Coutinho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Via Dulce",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua Conde de Linhares",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 249474",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Camboatá",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Evaldo Gomes da Paixão",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua do Sítio",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Mendanha",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Conde de São Miguel",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua José Bonifácio",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Avelino Lourenço",
            "nome":"Vila Militar"
         }
      },
      {
         "attributes":{
            "completo":"Rua Josué de Barros",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua São Miguel",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Brasil",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua I - PAA 11063 / PAL 43948",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 254201",
            "nome":"Jardim Botânico"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 253799",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 244269",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 238329",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Magarça",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Floriano Góes",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua A - PAL 30024",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Onagra",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 349522",
            "nome":"Taquara"
         }
      },
      {
         "attributes":{
            "completo":"Rua Dois",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Magarça",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Cinco",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 259648",
            "nome":"Santíssimo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 244624",
            "nome":"Piedade"
         }
      },
      {
         "attributes":{
            "completo":"Rua Azaleias do Outeiro",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247999",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua do Campo Alto",
            "nome":"Cosmos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 236539",
            "nome":"Anil"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 261206",
            "nome":"Santíssimo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 232066",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"Rua Justiniano da Rocha",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 250084",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 238253",
            "nome":"Todos os Santos"
         }
      },
      {
         "attributes":{
            "completo":"Beco do Gomes",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Serra do Sossego",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Pierre",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Beco Onze Irmãos",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Manoel Vieira",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Riacho de Santana",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Três ",
            "nome":"Rocinha"
         }
      },
      {
         "attributes":{
            "completo":"Rua Antônio Muniz Azevedo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida do Bráz de Pina",
            "nome":"Vista Alegre"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 364935",
            "nome":"São Francisco Xavier"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 241547",
            "nome":"Piedade"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 239657",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 417246",
            "nome":"Rio Comprido"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365346",
            "nome":"Tomás Coelho"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Bromélias do Jamelão",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 244269",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Beco sem nome",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua Suely",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 245852",
            "nome":"Vargem Pequena"
         }
      },
      {
         "attributes":{
            "completo":"Rua Pacheco Teles",
            "nome":"Ramos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 366534",
            "nome":"Quintino Bocaiúva"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365866",
            "nome":"Quintino Bocaiúva"
         }
      },
      {
         "attributes":{
            "completo":"Rua Soldado Eugênio da Silva",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 367714",
            "nome":"São Francisco Xavier"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Brasil",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 248898",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Alagoas",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 412320",
            "nome":"Cidade de Deus"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 257212",
            "nome":"Praça Seca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 257212",
            "nome":"Campinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome - CL 468207",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida A",
            "nome":"Campo dos Afonsos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256156",
            "nome":"Inhaúma"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 274589",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Rosário",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua Sete",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 262618",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Vinte Seis",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Campanário",
            "nome":"Braz de Pina"
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Engenho",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 262675",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 250217",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 410001",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem nome - CL 367680",
            "nome":"Catete"
         }
      },
      {
         "attributes":{
            "completo":"Rua Atinau",
            "nome":"Vila Valqueire"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 364968",
            "nome":"São Francisco Xavier"
         }
      },
      {
         "attributes":{
            "completo":"Rua Gastão",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 441428",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 255497",
            "nome":"Maracanã"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 413542",
            "nome":"Cidade de Deus"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 255992",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 241489",
            "nome":"Cachambi"
         }
      },
      {
         "attributes":{
            "completo":"Rua Santa Heloisa",
            "nome":"Jardim Botânico"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 441782",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Rua Salvador",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 338715",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 442798",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Ladeira do Joá",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Avenida das Américas",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 254474",
            "nome":"Copacabana"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 364265",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Pedreiro",
            "nome":"Praça Seca"
         }
      },
      {
         "attributes":{
            "completo":"Vila Candida",
            "nome":"Irajá"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 262519",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 362137",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Jose Higino",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 354498",
            "nome":"Santo Cristo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Dez",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Beco Dona Camila",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 239657",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247320",
            "nome":"Barra de Guaratiba"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 249425",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Luiz Bonfá",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Augusto Jose Ribeiro",
            "nome":"Barra de Guaratiba"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 369835",
            "nome":"Irajá"
         }
      },
      {
         "attributes":{
            "completo":"Rua C",
            "nome":"Tomás Coelho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 338061",
            "nome":"Anil"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 366633",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"Praça Silvinha Teles",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Equimar",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"Rua Manoel Augusto",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 443879",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 362475",
            "nome":"Del Castilho"
         }
      },
      {
         "attributes":{
            "completo":"Beco sem nome",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 237685",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 255851",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 369496",
            "nome":"Irajá"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 402883",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 366369",
            "nome":"Riachuelo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 252221",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua B",
            "nome":"Vila Kosmos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 254888",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 239616",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Pará",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Santo Paulo Provitina",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 237321",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242982",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Rua Leonardo Dantas da Rosa",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 255752",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 241265",
            "nome":"Engenho de Dentro"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 249904",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 366773",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 241299",
            "nome":"Cachambi"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 370460",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247262",
            "nome":"Barra de Guaratiba"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 350777",
            "nome":"Caju"
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Guandu",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":"Vista Alegre"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 230078",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua da Felicidade",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua Matias Aires",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"Rua E",
            "nome":"Tomás Coelho"
         }
      },
      {
         "attributes":{
            "completo":"Rua 1",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"Rua Alegrete",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Olímpia",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Caju"
         }
      },
      {
         "attributes":{
            "completo":"PAL 16810",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 265926",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua Palhaço Arrelia",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"Rua F",
            "nome":"Tomás Coelho"
         }
      },
      {
         "attributes":{
            "completo":"Rua J",
            "nome":"Campo dos Afonsos"
         }
      },
      {
         "attributes":{
            "completo":"PAL 3002",
            "nome":"Recreio dos Bandeirantes"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 243477",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"Rua Atilio da Silva Pinto",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"Praça da Fé",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 258152",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Estrada dos Três Rios",
            "nome":"Freguesia (Jacarepaguá)"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Ministro Ivan Lins",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Dois",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242719",
            "nome":"São Francisco Xavier"
         }
      },
      {
         "attributes":{
            "completo":"Rua G",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256016",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"Rua  F PAA 12234/PAL 47554",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 364745",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 364935",
            "nome":"São Francisco Xavier"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Brasil",
            "nome":"Bonsucesso"
         }
      },
      {
         "attributes":{
            "completo":"Rua Antonio Caetano",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Cesário de Melo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Mestre Heckel de Assis",
            "nome":"Vila Militar"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Mestre Heckel de Assis",
            "nome":"Deodoro"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 257766",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Rua B",
            "nome":"Itanhangá"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 367235",
            "nome":"Botafogo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 237826",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247999",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Santo Antônio",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 254938",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 257337",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 258608",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 363333",
            "nome":"Vicente de Carvalho"
         }
      },
      {
         "attributes":{
            "completo":"Rua Conselheiro da Paz",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256990",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 280180",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua Cinco",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Beco do Mota",
            "nome":"Praça da Bandeira"
         }
      },
      {
         "attributes":{
            "completo":"Beco Salvador Santrana",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Beco da Creche",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 345538",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 413617",
            "nome":"Cidade de Deus"
         }
      },
      {
         "attributes":{
            "completo":"Praça do Aleijadinho",
            "nome":"Itanhangá"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 368316",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 370387",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Praça Cícero Peregrino",
            "nome":"Méier"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 243816",
            "nome":"Rio Comprido"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 232652",
            "nome":"Pechincha"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 245712",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 238931",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247999",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Monte Castelo",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 361626",
            "nome":"Maré"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Clemente",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 444422",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 349548",
            "nome":"Taquara"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242859",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 250480",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Caminho da Grama",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 280107",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 232413",
            "nome":"Praça Seca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 341065",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 341065",
            "nome":"Gamboa"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 254425",
            "nome":"Botafogo"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Dona Maria",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242156",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 366765",
            "nome":"Bento Ribeiro"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 310649",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Porangaba",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365817",
            "nome":"Quintino Bocaiúva"
         }
      },
      {
         "attributes":{
            "completo":"Rua Rejane Paula de Melo",
            "nome":"Santíssimo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 246561",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Nelson Cesar de Mattos",
            "nome":"Vicente de Carvalho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256610",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua Joaquim de Queiroz",
            "nome":"Complexo do Alemão"
         }
      },
      {
         "attributes":{
            "completo":"Rua Rafael Texeira Osório",
            "nome":"Bento Ribeiro"
         }
      },
      {
         "attributes":{
            "completo":"Vila Claudionor Jordão",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"Rua Leny Eversong",
            "nome":"Taquara"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247999",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Gutemberg de Castro",
            "nome":"Recreio dos Bandeirantes"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 237602",
            "nome":"Méier"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 370411",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256537",
            "nome":"Penha"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 431759",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"Rua Rio do Pau - P 1963",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua Damião dos Santos",
            "nome":"Vila Militar"
         }
      },
      {
         "attributes":{
            "completo":"Vila Rica",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 364992",
            "nome":"Rocha"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Kindia",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Pedro Teixeira",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 410159",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua da Conceição",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Servidão",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Rua B",
            "nome":"Vargem Pequena"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 249185",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 254490",
            "nome":"Laranjeiras"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 245621",
            "nome":"Recreio dos Bandeirantes"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 264929",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 266072",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 241273",
            "nome":"Cachambi"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Doze",
            "nome":"Freguesia (Jacarepaguá)"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 364265",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem nome - CL 368738",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 265868",
            "nome":"Bento Ribeiro"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 430629",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"Rua Nove",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 266056",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 367243",
            "nome":"Botafogo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242594",
            "nome":"Cachambi"
         }
      },
      {
         "attributes":{
            "completo":"Rua Miguel Fernandes",
            "nome":"Méier"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Santa Luzia",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Santa Luzia",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"Rua Belacap",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Estrada Porto Nacional",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"Rua Manoel Mendonça",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Vega",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada 16 PAA 11015",
            "nome":"Recreio dos Bandeirantes"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 410837",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"Vila Argentina",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 294280",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 262840",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 371211",
            "nome":"São Conrado"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 241109",
            "nome":"Cachambi"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Carneiro",
            "nome":"Estácio"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 367854",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Martins Afonso",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua L",
            "nome":"Campo dos Afonsos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 243493",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365460",
            "nome":"Tomás Coelho"
         }
      },
      {
         "attributes":{
            "completo":"Rua da Alegria",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256883",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365239",
            "nome":"Piedade"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 412296",
            "nome":"Cidade de Deus"
         }
      },
      {
         "attributes":{
            "completo":"Rua Professor Luis Rondelli",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua Bento Gonçalves",
            "nome":"Engenho de Dentro"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365031",
            "nome":"Rocha"
         }
      },
      {
         "attributes":{
            "completo":"Rua Três - 3",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 250415",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256404",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 336362",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Santa Laura",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 237388",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 273763",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 286229",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 368175",
            "nome":"Ramos"
         }
      },
      {
         "attributes":{
            "completo":"Beco 25 de Agosto",
            "nome":"Maré"
         }
      },
      {
         "attributes":{
            "completo":"Rua Feliciano Pena",
            "nome":"Vila da Penha"
         }
      },
      {
         "attributes":{
            "completo":"Rua Coronel Alencastro",
            "nome":"Bento Ribeiro"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 241992",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 426676",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 366625",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 257345",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua José Alves Linhares",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Monteiro",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua C",
            "nome":"Tanque"
         }
      },
      {
         "attributes":{
            "completo":"Rua  Julio Cesar Cardoso de Brito",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247999",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":"Vista Alegre"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 366021",
            "nome":"Quintino Bocaiúva"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256909",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"Rua Graciette Matarazzo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 368134",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 236554",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem nome - CL 368373",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Estrada General Canrobert da Costa",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":"Jardim Sulacap"
         }
      },
      {
         "attributes":{
            "completo":"Rua Jose dos Reis",
            "nome":"Engenho de Dentro"
         }
      },
      {
         "attributes":{
            "completo":"Caminho do Canal",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Martinho da Vila",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 257311",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 257311",
            "nome":"Campinho"
         }
      },
      {
         "attributes":{
            "completo":"Largo do Catumbi",
            "nome":"Catumbi"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome - CL 450775",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"Rua D",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 266189",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua da Alegria",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Quatro",
            "nome":"Vista Alegre"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Brasil",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Hidrolândia",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Xavier d´Araújo",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"Rua Avelino Lourenço",
            "nome":"Vila Militar"
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Praça Nova Jersey",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 260919",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 368142",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"Vila da Paz",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"Beco B1",
            "nome":"Cidade de Deus"
         }
      },
      {
         "attributes":{
            "completo":"Rua Sargento Aquino",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 304410",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 336743",
            "nome":"Itanhangá"
         }
      },
      {
         "attributes":{
            "completo":"Rua Divino Salvador",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Ladeira São Januário",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242610",
            "nome":"Maracanã"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 255240",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 241489",
            "nome":"Cachambi"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome - CL 450759",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 431452",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 368654",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 368506",
            "nome":"Quintino Bocaiúva"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 240135",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada A PAA 12559/PAL 49018",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida João XXIII",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 237826",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365882",
            "nome":"Quintino Bocaiúva"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 233858",
            "nome":"Tanque"
         }
      },
      {
         "attributes":{
            "completo":"Rua Um - 1",
            "nome":"Magalhães Bastos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Basileia",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Acari",
            "nome":"Inhaúma"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 237784",
            "nome":"Jardim Sulacap"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 367102",
            "nome":"São Conrado"
         }
      },
      {
         "attributes":{
            "completo":"Rua Paço do Lumiar",
            "nome":"Pechincha"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Comerciária",
            "nome":"Ramos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Piedade",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247320",
            "nome":"Barra de Guaratiba"
         }
      },
      {
         "attributes":{
            "completo":"Rua Marcílio Dias",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 441410",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 244798",
            "nome":"Encantado"
         }
      },
      {
         "attributes":{
            "completo":"Rua B",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"Rua Rio do Pau - P 2001",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 244442",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 364885",
            "nome":"Riachuelo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Amoreiras",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Imbituba",
            "nome":"Vila Valqueire"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247999",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Malibu",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Dois",
            "nome":"Turiaçu"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 442798",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Escadaria da Independência",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua 31",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 265926",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 254441",
            "nome":"Gávea"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 254441",
            "nome":"Jardim Botânico"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242941",
            "nome":"Maracanã"
         }
      },
      {
         "attributes":{
            "completo":"Praça Getúlio Vargas",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"Rua Natal",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 257154",
            "nome":"Praça Seca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 230078",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Teixeira Soares",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 369272",
            "nome":"Vaz Lobo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247999",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 232579",
            "nome":"Pechincha"
         }
      },
      {
         "attributes":{
            "completo":"Largo das Mães",
            "nome":"Vila Valqueire"
         }
      },
      {
         "attributes":{
            "completo":"Rua L",
            "nome":"Campo dos Afonsos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 260802",
            "nome":"Santíssimo"
         }
      },
      {
         "attributes":{
            "completo":"Ladeira Gusmão",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"Rua da Coruja",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome - CL 367409",
            "nome":"Praça da Bandeira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247718",
            "nome":"Cosmos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Aruti",
            "nome":"Praça Seca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada 16 PAA 11015",
            "nome":"Recreio dos Bandeirantes"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 367425",
            "nome":"Praça da Bandeira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247999",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 260919",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Dezoito de Outubro",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 239905",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Fortaleza",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 374884",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Dois",
            "nome":"Piedade"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 411181",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 359604",
            "nome":"Acari"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 254870",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua José Amorim Machado do Parque União",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 237313",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"Beco sem nome",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"Estrada Capitão Pedro Afonso",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua B - PAA 11801 / PAL 45783",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Beco Terreirinho",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 367821",
            "nome":"São Francisco Xavier"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 411413",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Oito",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua Apora",
            "nome":"Inhaúma"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 238410",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Rio do Pau - P 2001",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Maragogipe",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"Ladeira do Joá",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 433508",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"Rua J",
            "nome":"Campo dos Afonsos"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Lucas Soares Filho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365023",
            "nome":"Riachuelo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365411",
            "nome":"Tomás Coelho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365965",
            "nome":"Quintino Bocaiúva"
         }
      },
      {
         "attributes":{
            "completo":"Avenida de Santa Cruz",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Brasil",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256016",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 254060",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Caminho do Cabuís",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Oito",
            "nome":"Vista Alegre"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 245043",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 258608",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Monte Horebe",
            "nome":"Inhoaíba"
         }
      },
      {
         "attributes":{
            "completo":"Rua Mil novecentos e e noventa e três",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua Curitiba",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"Rua Jaqueira",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 237669",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 266072",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua Dois",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 366773",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 345538",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"Rua Central",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"Rua Tancredo Martins Costa",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Beco dos Carneiros",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida João XXIII",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua A - PAA 10508/ PAL 40983",
            "nome":"Curicica"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 381897",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 381897",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 244020",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua J",
            "nome":"Campo dos Afonsos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 332593",
            "nome":"Praça Seca"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Alice",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242768",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 248658",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Guaiacá",
            "nome":"Padre Miguel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 235358",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Graciette Matarazzo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Francisco Flávio",
            "nome":"Vila Militar"
         }
      },
      {
         "attributes":{
            "completo":"Rua Palmaz",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 243410",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 413476",
            "nome":"Cidade de Deus"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 251579",
            "nome":"Barra de Guaratiba"
         }
      },
      {
         "attributes":{
            "completo":"Rua Várzea Paulista",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 291468",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Beco Cosme e Damião",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 410720",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256537",
            "nome":"Penha"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome - CL 456491",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 413377",
            "nome":"Cidade de Deus"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 369140",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Eufrásio",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Eufrásio",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Antuérpia de Souza Santos",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua Coronel Alencastro",
            "nome":"Bento Ribeiro"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 243477",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 243477",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 255000",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Vila Amazonas",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 367805",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 338590",
            "nome":"Inhaúma"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242859",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"Avenida João XXIII",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Rafael Texeira Osório",
            "nome":"Bento Ribeiro"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 258111",
            "nome":"Campinho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 258046",
            "nome":"Engenho da Rainha"
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Mato Alto",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 244830",
            "nome":"Piedade"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 257659",
            "nome":"Tanque"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247999",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365155",
            "nome":"Vila Kosmos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Dois",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua Quatro",
            "nome":"Turiaçu"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256081",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Upatininga",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Mestre Francisco Sombra",
            "nome":"Vila Militar"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Mestre Francisco Sombra",
            "nome":"Deodoro"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365338",
            "nome":"Tomás Coelho"
         }
      },
      {
         "attributes":{
            "completo":"Rua São João",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"Praça Professor Pecegueiro",
            "nome":"Gardênia Azul"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 411462",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Marechal Fontenele",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 370528",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua D",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 442624",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Rua Graciette Matarazzo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua São Bento",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua da Candelária",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome - CL 368696",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua J. Marques Jurandir",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256321",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua Nossa Senhora das Graças",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua Francisco Eugênio",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":"Bento Ribeiro"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 331603",
            "nome":"Campinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 368142",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 263632",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256644",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua Três - 3",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua Quatro",
            "nome":"Vista Alegre"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Flor-de-Lis do Jamelão",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 257170",
            "nome":"Quintino Bocaiúva"
         }
      },
      {
         "attributes":{
            "completo":"Travessa das Pranchas",
            "nome":"Paciência"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Antuérpia de Souza Santos",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua Mendes de Aguiar",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Projetada Sete PAA 12396/PAL48172",
            "nome":"Anil"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 354621",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Gilka Machado",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Moacyr Barbosa Soares",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Ribeira do Pombal",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256156",
            "nome":"Inhaúma"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 243162",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Praça Marilena Villas Boas Pinto",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Vila sem nome - CL 466433",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua Monsenhor Távola",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua General Magalhães Barata",
            "nome":"Jardim América"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"Rua São José",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua União",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 338715",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Canal 2 PAA 6172/PAL 18529",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Jurupari",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Aurino Gomes",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 366641",
            "nome":"Engenheiro Leal"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Santo Paulo Provitina",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sebastião Delfino Junior",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Alice",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 254953",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Umbuzeiro",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 262220",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 410779",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 382531",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 352393",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem nome - CL 409565",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Vila Luzimar",
            "nome":"Engenho de Dentro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Abib Selem",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 434936",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Albertino",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Darci Vargas do Parque União",
            "nome":"Maré"
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":"Vista Alegre"
         }
      },
      {
         "attributes":{
            "completo":"Rua da Jaguatirica",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Sargento Aquino",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"Rua Almino Afonso Senad",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 338798",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"Travessa sem nome",
            "nome":"Engenho de Dentro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Paz de Siqueira",
            "nome":"Jacaré"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Quatrocentos e oitenta",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Rua Lotus",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Quarenta e um",
            "nome":"Sepetiba"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242917",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 370346",
            "nome":"Bento Ribeiro"
         }
      },
      {
         "attributes":{
            "completo":"Praça São Constâncio",
            "nome":"Irajá"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Lonrado",
            "nome":"Cordovil"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 367268",
            "nome":"Catete"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 366088",
            "nome":"Inhaúma"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 354621",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"Rua F - PAA 11801 / PAL 45783",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Capitão Valentim",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Vila Pureza",
            "nome":"Irajá"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome - CL 466839",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Escadaria sem nome",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365627",
            "nome":"Água Santa"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365049",
            "nome":"Rocha"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 332171",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256529",
            "nome":"Vaz Lobo"
         }
      },
      {
         "attributes":{
            "completo":"Rua D",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Beco José Maria",
            "nome":"Inhaúma"
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome - CL 462390",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247999",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":"Braz de Pina"
         }
      },
      {
         "attributes":{
            "completo":"Estrada dos Bandeirantes",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 273839",
            "nome":"Engenho da Rainha"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 257394",
            "nome":"Vaz Lobo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Graciette Matarazzo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua General Belegarde",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Xavier d´Araújo",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Governo",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"Rua D",
            "nome":"Bento Ribeiro"
         }
      },
      {
         "attributes":{
            "completo":"Ladeira Estrela de Ouro",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Vila Claudionor Jordão",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 254433",
            "nome":"Botafogo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 369785",
            "nome":"Irajá"
         }
      },
      {
         "attributes":{
            "completo":"Rua Dois",
            "nome":"Praça Seca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 369199",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Monteiro Lobato",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"Vila Pedro Floresta",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 336115",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 238782",
            "nome":"Água Santa"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 254425",
            "nome":"Botafogo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Eutiquio Soledade",
            "nome":"Tauá"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 252098",
            "nome":"Pedra de Guaratiba"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256677",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"Rua Olegarinha",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Piaí",
            "nome":"Sepetiba"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 253211",
            "nome":"Inhoaíba"
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem nome - CL 367649",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 258095",
            "nome":"Campinho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 276147",
            "nome":"Irajá"
         }
      },
      {
         "attributes":{
            "completo":"Rua da Liberdade",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Carlos Lacerda",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Luiz Beltrão",
            "nome":"Vila Valqueire"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 366427",
            "nome":"Riachuelo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Graciette Matarazzo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 230110",
            "nome":"Ramos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 367235",
            "nome":"Botafogo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 255208",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Estrada Japoré",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça das Papoulas",
            "nome":"Vila Valqueire"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242743",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242743",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"Rua Rocha Pombo",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua Aritiba",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 446104",
            "nome":"Rocinha"
         }
      },
      {
         "attributes":{
            "completo":"Rua Capitão Barbosa",
            "nome":"Cocotá"
         }
      },
      {
         "attributes":{
            "completo":"Rua Capitão Barbosa",
            "nome":"Praia da Bandeira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 260919",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 370098",
            "nome":"Bento Ribeiro"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 254300",
            "nome":"Jardim Botânico"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 279307",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua B - PAA 11801 / PAL 45783",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Travessa dos Cajueiros",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Praça Antonio Goulart",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Carlos Passos Taveira",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua C",
            "nome":"Tanque"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365650",
            "nome":"Água Santa"
         }
      },
      {
         "attributes":{
            "completo":"Rua Baependi",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 367185",
            "nome":"Botafogo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Camargo Freire",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Travessa M. C. Euzébio",
            "nome":"Vila Militar"
         }
      },
      {
         "attributes":{
            "completo":"Travessa M. C. Euzébio",
            "nome":"Deodoro"
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":"Pedra de Guaratiba"
         }
      },
      {
         "attributes":{
            "completo":"Rua B",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 366658",
            "nome":"Engenheiro Leal"
         }
      },
      {
         "attributes":{
            "completo":"Rua União",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 305102",
            "nome":"Jardim Sulacap"
         }
      },
      {
         "attributes":{
            "completo":"Rua Araujo Leitão 925",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 241711",
            "nome":"Cachambi"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 241711",
            "nome":"Maria da Graça"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 280768",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 368530",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Frederico Faulhaber",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua da Horta ",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Bromélias do Jamelão",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 257485",
            "nome":"Encantado"
         }
      },
      {
         "attributes":{
            "completo":"Rua Nacional",
            "nome":"Taquara"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 240887",
            "nome":"Cachambi"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Bromélias do Jamelão",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Cesário de Melo",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 262790",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 413690",
            "nome":"Cidade de Deus"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 420141",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 262808",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 370098",
            "nome":"Bento Ribeiro"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 265850",
            "nome":"Bento Ribeiro"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Cesário de Melo",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Beco da Fontinha",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Castor de Andrade",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Alice",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 241927",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 249250",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 258103",
            "nome":"Campinho"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Padre Guilherme Decaminada",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 366278",
            "nome":"Riachuelo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365817",
            "nome":"Quintino Bocaiúva"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 369157",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 335620",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"Estrada Rio-São Paulo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sem Nome - CL 368704",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 413542",
            "nome":"Cidade de Deus"
         }
      },
      {
         "attributes":{
            "completo":"Rua Arlindo Lucio da Silva",
            "nome":"Deodoro"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 368142",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"Rua Iriquitia",
            "nome":"Taquara"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Cartagena",
            "nome":"Vila Kennedy"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 366864",
            "nome":"Bento Ribeiro"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 246173",
            "nome":"Vargem Pequena"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 258608",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Monte Castelo",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 257709",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 441410",
            "nome":"São Francisco Xavier"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 441410",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Rua Jorge Cesário",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Rua Quatro mil setecentos e seis H",
            "nome":"Tomás Coelho"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Carlos Lacerda",
            "nome":"Pilares"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Carlos Lacerda",
            "nome":"Abolição"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Carlos Lacerda",
            "nome":"Encantado"
         }
      },
      {
         "attributes":{
            "completo":"Avenida João XXIII",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 359554",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 433946",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"Rua Ayrton Senna",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Ladeira Trezentos e noventa e dois",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256875",
            "nome":"Engenho de Dentro"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 369561",
            "nome":"Irajá"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 255216",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Estrada Adhemar Bebiano",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 366112",
            "nome":"Engenho da Rainha"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 255752",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"Rua Conselheiro da Paz",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome - CL 457853",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256933",
            "nome":"Campinho"
         }
      },
      {
         "attributes":{
            "completo":"Estrada da Água Branca",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"Dois",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 237362",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"Travessa B",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 249342",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256487",
            "nome":"Del Castilho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365528",
            "nome":"Engenho da Rainha"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 411785",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua José da Fonseca",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Cinco",
            "nome":"Engenho da Rainha"
         }
      },
      {
         "attributes":{
            "completo":"Rua 1",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"Rua 1",
            "nome":"Caju"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Conselheiro da Paz",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 442913",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 254458",
            "nome":"Jardim Botânico"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 250035",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Travessa das Pranchas",
            "nome":"Paciência"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Mauro Santos",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 411330",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 245829",
            "nome":"Vargem Pequena"
         }
      },
      {
         "attributes":{
            "completo":"Estrada Vitor Dumas",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa João de Barro do Jamelão",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua Pedro Osório",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 410787",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 244459",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 298836",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 411843",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Mangara",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"Rua Quatro",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua Visconde de Santa Cruz",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Ucranianos",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Santa Luiza",
            "nome":"Maracanã"
         }
      },
      {
         "attributes":{
            "completo":"Rua União",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Brasil",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365916",
            "nome":"Quintino Bocaiúva"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 255950",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Capitão Valentim",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua General Azeredo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 281402",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 231845",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Ney Palmeiro",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 420414",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 315176",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua Pereira de Araujo",
            "nome":"Irajá"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Duque de Caxias",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Genival Londres",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa A",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 241893",
            "nome":"Engenho de Dentro"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Jose Paixão",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 315176",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 336065",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua 5",
            "nome":"Caju"
         }
      },
      {
         "attributes":{
            "completo":"Rua Santa Filomena",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 260919",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 430306",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"Rua Oitenta e três",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Belacap",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Ladeira Antônio",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 412262",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Praça Engenheiro Bernardo Saião",
            "nome":"Botafogo"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Brasil",
            "nome":"Maré"
         }
      },
      {
         "attributes":{
            "completo":"Rua Odilon Martins de Andrade",
            "nome":"Recreio dos Bandeirantes"
         }
      },
      {
         "attributes":{
            "completo":"Rua Toscana",
            "nome":"Ricardo de Albuquerque"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 244434",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 246561",
            "nome":"Cosmos"
         }
      },
      {
         "attributes":{
            "completo":"Rua São Gabriel",
            "nome":"Maria da Graça"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 409839",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua Ceará",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Gil Gafreé",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 352393",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Vila Minas Gerais",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 434217",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242099",
            "nome":"Piedade"
         }
      },
      {
         "attributes":{
            "completo":"Rua Matarazzo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada Urucânia",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 430041",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"Rua Celia Ribeiro da Silva Mendes",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Beco Isabel",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 381806",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"Avenida de Santa Cruz",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 426668",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"Vila Argentina",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Bom Pastor",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Doutor Paulo",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"Rua Salvador",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"Rua Telégrafo",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 441410",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 246561",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 257691",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Vieira Fazenda",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua São Luiz",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 263855",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 355925",
            "nome":"Barros Filho"
         }
      },
      {
         "attributes":{
            "completo":"Beco da Rua Silva Rego 79 fundos",
            "nome":"Jacaré"
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada B - PAL 48428/PAA 12440",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua da Paz",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 248658",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 255711",
            "nome":"Praça da Bandeira"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Alfredo Albuquerque",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Espírito da Paz",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Miranda",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"Praça João Carlos Vital",
            "nome":"Vargem Pequena"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 442863",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Duque de Caxias",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Sampaio",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 253997",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 260919",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Marechal Henrique Lott",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Central",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"Rua Acau",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 250027",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Antonio Goulart",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Vitor Meireles",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Alfredo Albuquerque",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Outeiro Santo",
            "nome":"Taquara"
         }
      },
      {
         "attributes":{
            "completo":"Avenida João XXIII",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 295543",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Rafael Texeira Osório",
            "nome":"Bento Ribeiro"
         }
      },
      {
         "attributes":{
            "completo":"Praça José Luiz Nunes",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada Mariana",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 259697",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Guaiacá",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 244442",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Barro Vermelho",
            "nome":"Rocha Miranda"
         }
      },
      {
         "attributes":{
            "completo":"Via Alan",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"Rua Gomensoro",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Albertino",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 254912",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Jardim do Seridó",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242453",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Rio",
            "nome":"Cachambi"
         }
      },
      {
         "attributes":{
            "completo":"Rua Passa Um",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 433581",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 330829",
            "nome":"Taquara"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 243451",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"Estrada Aterrado do Leme",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Leandro Martins",
            "nome":"Centro"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247999",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Otimismo",
            "nome":"Caju"
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 412023",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 231779",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Ana Lima",
            "nome":"Irajá"
         }
      },
      {
         "attributes":{
            "completo":"Travessa sem nome",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Sebastião de Oliveira",
            "nome":"Sepetiba"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 411967",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Praça do Cruzeiro",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 244442",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Beco 13",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua Arealva",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 369033",
            "nome":"Campinho"
         }
      },
      {
         "attributes":{
            "completo":"Beco João Alberto",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 433433",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"Avenida João XXIII",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Brasil",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Cantão",
            "nome":"Botafogo"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Canal",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 409979",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 411785",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 412072",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Estrada das Furnas",
            "nome":"Itanhangá"
         }
      },
      {
         "attributes":{
            "completo":"Travessa da Chácara",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada B - PAL 48428/PAA 12440",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Vitória",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"Rua Luiz Carlos Tourinho",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua da Tabua",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Estrada Bougainville",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Beco da Creche",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Brasil",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada 8 - PAA 11519 / PAL 44874",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 257790",
            "nome":"Engenho de Dentro"
         }
      },
      {
         "attributes":{
            "completo":"Caminho dos Fernandes",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Dois",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Doutor Paulo",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Rio Joana",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua São Luiz",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Piedade",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Manoel Rodrigues",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Estrada Cancela Preta",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242867",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Fátima",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247999",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Amaral",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Alagoas",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Cafundá",
            "nome":"Tanque"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Brasil",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 262055",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Cadete Polonia",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Seis",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Campinho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 253807",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"Rua da União",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"Rua Roberto Dantas",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Campinho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Beira Rio",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 260273",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 253997",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 431627",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 231845",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 356741",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua 31",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Praça Beira Rio",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua Clarimundo de Melo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365783",
            "nome":"Quintino Bocaiúva"
         }
      },
      {
         "attributes":{
            "completo":"Rua Letícia",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Carlos Lacerda",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Andre Cavalcanti",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua do Magistrado",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Pastor Martin Luther King Jr.",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 368852",
            "nome":"Campinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua E",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Nova Alvorada",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Beco Sargento Davi",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua 1",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"Beco do Limão",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"Estrada da Base Aérea",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Guapi",
            "nome":"Santo Cristo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Quatorze de Junho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 255752",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Antares",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Boulevard Vinte e oito de Setembro",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 266098",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Beco das Árvores",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua do Barco",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Cesário de Melo",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua Seritinga",
            "nome":"Braz de Pina"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 432351",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Guandu",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Esperança",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 435552",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"Praça José Gonzales",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"Rua Amaral",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Manaus",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"Rua Casa Nova",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa São José",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"Rua Lotério Mury",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Barão de Cotegipe",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Shalon",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Quinze de Agosto",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Carlos Sampaio Correa",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 369090",
            "nome":"Campinho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 246702",
            "nome":"Cosmos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 241083",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 444315",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Praça Lauro Corona",
            "nome":"Jardim Guanabara"
         }
      },
      {
         "attributes":{
            "completo":"Praça Professor Cardoso Fontes",
            "nome":"Vila Valqueire"
         }
      },
      {
         "attributes":{
            "completo":"Praça Professor Cardoso Fontes",
            "nome":"Marechal Hermes"
         }
      },
      {
         "attributes":{
            "completo":"Praça Raul Sendic Antonaccio",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Brasil",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 311860",
            "nome":"Santíssimo"
         }
      },
      {
         "attributes":{
            "completo":"Praça Benjamim Coelho da Costa",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Largo Pedro Passos",
            "nome":"Taquara"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Evaldo Gomes da Paixão",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 336743",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 260919",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Alagoas",
            "nome":"Praça da Bandeira"
         }
      },
      {
         "attributes":{
            "completo":"Rua Nestor",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Nova Jersey",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Nossa Senhora das Graças",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Vila Princesa",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Curitiba",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 260620",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Mandinga",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Padre Lino",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"Travessa do Matadouro",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 375717",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"Largo do Rio Grande",
            "nome":"Taquara"
         }
      },
      {
         "attributes":{
            "completo":"Rua Araticum",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Dez",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome - CL 470872",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Haroldo Teixeira Valladão",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 432153",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"Acesso da Rua Arará",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"Servidão sem nome - CL 457150",
            "nome":"Sepetiba"
         }
      },
      {
         "attributes":{
            "completo":"Rua Vitória",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 260620",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Cesário de Melo",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247999",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 260000",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Duque de Caxias",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247999",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Cosmos",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Arquiteto Henrique Mindlin",
            "nome":"Barra da Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 257345",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua Vitória",
            "nome":"Caju"
         }
      },
      {
         "attributes":{
            "completo":"Rua Pelópidas Passamani",
            "nome":"Guadalupe"
         }
      },
      {
         "attributes":{
            "completo":"Rua Damião dos Santos",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida das Américas",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada da Cachamorra",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Beco Cafundá",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 427591",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"Rua Marquês de Herval",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua Andre Rocha",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Beco do Amorim",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 444711",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Rua Senegal",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 410571",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 409748",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua da Pedreira",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 434191",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"Rua Soldado Felisbino dos Santos",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida das Américas",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Dom Helder Camara",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242966",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Estrada dos Sete Riachos",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 442863",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 237297",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"Praça Cabo João Machado",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Rua Lotério Mury",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Campo da Radiobrás",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 338822",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Armando Ribeiro",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Embaixador Abelardo Bueno",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Manoel Caldeira de Alvarenga",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua A ",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Ayrton Senna",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada dos Bandeirantes",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Couto de Magalhães",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida das Américas",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 260752",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 240945",
            "nome":"Cachambi"
         }
      },
      {
         "attributes":{
            "completo":"Estrada Marechal Alencastro",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Cunhataí",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua do Sítio",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Antares",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua São Luiz ",
            "nome":"Complexo do Alemão"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Governo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 239467",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Viaduto Procurador José Alves de Moraes",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Vila África",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247320",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 273847",
            "nome":"Engenho da Rainha"
         }
      },
      {
         "attributes":{
            "completo":"Estrada da Cachamorra",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 260299",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Projetada E",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida Marechal Henrique Lott",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua J",
            "nome":"Campo dos Afonsos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Domélia",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Peraúba",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Estrada Rio-São Paulo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 232439",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Artur Vargas",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Cantagalo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Largo Capitão Couto",
            "nome":"Quintino Bocaiúva"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Geremário Dantas",
            "nome":"Freguesia (Jacarepaguá)"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Alfredo Balthazar da Silveira",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 369025",
            "nome":"Campinho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256800",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"Avenida João XXIII",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua B - PAA 11467/ PAL 44778",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Senhor do Bonfim",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 236612",
            "nome":"Méier"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 369074",
            "nome":"Campinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua Jacareí",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Baldraco",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Magarça",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Luiza Barata",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Zilda Arns Neumann",
            "nome":"Vargem Pequena"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Cesário de Melo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Treze ",
            "nome":"Rocinha"
         }
      },
      {
         "attributes":{
            "completo":"Rua Padre Manuel da Nobrega",
            "nome":"Cascadura"
         }
      },
      {
         "attributes":{
            "completo":"Praça do Cruzeiro",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Avenida das Américas",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Pinto de Campos",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Marechal Falcão da Frota",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Soter de Araujo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua A",
            "nome":"Vargem Pequena"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 260703",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Humaitá",
            "nome":"Humaitá"
         }
      },
      {
         "attributes":{
            "completo":"Rua Elizeth Cardoso",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 250027",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Amaral",
            "nome":"Manguinhos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 427641",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 432534",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Cabuçu",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida das Américas",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Engenho de Dentro"
         }
      },
      {
         "attributes":{
            "completo":"Rua São José",
            "nome":"Complexo do Alemão"
         }
      },
      {
         "attributes":{
            "completo":"Beco sem nome",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Alice",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Praça Jornal do Comércio",
            "nome":"Gamboa"
         }
      },
      {
         "attributes":{
            "completo":"Praça Jornal do Comércio",
            "nome":"Saúde"
         }
      },
      {
         "attributes":{
            "completo":"Estrada Capitão Pedro Afonso",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua São Geraldo da Praia de Ramos",
            "nome":"Maré"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242123",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 242123",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Rua Andrade Santos",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Canoa Quebrada Bela VIsta",
            "nome":"Paciência"
         }
      },
      {
         "attributes":{
            "completo":"Rua Miguel de Carvalho",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Dario Rogerio",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"Estrada da Posse",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida das Américas",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 381202",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 444075",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 250027",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Beco 211",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Beco 211",
            "nome":"Cachambi"
         }
      },
      {
         "attributes":{
            "completo":"Rua Paulo de Carvalho Barbosa",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua 1",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 247320",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 259804",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Ana Paula Ribeiro",
            "nome":"Freguesia (Ilha)"
         }
      },
      {
         "attributes":{
            "completo":"Praça Miami",
            "nome":"Vila Kennedy"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Cabral",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Olimpia Portugal",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Sítio Três",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Agenor",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Sete de Setembro",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Sete de Setembro",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 245407",
            "nome":"Vargem Pequena"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Gravador",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 348102",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Caju"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 432302",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 345538",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"Rua Espiv",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 255463",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"Rua Ayrton Senna",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Beco João Alberto",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 430710",
            "nome":"Imperial de São Cristóvão"
         }
      },
      {
         "attributes":{
            "completo":"Travessa H",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Vasco da Gama"
         }
      },
      {
         "attributes":{
            "completo":"Praça Gonçalo Jacome",
            "nome":"Senador Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 367755",
            "nome":"Sampaio"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 356733",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Vila Pedro Floresta",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Diamantes do Andaraí",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Avenida das Américas",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 256826",
            "nome":"Madureira"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua Itagiba",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada do Mendanha",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada da Cachamorra",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Florenca",
            "nome":"Ricardo de Albuquerque"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 412064",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Rua Mario Gibson Barbosa - PAL 19518",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Escadaria sem nome",
            "nome":"Jacarepaguá"
         }
      },
      {
         "attributes":{
            "completo":"Escadaria sem nome",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Rua da Horta ",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 410548",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"Caminho dos Santos Rodrigues",
            "nome":"Rio Comprido"
         }
      },
      {
         "attributes":{
            "completo":"Rua Santa Filomena",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Rua Principal",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Andaraí"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Quatrocentos e oitenta",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Rua XV de Março",
            "nome":"Jacarezinho"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Marechal Rondon",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa São José",
            "nome":"Sepetiba"
         }
      },
      {
         "attributes":{
            "completo":"Rua Doutor José Valadão",
            "nome":"Sepetiba"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Jovem",
            "nome":"Tijuca"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 365833",
            "nome":"Quintino Bocaiúva"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 431536",
            "nome":"Benfica"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 431536",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"Rua Estrela",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"Rua Guilherme Karam",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 257360",
            "nome":"Oswaldo Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Rua Doutor Nunes",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Morro Tardini",
            "nome":"Engenho Novo"
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":"Pedra de Guaratiba"
         }
      },
      {
         "attributes":{
            "completo":"Estrada de Jacarepaguá",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Travessa Henrique Silva",
            "nome":"Caju"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Jupará",
            "nome":"Mangueira"
         }
      },
      {
         "attributes":{
            "completo":"Trevo das Missões",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Sao Miguel",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Via Joao Pequeno",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Estrada da Lama Preta",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Praça Josino Meira Vasconcelos",
            "nome":"Olaria"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome - CL 457689",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Beco Camarão",
            "nome":"Santa Cruz"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Hebridas",
            "nome":"Vila Kennedy"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Sítio",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"Rua Dona Ernestina",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 358721",
            "nome":"Pavuna"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 444422",
            "nome":"Vila Isabel"
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":"Paciência"
         }
      },
      {
         "attributes":{
            "completo":"Travessa Jacaré",
            "nome":"Lins de Vasconcelos"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 410589",
            "nome":"Grajaú"
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 294280",
            "nome":"Campo Grande"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Gláucio Gil",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Praça Cabo Luis Quevedo",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Vila do 106",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"Avenida João XXIII",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 240895",
            "nome":"Engenho de Dentro"
         }
      },
      {
         "attributes":{
            "completo":"Rua do Rio",
            "nome":"Cachambi"
         }
      },
      {
         "attributes":{
            "completo":"Avenida João XXIII",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Avenida das Américas",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Caju"
         }
      },
      {
         "attributes":{
            "completo":"Praça Bernardo Joblonski",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 311357",
            "nome":"Realengo"
         }
      },
      {
         "attributes":{
            "completo":"Avenida Gilka Machado",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 338830",
            "nome":"Bangu"
         }
      },
      {
         "attributes":{
            "completo":"Rua sem nome",
            "nome":"Caju"
         }
      },
      {
         "attributes":{
            "completo":"Estrada da Base Aérea",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"sem nome - CL 333211",
            "nome":None
         }
      },
      {
         "attributes":{
            "completo":"Rua Um",
            "nome":"Pavuna"
         }
      }
   ],
   "exceededTransferLimit":True
}


csv_file = "dados.csv"

# Extrair features
features = json_data.get("features", [])

# Abrir o arquivo CSV para escrita
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["rua", "bairro"])
    
    # Escrever o cabeçalho
    writer.writeheader()
    
    # Escrever as características
    for feature in features:
        attributes = feature.get("attributes", {})
        rua = attributes.get("completo", "")
        nome = attributes.get("nome")
        
        # Verificar se o campo "nome" não é None
        if nome is not None:
            writer.writerow({"rua": rua, "bairro": nome})

print(f'Arquivo CSV "{csv_file}" criado com sucesso.')