import pickle
from pathlib import Path

def save_object(file_path, obj):
    Path(file_path,obj).parent.mkdir(
        parents=True,
        exist_ok=True
    )
    with open(file_path,"wb") as file_obj:
        pickle.dump(obj, file_obj)