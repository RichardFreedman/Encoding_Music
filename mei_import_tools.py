import urllib3
import json
import fnmatch

class GitHubFileManager:
    def __init__(self, base_url):
        """Initialize with a GitHub repository URL"""
        self.base_url = base_url
        self.owner, self.repo = self._parse_base_url(base_url)
        self.http = urllib3.PoolManager()
        
    def _parse_base_url(self, url):
        """Parse repository owner and name from base URL"""
        parts = url.split('/')
        return parts[-2], parts[-1]
    
    def _get_tree_sha(self, branch='main'):
        """Get the tree SHA for a given branch"""
        api_url = f"https://api.github.com/repos/{self.owner}/{self.repo}/git/ref/heads/{branch}"
        headers = {
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'
        }
        
        response = self.http.request('GET', api_url, headers=headers)
        if response.status != 200:
            raise Exception(f"Failed to fetch tree SHA: {response.data.decode('utf-8')}")
            
        return json.loads(response.data.decode('utf-8'))['object']['sha']
    
    def _get_raw_url(self, path):
        """Convert API path to raw.githubusercontent.com URL"""
        return f"https://raw.githubusercontent.com/{self.owner}/{self.repo}/main/{path}"
    
    def _match_pattern(self, filename, pattern):
        """Match filename against pattern"""
        return fnmatch.fnmatch(filename, pattern)
    
    def list_files(self, directory_path="", patterns=None):
        """
        List raw URLs of files in a repository directory matching optional patterns
        
        Args:
            directory_path (str): Path to directory within repository
            patterns (list[str]): List of patterns to match filenames against
            
        Returns:
            list: List of raw URLs for matching files
        """
        tree_sha = self._get_tree_sha()
        
        api_url = f"https://api.github.com/repos/{self.owner}/{self.repo}/git/trees/{tree_sha}"
        params = {'recursive': '1'}
        headers = {
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'
        }
        
        response = self.http.request('GET', api_url, fields=params, headers=headers)
        if response.status != 200:
            raise Exception(f"Failed to fetch directory contents: {response.data.decode('utf-8')}")
            
        tree_data = json.loads(response.data.decode('utf-8'))
        urls = []
        
        for item in tree_data['tree']:
            if directory_path and not item['path'].startswith(directory_path):
                continue
                
            if item['type'] == 'blob':
                filename = item['path'].split('/')[-1]
                
                if patterns is None or any(self._match_pattern(filename, pattern) for pattern in patterns):
                    urls.append(self._get_raw_url(item['path']))
                
        return urls
