# from mongoengine import Document, StringField, IntField
import json

class Ordinal():
    def __init__(self, id, number, address, value, content_type, sat_rarity):
        self.id = id
        self.number = number
        self.address = address
        self.value = value
        self.content_type = content_type
        self.sat_rarity = sat_rarity

    def to_dict(self):
        return {
            "id": self.id,
            "number": self.number,
            "address": self.address,
            "value": self.value,
            "content_type": self.content_type,
            "sat_rarity": self.sat_rarity
        }

    def __repr__(self):
        return f"Ordinal(id='{self.id}', number={self.number})"


def load_seed_ordinals() -> list[Ordinal]:
    # Opening JSON file
    json_file_path = './data/seed.json'

    with open(json_file_path, 'r') as file:
        data = json.load(file)  # Load the JSON data from the file
        ordinals = [Ordinal(ordinal['id'], ordinal['number'], ordinal['address'], ordinal['value'], ordinal['content_type'], ordinal['sat_rarity'])
                    for ordinal in data['ordinals']]

    return ordinals
