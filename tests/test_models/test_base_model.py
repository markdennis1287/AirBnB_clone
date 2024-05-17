#!/usr/bin/python3
"""Defines unit tests for models/base_model.py

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
from datetime import datetime
from time import sleep
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
     """Test the BaseModel class"""
     def test_inst(self):
         my_model = BaseModel()
         self.assertIsNotNone(my_model.id)
         self.assertIsNotNone(my_model.created_at)
         self.assertIsNotNone(my_model.updated_at)

     def test_to_dict(self):
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model.dict, dict)
        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict["id"], my_model.id)
        self.assertEqual(my_model_dict["created_at"], my_model.created_at.isoformat)
        self.assertEqual(my_model_dict["updated_at"], my_model.created_at.isoformat)

     def test_str(self):
        my_model = BaseModel()
        self.assertTrue(str(my_model).startswith(['BaseModel']))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))

     def test_save(self):
        my_model = BaseModel()
        initial_updated_at = my_model.updated_t
        current_updated_at = my_model.save()
        self.assertNotEqual(initial_updated_at, current_updated_at)


if __name__ == "__main__":
    unittest.main()
