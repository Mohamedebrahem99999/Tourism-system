import json
import os

class JSONHandler:
    @staticmethod
    def read_json(file_path):
        if not os.path.exists(file_path):
            return {}
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"❌ Error reading JSON file ({file_path}): {e}")
            return {}

    @staticmethod
    def write_json(file_path, data):
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            return True
        except IOError as e:
            print(f"❌ Error writing to JSON file ({file_path}): {e}")
            return False