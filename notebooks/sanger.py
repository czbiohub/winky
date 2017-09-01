
from Bio import SeqIO
from Bio.SeqIO import AbiIO
import click

@click.command()
def read_trim_write(abi):
    """Read a sanger sequencing trace, trim it, and write to a fastq file
    
    Parameters
    ----------
    abi : str
        Name of a Sanger sequencing trace file
    
    Returns
    -------
    fastq : str
        Name of the trimmed sequence file, in a more commonly used format
    """
    # Open the Sanger sequencing trace
    record = SeqIO.read(filename, 'abi')
    
    # Remove bases with probability score less than 0.05
    trimmed = AbiIO._abi_trim(record)
    
    # Write the trimmed file to fastq
    fastq = filename.replace('.ab1', '.fastq')
    SeqIO.write(trimmed, fastq, 'fastq')
    
    # Write a message to the user (myself) so they know what happened
    print(f'Read "{filename}", trimmed, and wrote to "{fastq}"')
    
    # Return the name of a fastq file
    return fastq