import requests
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
    response_gender = requests.request("GET", f"https://api.genderize.io?name={forename}")
    response_age = requests.request("GET", f"https://api.agify.io?name={forename}")
    response_nationality = requests.request("GET", f"https://api.nationalize.io?name={forename}")

@cli.command()
@click.option('-f', '--forename', type=str, help='Please insert the forename of the individual to search')
@click.option('-s', '--surname', type=str, help='Please insert the surname of the individual to search')
def search(forename, surname):
    print(twitter_real_name(forename, surname))
    print(name_query(forename, surname))