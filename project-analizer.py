#!/bin/python
from git import Repo
import openpyxl
  
# load excel with its path
wrkbk = openpyxl.load_workbook("Libro1.xlsx")
sh = wrkbk.active
  
# iterate through excel and display data
for i in range(2, sh.max_row+1):
    print("Nombre: ", sh.cell(row=i, column=1).value)
    print("URL: ", sh.cell(row=i, column=2).value)
    print("Ramas: ")
    ramas=sh.cell(row=i, column=3).value.split(",")
    for rama in ramas:
        print("Rama: ", rama)
    users=sh.cell(row=i, column=4).value.split("\n")
    for user in users:
        user_token=user.split("->")
        print("User: ", user_token[0])
        user_tokens=user_token[1].split(",")
        for token in user_tokens:
            print("Token: ", token.strip())
        

def git_clone(url, path):
    # clone the repo
    cloned_repo = repo.clone(url, path)
