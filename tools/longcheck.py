"""list questions where the correct answer is clearly the longest option.
usage: python -I tools/longcheck.py study/bank [ratio]"""
import glob, os, sys
sys.stdout.reconfigure(encoding="utf-8")
d = sys.argv[1]; ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 1.25
tot = longest = flagged = 0
for f in sorted(glob.glob(os.path.join(d, "*.txt"))):
    q = c = None; w = []
    for line in open(f, encoding="utf-8").read().split("\n"):
        if line.startswith("@"): q = c = None; w = []
        elif line.startswith("Q:"): q = line[2:].strip()
        elif line.startswith("+"): c = line[1:].strip()
        elif line.startswith("-"): w.append(line[1:].strip())
        elif line.startswith("E:"):
            tot += 1
            mw = max(len(x) for x in w)
            if len(c) >= mw: longest += 1
            if len(c) > ratio * mw:
                flagged += 1
                if "-v" in sys.argv:
                    print(f"## {q}\n+ {c}\n" + "".join(f"- {x}\n" for x in w))
print(f"total {tot}, correct is longest {longest} ({longest*100//tot}%), flagged >{ratio}x {flagged}", file=sys.stderr)
