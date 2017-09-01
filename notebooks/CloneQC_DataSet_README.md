#  CloneQC_DataSet_README

Description: CloneQC_DataSet is a directory that contains raw Sanger sequence files and a fasta-formated reference sequence file as an example dataset for a Geneious workflow to QC sequences of clones from Gibson assembly of geneBlocks corresponding to ZEBOV nucleoprotein ORF inserted into the pCAGGS mammalian expression plasmid. 

Purpose - Identify at least 1 clone with no mutations to use as a starting reagent for all downstream studies of the ZEBOV nucleoprotein ORF.

Workflow in Geneious:

1. Make a directory in Geneious “SNPdata_ZNP”
2. Transfer `ZN_refseq.fasta` to SNPdata_ZNP directory (this is a fasta formatted file containing ZEBOV NP ORF and flanking sequences of pCAGGS that I designed for Gibson assembly & cloning).
3. Transfer the `.ab1` files for 3 sequenced clones (ZN-1, ZN-2, ZN-3) of
   interest to SNPdata_ZN (these correspond to raw forward and reverse Sanger
   sequence data that hopefully provides at least 1 read covering every base in
   target sequence of interest).
4. In SNPdata_ZNP, select all reads from ZN-1.
5. Go to Workflow, run “SangerSeqTrial” workflow I put together:
   1. For each document
   2. Trim Ends (trim 5’ and 3’ bases with >5% error probability)
   3. Group Documents
   4. Align/Assemble -> De Novo Assemble (default settings: assembler =
      Geneious, Sensitivity = Medium/Fast, Remove existing trim regions from
      sequences; Save in sub-folder, save contigs)

8. Repeat for ZN-2, and ZN-3 reads.
9. This generates 3 sub-directories: ZN-1 Assembly, ZN-2 Assembly, and ZN-3 Assembly. Each contains a file “Contig”. A copy of each contig is also saved in SNPdata parent directory, named Contig 1, Contig 2, and Contig 3, respectively.
10. In each directory, add a suffix “_ZN-1”, “_ZN-2”, or “_ZN-3” to the name of each Contig file to more obviously link the contig data to source clone from which it was derived.
11. In the Assembly sub-directory, select the contig file, then go to Align/Assemble button on toolbar and select “Map to reference” to align contig sequence assembled from Sanger reads to starting source sequence used for Gibson assembly design & cloning. (Default settings: Dissolve contains and re-assemble, Reference Sequence = ZN_refSeq.fasta, Mapper = Geneious, Sensitivity = Highest Sensitivity/slow, Save contigs)
12. This generates another file in Assembly sub-directory with suffix “assembled to ZN_refSeq. Selecting this brings up window with aligned view of consensus sequence, reference sequence, coverage plot, and Sanger sequence chromatograms.
13. Selecting Display tab brings up options to view—key ones for QC:
	a. Check Highlighting
	b. All Disagreements to Reference
	c. Go < > in any sequence
14. Use the < > radio buttons to advance forward or backward through the reference sequence to view tagged discrepancies to assess evidence base (chromatogram quality). Valid disagreements with reference that would disqualify a clone for passing QC have the following properties:
	a. High quality discrepant peak (or indel), especially if 
		1) only a single read covering the position
		2) only a single high quality read covering the position
15. Export consensus sequence for each clone (File>Export>Consensus sequence(s)>Threshold = Highest Quality; Assign Quality checked and “Highest” selected; Append text to name of alignment checked, with “consensus” specified).
16. Summarize results (pass/no pass) in Benchling notebook entry - attach raw ab1 source data files and consensus file.
17. Use consensus sequence file for your favorite clone passing QC and pCAGGS vector sequence to generate and annotate plasmid map in Benchling.

