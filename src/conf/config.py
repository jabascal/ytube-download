# Define dataclasses for hydra 
from dataclasses import dataclass


@dataclass 
class Paths:     
    log: str     
    downloads: str     
    data: str 
    
@dataclass 
class Params:     
    video: str     
    file_resolution: str     
    file_ext: str     
    url_list: str     
    url: str 
    
@dataclass 
class YTubeConfig:     
    paths: Paths     
    params: Params