from model import*
from view import*
from controller import*
from cli_interface import*
import sys
import click


@click.command()
@click.option('--interface', default='GUI', help="GUI or CLI")
def main(interface):
    if interface.lower() == 'gui':
        model = Model()
        controller = Controller(model)
        Garden(model, controller).run()
        sys.exit()
    elif interface.lower() == 'cli':
        cli_interface()
    else:
        click.echo('WRONG INPUT!')
        exit()



if __name__ == "__main__":
    main()