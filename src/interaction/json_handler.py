import json

class JSONHandler:
    def __init__(self, jsonFile_path: str):
        self.file_path = jsonFile_path

    def _read_json(self) -> dict:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            raise ValueError("Error decoding the JSON file!")

    def _write_json(self, data: dict):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def read(self, key: str = None):
        data = self._read_json()
        if key:
            return data.get(key)
        return data

    def write(self, key: str, value):
        data = self._read_json()
        data[key] = value
        self._write_json(data)

    def update(self, key: str, value):
        data = self._read_json()
        if key in data:
            data[key] = value
            self._write_json(data)
        else:
            raise KeyError(f"The key '{key}' does not exist in the JSON file!")

    def delete(self, key: str):
        data = self._read_json()
        if key in data:
            del data[key]
            self._write_json(data)
        else:
            raise KeyError(f"The key '{key}' was not found in the JSON file!")

json_h = JSONHandler('src/data/main.json')