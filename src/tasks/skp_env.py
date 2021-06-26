import os, sys, json, re
from pprint import pprint

# SKP
SKP_USER = os.environ["SKP_USER"]
SKP_HOME = os.environ["SKP_HOME"]

# VSCODE
try:
    VSCODE_HOME = os.environ["VSCODE_HOME"]
    VSCODE_NAME = os.environ["VSCODE_NAME"]
    VSCODE_VER = os.environ["VSCODE_VER"]
    VSCODE_PASSWD = os.environ["VSCODE_PASSWD"]
    VSCODE_HOST = os.environ["VSCODE_HOST"]
    VSCODE_PORT = os.environ["VSCODE_PORT"]
    VSCODE = True
except:
    VSCODE = False
