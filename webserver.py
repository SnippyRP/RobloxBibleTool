from pdfminer.high_level import extract_text
from os import read
import PyPDF2
import time
pagecount = PyPDF2.PdfFileReader(open('kjvbible.pdf', 'rb')).numPages

from flask_restful import Resource, Api
from flask import Flask, jsonify
from threading import Thread
from flask import Flask, request, render_template

from PIL import Image, ImageOps
from io import BytesIO

import requests

app = Flask(__name__)
api = Api(app)

@app.route("/",methods=["GET", "POST"])
def home():
  return f"Translation API working! Contant Snippy#1118 for any issues"
@app.route('/page/<pg>', methods=['GET', 'POST'])
def form_to_json(pg):
    pagecontent = extract_text("kjvbible.pdf", page_numbers = [int(pg)])
    Dat = {"success":True,"book":str.split(pagecontent,"\n")[0],"content":pagecontent}
    return jsonify(Dat) or Dat,200


@app.route('/ping', methods=['POST','GET'])
def form_to_json_ping():
  Dat = {"success":True,"code":200,"method":request.method}
  return jsonify(Dat) or Dat,200


class GetFunction(Resource):
  print("Functions loading")

  def get(self, Function : str = None):
    return {"success":False,"error":"An unknown error occoured"},400
  
  print("Functions loaded")

def run():
  app.run(host = "0.0.0.0", port = 8080)
def start():
  t = Thread(target = run)
  t.start()
