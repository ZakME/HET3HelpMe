"""apply option rewrites to study/bank/*.txt.
usage: python -I tools/apply_bank_edits.py <bank dir> <edits file>
edits: one per line, "question substring|old option line|new option line" (option lines keep their +/- prefix)"""
import glob, os, sys
src, ed = sys.argv[1], sys.argv[2]
files = sorted(glob.glob(os.path.join(src, "*.txt")))
data = {f: open(f, encoding="utf-8").read().split("\n") for f in files}
err = 0
for line in open(ed, encoding="utf-8").read().strip().split("\n"):
    if not line.strip() or line.startswith("#"): continue
    key, old, new = line.split("|", 2)
    if old.strip() == new.strip(): continue
    hits = []
    for f, L in data.items():
        for i, l in enumerate(L):
            if l.startswith("Q:") and key in l:
                j = i + 1
                while j < len(L) and not L[j].startswith("@"):
                    if L[j].strip() == old.strip(): hits.append((f, j))
                    j += 1
    if len(hits) != 1: print(len(hits), "hits:", key, "::", old); err += 1; continue
    f, j = hits[0]; data[f][j] = new.strip()
for f, L in data.items(): open(f, "w", encoding="utf-8", newline="\n").write("\n".join(L))
print("errors", err)
