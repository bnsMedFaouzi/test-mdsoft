import json
import unittest
from .xlsx_to_json import xlsx_to_list, IN_FILE_PATH


class TestXlsxToList(unittest.TestCase):

    def setUp(self):
        self.result_data = [
            {
                "reference": "3.1",
                "description": "EQUIPEMENTS DE CHANTIER",
                "level": 1,
                "type": "SECTION",
                "order": 0
            },
            {
                "reference": "3.2",
                "description": "RESEAUX DE TERRE",
                "level": 1,
                "type": "SECTION",
                "order": 1
            },
            {
                "description": "Prise de terre",
                "unity": "u",
                "quantity": 1.0,
                "type": "CELL",
                "order": 2
            },
            {
                "description": "Liaisons \u00e9quipotentielles principales",
                "unity": "ens",
                "quantity": 1.0,
                "type": "CELL",
                "order": 3
            },
            {
                "description": "Liaisons \u00e9quipotentielles secondaires",
                "unity": "ens",
                "quantity": 1.0,
                "type": "CELL",
                "order": 4
            },
            {
                "description": "Prise de terre local fibre",
                "unity": "u",
                "quantity": 1.0,
                "type": "CELL",
                "order": 5
            },
            {
                "reference": "3.3",
                "description": "BRANCHEMENTS",
                "level": 1,
                "type": "SECTION",
                "order": 6
            },
            {
                "reference": "3.3.1",
                "description": "Alimentation colonne R2V 4x150mm\u00b2+T depuis ECP2D sous fourreaux",
                "level": 2,
                "type": "SECTION",
                "order": 7
            },
            {
                "description": "R\u00e9servations, carottages, percements, p\u00e9n\u00e9trations et \u00e9tanch\u00e9it\u00e9s",
                "unity": "ens",
                "quantity": 2.0,
                "type": "CELL",
                "order": 8
            },
            {
                "description": "Dossier de branchement",
                "unity": "forfait",
                "quantity": 2.0,
                "type": "CELL",
                "order": 9
            },
            {
                "description": "Consuels",
                "unity": "u",
                "quantity": 50.0,
                "type": "CELL",
                "order": 10
            },
            {
                "reference": "3.3.2",
                "description": "T\u00e9l\u00e9phone - fibre optique",
                "level": 2,
                "type": "SECTION",
                "order": 11
            },
            {
                "reference": "3.4",
                "description": "COLONNES MONTANTES",
                "level": 1,
                "type": "SECTION",
                "order": 12
            },
            {
                "description": "Par colonne : Travers\u00e9es des dalles, obturateurs, fourreaux",
                "unity": "ens",
                "quantity": 4.0,
                "type": "CELL",
                "order": 13
            },
            {
                "description": "Colonne montante C14-100",
                "unity": "ens",
                "quantity": 2.0,
                "type": "CELL",
                "order": 14
            },
            {
                "description": "Circuits de terre",
                "unity": "ens",
                "quantity": 2.0,
                "type": "CELL",
                "order": 15
            },
            {
                "description": "Colonne IRVE",
                "unity": "ens",
                "quantity": 2.0,
                "type": "CELL",
                "order": 16
            },
            {
                "reference": "3.5",
                "description": "DERIVATIONS INDIVIDUELLES",
                "level": 1,
                "type": "SECTION",
                "order": 17
            },
            {
                "description": "D\u00e9rivation individuelle basse tension services g\u00e9n\u00e9raux",
                "unity": "u",
                "quantity": 2.0,
                "type": "CELL",
                "order": 18
            },
            {
                "description": "Fourreaux d\u00e9rivations individuelles basse tension IRVE",
                "unity": "ens",
                "quantity": 2.0,
                "type": "CELL",
                "order": 19
            },
            {
                "description": "D\u00e9rivation individuelle basse tension logement",
                "unity": "u",
                "quantity": 48.0,
                "type": "CELL",
                "order": 20
            },
            {
                "description": "D\u00e9rivation individuelle conducteur de protection",
                "unity": "u",
                "quantity": 50.0,
                "type": "CELL",
                "order": 21
            }
        ]

    def test_add_fish_to_aquarium_success(self):
        items = xlsx_to_list(IN_FILE_PATH)

        self.assertEqual(items, self.result_data)
