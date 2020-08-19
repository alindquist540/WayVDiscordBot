# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
a_dict = {"wayv": [{"member": {"name": "Kun", "age": "24", "quote": [{"quote1", "quote2"}]}},
                   {"member": {"name": "Ten", "age": "24", "quote": [{"quote1," "quote2"}]}}]
         }
with open("file_name.json", "w") as file:
  json.dump(a_dict, file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
