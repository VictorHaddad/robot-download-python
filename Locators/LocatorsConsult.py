class Locators:
  """
  This class represents a locator object.

  Attributes:
     __locator (str): The locator value.

  """
  def __init__(self):
    self.__hrefs_page = "a:has(h3)"

  @property
  def hrefs_page(self):
    """
    Set the locator value.

    Attributes:
        value (str): The locator value to set.

    """
    return self.__hrefs_page