"""Layer I: Data Ingestion and Representation
Inputs: Archaeological datasets, paleoclimate reconstructions, 
        geospatial distributions, textual corpora, trade records
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Any

class DataIngestionLayer:
    """Layer I: Data Ingestion"""
    
    def __init__(self, data_dir: str = "../data/"):
        self.data_dir = data_dir
        self.archaeological_data = None
        self.paleoclimate_data = None
        self.geospatial_data = None
        self.textual_corpora = None
    
    def load_archaeological(self, path: str) -> pd.DataFrame:
        """Load archaeological datasets: site inventories, radiocarbon dates"""
        self.archaeological_data = pd.read_csv(path)
        return self.archaeological_data
    
    def load_paleoclimate(self, path: str) -> pd.DataFrame:
        """Load paleoclimate: isotope records, pollen, speleothems"""
        self.paleoclimate_data = pd.read_csv(path)
        return self.paleoclimate_data
    
    def load_geospatial(self, path: str):
        """Load geospatial: settlement maps, territorial boundaries"""
        import geopandas as gpd
        self.geospatial_data = gpd.read_file(path)
        return self.geospatial_data
    
    def load_textual(self, path: str) -> List[str]:
        """Load textual corpora for NLP encoding"""
        with open(path, 'r') as f:
            self.textual_corpora = f.readlines()
        return self.textual_corpora
    
    def load_trade_records(self, path: str) -> pd.DataFrame:
        """Load trade and conflict records"""
        return pd.read_csv(path)
    
    def get_summary(self) -> Dict[str, Any]:
        return {
            'archaeological': self.archaeological_data is not None,
            'paleoclimate': self.paleoclimate_data is not None,
            'geospatial': self.geospatial_data is not None,
            'textual': self.textual_corpora is not None
        }
