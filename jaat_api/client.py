import requests
from typing import List, Any

class JAATError(Exception):
    """Base exception class for JAAT API errors."""
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API Error [{status_code}]: {message}")

class JAATClient:
    def __init__(self, api_key: str, base_url: str = "https://api.jaat.app"):
        if not api_key:
            raise ValueError("An API key must be provided to initialize the JAATClient.")
            
        self.base_url = base_url.rstrip("/")
        
        self.session = requests.Session()
        self.session.headers.update({
            "X-API-Key": api_key,
            "Content-Type": "application/json"
        })

    def _request(self, endpoint: str, data: dict) -> dict:
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = self.session.post(url, json=data)
            
            if response.status_code != 200:
                try:
                    err_detail = response.json().get("detail", response.text)
                except Exception:
                    err_detail = response.text
                raise JAATError(response.status_code, err_detail)
                
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise JAATError(500, f"Network communication failure: {str(e)}")

    def run_batch(self, module: str, texts: List[str]) -> List[Any]:
        """
        Processes an array of strings against a specific JAAT module.
        
        :param module: The module identifier string ('task', 'skill', 'ai', 'title') -> currently supported modules
        :param texts: A list of occupational text strings to evaluate
        :return: A list containing your cleanly serialized inference results
        """
        mod_clean = module.lower().strip()
        if mod_clean not in ["task", "skill", "ai", "title"]:
            raise ValueError("Invalid module selection. Choose from: 'task', 'skill', 'ai', or 'title'.")
            
        endpoint = f"/v1/{mod_clean}/batch"
        payload = {"texts": texts}
        
        response_data = self._request(endpoint, payload)
        return response_data.get("results", [])

    # for ease of use
    def get_tasks(self, texts: List[str]) -> List[Any]:
        return self.run_batch("task", texts)

    def get_skills(self, texts: List[str]) -> List[Any]:
        return self.run_batch("skill", texts)

    def get_ai(self, texts: List[str]) -> List[Any]:
        return self.run_batch("ai", texts)
    
    def get_title(self, texts: List[str]) -> List[Any]:
        return self.run_batch("title", texts)