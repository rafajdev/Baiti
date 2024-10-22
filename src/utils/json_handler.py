import json
from pathlib import Path

class JSONHandler:
    def __init__(self, file_path: Path):
        """
        Initialize the JSONHandler class.

        Parameters
        ----------
        file_path : Path
            The path to the JSON file.
        """

        self.file_path = file_path

    def read(self, key: str = None) -> dict:
        """
        Read the JSON file and return the dictionary.

        Parameters
        ----------
        key : str
            The key to return the value for. If not provided, the entire dictionary is returned.

        Returns
        -------
        dict
            The dictionary containing the data from the JSON file.
        """
        data = self._read_json()
        return data.get(key) if key else data

    def write(self, key: str, value):
        """
        Write a new value for a specific key.

        Parameters
        ----------
        key : str
            The key to write the value for.
        value : Any
            The value to write.
        """
        data = self._read_json()
        data[key] = value
        self._write_json(data)

    def update(self, key: str, value):
        """
        Update the value of a specific key if it exists.

        Parameters
        ----------
        key : str
            The key to update the value for.
        value : Any
            The new value to write.
        """
        data = self._read_json()
        if key in data:
            data[key] = value
            self._write_json(data)
        else:
            raise KeyError(f"The key '{key}' does not exist in the JSON file!")

    def delete(self, key: str):
        """
        Remove a specific key and its associated value.

        Parameters
        ----------
        key : str
            The key to remove.
        """
        data = self._read_json()
        if key in data:
            del data[key]
            self._write_json(data)
        else:
            raise KeyError(f"The key '{key}' was not found in the JSON file!")

    def add_to_history(self, role: str, parts: str):
        """
        Add a new item to the history list, or create a new list if it does not exist.

        Parameters
        ----------
        role : str
            The role to add to the history list.
        parts : str
            The parts to add to the history list.
        """
        data = self._read_json()
        history = data.setdefault('config', {}).setdefault('history', [])

        message = parts.replace('\n', ' ').strip()

        history.append({'role': role, 'parts': message})

        self._write_json(data)

    def _read_json(self) -> dict:
        """
        Read the JSON file and return the dictionary.

        Returns
        -------
        dict
            The dictionary containing the data from the JSON file.
        """
        try:
            with self.file_path.open('r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            raise ValueError("Error decoding the JSON file!")

    def _write_json(self, data: dict):
        """
        Write the dictionary to the JSON file.

        Parameters
        ----------
        data : dict
            The dictionary to write to the JSON file.
        """
        with self.file_path.open('w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

json_h = JSONHandler(Path('src/data/main.json'))