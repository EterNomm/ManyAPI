import requests
from .exceptions import *

class PypiStats:
    """
    A class to fetch pypistats.org API (https://pypistats.org/api/).
    ----
    Parameters:
    - package: `str` | Set packages to analysis.
    
    Methods:
    - downloads
    - operating_system (alias : os)
    - overall
    """
    
    def __init__(self, package:str):
        self.package = package
        
    def downloads(self, period:str=None):
        """
        Retrieve the aggregate download quantities for the last day/week/month.
        -------
        Parameters :
        - period: `str` (optional) | Day or week or month. If omitted returns all values.
        
        return total downloads based on period.
        """
        
        package = self.package
        if period == None:
            url = f"https://pypistats.org/api/packages/{package}/recent"
            try:
                req = requests.get(url)
                return req.json()["data"]
            except requests.RequestException as error:
                raise RequestsErrors(error)
        else:
            url = f"https://pypistats.org/api/packages/{package}/recent?period={period}"
            try:
                req = requests.get(url)
                return req.json()["data"][f"last_{period}"]
            except requests.RequestException as error:
                raise RequestsErrors(error)
    
            
    def operating_system(self, os:str=None):
        """
        Retrieve the aggregate daily download time series by operating system.
        -----
        Parameters :
        - os: `str` (optional) | the operating system name, e.g. windows, linux, darwin or other.
        
        return results on dict format.
        """
        package = self.package
        os = str.lower(os)
        if os == None:
           url = f"https://pypistats.org/api/packages/{package}/system"
        else:
           url = f"https://pypistats.org/api/packages/{package}/system?os={os}"

        try:
            req = requests.get(url)
            return req.json()["data"]
        except requests.RequestException as error:
            raise RequestsErrors(error)
        
    def overall(self):
        """
        Retrieve the aggregate daily download time series with or without mirror downloads.
        """
        package = self.package
        url = f"https://pypistats.org/api/packages/{package}/overall"

        try:
            req = requests.get(url)
            return req.json()["data"]
        except requests.RequestException as error:
            raise RequestsErrors(error)
        
    
    # "operating_system" funtion alias
    os = operating_system