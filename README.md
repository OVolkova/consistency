#Text markup consistency


Reproduction of the article:

Krippendorff, K. (2004). Measuring the Reliability of Qualitative Text Analysis Data. Quality and Quantity, 38 (6), 787-800.

Allows to calculate inter-coder agreement metric Krippendorff’s Alpha for IOB2 text format.

There are two main functions:
 - get_items_from_iob2
 transform IOB2 markup format to items 
 
 - alpha_agreement  
 calculate observed and expected disagreement, alpha if given items of 
 one class for several coders
 
 Example:
```
 		text	coder1	coder2	coder3
0	Germany	        B-LOC	B-LOC	B-LOC
1	's	        I-LOC	O	O
2	representative	O	O	O
3	to	        O	O	O
4	the	        O	O	O
5	European	B-ORG	B-ORG	B-ORG
6	Union	        I-ORG	I-ORG	I-ORG
7	's	        I-ORG	O	O
8	veterinary	O	O	O
9	committee	O	O	O
10	Werner	        B-PER	B-PER	B-PER
11	Zwingmann	I-PER	I-PER	I-PER
12	said	        O	O	O
13	on	        O	O	O
14	Wednesday	O	O	O
15	consumers	O	O	O
16	should	        O	O	O
17	buy	        O	O	O
18	sheepmeat	O	O	O
19	from	        O	O	O
20	countries	O	O	O
21	other	        O	O	O
22	than	        O	O	O
23	Britain	        B-LOC	B-LOC	B-LOC
24	until	        O	O	O
25	the	        O	O	O
26	scientific	O	O	O
27	advice	        O	O	O
28	was	        O	O	O
29	clearer	        O	O	O
30	.	        O	O	O
```

Krippendorff’s Alpha by classes:
```
	    observed disagreement	expected disagreement	Alpha agreement
MISC	    0.0000	                0.0000	                0.0000
LOC	    0.0007	                0.0057	                0.8790
PER	    0.0000	                0.0074	                1.0000
ORG	    0.0007	                0.0101	                0.9311
```

Interpretation of values could be found in Artstein, Ron, and Massimo Poesio. “Inter-Coder Agreement for Computational Linguistics.” Association for Computational Linguistics, vol. 34, no. 4, pp. 555–596.
