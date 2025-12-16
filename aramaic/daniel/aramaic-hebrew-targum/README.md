# Readme

## Text info


### Gordon Hebrew translation

Taking the beautiful Hebrew translation by Gordon of Daniel's Aramaic text (Ezra too?), I got the whole text of all chapters 2-7, and cleaned it up into a usable format. Note there were two instances with an extraneous new line that threw the script off, (one in ch 2, one in ch 6).

https://he.wikisource.org/w/index.php?title=%D7%93%D7%A0%D7%99%D7%90%D7%9C_%D7%91%D7%AA%D7%A8%D7%92%D7%95%D7%9D_%D7%A2%D7%91%D7%A8%D7%99_(%D7%92%D7%95%D7%A8%D7%93%D7%95%D7%9F)&action=edit


### Masoretic unicode MT (Aramaic) text

Got from here:

https://tanach.us/Server.html?Dan2:1-2:49&layout=Full&view=1&content=Accents&font=24&Englishfontsize=18&fontfamily=Taamey%20D%20Web&dh=Off&Brief=0

Can only do one chap at a time I think, and had to have a LOT of cleanup to make usable from bad unicode mess characters.

Then per chapter enter in like this:

https://tanach.us/Server.txt?Dan2:1-2:49&layout=Full&content=Accents

ie. `2:1-2:49` have to fill that out for each chapter, then did for all 6 chapters, and combined and cleaned up into a single usable text. To not have a HUGE mess had to not have verse numbers, but the Gordon text had them and I used that therefore as base.


## Merge script

`cd` into `texts` then:

`python ..\merge_files.py .\daniel-hebrew-trans-gordon.md .\daniel-aramaic-mt.md`

`python merge_files.py .\daniel-hebrew-trans-gordon.md .\daniel-aramaic-mt.md`

RUN example:

```bash
PS aramaic-hebrew-targum>python merge_files.py .\daniel-hebrew-trans-gordon.md .\daniel-aramaic-mt.md
Processing section 1: ## דניאל ב (49 lines)
Processing section 2: ## דניאל ג (33 lines)
Processing section 3: ## דניאל ד (34 lines)
Processing section 4: ## דניאל ה (30 lines)
Processing section 5: ## דניאל ו (29 lines)
Processing section 6: ## דניאל ז (28 lines)
Done! Output written to result-merged.md
```

for info:

`python merge_files.py -h`

