from flask import Flask, request,jsonify,render_template
import os
import json
def list():
    path = "static/images"
    list = os.listdir(path)
    print(type(list[0]))
    jsonlist = json.dumps(list)
list()
