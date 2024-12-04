class Locators:
  """
  This class represents a locator object.

  Attributes:
    __locator (str): The locator value.

  """
  def __init__(self):
    self.__versions = '[class="list-row-container menu"] .release-number'
    self.__download_rows = 'tbody tr'

  @property
  def versions(self):
    """
    Set the locator value.

    Attributes:
        value (str): The locator value to set.

    """
    return self.__versions
  
  @property
  def download_rows(self):
    """
    Set the locator value.

    Attributes:
        value (str): The locator value to set.

    """
    return self.__download_rows