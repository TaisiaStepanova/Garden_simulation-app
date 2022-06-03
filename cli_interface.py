import json
import click
from click_shell import shell
from model import*
from view import*
from controller import*


@shell(prompt='Garden > ', intro='Starting simulation...')
def cli_interface():
    global garden
    garden = Model()
    garden.get_data_from_file()
    click.echo("Вечера")
    click.echo(garden.show())
    garden.next_day()
    garden.set_data_in_file()
    click.echo("Сегодня")
    click.echo(garden.show())

@cli_interface.command()
def add_bed():
    click.echo(garden.add_garden_bed())
    garden.set_data_in_file()
    click.echo(garden.show())

@cli_interface.command(help = 'Plant tree: apple or pear')
@click.argument('type')
def plant_tree(type):
    click.echo(garden.plant_tree(type))
    garden.set_data_in_file()
    click.echo(garden.show())

@cli_interface.command(help = 'Plant cultivated plant (tomato, potato or pepper) in garden bed №...')
@click.argument('type')
@click.argument('count')
def plant_cult(type, count):
    click.echo(garden.plant_cultivated_plant(type, int(count) - 1))
    garden.set_data_in_file()
    click.echo(garden.show())

@cli_interface.command(help = 'Watering cultivated plant in garden bed №...')
@click.argument('count')
def watering(count):
    click.echo(garden.watering(int(count) - 1))
    garden.set_data_in_file()
    click.echo(garden.show())

@cli_interface.command(help = 'Fertilize cultivated plant in garden bed №...')
@click.argument('count')
def fertilize(count):
    click.echo(garden.fertilize(int(count) - 1))
    garden.set_data_in_file()
    click.echo(garden.show())

@cli_interface.command(help = 'Kill pest on plant (cult or tree) in garden bed №... or on tree №...')
@click.argument('type')
@click.argument('count')
def kill_pest(type, count):
    click.echo(garden.kill_pest(type, int(count) - 1))
    garden.set_data_in_file()
    click.echo(garden.show())

@cli_interface.command(help = 'Treatment on plant (cult or tree) in garden bed №... or on tree №...')
@click.argument('type')
@click.argument('count')
def treatment(type, count):
    click.echo(garden.treatment(type, int(count) - 1))
    garden.set_data_in_file()
    click.echo(garden.show())

@cli_interface.command(help = 'Weeding cultivated plant in garden bed №...')
@click.argument('count')
def weeding(count):
    click.echo(garden.weeding(int(count) - 1))
    garden.set_data_in_file()
    click.echo(garden.show())

@cli_interface.command(help = 'Harvesting on plant (cult or tree) in garden bed №... or on tree №...')
@click.argument('type')
@click.argument('count')
def harvesting(type, count):
    click.echo(garden.harvesting(type, int(count) - 1))
    garden.set_data_in_file()
    click.echo(garden.show())
