import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:secret@db/inventory_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
