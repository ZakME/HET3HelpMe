# How to use this guide {#intro}

This guide condenses the third period HET notes ([ILM version 24/25 summary by Matéo Lusson](https://docs.google.com/document/d/1Kx0yknuqAoN13r4I1tWwqruwL0g3m-6SA_QDxVSvOqs)) into exam-ready points for all three courses: **301 Hydraulics II**, **302 Steering, Suspension, Accessories, Electrical and Apprenticeship**, and **303 Powertrain**.

Unofficial study help made by an apprentice. It is not from AIT, NAIT or SAIT, and it can have mistakes. Your ILMs are the final word.

Your quiz progress and exam history are saved in your own browser only. Nothing is sent anywhere.

- ==Highlighted== text is what the original notes marked as "has been on tests / likely to be on tests". Learn these first.
- **Bold** is a key term or the part of a fact that gets tested.
- "Exam trap" boxes point out answers that are easy to mix up.
- Where the source notes contradict themselves or have a typo, a "Note" box gives the correct version.

## Exam strategy {#strategy}

- The AIT third period exam is about **120 questions**. Roughly **half are hydraulics (301)**, powertrain (303) is next, and steering/suspension/electrical (302) is the smallest share. Spend your study time the same way.
- AIT and Red Seal style questions come in three flavours (from 302g): **recall** (what is it), **application** (a procedure, at least two steps) and **critical thinking** (cause and effect, the most common on newer exams). Practise all three in the quiz tab.
- For cause-and-effect questions, ask: is this a **flow** problem (speed, cycle time) or a **pressure** problem (force, torque)? That one split answers a lot of hydraulic and transmission questions.
- Diagnostic order the ILMs repeat in nearly every module: **gather information → talk to the operator → visual inspection (oil level and condition first) → operational tests at operating temperature → pressure / flow tests → find the root cause**.
- When two answers look right, pick the one that matches the ILM wording. These exams are written from the ILMs.

## Formula sheet {#formulas}

| Formula | Use | Module |
|---|---|---|
| HP = (GPM × PSI) ÷ 1714 | Hydraulic horsepower | 301a |
| Pressure = Force ÷ Area | Cylinder force, gauge reading | 301a |
| Flow rate = Cylinder volume ÷ Time | Cycle time questions | 301a |
| Pump flow = Displacement × RPM | Pump output | 301b |
| Volumetric eff. % = (Actual flow × 100) ÷ Theoretical flow | Pump wear check | 301b |
| Force (base side) = Piston area × Pressure | Cylinder extend force | 301d |
| Force (rod side) = (Piston area − Rod area) × Pressure | Cylinder retract force | 301d |
| Circuit leakage = Pump full-load flow − Circuit flow | Tee test | 301h |
| % flow loss = (GPM @ 100 psi − GPM @ 1000 psi) ÷ GPM @ 100 psi × 100 | Cushion hitch pump test, over 5% is bad | 302b |
| P = I × E (Watts = Amps × Volts) | Fuse / breaker sizing | 302dA |
| E = I × R, I = E ÷ R, R = E ÷ I | Ohm's law | 302e |
| 1/Rt = 1/R1 + 1/R2 + … | Parallel resistance | 302e |
| Gear ratio = Driven teeth ÷ Drive teeth (written ?:1) | All gearing | 303a |
| Output torque = Input torque × Ratio; Output RPM = Input RPM ÷ Ratio | "Multiply torque, divide RPM" | 303a |
| Total ratio = Ratio 1 × Ratio 2 × … | Multiple reductions | 303a / 303i |
| Planetary: carrier "teeth" = Sun + Ring | Planetary ratio | 303a |
| Wheel torque = Bevel gear torque ÷ 2 | Open differential | 303jA |
| RPM left + RPM right = Bevel gear RPM × 2 | Open differential | 303jA |
| Torque = Force × Lever length | Pinion bearing preload with spring scale | 303jB |

## Key numbers {#numbers}

| Number | What it is |
|---|---|
| 1714 | Hydraulic HP constant |
| 90 | Minimum viscosity index most OEMs recommend |
| 0.5% / 1% water | Oil looks dull or smoky / milky |
| 100 h | Typical short initial service interval (built-in contamination) |
| 12 psia | Pump inlet pressure below this = inlet restriction (cavitation risk) |
| 80% | Pump efficiency below this = repair or replace |
| 2× | Gauge range should be double the expected pressure (most accurate at half scale) |
| 99.8% | Dry nitrogen purity for accumulators and struts |
| 4.2 L in 30 s | Cushion hitch pump drain flow that is too much (if no OEM spec) |
| 5% | Cushion hitch pump flow loss limit |
| 6 months | Typical fire suppression inspection interval |
| 9.6 kb/s | J1587/J1708 baud rate |
| 250 kb/s | J1939 and ISO 11783 CAN baud rate |
| 40 m / 1 m | Max backbone / stub length |
| 20 | Max nodes on J1708 |
| 120 Ω each, 60 Ω total | CAN terminating resistors (measured between CAN-H and CAN-L) |
| 2.5 V | CAN-H and CAN-L at idle (inactive) |
| 0.5 V / 1 V | Max voltage drop for a 12 V / 24 V system |
| 1.265–1.280 @ 27 °C | Battery specific gravity at 100% charge |
| 0.05 | Max specific gravity difference between cells |
| 70% | Red Seal exam pass mark |
| 250 °F (121 °C) | Max torque converter outlet and retarder oil temperature |
| 275 °F (135 °C) | Retarder damage above this |
| 150–180 °F | Transmission oil temperature for testing |
| 30 s | Max stall test duration, then 30 s in neutral to cool |
| 50 V | DC bus must be verified discharged (above 50 V is a hazard) |
| 12 in / 2.5 ft | Electric drive safe working distance with / without PPE |
