import json
from pathlib import Path


class JSONHandler:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def read(self, key: str = None) -> dict:
        data = self._read_json()
        return data.get(key) if key else data

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

    def add_to_history(self, role: str, parts: str):
        data = self._read_json()
        history = data.setdefault('config', {}).setdefault('history', [])

        message = parts.replace('\n', ' ').strip()

        history.append({'role': role, 'parts': message})

        self._write_json(data)

    def _read_json(self) -> dict:
        try:
            with self.file_path.open('r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            raise ValueError("Error decoding the JSON file!")

    def _write_json(self, data: dict):
        with self.file_path.open('w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


json_h = JSONHandler(Path('src/data/main.json'))