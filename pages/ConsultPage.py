from Locators.LocatorsConsult import Locators
from playwright.sync_api import Page, expect
from database.MongoDB import MongoDB
from settings import MAIN_URL

mongodb = MongoDB("robot-download-python") 

class ConsultPage:
  def __init__(self, page: Page):
    self.locators = Locators()
    self.page = page

  def search_google(self, query: str):
    try:
      self.page.goto('https://www.google.com', wait_until="load")

      search_box = self.page.get_by_label("Pesquisar", exact=True)
      search_box.fill(query)
      self.page.keyboard.press("Enter")

      self.page.wait_for_timeout(timeout=800)
      
    except Exception as e:
      mongodb.create({'event': f'Erro ao realizar consulta: {str(e)}', 'error': True})
      return {
        'error': True,
        'message': f'Erro ao realizar consulta: {e}',
        'data': None,
      }
      
    return {
      'error': False,
      'message': None,
      'data': None,
    }
    
    
  def find_download_link(self, main_url: str):
    try:
      hrefs = self.page.locator(self.locators.hrefs_page)

      for element in hrefs.element_handles():

        href = element.get_attribute('href')

        if href and main_url in href:
          return {
            'error': False,
            'message': 'Link de download encontrado.',
            'data': href if "downloads" in href else f"{main_url}downloads",
          }
            
    except Exception as e:
      mongodb.create({'event': f'Erro ao encontrar link de download: {str(e)}', 'error': True})
      return {
        'error': True,
        'message': f'Erro ao realizar consulta: {str(e)}',
        'data': None,
      }
      
    return {
      'error': False,
      'message': None,
      'data': None,
    }
    

  def handle_consultation(self):
    """
    Realiza uma consulta para buscar e acessar o link de download do Python.

    A função faz uma busca no Google, encontra o link de download e, se não for encontrado, registra o erro e interrompe a execução.

    Caso haja qualquer erro durante o processo, o erro é registrado e retornado.

    Returns:
      dict: Um dicionário com informações sobre o sucesso ou falha da consulta.
        - 'error': Indica se ocorreu um erro (True ou False).
        - 'message': Mensagem de erro, se houver.
        - 'data': Nenhum dado adicional é retornado.

    Raises:
      Exception: Caso o link de download não seja encontrado ou outro erro ocorra durante a execução.
    """
    try:
      search = self.search_google("baixar python")
      if search['error']:
        return search
      
      download_link = self.find_download_link(MAIN_URL)
      if download_link['error']:
        return download_link
      
      if not download_link['data']:
        mongodb.create({'event': 'Link de download não encontrado', 'error': True})
        raise Exception("Link de download não encontrado.")

      self.page.goto(download_link['data'], wait_until="load")
        
    except Exception as e:
      mongodb.create({'event': f'Erro ao realizar consulta: {str(e)}', 'error': True})
      return {
        'error': True,
        'message': f'Erro ao realizar consulta: {e}',
        'data': None
      }

    return {
      'error': False,
      'message': None,
      'data': None
    }