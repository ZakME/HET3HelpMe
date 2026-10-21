# HET3HelpMe

study site for alberta heavy equipment tech 3rd period. study guide, practice quizzes and mock AIT style exams for all three courses:

- 301 hydraulics II
- 302 steering, suspension, accessories, electrical + apprenticeship stuff
- 303 powertrain

**use it here: https://het3.zakary.vip**

## what's in it

- **study guide** - every module boiled down to the stuff you need. the facts the notes flagged as "been on tests" are highlighted, and there's a "highlighted facts only" toggle for cramming. also has a formula sheet and a key numbers table up top. search box works too
- **practice quizzes** - 969 questions. you get the answer + an explanation right after each one. a bunch of presets (on the test, calculations, critical thinking, safety, symbols & valves, hydrostatics, planetaries, CAN/networks, weak spots, etc) or build your own from whatever modules you want
- **mock AIT exams** - 6 fixed 100 question exams (same questions every retake so you can see if you're getting better), plus random ones and single course exams. timed (90 sec a question), no answers till you submit, flag questions, then you get your score, a breakdown by course and module (worst first) and a review of everything you missed

your progress and exam history save in your own browser. nothing gets sent anywhere, there's no account or anything.

## using it offline

the whole thing is one file. download `index.html` (or the repo zip), double click it, done. works in chrome, edge, firefox, safari, on phones too. no internet needed after that.

## heads up

- this is unofficial, made by an apprentice. it's not from AIT/NAIT/SAIT and there's probably a mistake or two in here. your ILMs are the final word
- the real AIT exam is about 120 questions. the mocks are 100 but weighted the same way: about half hydraulics, then powertrain, then 302 (steering/suspension/electrical) the least. check the real pass mark and time limit with your school
- where the notes contradicted themselves i went with the ILM version and left a note in the guide

## credits

the guide and most of the questions are built off Matéo Lusson's 3rd period notes (summary of the 24/25 ILMs), which were shared for anyone to use: https://docs.google.com/document/d/1Kx0yknuqAoN13r4I1tWwqruwL0g3m-6SA_QDxVSvOqs

## fixing stuff / adding questions

if you find a wrong answer open an issue or a PR.

- guide sections are in `study/guide/*.md`
- questions are in `study/bank/*.txt` (the extra 303 ones are in `study/bank/ilm/`)
- the page layout + quiz code is `study/app.html`

question format:

```
@303a|Planetary|hl calc
Q: the question
+ the right answer
- wrong answer
- wrong answer
- wrong answer
E: explanation
```

the tags after the second `|` are optional: `hl` (highlighted in the notes), `ct` (critical thinking), `calc`, `safe`, `plan`, `hst`, `net`, `valve`, `fail`. answers get shuffled so it doesn't matter where the right one is.

then rebuild `index.html` (just needs python 3, nothing to install):

```
python tools/build_study.py
```
