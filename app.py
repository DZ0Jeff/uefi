from typing import Container
from utils.setup import setSelenium
from utils.parser_handler import init_crawler
from utils.file_handler import dataToExcel, read_excel_file, save_counter
from requests.exceptions import ConnectionError 


def find_details():
    # profile["name"] = container.find('a').text
    # profile["Cuit"] = container.select_one('div.doc-facets span.linea-cuit-persona span.cuit').text

    # bullet_list = []
    # for bullet in container.find_all('span', class_='bullet'):
    #     bullet_list.append(bullet)

    # print(bullet_list)
    # profile["Pessoa"] = bullet_list[1].next_sibling
    # profile["Lucro"] = bullet_list[2].next_sibling
    # profile["IVA"] = bullet_list[2].next_sibling
    # profile["Empregador"] = bullet_list[3].next_sibling

    # for key, value in profile.items():
    #     print(f"{key}: {value}")
    pass


def main():
    '''
    Insert your code here
    '''
    print('> Iniciando crawler...')
    cuits = read_excel_file('amostra_cuits.xlsx')
    print('> arquivo de entrada lido!')

    print(f'> {len(cuits)} encontrados!')
    for index, cuit in enumerate(cuits):
        print(f'> Extraindo {index + 1} dados...')
        if index >= 818:
            try:
                soap = init_crawler(f'https://www.cuitonline.com/search.php?q={cuit}')
                container = soap.find('div', class_='hit')
                formated_container = str(container.text).replace('•','\n')
                dataToExcel({"Detalhes": [formated_container]}, 'cuits.csv')

                save_counter(index)
            
            except (AttributeError, ConnectionError):
                print('> erro ao pegar dados...')
                continue
    

if __name__ == "__main__":
    main()
