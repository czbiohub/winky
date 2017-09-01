from Bio import SeqIO
from Bio.SeqIO import AbiIO
import click


@click.command(short_help='Convert Sanger sequencing format (ABI) to FASTQ')
@click.argument('filename')
@click.option('--verbose', is_flag=True, help="Show progress messages")
def abi_to_fastq(filename, verbose):
    # Open the Sanger sequencing trace
    if verbose:
        click.echo(f'Reading "{filename}" ...')

    record = SeqIO.read(filename, 'abi')

    # Remove bases with probability score less than 0.05
    if verbose:
        click.echo(f'\tTrimming bases with probability score < 0.05 ...')
    trimmed = AbiIO._abi_trim(record)

    if verbose:
        click.echo('\tBefore trimming:', len(record),
                   '\tAfter trimming:', len(trimmed))

    # Write the trimmed file to fastq
    fastq = filename.replace('.ab1', '.fastq')
    SeqIO.write(trimmed, fastq, 'fastq')

    # Write a message to the user (myself) so they know what happened
    click.echo(f'\tDone. Wrote to "{fastq}"')

