import click

from winky.abi_to_fastq import abi_to_fastq


settings = dict(help_option_names=['-h', '--help'])


@click.group(options_metavar='', subcommand_metavar='<command>',
             context_settings=settings)
def cli():
    """
    Hi! Winky is the heroic house-elf that automates checking and assembly of 
    Sanger sequencing traces. And, of course, Winky is free.
    """
    pass


cli.add_command(abi_to_fastq)

if __name__ == "__main__":
    cli()