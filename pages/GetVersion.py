from Locators.LocatorsGet import Locators
from utils.utils import verificar_bits
from playwright.sync_api import Page
from database.MongoDB import MongoDB
from settings import MAIN_VERSION
from pathlib import Path
import subprocess

mongodb = MongoDB("robot-download-python")

class VersionFetcher():
  def __init__(self, page: Page):
    self.locator = Locators()
    self.page = page

  def __download(self):
    try:
      version_rows = self.page.locator(self.locator.download_rows)

      for i in range(version_rows.count()):
        model = version_rows.nth(i)
        version_info = model.locator('td').all()
        version = version_info[0]

        if verificar_bits() and "Windows" in version.inner_text():
          href = version.locator('a').get_attribute('href')

          with self.page.expect_download() as download_info:
            self.page.locator(f'a[href="{href}"]').click()            
          
          download = download_info.value

          mongodb.create({'event': 'Download realizado com sucesso', 'error': False})
          return {
            'error': False,
            'message': None,
            'data': download.path()
          }

    except Exception as e:
      mongodb.create({'event': 'Erro ao realizar download', 'error': True})
      return {
        'error': True,
        'message': f'Message: {e}',
        'data': None,
      }
  
  def __install_version(self, download):
    try:
      download_path = Path(download)

      if download_path.exists():
        
        try:
          subprocess.run( 
            [str(download_path), "/quiet", "InstallAllUsers=1", "PrependPath=1"],
            check=True
          )

          mongodb.create({'event': 'Instalação realizada com sucesso', 'error': False})
          return {
            'error': False,
            'message': None ,
            'data': None,
          }

        except subprocess.CalledProcessError as e:
          mongodb.create({'event': 'Erro ao realizar instalação', 'error': True})
          return {
            'error': True,
            'message': 'Error ao realizar instalação',
            'data': None,
          }
        
      else:
        mongodb.create({'event': 'Erro ao localizar caminho do arquivp', 'error': True})
        print("Falha no download do arquivo.")
      
    except Exception as e:
      return {
        'error': True,
        'message': f'Message: {e}',
        'data': None,
      }

    return {
      'error': False,
      'message': None ,
      'data': None,
    }
  

  def retrieve_version(self):
    """
    Recupera a versão desejada, faz o download e realiza sua instalação.

    Este método localiza a versão especificada por `MAIN_VERSION` na página, 
    acessa o link correspondente, faz o download do arquivo e, em seguida, 
    realiza sua instalação. Caso ocorra um erro em qualquer etapa, 
    o erro será registrado no MongoDB.

    Returns:
      dict: Um dicionário contendo:
        - `error` (bool): Indica se houve erro durante o processo.
        - `message` (str): Mensagem de erro, se aplicável.
        - `data` (str ou None): Caminho do arquivo baixado em caso de sucesso, 
          ou `None` em caso de erro.

    Exceptions:
      - Registra exceções gerais no MongoDB com detalhes do erro.
    """

    try:
      versions = self.page.locator(self.locator.versions)
      
      for i in range(versions.count()):
        version = versions.nth(i)
        text_ver = version.inner_text()
        
        if MAIN_VERSION in text_ver:
          
          href = version.locator('a').first.get_attribute('href')
          self.page.goto(f'https://www.python.org{href}', wait_until='load') 

          full_path = self.__download()
          if full_path['error']:
            return full_path

          install = self.__install_version(full_path["data"])
          if install['error']:
            return install
          
          else:
            break

    except Exception as e:
      mongodb.create({'event': 'Erro entra na page da versão', 'error': True})
      return {
        'error': True,
        'message': f'Message: {e}',
        'data': None,
      }

    return {
      'error': False,
      'message': None,
      'data': None,
    }