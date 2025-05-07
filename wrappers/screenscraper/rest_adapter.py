import requests
import requests.packages
import logging
from typing import List, Dict, Optional
from json import JSONDecodeError
from exceptions import RESTException
from models.result import Result

class RestAdapter:

    def __init__(self, hostname: str = '', api_key: str = '', ver: str = '', ssl_verify: bool = True, logger: logging.Logger = None):
        
        """
        Constructor for RestAdapter
        :param hostname: API hostname e.g. api.screenscraper.fr
        :param api_key: (optional) used for authentication for POST or DELETE requests
        :param ver: api version e.g. api2
        :param ssl_verify: Normally True, but can be False to prevent SSL/TLS certificate validation issues
        :param logger: (optional) if app consuming this function has a logger, pass here
        """
        
        self.session = requests.Session()
        self.url = "https://{}/{}/".format(hostname, ver)
        self._api_key = api_key
        self._logger = logger or logging.getLogger(__name__)
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            requests.packages.urllib3.disable_warnings()
    
    def _do(self, http_method: str, endpoint: str, params: Optional[Dict] = None, data: Optional[Dict] = None, headers: Optional[Dict] = None) -> Result:

        """
        HTTP request handler
        :param self: Instance of RestAdapter
        :param http_method: HTTP request method, e.g. 'GET'
        :param endpoint: endpoint for HTTP request
        :param params: parameters passed to requests module
        :param data: data passed to requests module
        :param headers: headers passed to requests module
        """

        full_url = self.url + endpoint
        headers = headers or {}
        headers.setdefault('api-key', self._api_key)

        log_line_pre = f"method={http_method}, url={full_url}, params={params}"
        log_line_post = ', '.join((log_line_pre, "success={}, status_code={}, message={}"))

        # Log HTTP params and perform HTTP request. Catch and raise any exceptions.
        try:
            self._logger.debug(msg=log_line_pre)
            response = self.session.request(method=http_method, url=full_url, verify=self._ssl_verify, headers=headers, params=params, json=data)
        except requests.exceptions.RequestException as e:
            self._logger.error(msg=(str(e)))
            raise RESTException("Request failed") from e

        # Deserialize JSON output to Python object or return failed Result on exception
        try:
            data_out = response.json()
        except (ValueError, JSONDecodeError) as e:
            self._logger.error(msg=log_line_post.format(False, None, e))
            raise RESTException("Bad JSON in response") from e
        
         # If status_code is 200-299, return success Result with data, otherwise raise exception
        is_success = 299 >= response.status_code >= 200
        log_line = f"{log_line_pre}, success={is_success}, status_code={response.status_code}, message={response.reason}"
        
        if is_success:
            self._logger.debug(msg=log_line)
            return Result(response.status_code, message=response.reason, data=data_out)
        self._logger.error(msg=log_line) 
        raise RESTException(f"{response.status_code}: {response.reason}")
    
    def close(self) -> None:
        """
        Close requests session
        """
        self.session.close()
    
    def get(self, endpoint: str, params: Dict = None) -> Result:

        """
        GET request handler
        :param self: Instance of RestAdapter
        :param endpoint: endpoint for HTTP request
        :param params: parameters passed to requests module
        """

        return self._do(http_method='GET', endpoint=endpoint, params=params)
    
    def post(self, endpoint: str, params: Dict = None, data: Dict = None) -> Result:

        """
        POST request handler
        :param self: Instance of RestAdapter
        :param endpoint: endpoint for HTTP request
        :param params: parameters passed to requests module
        :param data: data passed to requests module
        """

        return self._do(http_method='POST', endpoint=endpoint, params=params, data=data)
    
    def delete(self, endpoint: str, params: Dict = None, data: Dict = None) -> Result:
        
        """
        :param self: Instance of RestAdapter
        :param endpoint: endpoint for HTTP request
        :param params: parameters passed to requests module
        :param data: data passed to requests module
        """

        return self._do(http_method='DELETE', endpoint=endpoint, params=params, data=data)