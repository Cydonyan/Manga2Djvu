# Manga2Djvu

A handy-dandy python script to convert chapters downloaded[^1] from mangalib.me to a single DJVU book

***LINUX ONLY***

could be ported to windows, but, bruh, i am not doing that

### Installation

1. Download the script.py and place it anywhere you want
2. Install `python3`, `djvulibre-bin` packages
3. ???
4. Profit!

### Usage

On the top of the script you need to specify:
- `indir` path (thats a path to the directory in which all downloaded chapters are stored and ***nothing else should be there***),
- `outdir` path (a path where all temporary files will be output, ideally it should be empty, but thats not necessary)
- `outfname` (a name of a final DJVU file)
- ***optionally*** you can set a `DPI` parameter which contols, you guessed it, the DPI of the page

After all parameters are specified, launch a python script with `python3 script.py`.(duh)

Then you should sit and wait untill you see "done!" printed

The final book will be in the `outdir` path somwhere between countless "vol" folders

### If something went wrong and it spits a bunch of errors at you:

https://www.python.org/doc/

https://linux.die.net/man/1/djvu

Good luck!

------------

[^1]: Downloading from mangalib.me can be eased by this tampermonkey [script](https://greasyfork.org/ru/scripts/399534-mangalib-download-all-chapters)
