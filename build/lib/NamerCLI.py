import requests
import json
import bazzellpy
import click
from bazzellpy import functions
from bazzellpy.functions import twitter_real_name, name_query

print('''
████████    ██████   █████████████    ██████  ████████ 
░░███░░███  ░░░░░███ ░░███░░███░░███  ███░░███░░███░░███
 ░███ ░███   ███████  ░███ ░███ ░███ ░███████  ░███  ░░░ 
 ░███ ░███  ███░░███  ░███ ░███ ░███ ░███░░░   ░███     
 ████ █████░░████████ █████░███ █████░░██████  █████    
 ░░░░ ░░░░░  ░░░░░░░░ ░░░░░ ░░░ ░░░░░  ░░░░░░  ░░░░░  
''')

@click.group()
def cli():
    pass

@cli.command()
@click.option('-f', '--forename', type=str, help='Please insert the forename you want to predict demographics for')
def predict(forename):
    result_g = json.loads(requests.request("GET", f"https://api.genderize.io?name={forename}").text)
    result_a = json.loads(requests.request("GET", f"https://api.agify.io?name={forename}").text)
    result_n = json.loads(requests.request("GET", f"https://api.nationalize.io?name={forename}").text)
    print(result_g)
    print(result_a)
    print(result_n)
    
@cli.command()
@click.option('-f', '--forename', type=str, help='Please insert the forename of the individual to search')
@click.option('-s', '--surname', type=str, help='Please insert the surname of the individual to search')
def search(forename, surname):
    print(twitter_real_name(forename, surname))
    print(name_query(forename, surname))