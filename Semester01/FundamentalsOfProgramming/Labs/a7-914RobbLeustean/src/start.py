from repository.binary_file_repository import BinaryFileRepository
from repository.memory_repository import MemoryRepository
from repository.text_file_repository import TextFileRepository
from repository.json_file_repository import JSONFileRepository
from repository.sql_repository import SQLRepository
from tests.test import Test
from ui.ui import UI


def get_repository_from_settings():
   """
   Reads the settings file and returns the repository specified there.
   Formatted as such: REPOSITORY=binary
   :return: The repository specified in the settings file.
   """
   
   with open("settings.properties", "r") as settings_file:
        for line in settings_file:
            line = line.strip()
            if line.startswith("REPOSITORY="):
                repository_type = line[len("REPOSITORY=") :]
                if repository_type == "memory":
                    return MemoryRepository()
                elif repository_type == "text":
                    return TextFileRepository("expenses.txt")
                elif repository_type == "binary":
                    return BinaryFileRepository("expenses.data")
                elif repository_type == "json":
                    return JSONFileRepository("expenses.json")
                elif repository_type == "sql":
                    return SQLRepository("expenses.db")
                else:
                    raise ValueError("Invalid repository type!")
            else:
               raise ValueError("Invalid settings file!")

         
         
if __name__ == "__main__":
   repository = get_repository_from_settings()
   user_interface = UI(repository)
   user_interface.run()