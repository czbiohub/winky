## Terminal output from using velvet an bwa

```
(winky) ➜  winky git:(master) ✗ velveth  
velveth - simple hashing program
Version 1.2.10

Copyright 2007, 2008 Daniel Zerbino (zerbino@ebi.ac.uk)
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compilation settings:
CATEGORIES = 4
MAXKMERLENGTH = 191
OPENMP
LONGSEQUENCES

Usage:
./velveth directory hash_length {[-file_format][-read_type][-separate|-interleaved] filename1 [filename2 ...]} {...} [options]

	directory	: directory name for output files
	hash_length	: EITHER an odd integer (if even, it will be decremented) <= 191 (if above, will be reduced)
			: OR: m,M,s where m and M are odd integers (if not, they will be decremented) with m < M <= 191 (if above, will be reduced)
				and s is a step (even number). Velvet will then hash from k=m to k=M with a step of s
	filename	: path to sequence file or - for standard input

File format options:
	-fasta	-fastq	-raw	-fasta.gz	-fastq.gz	-raw.gz	-sam	-bam	-fmtAuto
	(Note: -fmtAuto will detect fasta or fastq, and will try the following programs for decompression : gunzip, pbunzip2, bunzip2

File layout options for paired reads (only for fasta and fastq formats):
	-interleaved	: File contains paired reads interleaved in the one file (default)
	-separate	: Read 2 separate files for paired reads

Read type options:
	-short	-shortPaired
	-short2	-shortPaired2
	-short3	-shortPaired3
	-short4	-shortPaired4
	-long	-longPaired
	-reference

Options:
	-strand_specific	: for strand specific transcriptome sequencing data (default: off)
	-reuse_Sequences	: reuse Sequences file (or link) already in directory (no need to provide original filenames in this case (default: off)
	-reuse_binary	: reuse binary sequences file (or link) already in directory (no need to provide original filenames in this case (default: off)
	-noHash			: simply prepare Sequences file, do not hash reads or prepare Roadmaps file (default: off)
	-create_binary  	: create binary CnyUnifiedSeq file (default: off)

Synopsis:

- Short single end reads:
	velveth Assem 29 -short -fastq s_1_sequence.txt

- Paired-end short reads (remember to interleave paired reads):
	velveth Assem 31 -shortPaired -fasta interleaved.fna

- Paired-end short reads (using separate files for the paired reads)
	velveth Assem 31 -shortPaired -fasta -separate left.fa right.fa

- Two channels and some long reads:
	velveth Assem 43 -short -fastq unmapped.fna -longPaired -fasta SangerReads.fasta

- Three channels:
	velveth Assem 35 -shortPaired -fasta pe_lib1.fasta -shortPaired2 pe_lib2.fasta -short3 se_lib1.fa

Output:
	directory/Roadmaps
	directory/Sequences
		[Both files are picked up by graph, so please leave them there]
(winky) ➜  winky git:(master) ✗ velveth ZN-1.21 21 -fasta -long test/data/ZN-1*.fastq
zsh: no matches found: test/data/ZN-1*.fastq
(winky) ➜  winky git:(master) ✗ pwd
/Users/olgabot/code/winky
(winky) ➜  winky git:(master) ✗ velveth ZN-1.21 21 -fasta -long winky/test/data/ZN-1*.fastq
velveth: winky/test/data/ZN-1_ZNif1__2017-06-07_B01.fastq does not seem to be in FastA format
(winky) ➜  winky git:(master) ✗ velveth ZN-1.21 21 -fastq -long winky/test/data/ZN-1*.fastq
[0.000001] Reading FastQ file winky/test/data/ZN-1_ZNif1__2017-06-07_B01.fastq;
[0.000087] 1 sequences found
[0.000090] Done
[0.000103] Reading FastQ file winky/test/data/ZN-1_ZNir1__2017-06-07_E01.fastq;
[0.000132] 1 sequences found
[0.000134] Done
[0.000144] Reading FastQ file winky/test/data/ZN-1_pCAGGSf__2017-05-31_A06.fastq;
[0.000171] 1 sequences found
[0.000174] Done
[0.000183] Reading FastQ file winky/test/data/ZN-1_pCAGGSr__2017-05-31_G03.fastq;
[0.000209] 1 sequences found
[0.000210] Done
[0.876544] Reading read set file ZN-1.21/Sequences;
[0.876942] 4 sequences found
[0.877297] Done
[0.877306] 4 sequences in total.
[0.883273] Writing into roadmap file ZN-1.21/Roadmaps...
[0.883529] Inputting sequences...
[0.883694] Inputting sequence 0 / 4
[0.896734]  === Sequences loaded in 0.013312 s
[0.896965] Done inputting sequences
[0.896971] Destroying splay table
[0.898040] Splay table destroyed
(winky) ➜  winky git:(master) ✗ # velvetg ecoli.21 -exp_cov auto
(winky) ➜  winky git:(master) ✗ velvetg  
velvetg - de Bruijn graph construction, error removal and repeat resolution
Version 1.2.10
Copyright 2007, 2008 Daniel Zerbino (zerbino@ebi.ac.uk)
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
Compilation settings:
CATEGORIES = 4
MAXKMERLENGTH = 191
OPENMP
LONGSEQUENCES

Usage:
./velvetg directory [options]

	directory			: working directory name

Standard options:
	-cov_cutoff <floating-point|auto>	: removal of low coverage nodes AFTER tour bus or allow the system to infer it
		(default: no removal)
	-ins_length <integer>		: expected distance between two paired end reads (default: no read pairing)
	-read_trkg <yes|no>		: tracking of short read positions in assembly (default: no tracking)
	-min_contig_lgth <integer>	: minimum contig length exported to contigs.fa file (default: hash length * 2)
	-amos_file <yes|no>		: export assembly to AMOS file (default: no export)
	-exp_cov <floating point|auto>	: expected coverage of unique regions or allow the system to infer it
		(default: no long or paired-end read resolution)
	-long_cov_cutoff <floating-point>: removal of nodes with low long-read coverage AFTER tour bus
		(default: no removal)

Advanced options:
	-ins_length* <integer>		: expected distance between two paired-end reads in the respective short-read dataset (default: no read pairing)
	-ins_length_long <integer>	: expected distance between two long paired-end reads (default: no read pairing)
	-ins_length*_sd <integer>	: est. standard deviation of respective dataset (default: 10% of corresponding length)
		[replace '*' by nothing, '2' or '_long' as necessary]
	-scaffolding <yes|no>		: scaffolding of contigs used paired end information (default: on)
	-max_branch_length <integer>	: maximum length in base pair of bubble (default: 100)
	-max_divergence <floating-point>: maximum divergence rate between two branches in a bubble (default: 0.2)
	-max_gap_count <integer>	: maximum number of gaps allowed in the alignment of the two branches of a bubble (default: 3)
	-min_pair_count <integer>	: minimum number of paired end connections to justify the scaffolding of two long contigs (default: 5)
	-max_coverage <floating point>	: removal of high coverage nodes AFTER tour bus (default: no removal)
	-coverage_mask <int>	: minimum coverage required for confident regions of contigs (default: 1)
	-long_mult_cutoff <int>		: minimum number of long reads required to merge contigs (default: 2)
	-unused_reads <yes|no>		: export unused reads in UnusedReads.fa file (default: no)
	-alignments <yes|no>		: export a summary of contig alignment to the reference sequences (default: no)
	-exportFiltered <yes|no>	: export the long nodes which were eliminated by the coverage filters (default: no)
	-clean <yes|no>			: remove all the intermediary files which are useless for recalculation (default : no)
	-very_clean <yes|no>		: remove all the intermediary files (no recalculation possible) (default: no)
	-paired_exp_fraction <double>	: remove all the paired end connections which less than the specified fraction of the expected count (default: 0.1)
	-shortMatePaired* <yes|no>	: for mate-pair libraries, indicate that the library might be contaminated with paired-end reads (default no)
	-conserveLong <yes|no>		: preserve sequences with long reads in them (default no)

Output:
	directory/contigs.fa		: fasta file of contigs longer than twice hash length
	directory/stats.txt		: stats file (tab-spaced) useful for determining appropriate coverage cutoff
	directory/LastGraph		: special formatted file with all the information on the final graph
	directory/velvet_asm.afg	: (if requested) AMOS compatible assembly file
(winky) ➜  winky git:(master) ✗ velvetg ZN-1.21 -exp_cov auto
[0.000000] Reading roadmap file ZN-1.21/Roadmaps
[0.000083] 4 roadmaps read
[0.000121] Creating insertion markers
[0.000126] Ordering insertion markers
[0.000728] Counting preNodes
[0.000737] 13 preNodes counted, creating them now
[0.000998] Adjusting marker info...
[0.001088] Connecting preNodes
[0.001212] Cleaning up memory
[0.001221] Done creating preGraph
[0.001224] Concatenation...
[0.001239] Renumbering preNodes
[0.001241] Initial preNode count 13
[0.001256] Destroyed 5 preNodes
[0.001259] Concatenation over!
[0.001260] Clipping short tips off preGraph
[0.001263] Concatenation...
[0.001276] Renumbering preNodes
[0.001280] Initial preNode count 8
[0.001282] Destroyed 4 preNodes
[0.001284] Concatenation over!
[0.001285] 2 tips cut off
[0.001287] 4 nodes left
[0.001499] Writing into pregraph file ZN-1.21/PreGraph...
[0.002299] Reading read set file ZN-1.21/Sequences;
[0.002319] 4 sequences found
[0.002364] Done
[0.002697] Reading pre-graph file ZN-1.21/PreGraph
[0.002713] Graph has 4 nodes and 4 sequences
[0.003431] Scanning pre-graph file ZN-1.21/PreGraph for k-mers
[0.003566] 2548 kmers found
[0.003902] Sorting kmer occurence table ...
[0.004768] Sorting done.
[0.004777] Computing acceleration table...
[0.047984] Computing offsets...
[0.048156] Ghost Threading through reads 0 / 4
[0.048209]  === Ghost-Threaded in 0.000169 s
[0.048247] Threading through reads 0 / 4
[0.061587]  === Threaded in 0.013369 s
[0.069926] Correcting graph with cutoff 0.200000
[0.069996] Determining eligible starting points
[0.070032] Done listing starting nodes
[0.070035] Initializing todo lists
[0.070038] Done with initilization
[0.070039] Activating arc lookup table
[0.070044] Done activating arc lookup table
[0.070416] Concatenation...
[0.070422] Renumbering nodes
[0.070424] Initial node count 4
[0.070427] Removed 3 null nodes
[0.070429] Concatenation over!
[0.070430] Clipping short tips off graph, drastic
[0.070432] Concatenation...
[0.070433] Renumbering nodes
[0.070434] Initial node count 1
[0.070436] Removed 0 null nodes
[0.070437] Concatenation over!
[0.070439] 1 nodes left
[0.070615] Writing into graph file ZN-1.21/Graph2...
[0.071193] Measuring median coverage depth...
[0.071197] Median coverage depth = 0.000000
[0.071227] Removing contigs with coverage < 0.000000...
[0.071230] Concatenation...
[0.071232] Renumbering nodes
[0.071234] Initial node count 1
[0.071237] Removed 0 null nodes
[0.071240] Concatenation over!
[0.071241] Concatenation...
[0.071242] Renumbering nodes
[0.071244] Initial node count 1
[0.071246] Removed 0 null nodes
[0.071247] Concatenation over!
[0.071251] Clipping short tips off graph, drastic
[0.071253] Concatenation...
[0.071254] Renumbering nodes
[0.071255] Initial node count 1
[0.071257] Removed 0 null nodes
[0.071258] Concatenation over!
[0.071260] 1 nodes left
[0.071261] WARNING: NO EXPECTED COVERAGE PROVIDED
[0.071263] Velvet will be unable to resolve any repeats
[0.071264] See manual for instructions on how to set the expected coverage parameter
[0.071266] Concatenation...
[0.071267] Renumbering nodes
[0.071268] Initial node count 1
[0.071270] Removed 0 null nodes
[0.071271] Concatenation over!
[0.071272] Removing reference contigs with coverage < 0.000000...
[0.071275] Concatenation...
[0.071276] Renumbering nodes
[0.071278] Initial node count 1
[0.071280] Removed 0 null nodes
[0.071282] Concatenation over!
[0.071412] Writing contigs into ZN-1.21/contigs.fa...
[0.071962] Writing into stats file ZN-1.21/stats.txt...
[0.072119] Writing into graph file ZN-1.21/LastGraph...
[0.072696] Estimated Coverage = 0.000000
[0.072702] Estimated Coverage cutoff = 0.000000
Final graph has 1 nodes and n50 of 2529, max 2529, total 2529, using 4/4 reads
(winky) ➜  winky git:(master) ✗ ll
total 24
-rw-r--r--   1 olgabot  staff    42B Sep  1 01:41 MANIFEST.in
drwxr-xr-x  10 olgabot  staff   340B Sep  1 02:19 ZN-1.21
drwxr-xr-x@ 20 olgabot  staff   680B Sep  1 01:39 notebooks
-rw-r--r--   1 olgabot  staff     0B Sep  1 01:41 requirements.txt
-rw-r--r--   1 olgabot  staff    62B Sep  1 01:41 setup.cfg
-rw-r--r--   1 olgabot  staff   551B Sep  1 02:12 setup.py
drwxr-xr-x   7 olgabot  staff   238B Sep  1 02:15 winky
drwxr-xr-x   7 olgabot  staff   238B Sep  1 02:12 y.egg-info
(winky) ➜  winky git:(master) ✗ ll ZN-1.21
total 80
-rw-r--r--  1 olgabot  staff   5.1K Sep  1 02:19 Graph2
-rw-r--r--  1 olgabot  staff   5.1K Sep  1 02:19 LastGraph
-rw-r--r--  1 olgabot  staff   1.5K Sep  1 02:19 Log
-rw-r--r--  1 olgabot  staff   2.6K Sep  1 02:19 PreGraph
-rw-r--r--  1 olgabot  staff   118B Sep  1 02:17 Roadmaps
-rw-r--r--  1 olgabot  staff   3.9K Sep  1 02:17 Sequences
-rw-r--r--  1 olgabot  staff   2.6K Sep  1 02:19 contigs.fa
-rw-r--r--  1 olgabot  staff   266B Sep  1 02:19 stats.txt
(winky) ➜  winky git:(master) ✗ ll
total 24
-rw-r--r--   1 olgabot  staff    42B Sep  1 01:41 MANIFEST.in
drwxr-xr-x  10 olgabot  staff   340B Sep  1 02:19 ZN-1.21
drwxr-xr-x@ 20 olgabot  staff   680B Sep  1 01:39 notebooks
-rw-r--r--   1 olgabot  staff     0B Sep  1 01:41 requirements.txt
-rw-r--r--   1 olgabot  staff    62B Sep  1 01:41 setup.cfg
-rw-r--r--   1 olgabot  staff   551B Sep  1 02:12 setup.py
drwxr-xr-x   7 olgabot  staff   238B Sep  1 02:15 winky
drwxr-xr-x   7 olgabot  staff   238B Sep  1 02:12 y.egg-info
(winky) ➜  winky git:(master) ✗ cd ZN-1.21
(winky) ➜  ZN-1.21 git:(master) ✗ ll
total 80
-rw-r--r--  1 olgabot  staff   5.1K Sep  1 02:19 Graph2
-rw-r--r--  1 olgabot  staff   5.1K Sep  1 02:19 LastGraph
-rw-r--r--  1 olgabot  staff   1.5K Sep  1 02:19 Log
-rw-r--r--  1 olgabot  staff   2.6K Sep  1 02:19 PreGraph
-rw-r--r--  1 olgabot  staff   118B Sep  1 02:17 Roadmaps
-rw-r--r--  1 olgabot  staff   3.9K Sep  1 02:17 Sequences
-rw-r--r--  1 olgabot  staff   2.6K Sep  1 02:19 contigs.fa
-rw-r--r--  1 olgabot  staff   266B Sep  1 02:19 stats.txt
(winky) ➜  ZN-1.21 git:(master) ✗ cat contigs.fa
>NODE_1_length_2529_cov_1.457098
GCTGTCCGCGGGGGGACGGCTGCCTTCGGGGGGGACGGGGCAGGGCGGGGTTCGGCTTCT
GGCGTGTGACCGGCGGCTCTAGAGCCTCTGCTAACCATGTTCATGCCTTCTTCTTTTTCC
TACAGCTCCTGGGCAACGTGCTGGTTATTGTGCTGTCTCATCATTTTGGCAAAGAATTCA
TGGATAGCCGCCCACAGAAAATTTGGATGGCACCATCCCTGACCGAAAGTGATATGGACT
ATCATAAGATTTTGACTGCCGGCTTGAGTGTACAACAAGGGATTGTAAGACAGAGAGTTA
TCCCGGTCTACCAAGTGAACAATTTGGAAGAGATCTGTCAGCTGATTATCCAGGCGTTTG
AAGCGGGCGTAGATTTCCAAGAATCAGCCGATTCTTTTCTCCTTATGCTGTGCCTTCATC
ACGCATATCAAGGTGATTATAAACTCTTCTTGGAATCTGGCGCGGTCAAATACTTGGAAG
GGCATGGTTTCAGATTCGAGGTGAAGAAAAGGGACGGAGTCAAGAGGCTGGAGGAGCTTC
TGCCGGCCGTTTCTAGTGGCAAAAACATTAAACGCACACTCGCCGCGATGCCTGAAGAGG
AGACTACAGAAGCGAATGCCGGCCAATTTCTGTCATTCGCGTCTTTGTTCCTGCCAAAGC
TCGTAGTAGGTGAAAAAGCATGCCTGGAAAAAGTACAGCGCCAAATTCAGGTGCATGCCG
AACAAGGTCTTATCCAGTACCCAACGGCTTGGCAGTCAGTTGGCCACATGATGGTGATCT
TTAGACTTATGCGAACAAACTTTCTGATCAAGTTCCTGTTGATTCACCAAGGTATGCATA
TGGTAGCCGGGCACGACGCCAATGATGCTGTCATAAGCAATAGCGTTGCGCAAGCGCGAT
TTTCAGGGCTTCTGATCGTGAAAACAGTTCTCGATCATATTCTGCAAAAGACAGAACGCG
GCGTCCGATTGCATCCTCTCGCACGGACGGCTAAGGTGAAAAATGAGGTCAACTCTTTCA
AGGCCGCACTGAGCTCTCTGGCAAAACACGGGGAATATGCCCCATTCGCGAGACTGCTTA
ATTTGTCTGGAGTCAACAATCTGGAGCATGGGCTTTTTCCGCAACTTAGTGCGATTGCCC
TGGGGGTAGCTACAGCACACGGTAGCACTTTGGCCGGCGTTAACGTCGGTGAGCAATATC
AACAACTGCGAGAAGCAGCGACGGAGGCAGAGAAACAACTGCAACAGTATGCCGAGTCTA
GGGAACTGGATCACCTCGGTCTGGATGACCAGGAAAAGAAAATTCTCATGAACTTTCATC
AAAAGAAGAACGAGATATCATTTCAGCAGACTAATGCGATGGTCACTCTTCGGAAAGAGC
GACTTGCTAAACTCACAGAAGCGATAACAGCAGCATCCTTGCCGAAGACATCAGGCCACT
ATGACGACGACGACGATATTCCCTTTCCGGGTCCGATTAACGATGACGATAACCCGGGTC
ATCAAGACGATGATCCCACAGACTCCCAGGACACCACCATCCCCGATGTAGTTGTGGATC
CTGATGATGGCTCATACGGCGAGTACCAAAGCTATAGTGAGAATGGCATGAACGCCCCGG
ACGATTTGGTATTGTTCGACCTCGATGAAGATGACGAGGATACTAAGCCTGTACCCAACC
GAAGTACCAAGGGCGGCCAGCAAAAAAACAGCCAAAAGGGACAACATATTGAAGGGAGGC
AGACGCAATCCAGACCGATACAAAAtgtcccgggtccccaccgcaccattcaccatgctt
ccgctccactcactgacaatgatagacgaaatgaaccttcaggttccaccagtcctagga
tgctcacccccattaacgaagaggcagatccgctggatgacgcggacgacgagactagta
gccttccgccgcttgagtctgacgacgaagagcaagatagggatggcacatctaaccgga
ctcctaccgtcgcgcctccggccccggtttaccgcgaccactccgaaaagaaggagctcc
cacaggacgagcaacaggaccaagaccatacgcaagaggctagaaatcaagacagtgaca
acacccaatctgagcactcattcgaggagatgtacaggcatatattgaggagccaagggc
cgttcgatgcggtattgtactatcacatgatgaaggacgaaccggtcgtcttttcaacct
ctgacggaaaggagtatacatacccagacagcctcgaggaggagtacccaccatggctta
cggaaaaggaggcgatgaatgaggaaaacaggtttgttacgctcgatgggcagcaattct
actggcctgtaatgaatcataagaataaatttatggcgatactgcaacaccaccaatgag
aattcgagctcatcgatgcatggtacccgggcatgctcgagctagcagatctttttccct
ctgccaaaaattatggggacatcatgaagccccttgagcatctgacttcggctaataaag
gaaatttattttcattgcaatagtgtgtg
(winky) ➜  ZN-1.21 git:(master) ✗ cd ..
(winky) ➜  winky git:(master) ✗ bwa
zsh: command not found: bwa
(winky) ➜  winky git:(master) ✗ conda install bwa
Fetching package metadata ...............
Solving package specifications: .

Package plan for installation in environment /Users/olgabot/anaconda3/envs/winky:

The following NEW packages will be INSTALLED:

    bwa: 0.7.15-1 bioconda

Proceed ([y]/n)? y

(winky) ➜  winky git:(master) ✗ bwa -h
[main] unrecognized command '-h'
(winky) ➜  winky git:(master) ✗ bwa

Program: bwa (alignment via Burrows-Wheeler transformation)
Version: 0.7.15-r1140
Contact: Heng Li <lh3@sanger.ac.uk>

Usage:   bwa <command> [options]

Command: index         index sequences in the FASTA format
         mem           BWA-MEM algorithm
         fastmap       identify super-maximal exact matches
         pemerge       merge overlapping paired ends (EXPERIMENTAL)
         aln           gapped/ungapped alignment
         samse         generate alignment (single ended)
         sampe         generate alignment (paired ended)
         bwasw         BWA-SW for long queries

         shm           manage indices in shared memory
         fa2pac        convert FASTA to PAC format
         pac2bwt       generate BWT from PAC
         pac2bwtgen    alternative algorithm for generating BWT
         bwtupdate     update .bwt to the new format
         bwt2sa        generate SA from BWT and Occ

Note: To use BWA, you need to first index the genome with `bwa index'.
      There are three alignment algorithms in BWA: `mem', `bwasw', and
      `aln/samse/sampe'. If you are not sure which to use, try `bwa mem'
      first. Please `man ./bwa.1' for the manual.

(winky) ➜  winky git:(master) ✗ bwa index notebooks/ZN_refSeq.fasta
[bwa_index] Pack FASTA... 0.00 sec
[bwa_index] Construct BWT for the packed sequence...
[bwa_index] 0.00 seconds elapse.
[bwa_index] Update BWT... 0.00 sec
[bwa_index] Pack forward-only FASTA... 0.00 sec
[bwa_index] Construct SA from BWT and Occ... 0.00 sec
[main] Version: 0.7.15-r1140
[main] CMD: bwa index notebooks/ZN_refSeq.fasta
[main] Real time: 0.007 sec; CPU: 0.006 sec
(winky) ➜  winky git:(master) ✗ ll
total 24
-rw-r--r--   1 olgabot  staff    42B Sep  1 01:41 MANIFEST.in
drwxr-xr-x  10 olgabot  staff   340B Sep  1 02:19 ZN-1.21
drwxr-xr-x@ 25 olgabot  staff   850B Sep  1 02:20 notebooks
-rw-r--r--   1 olgabot  staff     0B Sep  1 01:41 requirements.txt
-rw-r--r--   1 olgabot  staff    62B Sep  1 01:41 setup.cfg
-rw-r--r--   1 olgabot  staff   551B Sep  1 02:12 setup.py
drwxr-xr-x   7 olgabot  staff   238B Sep  1 02:15 winky
drwxr-xr-x   7 olgabot  staff   238B Sep  1 02:12 y.egg-info
(winky) ➜  winky git:(master) ✗ ll notebooks
total 7528
-rw-r--r--  1 olgabot  staff   414K Sep  1 01:39 000_plotting_traces.ipynb
-rwxr-xr-x  1 olgabot  staff   3.6K Aug  3 13:36 CloneQC_DataSet_README.md
-rwxr-xr-x@ 1 olgabot  staff   278K Aug  2 17:04 ZN-1_ZNif1__2017-06-07_B01.ab1
-rwxr-xr-x@ 1 olgabot  staff   277K Aug  2 17:04 ZN-1_ZNir1__2017-06-07_E01.ab1
-rwxr-xr-x@ 1 olgabot  staff   269K Aug  2 17:04 ZN-1_pCAGGSf__2017-05-31_A06.ab1
-rwxr-xr-x@ 1 olgabot  staff   268K Aug  2 17:04 ZN-1_pCAGGSr__2017-05-31_G03.ab1
-rwxr-xr-x@ 1 olgabot  staff   278K Aug  2 17:04 ZN-2_ZNif1__2017-06-07_C01.ab1
-rwxr-xr-x@ 1 olgabot  staff   278K Aug  2 17:04 ZN-2_ZNir1__2017-06-07_F01.ab1
-rwxr-xr-x@ 1 olgabot  staff   269K Aug  2 17:04 ZN-2_pCAGGSf__2017-05-31_B06.ab1
-rwxr-xr-x@ 1 olgabot  staff   268K Aug  2 17:04 ZN-2_pCAGGSr__2017-05-31_H03.ab1
-rwxr-xr-x@ 1 olgabot  staff   277K Aug  2 17:04 ZN-3_ZNif1__2017-06-07_D01.ab1
-rwxr-xr-x@ 1 olgabot  staff   277K Aug  2 17:04 ZN-3_ZNir1__2017-06-07_G01.ab1
-rwxr-xr-x@ 1 olgabot  staff   269K Aug  2 17:04 ZN-3_pCAGGSf__2017-05-31_C06.ab1
-rwxr-xr-x@ 1 olgabot  staff   269K Aug  2 17:04 ZN-3_pCAGGSr__2017-05-31_A04.ab1
-rwxr-xr-x@ 1 olgabot  staff   2.3K Aug  2 17:04 ZN_refSeq.fasta
-rw-r--r--  1 olgabot  staff     9B Sep  1 02:20 ZN_refSeq.fasta.amb
-rw-r--r--  1 olgabot  staff    88B Sep  1 02:20 ZN_refSeq.fasta.ann
-rw-r--r--  1 olgabot  staff   2.3K Sep  1 02:20 ZN_refSeq.fasta.bwt
-rw-r--r--  1 olgabot  staff   569B Sep  1 02:20 ZN_refSeq.fasta.pac
-rw-r--r--  1 olgabot  staff   1.2K Sep  1 02:20 ZN_refSeq.fasta.sa
-rw-r--r--  1 olgabot  staff   1.9K Sep  1 01:38 example.fastq
-rw-r--r--  1 olgabot  staff   915B Aug  3 14:00 sanger.py
(winky) ➜  winky git:(master) ✗ bwa aln

Usage:   bwa aln [options] <prefix> <in.fq>

Options: -n NUM    max #diff (int) or missing prob under 0.02 err rate (float) [0.04]
         -o INT    maximum number or fraction of gap opens [1]
         -e INT    maximum number of gap extensions, -1 for disabling long gaps [-1]
         -i INT    do not put an indel within INT bp towards the ends [5]
         -d INT    maximum occurrences for extending a long deletion [10]
         -l INT    seed length [32]
         -k INT    maximum differences in the seed [2]
         -m INT    maximum entries in the queue [2000000]
         -t INT    number of threads [1]
         -M INT    mismatch penalty [3]
         -O INT    gap open penalty [11]
         -E INT    gap extension penalty [4]
         -R INT    stop searching when there are >INT equally best hits [30]
         -q INT    quality threshold for read trimming down to 35bp [0]
         -f FILE   file to write output to instead of stdout
         -B INT    length of barcode
         -L        log-scaled gap penalty for long deletions
         -N        non-iterative mode: search for all n-difference hits (slooow)
         -I        the input is in the Illumina 1.3+ FASTQ-like format
         -b        the input read file is in the BAM format
         -0        use single-end reads only (effective with -b)
         -1        use the 1st read in a pair (effective with -b)
         -2        use the 2nd read in a pair (effective with -b)
         -Y        filter Casava-filtered sequences

(winky) ➜  winky git:(master) ✗ bwa aln notebooks/ZN_refSeq.fasta winky/test/data/ZN-1_*fastq
[bwa_aln] 17bp reads: max_diff = 2
[bwa_aln] 38bp reads: max_diff = 3
[bwa_aln] 64bp reads: max_diff = 4
[bwa_aln] 93bp reads: max_diff = 5
[bwa_aln] 124bp reads: max_diff = 6
[bwa_aln] 157bp reads: max_diff = 7
[bwa_aln] 190bp reads: max_diff = 8
[bwa_aln] 225bp reads: max_diff = 9
SAI

??
[bwa_aln_core] calculate SA coordinate... 0.00 sec
[bwa_aln_core] write to the disk... 0.00 sec
[bwa_aln_core] 1 sequences have been processed.
?#=???? [main] Version: 0.7.15-r1140
[main] CMD: bwa aln notebooks/ZN_refSeq.fasta winky/test/data/ZN-1_ZNif1__2017-06-07_B01.fastq winky/test/data/ZN-1_ZNir1__2017-06-07_E01.fastq winky/test/data/ZN-1_pCAGGSf__2017-05-31_A06.fastq winky/test/data/ZN-1_pCAGGSr__2017-05-31_G03.fastq
[main] Real time: 0.042 sec; CPU: 0.039 sec
(winky) ➜  winky git:(master) ✗ cat winky/test/data/ZN-1_*.fastq > winky/test/data/ZN-1-concatenated.fastq
(winky) ➜  winky git:(master) ✗ bwa aln notebooks/ZN_refSeq.fasta winky/test/data/ZN-1-concatenated.fastq
[bwa_aln] 17bp reads: max_diff = 2
[bwa_aln] 38bp reads: max_diff = 3
[bwa_aln] 64bp reads: max_diff = 4
[bwa_aln] 93bp reads: max_diff = 5
[bwa_aln] 124bp reads: max_diff = 6
[bwa_aln] 157bp reads: max_diff = 7
[bwa_aln] 190bp reads: max_diff = 8
[bwa_aln] 225bp reads: max_diff = 9
SAI

??
[bwa_aln_core] calculate SA coordinate... 0.00 sec
[bwa_aln_core] write to the disk... 0.00 sec
[bwa_aln_core] 4 sequences have been processed.
?#=???? [main] Version: 0.7.15-r1140
[main] CMD: bwa aln notebooks/ZN_refSeq.fasta winky/test/data/ZN-1-concatenated.fastq
[main] Real time: 0.036 sec; CPU: 0.036 sec
(winky) ➜  winky git:(master) ✗
```