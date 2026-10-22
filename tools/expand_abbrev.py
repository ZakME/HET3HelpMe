"""spell out abbreviations the first time they show up in a question.
usage: python -I tools/expand_abbrev.py [--write]
without --write it only prints what would change."""
import glob, re, sys
sys.stdout.reconfigure(encoding="utf-8")

# abbreviation -> what it stands for
ABBR = {
    "DCV": "directional control valve",
    "ECM": "electronic control module",
    "OEM": "original equipment manufacturer",
    "PWM": "pulse width modulation",
    "ROPS": "roll over protective structure",
    "FOPS": "falling object protective structure",
    "AFFF": "aqueous film-forming foam",
    "PPE": "personal protective equipment",
    "A/C": "air conditioning",
    "PM": "preventive maintenance",
    "HST": "hydrostatic transmission",
    "NFC": "negative flow control",
    "LSPC": "load sensing pressure compensated",
    "LED": "light emitting diode",
    "TDC": "top dead centre",
    "IGBT": "insulated gate bipolar transistor",
    "RTV": "room temperature vulcanizing",
    "HMU": "hand metering unit",
    "UV": "ultraviolet",
    "NTC": "negative temperature coefficient",
    "PTC": "positive temperature coefficient",
    "MID": "message identifier",
    "PID": "parameter identifier",
    "CEMF": "counter-electromotive force",
    "DMM": "digital multimeter",
    "AIT": "Apprenticeship and Industry Training",
    "NOA": "National Occupational Analysis",
    "PTO": "power take-off",
    "HET": "heavy equipment technician",
    "OBD-II": "on-board diagnostics",
    "ILM": "individual learning module",
    "CAN": "controller area network",
    "CAN-H": "CAN high",
    "CAN-L": "CAN low",
    "AC": "alternating current",
    "DC": "direct current",
}
# abbreviations only expanded in the question stem (they show up all over the answers)
STEM_ONLY = set()
# questions where spelling it out would give the answer away
SKIP_Q = ("stands for", "the CRC field", "GVW")

VOWEL_SOUND = re.compile(r"^[aeiouAEIOU]")


def expand_once(text, ab, full, at_start_ok=True):
    """replace the first standalone use of ab in text with 'full (ab)'."""
    tail = r"(?![\w/-])" + (r"(?! [Hh]igh| [Ll]ow)" if ab == "CAN" else "")
    pat = re.compile(r"(?<![\w(/-])" + re.escape(ab) + tail)
    m = pat.search(text)
    if not m:
        return text, False
    pre, post = text[:m.start()], text[m.end():]
    if post.startswith(" ("):  # already defined right after
        return text, False
    rep = full
    if m.start() == 0 or re.search(r"(^|[.:?]\s)$", pre):
        rep = rep[0].upper() + rep[1:]
    # fix a/an in front of it
    art = re.search(r"\b(a|an|A|An)\s$", pre)
    if art:
        want = "an" if VOWEL_SOUND.match(full) else "a"
        if art.group(1)[0].isupper(): want = want.capitalize()
        pre = pre[:art.start(1)] + want + " "
    return pre + rep + " (" + ab + ")" + post, True


def process(lines):
    changes, out, i = [], list(lines), 0
    while i < len(out):
        if out[i].startswith("Q:"):
            j = i + 1
            while j < len(out) and not out[j].startswith("E:") and not out[j].startswith("@"):
                j += 1
            block = "\n".join(out[i:j])
            if not any(s in out[i] for s in SKIP_Q):
                for ab in sorted(ABBR, key=len, reverse=True):
                    if "(" + ab + ")" in block or ABBR[ab].lower() in block.lower():
                        continue
                    new, ok = expand_once(out[i], ab, ABBR[ab])
                    if ok:
                        changes.append((out[i], new)); out[i] = new; block = "\n".join(out[i:j]); continue
                    if ab in STEM_ONLY:
                        continue
                    for k in range(i + 1, j):
                        new, ok = expand_once(out[k][1:].lstrip(), ab, ABBR[ab])
                        if ok:
                            new = out[k][0] + " " + new
                            changes.append((out[k], new)); out[k] = new
            i = j
        else:
            i += 1
    return out, changes


write = "--write" in sys.argv
total = 0
for f in sorted(glob.glob("study/bank/*.txt") + glob.glob("study/bank/ilm/*.txt")):
    lines = open(f, encoding="utf-8").read().split("\n")
    out, ch = process(lines)
    total += len(ch)
    for a, b in ch:
        print(f"{f}\n  - {a}\n  + {b}")
    if write and ch:
        open(f, "w", encoding="utf-8", newline="\n").write("\n".join(out))
print("changes:", total, "(written)" if write else "(dry run)")
