import os
import json
import privforge.utils.output_handler as oh

def load_binaries_json():
    
    base_path = os.path.dirname(__file__)
    json_path = os.path.join(base_path, 'data', 'binaries.json')
    
    try:
        with open(json_path) as f:
            return json.load(f)
    except FileNotFoundError:
        oh.output_handler(is_error=True,message="binaries.json not found!")