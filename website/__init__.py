from flask import Flask, Blueprint, render_template
from pymongo import MongoClient


app = Flask(__name__)


client = MongoClient(host='localhost', port=27107)
