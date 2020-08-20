# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# crying because this might have not been the most efficient way to do this but it's fine
import json
a_dict = {"wayv": [{"member1": {"name": "Kun",
                                "birthday": "19960101",
                                "zodiac sign": "Capricorn",
                                "blood type": "B",
                                "height": "176",
                                "instagram": "@kun11xd",
                                "quote": [{"quote1", "quote2"}]
                                }},
                   {"member2": {"name": "Ten",
                                "birthday": "19960227",
                                "zodiac sign": "Pisces",
                                "blood type": "A",
                                "height": "170",
                                "instagram": "@tenlee_1001",
                                "quote": [{"quote1", "quote2"}]
                                }},
                   {"member3": {"name": "Winwin",
                                "birthday": "19971028",
                                "zodiac sign": "Scorpio",
                                "blood type": "B",
                                "height": "179",
                                "instagram": "@wwiinn_7",
                                "quote": [{"quote1", "quote2"}]
                                }},
                   {"member4": {"name": "Lucas",
                                "birthday": "19990125",
                                "zodiac sign": "Aquarius",
                                "blood type": "O",
                                "height": "183",
                                "instagram": "@lucas_xx444",
                                "quote": [{"quote1", "quote2"}]
                                }},
                   {"member5": {"name": "Xiaojun",
                                "birthday": "19990808",
                                "zodiac sign": "Leo",
                                "blood type": "A",
                                "height": "172",
                                "instagram": "@djxiao_888",
                                "quote": [{"quote1", "quote2"}]
                                }},
                   {"member6": {"name": "Hendery",
                                "birthday": "19990928",
                                "zodiac sign": "Libra",
                                "blood type": "O",
                                "height": "177",
                                "instagram": "@i_m_hendery",
                                "quote": [{"quote1", "quote2"}]
                                }},
                   {"member7": {"name": "Yangyang",
                                "birthday": "20001010",
                                "zodiac sign": "Libra",
                                "blood type": "O",
                                "height": "he has no height he is a SPECK of DUST (jk we couldn't find it)",
                                "instagram": "@yangyang_x2",
                                "quote": [{"quote1", "quote2"}]}
                    }]
         }
with open("file_name.json", "w") as file:
  json.dump(a_dict, file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
