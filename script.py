import os
import zipfile

indir = ""
outdir = ""
outfname = "" 
DPI = 212


L = sorted(os.listdir(indir), key = lambda x: int(x.split()[4]))
t = len(L)

os.system(f"mkdir {outdir}")

chapternames = ""
for i in range(len(L)):
	fname = L[i]
	splt = fname.split()
	Volume = int(splt[2])
	Chapter = int(splt[4])
	if os.path.exists(f"{outdir}/vol{Volume}"):
		pass
	else:
		os.makedirs(f"{outdir}/vol{Volume}")
	pagenames = ""
	if os.path.exists(f"{outdir}/vol{Volume}/ch{Chapter}.djvu"):
		print(f"Chapter {Chapter} already exists")
		chapternames += f"{outdir}/vol{Volume}/ch{Chapter}.djvu "
		continue
	with zipfile.ZipFile(f"{indir}/{fname}", mode="r") as archive:
		for file in sorted(archive.namelist(), key = lambda x: int(x.split('.')[0])):
			if file.split('.')[-1] == 'png':
				print("Potentially fucked up page, skipping")
				continue
			archive.extract(file, f"{outdir}/vol{Volume}/ch{Chapter}/")
			os.system(f"convert {outdir}/vol{Volume}/ch{Chapter}/{file} {outdir}/vol{Volume}/ch{Chapter}/{file.split('.')[0]}.pbm")
			os.system(f"rm {outdir}/vol{Volume}/ch{Chapter}/{file}")
			#cjb2 -clean
			os.system(f"cjb2 -clean -dpi {DPI} {outdir}/vol{Volume}/ch{Chapter}/{file.split('.')[0]}.pbm {outdir}/vol{Volume}/ch{Chapter}/{file.split('.')[0]}.djvu")
			pagenames += (f"{outdir}/vol{Volume}/ch{Chapter}/{file.split('.')[0]}.djvu ")
			os.system(f"rm {outdir}/vol{Volume}/ch{Chapter}/{file.split('.')[0]}.pbm")
#			print(f"page {file.split('.')[0]} of chapter {Chapter} made")
			print("I", end = ' ')
	os.system(f"djvm -c {outdir}/vol{Volume}/ch{Chapter}.djvu {pagenames}")
	chapternames += f"{outdir}/vol{Volume}/ch{Chapter}.djvu "
	print(f"\nChapter {Chapter} combined, {int(i*100/t)}% done")
print("Combining final book")
os.system(f"djvm -c {outdir}/{outfname}.djvu {chapternames}")
print("done!")

