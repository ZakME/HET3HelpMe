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

# 301 · Hydraulics II {#c301}

## Hydraulic symbols {#301sym}

The notes give symbols as pictures. These are the standard ISO 1219 / ANSI forms the ILM uses.

| Symbol | Meaning |
|---|---|
| Solid line | ==Main (working) line==: high pressure, high flow |
| Long dashes | ==Pilot line==: low flow, high pressure (a control signal) |
| Short dashes | ==Drain line==: low flow, lower pressure (case drain, leakage) |
| Dash-dot line around several symbols | Enclosure line: the valves inside are one body |
| Dot where lines meet / T junction | Lines are connected (a T is always connected) |
| Lines crossing with no dot (or a hump) | Not connected |
| Solid (filled) triangle | Hydraulic flow / hydraulic energy |
| Hollow triangle | Pneumatic flow |
| Diagonal arrow through a symbol | Variable or adjustable |
| Small arrow at right angles to a flow arrow | Pressure compensated |
| Zig-zag | Spring (with diagonal arrow = adjustable spring) |
| Diamond with a dashed line across it | Filter or strainer |
| Open-top rectangle | Vented reservoir (line drawn to the bottom = below fluid level) |
| Vertical capsule / oval | Accumulator (gas, spring or weight loaded) |
| Circle with a dial line | Pressure gauge |
| Circle, triangle pointing **out** | Pump (two triangles = reversible, arrow through = variable) |
| Circle, triangle pointing **in** | Motor |
| Ball in a V seat | Check valve |
| Pinched lines | Orifice (arrow through = variable orifice) |
| Each square (envelope) on a valve | One valve position |
| Arrow in the envelope offset from the ports | Normally closed pressure valve |
| Arrow connecting the ports | Normally open valve |

- Actuation symbols on the end of a valve: push button, lever, pedal, spring, solenoid (box with diagonal line), hydraulic pilot (triangle on a dashed line), electro-hydraulic (solenoid plus pilot).
- Pressure valves show where they **sense** pressure: internal upstream, internal downstream or external.

> **Exam trap:** pump vs motor. In a pump the triangle points **out** (oil leaves). In a motor it points **in** (oil drives it).

## 301a · Hydraulic principles {#301a}

### Pros and cons
- Advantages: compact, flexible installation, easy cooling and lube, operator controls several functions at once, precise smooth positioning, ==easily protected from overload==.
- Disadvantages: pressurized fluid can injure or kill, noise, leaks (contamination or fire), temperature affects performance, trapped air causes problems.

### Energy and work
- ==**Work** = force acting through a distance.== ==**Energy** = the ability to do work.==
- ==Energy cannot be created or destroyed, only transformed.== Engine: chemical → heat → mechanical. **Pump**: mechanical → hydraulic. **Actuator**: hydraulic → mechanical.
- ==**Kinetic** = movement / motion== (oil flow, supplied by the pump). ==**Potential** = stored energy, creates force (pressure)== (example: accumulator).
- **Bernoulli**: total energy stays constant, so pressure + velocity stays constant. ==High kinetic = low potential; low kinetic = high potential.== This is how an orifice works: it slows flow and raises pressure **before** the orifice.

### Power, pressure and flow
- ==HP = (GPM × PSI) ÷ 1714.== ==Pressure = Force ÷ Area.== Pressure is created by **resistance to flow** (psi or kPa).
- ==Flow rate = Cylinder volume ÷ Time.==
- ==Efficiency = output power compared with input power (%).==

### Losses
- ==A difference in potential energy creates flow== (high to low). That pressure drop does no useful work and becomes **heat** (from fluid friction). More pressure loss = more heat.
- ==**Laminar flow**: smooth, straight parallel lines, no turbulence, low friction.== ==Turbulence creates pressure losses.== Caused by lines too small, sharp changes in cross-section, sharp changes in direction.
- ==**Backpressure** = resistance to flow on the **return** side.== Raises internal resistance, lowers efficiency.
- **Flow losses** = excessive internal leakage. ==Complaint will be **slower actuator operation**.==

### Series vs parallel circuits
| | Series | Parallel |
|---|---|---|
| Flow path | ==Only one path== | ==Flow is divided== |
| Each actuator gets | Full flow, reduced pressure | Split flow, identical pressure |
| Motors | ==Higher speed, lower torque== | ==Lower speed, higher torque== |
| Note | | ==Pressure set by the easiest-to-move actuator== |

- Series-parallel: motors in series switch to parallel as load rises (more torque).

### Hydraulic fluids
- **Petroleum**: most common, flammable. ==Dispose of where it cannot reach ground or water.==
- Fire resistant: ==water-oil emulsion== (60% water, 40% oil), ==invert emulsion== (40% water, 60% oil). Water lubricates poorly, grows bacteria, freezes, foams. ==Water glycol==: like coolant (60% glycol / 40% water), better in cold and fire, less lubricating.
- **Phosphate ester** (synthetic): most fire resistant, most expensive, ==not compatible with nitrile rubber== (use Teflon-type seals), forms acids with water.
- **Biodegradable**: 70–80% broken down by microorganisms, harmless to organisms, poor temperature range.
- ==**Viscosity** = resistance to flow== (sets lubricating ability; higher viscosity = thicker film).
- ==**Viscosity index** = how much viscosity changes with temperature.== ==High VI = small change; low VI = large change.== Most OEMs want **90 minimum**.
- **Oxidation** = combining with oxygen; forms soaps and weak acids; heat speeds it up. ==Oxidized oil is darker and smells burnt.==
- ==**Demulsification** = ability to separate water.== 0.5% water = dull/smoky; 1%+ = milky.

### Contamination
- ==**Built-in**: present on new or rebuilt machines== (casting sand, wear-in). Reason initial service is short (~100 h).
- ==**Ingressed**== (from outside): faulty breathers, leaking pump inlet, ==cylinder wiper seals== (fine dirt pulled in as rods retract), ==unclean maintenance (the most common cause)==.
- **Internally generated**: wear, fatigue, cavitation, oxidation.
- Failures: ==**catastrophic**== (sudden total failure, "grenading"), ==**intermittent**== (comes and goes; ==transient, can move from component to component==, may self-correct), ==**degradation**== (gradual wear).

## 301b · Hydraulic pump fundamentals {#301b}

- ==A pump converts mechanical energy into hydraulic energy; it takes power from the prime mover and **generates flow**== (it does not make pressure).
- ==Displacement = internal volume== per revolution (in³/rev or cc/rev).
- ==**Positive displacement**: sealed between inlet and outlet; delivers a nearly constant volume regardless of resistance.== ==All hydraulic pumps are positive displacement.== Non-positive (engine water pump): inlet and outlet connected, high flow, low pressure.
- ==Max flow is directly proportional to speed.== ==Flow = displacement × RPM.== Too much speed can cause cavitation.

### Efficiency
- **Mechanical**: theoretical vs actual torque; ==power needed to overcome internal friction==.
- **Volumetric**: theoretical vs actual flow; ==set by internal leakage==; poor volumetric efficiency = longer cycle times. VE % = actual × 100 ÷ theoretical (or no-load vs full-load flow).
- ==**Overall**: input power vs delivered power== (mechanical + flow losses). Peaks at normal operating pressure, ==drops at higher pressure because internal leakage increases==.

### Pump basics
- ==Rotation is always viewed from the driveshaft end.==
- ==**Uni-directional**: built to rotate one way== (inlet usually larger than outlet; may need internal changes to reverse).
- ==**Bi-directional**: inlet and outlet the same size==, runs either rotation.
- ==**Reversible**: reverses oil flow direction while the driveshaft keeps turning the same way.==

> **Note:** the ILM uses "bi-directional" and "reversible" interchangeably. Read the question carefully.

- ==**Fixed** displacement: same volume every revolution== (gear, vane or piston). ==**Variable**: chamber volume can change== (vane or piston only).
- **Balanced**: inlet/outlet thrust loads cancel. ==**Unbalanced**: inlet and outlet forces create a thrust (side) load.==
- ==**Pressure compensated**: flow adjusted automatically by outlet pressure.==
- ==Internal leakage: some is needed for lubrication==; it reduces flow for work (slower motors). **Slip** = leakage from the high to low pressure side. ==Higher pressure = more leakage.==
- ==**Case drain** returns internal leakage to the reservoir== (often gravity fed). ==Port goes on the **top** so the case stays flooded.== **Required on piston pumps**; gear and vane pumps route leakage internally to the inlet.

### Gear pumps (external)
- Simple, cheap, rugged, tolerate dirt; low max pressure; fixed displacement only.
- ==Drive gear (from power source) meshes with the driven gear.== ==Pressure plate limits leakage at the gear faces.==
- ==Oil is carried around the **outside** of the housing in the tooth pockets, inlet to outlet.==
- Unbalanced: ==inlet and outlet forces oppose on all but one tooth==.
- ==**Outlet** = gears coming **into** mesh. **Inlet** = gears coming **out of** mesh.==

### Vane pumps
- ==More efficient and higher pressure than gear pumps==; more expensive and more sensitive to dirt.
- ==Rotor = slotted cylinder (driven); vanes = sliding plates in the slots;== ==vane pocket = space between two vanes that carries oil==.
- ==Vanes held out by **centrifugal force** plus **outlet pressure** ported under the vane== (some have small springs for start-up).
- ==**Bevelled** vane: high point is the leading edge; used at high speed and pressure; uni-directional only (cannot be used in bi-directional pumps).== Rounded tips = bi-directional.
- ==**Intra-vane**: adjusts vane loading as it passes inlet and outlet.==
- ==Cam ring = riding surface for vanes== (elliptical or circular). ==Pressure plates control rotor-face clearance.== **Cartridge** = cam ring, rotor, vanes and plates as one unit.
- ==**Unbalanced**: circular cam ring, rotor offset.== Variable displacement is always unbalanced: the cam ring moves to change eccentricity (centred = zero flow); may be pressure compensated.
- ==**Balanced**: elliptical cam ring, two opposing inlets and two opposing outlets== → higher pressure.

### Piston pumps
- ==Reciprocating motion; most efficient and highest pressure; very sensitive to contamination; used when variable displacement is needed.== Charge pumps often used to prevent cavitation.
- ==**Radial**: pistons perpendicular (90°) to the driveshaft.== ==Check valves on each piston's inlet and outlet.== ==**Rotating cam**== (fixed pistons, rotating lobe) or ==**rotating piston**== (pistons in a rotating block against a cam ring).
- **Axial**: ==most common in mobile equipment; pistons parallel to the driveshaft; barrel turns, pistons slide on a swash plate.== ==Swash plate angle sets stroke length, so more angle = more displacement.== Drilled piston passages ==balance the piston and lubricate the shoes==.
- ==**Pressure compensated** axial pump: system pressure acts on the compensator.== ==**Bias** piston + spring pushes toward **maximum** displacement.== ==**Stroking** piston (large, pressure controlled) pushes toward **zero** displacement== (swash plate flat). No relief valve needed because the pump destrokes itself.
- ==**Reversible**: swash plate angle is reversed== (manual or hydraulic).
- **Bent axis**: housing angled to driveshaft; ==pistons held by ball joints, not sliding on a swash plate==; more reliable; variable by changing the barrel-to-shaft angle.

## 301c · Hydraulic pump service {#301c}

- Start-up: ==back off pressure controls== (prevents overload), ==idle, load to warm oil, check max engine speed, test==.
- ==After a component failure==: change oil and filters, clean the reservoir, flush the system as needed. Check the shaft slides freely in the coupling, check rotation, ==mark all mated parts and housings==, ==pre-lubricate the pump before start-up== (fill and turn by hand).

### Failure analysis
| Failure | Evidence | Typical cause |
|---|---|---|
| ==Overloading== | Broken housings or shafts, seal leaks | Excessive system pressure |
| ==Contamination (greatest cause)== | Sandblasted, dull internals, scoring | Dirty oil; check filters |
| ==Cavitation== | ==Pitting== on internal surfaces | Wrong oil, ==inlet restriction==, excessive speed |
| ==Lack of lubrication== | Heavy wear, ==blue spots (overheating)==, smearing, seizure | Low or wrong oil, severe aeration |

- Gear pump: mark housings and gears. ==Inlet = out of mesh, outlet = into mesh.== ==The pressure plate trap (relief groove) is on the outlet side.== Aluminum housings are designed to be cut by the gears during break-in (==tiny clearance==). Trap groove gives trapped oil an escape (less noise, better performance).
- Vane pump: ==cam ring inlet and outlet must be in the correct position==; backwards = low or no flow and cavitation.
- Piston pump: pistons are mated to their original bores.

## 301d · Hydraulic actuator fundamentals {#301d}

### Cylinders
- ==Convert hydraulic energy into **linear** mechanical energy.==
- Parts: barrel (honed, maybe chromed), rod end cap/gland (seals and wiper), piston and rod, seals, bearings. ==Wiper seal keeps contaminants out.==
- Base side force = piston area × pressure. Rod side force = (piston area − rod area) × pressure. ==Smaller cylinders extend faster (less volume to fill).==
- ==**Single acting**: powered one way, external force returns it.== Ram type: oil passes the piston, sealed by packing at the end. **Telescoping**: ==stages fitted inside each other==, each stage less force and more speed; ==the largest (first) stage moves first==.
- ==**Double acting**: powered both ways.== Single rod (differential): ==extension = more force, slower; retraction = less force, faster.==
- ==Internal leakage reduces speed (longer cycle times).== Pressure equalizes both sides so only the rod area produces force.
- ==**Drift**: a leaking cylinder drifts toward **extension**.== ==**Pressure intensification**: the cylinder cannot drift to retract, and pressure inside can rise **higher than system pressure**== (excavators especially).
- ==Double rod (non-differential): equal area and volume both sides → same force and speed both ways.==
- Double-acting telescoping (haul trucks): last stage out is first back in.
- ==**Piston relief valve**: lets oil bypass when the piston bottoms== (a double check valve in the piston; used where the reservoir is small).
- ==**Cushions** slow the cylinder at end of stroke== (plunger restricts return oil, or drillings get blocked progressively).
- ==**Quick drop valve**: faster lowering by **regeneration**== (rod-end oil fed to the base end in full lower; in parallel with the actuator).

### Motors
- ==Convert hydraulic energy into **rotary** mechanical energy.==
- ==Speed (RPM) depends on inlet flow and displacement.== More flow = faster; more displacement = slower.
- ==Torque depends on inlet pressure and displacement.== More pressure or displacement = more torque.
- ==Inlet pressure is set by the resistance on the motor shaft.==
- ==Same port sizes = bi-directional; different = uni-directional.== ==Motors need a case drain.==

| Motor | Key facts |
|---|---|
| ==External gear== | ==Poor torque generators== (forces oppose on all but one tooth), fixed |
| ==Gerotor (orbit)== | ==Low RPM, high torque==, fixed; star gear in an internal gear; ==spool valve on the shaft is timed to the gerotor== |
| ==Geroller== | Same as gerotor but rollers as lobes (less friction, wear); ==disc valve instead of spool valve== |
| ==Vane== | ==Needs springs to hold vanes on the cam ring at start-up==; variable versions can't be balanced; reverse by reversing flow |
| ==Piston== | ==Most efficient, highest RPM and torque==; mostly fixed |
| Axial piston | ==Odd number of pistons (less pulsation)==; variable swash plate ==can never go flat (motor would freewheel/stall)==; may be pressure compensated (==displacement changes with load==) |
| Bent axis | ==Ball joints, not sliding shoes==; bigger angle = slower, more torque; tracked excavator propel |
| ==Radial piston== | ==Low RPM, high torque==; ==crankshaft type (eccentric pushes pistons out)== or ==cam type (pistons ride the inside of a cam)==; balanced |

## 301e · Hydraulic actuator service {#301e}

- Cylinder problems: external leaks, internal leaks, structural damage. ==Internal leakage makes heat during movement.==
- ==Internal leak test: stall the cylinder and remove the return line==; very little oil should come out.
- Remove: depressurize, follow OEM, use lifting gear. ==Never use compressed air to force the piston out.==
- Inspection: hone the barrel, compare ID to spec, re-chrome rod if needed. ==Check rod straightness==: straightedge (quick) or ==V-blocks and a dial indicator (accurate)==.
- Assembly: ==soften seals in warm water or oil==, ==light coat of oil==, ==torque the piston retaining fastener to spec== (a loose piston = catastrophic failure). Reversed lines = backwards operation.
- Testing: ==use pressurized oil, never compressed air==. ==Final test = cycle times.==
- Motors: ==release pressure==, keep clean, ==component failure contaminates the system== (oil, filters, reservoir, flush). Mark housings and mated parts.
- Motor cavitation: ==pitting==, happens when the ==load overruns the motor== (motor spins faster than the pump supplies).
- Install: ==pre-lubricate the motor== (flood it). Start-up: ==back off controls==, idle, warm, ==slowly apply pressure and check for leaks==. Don't run with leaks or odd noises.

## 301f · Hydraulic valves II {#301f}

### Pressure control valve basics (Part A)
- ==Normal position = state with no pressure in the system== (spring returns it). ==NO = flow unrestricted in normal position; NC = flow blocked.==
- ==PCV jobs: limit/regulate pressure==, create a pressure condition, sequence actuators.
- ==Balances spring force against oil pressure.== Spring cavity must drain to the reservoir (or it hydraulically locks). ==Externally drained = outlet is under pressure; internally drained = outlet goes to tank.==
- ==**Modulation** = constant opening and closing.== ==**Spring constant** = stiffness.== ==**Cracking pressure** = pressure where oil starts to flow.== ==**Full flow** = fully open.== ==**Pressure override** = full flow pressure − cracking pressure.==
- ==Upstream = before the valve; downstream = after.==
- ==**Direct acting**: pressure directly against the spring== (low flow uses).
- ==**Pilot operated**: two poppets.== ==Pilot poppet = low flow, high pressure (strong spring, small poppet).== ==Main poppet = high flow, low pressure (weak spring, large poppet).== ==Main spring sets the override.== ==Main advantage: minimizes pressure override==; more accurate, less chatter, higher range.

| Valve | Function | Location / notes |
|---|---|---|
| Main relief | Limits max **system** pressure | Parallel with pump and DCV; often in DCV; ==often pilot operated==; high flow |
| Circuit relief | Limits max **circuit** pressure | After the DCV; ==protects actuators from shock loads with the DCV in neutral==; ==often direct acting==; set **higher** than system relief; ==tested at cracking pressure== (==hand pump== or ==temporarily raise system pressure==) |
| Unloader | ==Returns full pump flow to tank nearly unrestricted== | ==Takes the place of the relief valve== in closed centre with fixed pump; ==needs a check valve upstream== (accumulator downstream); ==hi-lo tandem pumps: opens under low load== to unload one pump |
| ==Pressure reducing== | One circuit runs below system pressure | ==In series; normally open==; controls actuator force; bypass check for reverse flow |
| Sequence | Actions happen in a set order | Keeps pressure in the primary circuit while the secondary works |
| Counterbalance | ==Controls lowering speed== (safety) | Series in actuator return; ==internal pilot==; load weight must be known; poor with varying loads |
| Brake valve | Stops a load overspeeding a motor | Series with motor; ==pilot from the opposite work line==; check valve needed with reversible motor |
| Lock valve | Holds a suspended load if a line leaks | ==Prevents drift with DCV in neutral==; usually not adjustable |

- Relief service: gauge in **parallel**, warm oil, stall, compare, adjust, retest. ==Main relief adjusted at **high idle**== with gauge at the pump outlet.
- ==Backpressure valves restrict return oil to control actuators (a safety valve).== Be careful in the rod end: ==pressure intensification==.

### Flow controls
- ==Control actuator **speed** by controlling input flow.== ==An orifice restricts flow and causes a pressure drop.== ==Pressure after the orifice = the load after it.==
- ==Orifice flow depends on size and shape, pressure drop, and oil viscosity.== May be temperature compensated.

| Type | Key points |
|---|---|
| Bypass type | ==Sends excess flow to the reservoir==; fed by a fixed pump; ==meter-in only== |
| Non-compensated | ==Flow varies with load== (more load = less flow) |
| ==Pressure compensated== | ==Constant flow through the orifice==; ==flow set by orifice size and pressure drop==; compensator senses downstream |
| Restrictor PC | More efficient than bypass; ==stronger spring = more drop== |
| ==Meter-in== | Controls flow **into** the actuator; use when the ==load opposes== the actuator; ==can cause cavitation if the load runs with it== |
| ==Meter-out== | Controls flow **out**; for loads that change direction and size; ==can cause intensification, worst on a cylinder's rod outlet== |
| ==Priority divider== | ==All flow to the priority circuit until satisfied==, then secondary (steering, transmission) |
| ==Proportional divider== | ==Splits flow== by orifice size; constant regardless of pressure |

### Accumulators
- ==Functions: energy storage, react to pressure fluctuations, shock absorption, gradual pressure build-up, constant pressure maintenance.==
- ==Always discharge before service.==
- Weighted (most basic, constant force), spring (==force not constant==), ==gas charged (most common) with **nitrogen**==: piston or bladder type.
- ==Never use oxygen or compressed air== (can explode with oil).

### Directional control valves (Part B)
- ==Classified by **flow paths (ways)**, **positions**, actuation and detents.== Types: poppet (==simple check valve==), rotary spool (==high leakage, low pressure and flow==), ==sliding spool (most common, linear)==. Spool and housing are a **matched set**.
- Lands have grooves (lube, sealing, centring). ==Metering notches = "U" cuts at land edges for **feathering**.== ==Centering spring returns the spool to neutral.==
- Positions = number of envelopes. ==**Hold** = work ports blocked (hydrostatic lock).== ==**Float** = work ports to tank.== ==Diverter = 2-position 3-way, picks which of two circuits gets flow.==
- ==Ways = how many lines connect to the valve.==

| Centre | Notes |
|---|---|
| Closed centre | Needs a ==PC variable pump== or a ==fixed pump + unloader== |
| Open work ports (==motor spool / float centre==, H-spool) | Lets ==brake valves== in the work lines control a motor |
| Tandem (open centre) | Fixed pumps; valves can be in series |
| Closed work ports (==hold==) | Locks the actuator |
| Float | 4-position valves; implement follows the ground |
| Regen centre | ==Not in the ILM==; faster speed in place of a regen valve |

- Actuation: ==mechanical (lever, pedal, button)==, ==pilot (hydraulic or air)== for remote valves (pilot pump, pilot relief, ==pressure regulating controller==), ==electric solenoid==: ==electrical = on/off (no feathering); electronic = infinitely variable==; ==combinations== (electric-over-pilot gives feathering and force).
- ==Detents hold the spool in position== (ball and spring, or electromagnet).
- ==**Load check**: stops a suspended load dropping momentarily when going from hold to raise.== ==**Anti-cavitation check**: prevents a void when the load drives the actuator faster than the pump supplies (tank oil fills in).== **Flow compensator**: constant pressure drop across the spool so several valves work at once.
- Banks: unibody or stacks. **Power beyond** extends the series passage to another DCV (main has priority). Closed centre banks are in parallel.
- ==Series passageway: first valve has priority; downstream valves lose flow.== Tandem: return oil feeds the next valve (actuators in series). ==Series-parallel: series in neutral, parallel when operated together, lightest load has priority.== ==Diverter valve: DCVs cannot work at the same time.==

## 301g · Hydraulic system types {#301g}

- ==**System** = all interconnected components; **circuit** = a group within a system for one function.==
- ==Variable pumps vary flow with demand==; ==pump HP must be limited so the engine doesn't stall== (reduce pressure or flow).

### Open centre
- ==Pump flow returns to tank with the DCV in neutral.== Usually ==fixed displacement==. ==**Constant flow**: delivers flow even with no work.==
- ==Pump pressure = load resistance.== ==Neutral DCV = low resistance.==
- ==Best for systems **not** used for a high % of the duty cycle== (wastes power at low demand and high RPM).
- ==**Constant horsepower**: regulates pump flow by load, keeps max HP, high displacement at low pressure and destrokes as pressure rises.== Keeps engine speed constant; fast at light loads. Often side-by-side pumps. ==Any rise in the three regulator pressures destrokes the pump==: NFC (==monitors flow through each DCV bank==), PRV/power shift (==ECM controlled, set by engine speed dial==), cross-sensing (the other pump's outlet).

### Closed centre
- ==Blocks flow with the DCV in neutral==; holds the system at max pressure. Fixed pump + unloader, or variable pump. Relief is a backup, set **higher** than the compensator.
- ==**Demand flow**: flow only when needed for work.== Pressure compensated: limits flow, not pressure.
- ==**Load sensing**: exact flow for the load.== **Margin pressure**: pump is kept slightly above load pressure.
  - ==Standby: margin pressure only at the pump; no pressure at the load.==
  - ==Moving: pump pressure = load + margin.==
  - ==Stalled: pump at max (set by the pressure compensator), same as load.==
- LSPC parts: pump, ==stroking piston (destrokes)==, ==pressure compensator (sets max system pressure, opens on stall)==, ==flow compensator (keeps margin)==, load sense line, DCV, actuator, ==bias spring/piston (upstrokes)==.

### Hydrostatic transmissions
- ==Pump + motor; usually propel.== ==Highest speed = min motor + max pump displacement. Lowest = max motor + min pump.== ==More motor displacement = more torque.==
- ==**Open loop**: pump from tank, motor back to tank== (DCV reverses). ==**Closed loop**: motor outlet to pump inlet, no path to tank== (reversible pump reverses).
- ==Most common: closed loop, variable pump, fixed motor.==
- Advantages: infinite speed control, quick response, hydrostatic lock at zero, ==automatic braking== (load can't overrun).
- ==Flushing valve: pulls hot oil from the low side through the motor case to cool; only works when the motor turns.== Oil is hottest at the motor outlet.
- ==Crossover relief: dumps high side to low side; set wrong = drift under load.==
- Isolation checks let charge oil into the low side only. **Charge pump** (gear) replaces leakage, prevents HST pump cavitation.
- ==Flushing/hot oil relief is set **lower** than the charge relief.== ==Joysticks must be calibrated.==

## 301h · Hydraulic system testing and service {#301h}

- Troubleshooting: information, ==operator==, visual (==oil level and condition==, leaks, damage, wear), check filter for contamination.
- ==Warm oil to operating temperature first== (open centre: stall an actuator at full throttle).
- ==Cycle time at full throttle== = quick check for flow loss. ==If slow, always check engine RPM first.== Slow cycles = internal leakage.
- ==Stall tests==: engine speed at max load, ==several actuators and directions== (system vs circuit problem).
  - ==Excessive RPM drop==: weak engine, or relief set too **high**.
  - ==No RPM drop==: engine power increased, or relief set too **low**.
  - ==Closed centre: engine should **not** labour at stall== (if it does: unloader or compensator fault).
- ==**Flow problems affect speed; pressure problems affect force.==**
- Safety: lower loads, relieve tank pressure, discharge accumulators.

### Gauges
- Bourdon tube straightens under pressure. Protect with ==snubber (inlet orifice)== or ==glycerine fill (damps needle vibration)==.
- ==Choose a gauge twice the expected pressure== (accurate at mid scale). ==Install in **parallel**.== Compound = vacuum + pressure. Absolute = psia.

### What readings mean
| Test | Reading → meaning |
|---|---|
| ==Pump inlet== | The pump normally pulls a slight vacuum here. ==Below 12 psia: restricted inlet==, too fast, wrong oil (pulling too hard, so cavitation). ==Higher: inlet line leaking air== (air fills in the vacuum, so aeration) |
| ==Pump outlet== | System resistance, friction, ==return line and filter resistance== |
| Neutral | ==Should be as low as possible== |
| Working, no load | ==Load from friction== |
| Max system | ==Low: relief faulty/set low. High: relief faulty/set high or outlet restriction== |
| Closed centre | ==Load sensing pilot pressure== (operates the compensator) |
| HST | ==Charge pump inlet/outlet==, loop pressure both sides, ==case drain== (high = damage) |

### Leakage tests
- ==Cylinder drift = movement with the unit stopped== (tape on rod; excavator bucket tip to ground measures all cylinders).
- ==A leaking component gets hotter faster== (infrared/digital thermometer).
- ==Motor: remove drain line, stall at full throttle, measure drain flow for 10 s.== ==Cylinder: stall and remove the opposite line.==
- Flowmeter: in a test unit with a load valve. Downsides: slow, system opened, contamination risk.
- ==Pump efficiency: flowmeter in series; below 80% = repair or replace.== High case drain flow = wear.
- ==Circuit leakage (tee test): flowmeter in parallel between pump outlet and return; leakage = full-load pump flow − circuit flow.== Can also find relief cracking and full flow.
- Faults: learn the system, easy checks first, ==speed = flow, force = pressure==, ==fix the root cause or the new part fails too==.

## 301i · Electrohydraulics {#301i}

- ==Electrical = on/off; electronic = variable.==
- Electrical control: battery, protection, key switch, relays, controls, solenoids (==discrete: on or off==), ==clamping diodes (absorb induced voltage, stop relay arcing)==, harness. ==Proximity switch closes the circuit when a metal plate passes.==
- ==Electronic systems use less than system voltage (5 V).== Faster, more accurate, less maintenance, better over distance, self-diagnostics.
- Inputs: ==reference-voltage sensors (5 V out, return measured)==, ==variable (resistor type: temperature, joystick potentiometer)==, ==discrete (on/off switches)==, ==voltage generating (speed sensors)==.
- ==Outputs: a typical solenoid is discrete; a proportional solenoid moves in proportion to the signal== (PWM).
- ==**Open loop**: no feedback. **Closed loop**: feedback sensors== for accurate position, speed, acceleration. Servo valve mimics operator input; torque motor gives limited rotation.
- ==Much less tolerant of contamination== (tight tolerances).
- ==**PWM** = digital on/off signal; duty cycle = % on time; reduces heat (less average current).==
- **Hysteresis**: spool needs more current one way than the other. ==**Stiction** = more effort to start a spool moving==; cure = **dither** (constant small oscillation).
- ==Talk to the operator: most important information source.==
- Protect the ECM: unplug when welding, no fast charging with ECM connected, never disconnect batteries with engine running, don't unplug while operating, keep it cool.

# 302 · Steering, Suspension, Accessories, Electrical and Apprenticeship {#c302}

## 302a · Wheeled equipment steering {#302a}

### Steering types (Part A)
- Front wheel steer. ==**Wheel lean** (motor graders): front wheels tilt left/right== to offset side thrust from the blade.
- Rear wheel steer: tight spaces (forklifts).
- **Crab steering**: all four wheels turn the **same** direction (diagonal travel); ==gives maximum flotation== (each tire on its own ground).
- **Co-ordinated steering**: front and rear turn **opposite** (tight circle).
- Combination: front or rear plus crab and co-ordinated, chosen with a selector switch.
- **Skid steering**: one side slows, stops or reverses.
- **Articulated**: machine pivots at its centre; ==cannot have a rigid frame== (loaders, graders, scrapers, rock trucks, packers). Every other type uses a rigid frame.

### Power steering
- Part-time = on-highway power assist. Full-time = off-road hydraulic steering: ==the steering wheel is **not** physically connected to the wheels==.
- ==**Follower valve**: the wheels turn a fixed amount for a given steering wheel movement.== Without it, holding the wheel turned keeps the wheels turning until released.
- Steering usually has **priority** over other hydraulic functions.

### Components
- Reservoir: stores, cools, settles air and dirt; baffles; ==may have a clean-out cover for servicing the bottom==.
- Pump: fixed or variable, gear/vane/piston, ==generally engine driven==; may have an electric or ground-driven backup.
- ==**Cavitation**: inadequate inlet pressure== (plugged inlet, low oil). Vacuum bubbles implode. ==High-pitched squeal under load; "chewing marbles" at no load.==
- Most pump failures = contaminated oil.
- Flow controls; a flow divider can work with a steering shuttle valve to control an emergency steering pump.
- ==**Hand metering unit (orbital)**: a rotary DCV plus a gerotor pump.== ==If the pump fails, the operator can turn the gerotor by hand to steer.== Meters oil while steering.
- ==Spool type steering valves are used with a **joystick** instead of a steering wheel.==
- Cylinders: ==often two double acting cylinders==; displaced oil from one may feed the other.
- ==**Non-differential** cylinder: one cylinder, rod out both ends, equal pressure/area both sides.== ==Single-rod double acting = **differential** cylinder.==
- Cushion stops limit articulation. ==**Neutralizer valve**: relieves steering cylinder pressure just as full lock is reached== (prevents hammering the stops; often adjustable).
- Filters: depth (through the media) or surface. ==Depth filters are typical.== Filters rated in microns, strainers in mesh. ==Usually in the return line to tank.== Magnets with fire-resistant oil.

### Machine steering behaviour
| Machine | Behaviour |
|---|---|
| Motor grader | Front wheels steer and frame articulates; ==articulates very little compared with wheel turn== |
| Wheel loader | Articulates at centre; ==rear wheels follow the front wheels== (less effort) |
| Tractor-scraper | Articulates near the front; ==rear tires follow inside the front track==; very sharp turns |
| Rough terrain crane | Rigid frame, combination steering |

### Diagnosis and service
- ==70%+ of hydraulic problems relate to the oil.== ==Cleanliness== (cap and plug every opening).
- ==Safety==: lower everything, let oil cool and relieve pressure before opening, cardboard (never a hand) for leaks, ==lock bars on the articulation joint==.
- ==Know the system, talk to the operator, visual inspection, test.== Infrared heat gun checks components without opening them.
- Don't hammer pivot pins or caps (deforms the knuckle). Tie rods set toe; thread fully engaged. Articulation joint repair = split the machine, depressurize, disconnect cylinders, stands and hoists, protect chrome, new O-rings.
- Pressure **too low = sluggish**; **too high = jerky** and stresses parts.

### Skid steers (Part B)
- ==Small reservoir== (so the ==oil cooler is critical==). Closed loop: one or two reversible variable piston pumps (hydrostatic) to two motors.
- ==A separate gear pump supplies charge oil.== ==Each motor drives one side== (wheels or tracks). Case drains return leakage.
- ==Wheeled: belts, chains, sprockets or gears let one motor drive both wheels on a side.== Tracked: final drive + hydraulic motor.

## 302b · Suspension systems {#302b}

- Suspension: absorbs and transmits torque to the frame, responds to terrain, cushions, positions axles, lets axles move independently.

### Scraper cushion hitch
- ==Located between the front tractor and the rear bowl.== Allows articulation and slight side tilt.
- ==**Basic hitch** (no vertical movement) = "stiffneck".==
- Cushion hitch: two links and a load cylinder with accumulators.
  - ==**Tractor bracket**: mounted on the tractor, holds the **head** end of the load cylinder.==
  - ==**Scraper hitch assembly**: on the scraper, holds the **rod** end.==
- Parts: 1–2 accumulators, ==leaf spring linked to the leveling valve==, control lever, bleed valve, variable pump, load cylinder.
- ==Operator controlled==: suspension or rigid. Suspension stops "loping".
- ==Pump and reservoir are the only parts shared with the rest of the hydraulic system.== Axial piston pump driven by the transmission.
- Push-pull (twin engine) scrapers use a ==bail (pull loop) and hook==. Options: ==bail down lockdown, bail up lockdown, cushion ride==.
- **Cushion ride**: hitch lifted off its rest by the load cylinder; used ==travelling== (loaded or empty).
- ==**Lockdown**: hitch sits on the tractor bracket, held by oil pressure keeping the cylinder retracted; used when **loading**.==
- ==**Leveling valve** (moved by the leaf spring) maintains ride height (hitch-to-bracket clearance).== Bleeds down at shutdown.
- ==Oil from the load cylinder moves into the accumulator and compresses nitrogen → cushion.==
- ==**Pump servo valve** moves the control piston to set swashplate angle by pressure.==

### Cushion hitch service
- Level ground, engine off, park brake, lower equipment, visual check, ==cycle controls to bleed pressure==, check oil.
- Ops test: warm oil, time the load cylinder extension in cushion ride, compare to spec. ==Leaf spring to leveling valve linkage may need adjusting.==
- ==% flow loss = (GPM @ 100 psi − GPM @ 1000 psi) ÷ GPM @ 100 psi × 100==; ==more than 5% loss is bad==.

> **Note:** the source notes write the formula without the "÷ GPM @ 100 psi". The percentage form above is the correct one.

- ==Oil leakage test: check case drain output== (OEM spec, or 4.2 L in 30 s is bad) = internal wear.
- Accumulator charging: ==dry nitrogen only (99.8%)==. ==Oxygen = explosion.== Too high a charge = stiff ride. Engine off, pressure discharged. ==Correct the nitrogen pressure for ambient temperature== (charge cold = overfill; charge hot = underfill). ==When installing, purge air by putting a little oil on the nitrogen side and expelling it.==

### Haul trucks
- ==Rubber blocks on smaller trucks, hydropneumatic on larger.== Rubber blocks ==usually sit above the axle housing==, carry vertical loads only, stiffen when loaded.
- ==**Panhard rod** keeps the axle centred left to right under the frame.== ==Worn panhard bushings cause repeated tearing of the rear rubber blocks.==
- Walking beam lets tandem axles see-saw. ==**A-frames** locate the axles front to rear (longitudinal support).==
- **Hydrair struts**: ==control vertical movement; front struts are part of the steering== (==attached to the steering knuckle==). Nitrogen above the piston, oil below; orifices and check valve damp movement. ==No shock absorbers needed.==
- Struts need regular greasing, ==often from a central point==. Charging valve (keep the cover on). ==Payload valve converts strut pressure to an electrical signal to estimate load.== Seals seal the piston to the wall; ==wiper keeps dirt out== (and wears the chrome over time).
- Service: ==lower or secure everything==, empty the box. ==Soapy water finds nitrogen leaks.== Don't check oil until all nitrogen is out; don't remove fittings until the rod is fully retracted and gas released.
- ==Service if: fault code, missing chrome, oil/gas leaks, harsh ride, rod fully extended when empty.==
- ==Charge both sides (both fronts or both rears) at the same time== so ride height is level.

## 302c · Accessories and attachments {#302c}

### Structures (Part A)
- ==**FOPS** = falling object protective structure== (an umbrella for rocks; on haul trucks may be built into the box).
- ==**ROPS** = roll over protective structure== (usually part of the cab).
- Screens and guards protect from branches and logs; ==required on units with winches==; may keep the operator's arms inside (skid steers).
- ==Only use OEM-approved fasteners.== Avoid cutting or welding on structures. ==Contact the OEM== with questions. ==Attach only in ways approved by an engineer.==

### Fire suppression
- Actuators (manual, with a safety release; reachable by operator and ground crew). ==Sensors provide automatic operation==: ==linear detection wire (two wires that melt together; protect it from welding heat)==, spot sensors.
- Dry chemical: ==monoammonium phosphate for A, B and C fires== (A = ordinary combustibles, B = flammable liquids, C = electrical). Knocks the fire down. Poor underground (toxic dust).
- Liquid: AFFF foam for A and B fires; flows into places powder can't; prevents flare-up; used instead of powder underground.
- ==Expellant gas is often nitrogen, sometimes CO2.==
- ==Automatic sequence: alarm, engine shutdown, hydraulic tank vents, system discharges.==
- ==Inspect regularly (often every 6 months)==; weigh cylinders against spec. ==When working on it: safety pins in, system disabled.==

### Ground engaging tools (GET)
- ==Cutting edges are cheap, replaceable wear parts that protect the softer blade or shank== and help penetration.
- Dozers: edges and corner bits; ==not designed for backblading== (unprotected bolts wear fast). ==Tilt up = carry; tilt down = breakout.== C-frame mounts the blade to the track frame.
- Rippers: spikes at the rear, break hard ground (drawbar, shank, point). ==Most versatile ripper = adjustable **parallelogram**== (moves straight up and down, angle adjustable).
- Graders: ==move material that is already loose==. Blade = **moldboard**. ==Edges can be turned over to double their life.== Serrated edges score ice. ==Scarifiers break up the top layer.== Snow wing, V-plow.
- Loaders: edges, bits, teeth/shanks for hard digging. Excavators: teeth (wider for soft material), flat edges for clean-up; teeth fall off from poor install, wrong fit, worn adapter.

### Part B
- PPE for edges; get help lifting; never use fingers to align bolt holes; block or stand the blade.
- ==Clean all rust, dirt and paint off the mounting surface or the bolts will loosen.==
- Change edge or tooth type for different material; weld-on edges for hard ground. ==Tighten blade bolts from the centre outward.== ==Minimum heat when removing weld-on parts.==
- ==Hard surfacing (crosshatch weld) protects against abrasive soils.==
- Winches: hydraulic, PTO or gear-driven; pipelayers use two (boom and pipe). ==Brake usually spring applied, hydraulically released.== ==Drum-and-band in PTO winches; multi-disc clutch packs in hydraulic winches.== Mount solidly (torque many times machine weight); align drives.
- Wire rope: gloves, stay clear under tension, ==underwound rope is most stable==, ==use only rope recommended by the winch maker==, don't kink. Ferrule ends (zinc or brass spike).

## 302d · Off-road electrical fundamentals {#302d}

### Part A
- ==Battery disconnect switch: in **series** with the positive or negative== of the battery group; isolates batteries.
- Breakers are in **series**:
  - ==**Type I**: cycling, auto reset fast; safety circuits (headlights).==
  - ==**Type II**: a heat-producing resistor holds it open while overloaded; must cool (power removed) to reset.==
  - ==**Type III**: non-cycling, manual reset button.==
- ==P = I × E== (sizing; fuse slightly larger than the load).
- Lights: head, flood/work, tail (red), clearance (amber). ==Panel lights dim with a rheostat or PWM==; may use fibre optics.
- ==Turn signal flasher is in **series** with the lamps.== ==LED retrofit needs an electronic/solid-state flasher== (LEDs don't draw enough current for a thermal flasher).
- DC motors: permanent magnet or wound field. Armature = rotating part. ==Commutator = sliding contact surface for brushes, made of bars that feed specific windings.==
- ==**CEMF**: the faster the motor, the more CEMF; less CEMF = more current draw; CEMF limits top speed.==
- Right-hand rule: thumb = current (+ to −), fingers = flux. ==Like poles repel, unlike attract.== ==Field goes north to south.== ==Armature moves from the strong field side to the weak side.==
- Gauges: direct (air gauge) or indirect (sensor). Air core (ferrite core). ==Balancing coil: pointer moves by electromagnetism.== ==Bimetal: heating coil heats the strip according to voltage.==
- ==Closed loop sensor: power and ground return to the ECM. Open loop: ground does not return to the ECM.==
- ==Changing tire size changes the speedometer reading.== Hourmeters use EEPROM.
- ==Thermistor = temperature-sensitive resistor.== ==PTC: temp up, resistance up. NTC: temp up, resistance down== (most engine temp sensors).
- ==Pressure transducer: three wires (5 V ref, signal, return).== ==Fixed resistor in series with a strain gauge, voltage drop compared with two fixed resistors== (a bridge), with an amplifier.
- Ammeter in **series** (or clamp style); voltmeter in **parallel**.

### Part B: networks
- ==**Multiplexing** = sending and receiving digital signals on a data link== (fewer wires, shared data).
- ==**Baud rate** = data speed.== J1587/J1708 = 9.6 kb/s; ==J1939 = 250 kb/s==; ISO 11783 = 250 kb/s.
- ==**Backbone** (data bus) = the physical connection==, max 40 m. Stub = branch to a node, max 1 m. Node = module with an address.
- ==**Terminating resistor** at each end reduces standing waves (reflections) and interference.==
- ==**Protocol** = common language.== ==Twisted pair resists magnetic fields; shielding (foil + drain wire) adds resistance to interference.==
- Topology: ring (series, one fails = all fail), star (master module), ==linear (modern: independent modules on a backbone)==.
- ==CAN is serial (one bit after another), no master; a module must wait until the bus is idle to transmit.==
- J1587/J1708: MID (source), PID (parameter), FMI (fault type), ==checksum (end of message)==. ==Unshielded orange/white twisted pair==, 40 m, 20 nodes. Connectors: 6-pin Deutsch 1996–2001, 9-pin from 2001.
- J1939: PGN (message), ==SPN (where the fault is; replaces PID)==, FMI. Frame: arbitration (priority, sender), control/data, CRC, ACK, end of frame.
- ==CAN-H yellow, CAN-L green.== ==J1939-15 "lite" = unshielded; J1939-11 "heavy" = shielded.== ==Drain wire goes to battery ground.==
- ==120 Ω at each end; 60 Ω measured between CAN-H and CAN-L.== ==Less than 60 = short; more than 60 = open.== CAN lines ~2.5 V idle. ==CAN-H/CAN-L to ground: no continuity (1–4 MΩ or OL).==
- ==ISO 11783: any make of machine connects to any make of implement== (ag/forestry); ==unshielded twisted quad== (CAN-H, CAN-L, power, ground for the terminating bias circuit).

## 302e · Off-road electrical service {#302e}

- ==Schematics are drawn **de-energized**, components in their **normal** position.==
- Circuit = source, load, conductors, control (+ protection).
- ==**Series**: R total = sum; voltage drops add to source voltage; current is the same everywhere.==
- ==**Parallel**: total current = sum of branches; same voltage on each branch; adding branches **lowers** total resistance; total is less than the smallest branch.==
- ==E = I × R.== Resistance turns electrical energy mostly into heat.
- ==Kirchhoff current law: current in = current out.== ==Voltage law: voltage drops = source voltage.==

| Fault | Symptom |
|---|---|
| ==Open== | ==No current (series); less current, more resistance (parallel)== |
| ==Short (copper to copper)== | ==More current draw== |
| ==Short to ground (copper to steel)== | ==Much more current, blown fuse== |
| ==High resistance== | ==Less current, dim lights, slow actuators, voltage drop== |

- ==Isolating = eliminating components that aren't the cause.== OEM flow charts.
- Voltage drop must be tested ==with current flowing==. ==Max 0.5 V (12 V) or 1 V (24 V).==
- Repairs: ==electrically sound, resistance-free splice (crimped or soldered)==; ==replacing the harness is the ideal repair==. Western Union (solid wire, soldered), crimp splice.
- ==**Replace**: oil-soaked or melted insulation, faulty switches/relays/breakers, lamps with opens or shorts.==
- ==Specific gravity 1.265–1.280 @ 27 °C = full charge; cells within 0.05.==
- ==Bimetal gauges are affected by voltage, so a small voltage regulator keeps them accurate.== LCD = no light emitted; LED = forward biased; VFD = glowing pixels.
- Precautions: ==high impedance DMM==, ==never pierce insulation==, ==wrist strap (or touch ground)==, disconnect power/ground and ECMs before welding, don't force connectors.

## 302f · Workplace coaching skills {#302f}

- **Journeypersons/supervisors**: coach, mentor, supervise apprentices, fill out the record book. **Employers**: provide training and supervision, make sure the book is filled out. **Apprentices**: complete training and keep the record book (blue book) current.
- Good mentors lead by example, are approachable, willing to teach, challenge trainees, respect them and encourage independent work.
- ==Coaching method: **Plan → Tell → Show → Do**== (then feedback).
- Feedback: **positive** (says what was good, builds confidence), **empty** ("good job", says nothing specific), **constructive** (corrects without insulting).
- A lesson has: the point, the link to the trade, the individual steps.

## 302g · Red Seal program {#302g}

- Red Seal = ==mobility of skilled workers across Canada== and a standard of excellence. One host jurisdiction handles each trade. Sponsored by HRSDC.
- ==The **NOA** (National Occupational Analysis) is the foundation document for the Red Seal exam.== Organized into **blocks → tasks → sub-tasks**.
- NOA development: host holds a workshop with HRSDC → draft → sent to all jurisdictions → feedback → committee revises → HRSDC publishes.
- ==Pass mark: 70%.== Questions written by industry practitioners.
- Question types: **recall/knowledge**, **procedural/application** (at least two steps), ==**critical thinking** (cause and effect; most common on newer exams)==.

# 303 · Powertrain {#c303}

## 303a · Gearing principles {#303a}

### Terminology
| Term | Meaning |
|---|---|
| ==Pitch line== | ==Top-to-bottom dividing line== of the tooth |
| ==Face== | ==Top portion== (above pitch line) |
| ==Flank== | ==Bottom portion== (below pitch line) |
| ==Centreline== | ==Left-to-right dividing line== |
| ==Toe== | ==Small end== (inner) |
| ==Heel== | ==Large end== (outer) |
| ==Drive side== | Side that is driven under power, ==convex (curved out)== |
| Coast side | Driven by the load in neutral/coasting, concave (curved in) |
| Root fillet | Valley between teeth |
| Path of power | How power flows through a gear set |

> **Note:** 303jA in the source notes calls the drive side "concave". Ring gear drive side is **convex**, coast side is **concave** (303a and 303jB agree).

- Diameters: root, pitch (pitch line to pitch line), outside. ==Circular pitch must match for two gears to mesh.==
- ==**Clearance**: tip of one tooth to root of the other== (needed for lubrication).
- ==**Backlash**: gap between faces/flanks in mesh== (heat expansion and lube).
- ==**Timed** gears: certain teeth must mesh together.== ==**Non-hunting** = must be timed; whole-number ratio (2:1)==; distinct wear patterns.
- **Partial non-hunting**: ratio with 1–2 decimals (4.5:1); must be timed.
- ==**Hunting**: every pinion tooth meets every crown tooth; no timing needed== (uneven ratio such as 3.333:1).

### Ratios
- ==Ratio = driven teeth ÷ drive teeth, written ?:1.== ==Multiply torque, divide RPM.== ==Total ratio = all ratios multiplied together.==

| Type | Gears | RPM | Torque | Ratio |
|---|---|---|---|---|
| ==Direct drive== | Same size | Same | Same | 1:1 |
| ==Reduction== | Small drive, large driven | Down | Up | More than 1:1 (3:1) |
| ==Overdrive== | Large drive, small driven | Up | Down | Less than 1:1 (0.5:1) |

- Two external gears turn opposite ways. ==An **idler** changes output direction but does not change torque or RPM.==

### Gear types
- **Spur** (straight cut): basic, ==no end thrust==, one tooth in contact (lower torque).
- Internal gear: teeth on the inside of a ring.
- ==**Helical**: handles more torque and runs quieter than spur== (several teeth in contact) but creates ==axial (end) thrust==.
- ==**Double helical (herringbone)**: axial loads cancel; very high load and torque.==
- Rack and pinion: rotary to linear.
- Angle drives: ==**pinion** = small drive gear; **crown** = large driven gear==. Straight bevel = noisy, low torque. Spiral = curved teeth, quieter, better contact.
- **Spiral bevel**: pinion in line with crown centreline.
- ==**Amboid**: pinion **above** crown centreline== ("A for above"); ==maximum ground clearance== (driveshaft higher).
- ==**Hypoid**: pinion **below** crown centreline==; lots of sliding contact, needs extreme-pressure (EP) oil.
- Worm and wheel: high torque, big reduction.

### Simple planetary
- Input and output shafts stay ==aligned==. ==Sun (centre), planet pinions on a carrier, ring (internal) gear.==
- Each set needs a drive, a driven and a held (reaction) member.
- ==Ratio trick: don't count planet pinion teeth. Carrier "teeth" = sun + ring.== Size order: sun (fewest) < ring < carrier (most).
- ==Direct drive = two members locked. Neutral = nothing held. Reverse = carrier held. Reduction = carrier driven (output). Overdrive = carrier drive (input).==

| Carrier | Ring | Sun | Result |
|---|---|---|---|
| Drive | Driven | Held | Overdrive, forward |
| Drive | Held | Driven | Large overdrive, forward |
| Driven | Drive | Held | Reduction, forward |
| Driven | Held | Drive | Large reduction, forward |
| Held | Driven | Drive | Reduction, reverse |
| Held | Drive | Driven | Overdrive, reverse |

> **Worked example:** sun 30 teeth, ring 90. Sun in, ring held, carrier out: carrier = 30 + 90 = 120, ratio = 120 ÷ 30 = **4:1** (largest reduction). Ring in, sun held, carrier out: 120 ÷ 90 = **1.33:1**. Carrier held, sun in, ring out: 90 ÷ 30 = **3:1 reverse**.

## 303b · Torque converters {#303b}

- ==Hydrodynamic drive: transfers energy through **fluid motion**.== Energy transfer depends on volume (size, vanes), velocity (impeller speed) and viscosity.
- Fluid clutch: replaces a mechanical clutch; ==slippage prevents engine stall with the machine stopped==.
- ==**Impeller** = engine side (input).== ==**Turbine** = driveline/transmission side (output).==
- ==Low engine speed = high slippage; high speed = low slippage.==
- Fluid clutch pros: no mechanical link, ==shock absorption==, gradual start. Cons: slip losses, heat, ==only transmits torque; cannot multiply it==.
- ==**Torque converter** = a fluid coupling that **multiplies** torque.==

### Flow and phases
| | Vortex flow | Rotary flow |
|---|---|---|
| Phase | ==Converter phase== | ==Coupling phase== |
| Path | ==Impeller → turbine → back to impeller== (around the doughnut) | ==Same direction as impeller rotation== |
| Speeds | ==Turbine much slower than impeller== | ==Turbine ≈ impeller== |
| Result | ==High heat, low speed, high torque== | ==Low heat, high speed, low torque== |

- ==**Lockup phase**: turbine locked to impeller, 1:1== (only with a lockup clutch).
- **Stages** = ==number of turbines== (times the oil hits a turbine before returning). Usually 1.
- ==**Stall**: turbine stopped, impeller at max engine speed== = max torque, max vortex flow, max heat.

### Parts
- ==Impeller (pump): bolted to the flywheel; vanes turn mechanical energy into fluid kinetic energy.== ==Turbine: to the transmission; kinetic → mechanical.==
- ==**Stator** (reaction member): redirects oil back to the impeller; multiplies torque only when **stationary**.==
- ==Split guide ring: reduces turbulence== (between impeller and turbine).
- Torque multiplication needs: ==impeller faster than turbine **and** stator stopped==.
- Fixed stator: never reaches coupling, constant multiplication, very hot. ==**Freewheeling** stator (overrunning clutch): held in converter phase, freewheels in coupling phase.==
- ==**Lockup clutch**: physically connects impeller and turbine, removes slip, raises efficiency, used in rotary flow, 1:1, no multiplication.== Wet multi-disc.
- ==**Variable capacity**: changes torque to suit demand== (dual impeller with one clutched, dual turbine, variable pitch stator).
- ==Temperature sender in the **converter outlet**; max **250 °F (121 °C)**.==
- Oil: light, usually shared with the transmission. ==Too heavy = transmits torque in the cold== (start in neutral).
- Housings: dry, or ==wet (lubricates gears, can drive a PTO)== with low oil level to avoid drag. Scavenging by gravity, or a ==scavenge pump when the converter is level with the transmission==.

### Torque divider
- ==Torque converter + planetary set; torque is split; more multiplication than a plain converter.==
- ==Impeller and sun at engine speed; turbine and ring gear together; carrier = output.== Fixed stator.
- ==With the output stalled, the turbine turns in **reverse**.==

### Mounting, diagnosis, service
- ==**Engine mount** (integral, driven by flywheel) or **remote mount** (driveline between engine and converter).==
- ==Use gauges rated above expected readings.==
- ==Stall test in the **highest gear**== (low gears risk driveline damage), level open ground, park brake on, ==keep oil below 250 °F==.

| Stall result | Cause |
|---|---|
| ==High stall speed== | Converter not multiplying, ==slipping clutch== |
| ==Low stall speed== | ==Engine not making power, slipping stator overrunning clutch== |

- ==Overheating==: gear too high, operator misuse, plugged cooler, bad charge pump, low oil, high oil (drag), hot ambient.
- Removal: note leaks and damage; ==converter may need to be secured to the transmission==. Mark parts, leak test under water, aluminum-safe cleaner, pre-lube, ==plug every hole for storage==.
- Mounting checks: crankshaft endplay (always after install), flywheel housing bore and face, crank hub runout and face, flexplate flatness, converter axial location, pilot diameter.
- ==Shift linkage must be adjusted== or two gears can engage.

## 303c · Powershift and automatic transmission components {#303c}

- Transmission jobs: modify power, multiply torque, reverse, ==provide a PTO==, change speed/direction without interrupting power.
- ==**Powershift**: operator shifts speed and direction==, can shift under full load; ==cycling work (forward/reverse)==.
- ==**Automatic**: shifts happen without operator action== (operator still picks F/R); ==hauling work==.
- Planetary advantages: constant mesh, compact, thrust loads offset, very versatile. Needle bearings on pinion shafts, thrust washers; more planets = more torque capacity.
- ==Neutral: input but no output.==

### Planetary rules
- Two external gears: opposite rotation. External + internal: same direction.
- ==Carrier output = always reduction. Carrier input = always overdrive. Carrier held = always reverse.==
- ==Neutral = input but nothing held. Direct = any two members locked (or two driven at the same speed).==

| | Sun | Ring | Carrier |
|---|---|---|---|
| 1st reduction | Input | Held | Output |
| 2nd reduction | Held | Input | Output |
| 1st overdrive | Held | Output | Input |
| 2nd overdrive | Output | Held | Input |
| 1st reverse | Input | Output | Held |
| 2nd reverse | Output | Input | Held |

- ==**Dual input**: two inputs, one output, nothing held.== Inputs same direction = more speed; opposite = less. Equal and opposite inputs = zero output.
- Dual output: two sets share two rotating members.
- ==**Tooth speed** = teeth passing a point per second; not the same as RPM.==

### Components
- ==Clutches: hydraulically applied, (usually) spring released.== ==**Rotating clutch** locks two rotating members; **stationary clutch** locks a ring gear to the housing.==
- ==Friction discs: grooves allow lube when released and let oil escape when squeezed== (no delayed engagement). ==Steel plates go between every pair of friction discs== (reaction surface; tangs/teeth on outside).
- ==Pistons are hydraulically actuated==; return springs; splines stop rotation.
- ==**Countershaft** transmission: spur gears on parallel shafts; rotating wet multi-disc clutches lock gears to the countershafts.== ==Not as compact (big bearings, thrust not cancelled)== but cheaper; good for shuttling; ==lowers the path of power== and can feed front and rear axles with no transfer case.
- ==High/low unit: no idler (both turn the same way). Reversing unit: idler between input and countershaft.==

## 303d · Transmission control and shifting {#303d}

- ==Three circuits in priority order: 1. clutch application (highest pressure), 2. torque converter charging, 3. lubrication (last).==
- Oil path: reservoir → charge pump → selector/clutch pressure regulator → converter (with relief) → filter → cooler → lube (with relief).
- ==Charge pump provides flow for transmission control.== ==Towing can damage the transmission (no lube): disconnect the driveshaft or lift the drive wheels.==
- Pumps: ==transmission scavenge (leakage from main housing to reservoir)==, ==converter scavenge (from converter housing)==, ==charging pump (feeds the circuits)==, steering clutch/brake lube.
- Filter bypass valve passes unfiltered oil if plugged. ==**Priority valve** (normally closed) guarantees steering and brake pressure.==
- ==**Shift selector valve**: speed and direction== (speed spool, direction spool).
- ==**Modulating relief valve**: max clutch pressure.== ==**Load piston**: rate of pressure rise in the clutch== (prevents shock and slipping). Ratio valve = converter relief. Pressure differential valve = holds pressure to the speed clutch.
- ==Converter **outlet** relief: max working pressure in the converter== (cold start protection) and keeps it full at shutdown.
- ==**Clutch modulation**: gradual pressure rise = controlled slip, no shift shock.==

### Automatic (hydraulic) control
- ==Shift points depend on **ground speed** and **throttle** (operator demand).==
- ==**Governor**: turns output shaft speed into hydraulic pressure; spool balances centrifugal force against governor pressure.== ==Low speed = low pressure; high speed = high pressure.==
- ==Shift signal valves apply/release clutches through a relay valve==; lower gears' signal valves have weaker springs.
- ==Orifice in the governor line prevents a rapid downshift== if pressure drops (hard braking or governor failure).
- ==**Modulator**: changes shift points with throttle; opposes governor pressure.== ==Full throttle = later (delayed) shifts== (more HP and momentum per gear).

| Problem | Result |
|---|---|
| ==Release too fast== | Momentarily out of gear: ==RPM flare, freewheeling== |
| ==Release too slow== | Two clutches at once: ==engine lugging, harsh shift / shift shock== |

- Orifices control **release** rate. ==**Trimmer valve** controls **application** rate.== ==Trimmer modulator boost stops trimming under heavy load (prevents slip).==
- ==Automatic shifting can be prevented== under heavy work (loading, pushing).

### Electronic control
- Inputs: power, shift selector, ==input and output speed sensors (replace the governor, set shift points; not needed on powershift, only automatics)==, ==throttle position (replaces the modulator)==, pressure and temp sensors, data link.
- ECM: shifting, modulation, diagnostics.
- Outputs: ==shift solenoids (speed, direction, converter lockup)==, warnings, backup alarm.

## 303e · Hydraulic retarders {#303e}

- ==A supplementary brake that absorbs kinetic energy== by fluid friction. ==Designed to slow, not stop.== Extends brake life.
- ==**Input** retarder: integral with the transmission== (between converter and transmission); ==works with the transmission (downshift after applying) to be more effective==.
- ==**Output** retarder: on the output shaft; independent of engine RPM and gear; most effective at **high vehicle speed**.==
- ==**Remote / driveline** mount.==
- Parts: ==rotor (input side) with vanes== inside the ==housing (stator, stationary)==, pump and supply (own or shared), cooler (air or coolant), control (==manual, air over hydraulic, electronic==), accumulator (fast fill), sometimes wet brakes for faster braking.
- ==Max oil temp 250 °F (121 °C)==; damage above 275 °F (135 °C).
- ==When off, all oil is drained from the housing.== ==Kinetic energy → heat by friction between rotor and oil.==
- ==Retarders are most effective at high vehicle speed.== Converter lockup is required when the retarder is between the crank and flywheel.
- Electronic: inputs (throttle, retarder temp, output speed, brake applied), outputs (solenoid, warning light, brake lights, temp light).
- Troubleshooting: low temps, clean oil, right level, rotor clearance, ==check for leaks==.

| Filter debris | Source |
|---|---|
| Shiny steel | Pump wear |
| Aluminum | Retarder rotor |
| Rubber | Seal or hose |
| Iron/steel chips | Broken parts |

- ==Overheating speeds oxidation and kills lubrication==: low oil, ==retarder too small for the job==.

## 303f · Transmission testing and service {#303f}

- Steps: information → ==operator (most important source)== → visual (==oil level and condition always first==; water/glycol is very damaging; check filter) → operational tests.
- ==Warm oil to 150–180 °F before testing== (leakage rises with heat; problems may hide when cold).
- ==**Stall test**: brakes on, **highest gear**, full throttle, open area, watch temperature; the machine may move.== Max 30 s, then neutral 30 s to cool. Don't overheat.

| Stall speed | Cause |
|---|---|
| ==Lower than spec== | ==Weak engine, slipping stator== |
| ==Higher than spec== | ==Too much engine power, slipping transmission clutches, converter cavitation (low oil)== |

### Pressure tests
- ==Gauge rated for double system pressure.==
- ==Charging pump inlet: below 12 psia = inlet restriction== (the pump is pulling too hard, so cavitation). ==Higher than normal = air being drawn in== through a leak, which fills in the normal slight vacuum.
- ==Clutch pressure (set by clutch pressure regulator): check at low and high idle; should be the same.== ==Low at idle but normal at high idle = internal leakage.==
- ==Converter charge pressure: resistance in the converter; max set by the converter relief on the **inlet** side.== Low = poor pump flow, clutch or converter circuit leakage.
- ==Lube pressure: last circuit to get oil.== Low = poor pump flow, clutch/converter leakage, ==low in one range = a leaking clutch piston==, lube leaks.
- ==Flowmeter (in series) accurately finds internal leakage== upstream of it.
- ==Shift points are adjusted against governor pressure==, output shaft speed, odometer (usually by shift signal valve spring tension; check governor pressure first).
- Electronic: fault codes, ==follow the manufacturer manual==; protect the ECM.

### Rebuild
- Safety, relieve pressure, follow the service manual. Clean, closed containers; lint-free towels.
- ==Nicks and scratches on valve parts = sticking valves.==
- ==Clean bearings and friction discs only with mineral spirits==; dry with dry air; soft wire for passages.
- Disc wear: micrometer. ==Warpage and cone: on a flat surface with a feeler gauge== (cause drag).
- ==**Clutch clearance**: gap with the clutch released. Too little = drag (heat, wear). Too much = delayed engagement.== ==Adjust with different reaction disc or piston thickness.== Measure with feeler/go-no-go or stack height.
- ==Wrong control valve torque = spool binding.==
- Install: ==new oil and filters; flush the cooler and lines==. ==Misalignment = vibration.== ==Check crankshaft endplay before removal and after installation.== Adjust linkages.

## 303g · Tracked equipment steering {#303g}

### Clutch and brake steering (Part A)
- ==Gradual turn: clutch disconnects power to that side. Sharp turn: brake also applied on that side== (pivot).
- Levers work clutch and brake per side; brake pedals brake without releasing clutches; park brake is mechanical.
- ==Steering clutches deliver power to the final drives.== Bevel pinion → bevel gear on a cross shaft; clutches on each end.
- ==Conventional clutch: **spring applied, hydraulically released**==, multi-disc.
- ==Band brake: contracting band over the drum; the clutch sits **inside** the brake drum.== Service brake applied hydraulically with a booster.

> **Note:** the Google Doc calls the conventional clutch and band "wet", but the ILM objective sheets (and the older powertrain quiz bank) describe the conventional clutch and brake compartment as **dry**, which is why oil in that compartment makes the clutch slip. Expect the ILM version on the exam. Modular units are wet.

- ==Clutch engaged = no input. Lever partly pulled = clutch released. Lever fully pulled, pedal, or park = brake on.==
- ==**Modular**: clutch **and** brake both spring applied (Belleville springs), released by oil; wet multi-disc; one housing; oil circuits in **series**.== ==Clutch engaged → brake released; clutch released → brake applied.== Clutch on input, brake on output.
- ==Priority valve guarantees steering and brakes before the transmission.== Steering valve gives proportional control.

| Lever | Clutch | Brake |
|---|---|---|
| Not pulled | Engaged | Released |
| Partly pulled | Partly released | Released |
| Fully pulled | Released | Applied |

- Diagnosis: oil, leaks, linkage, ==track condition and adjustment==, filters and screens.
- Stall test: warm, park on, in gear; ==brake slip = creep==; ==open area==; test all ranges.
- ==Clutch pressure = 0 until the lever is pulled==, then rises smoothly. ==Brake pressure = 0 until the clutch is released==, then rises smoothly. Also: steering relief, cooler restriction and bypass.
- Removal: ==modular = remove track and final drive; conventional = also the cab and fuel tank.==
- ==Beware spring pressure when disassembling.== ==Mineral spirits only for bearings and friction discs.== Warpage/cone with a feeler gauge (drag). ==Disc clearance with a feeler gauge; too little = drag, overheating, failure.== ==Adjust linkages.==

### Hydrostatic steering (Part B)
- ==Two variable, reversible pumps, each feeding its own motor and final drive.== (A big skid steer.)
- ==Power at **both** tracks while turning==; infinite speed. ==**Counter-rotation (spot turn)**: one track forward, the other reverse.==
- Charge pump replaces oil. ==Flushing valve (3-position shuttle) cools the closed loop== by sending the low side to the charge relief.
- Electronics: engine speed, steer, decelerator, speed, FNR; ==track motor speed sensors (tracking)==; ==pump speed sensor lets the ECM prevent engine kill== under heavy load.

### Differential steering
- ==Transmission input = speed and direction. Hydraulic steering motor = left/right turns== (drives the steering ring gears).
- ==Brakes: modular multi-disc wet, spring applied, hydraulically released; used to stop or slow, **not** to steer.==
- ==Both tracks always powered, even cornering; what one loses in speed the other gains.==
- ==Straight: steering motor holds (stationary).== ==Turn: power from both motor and transmission.== ==Counter-rotation: motor supplies all power, transmission in neutral.==
- 2-planetary: transmission drives both suns, carriers output to finals, motor controls both rings. 3-planetary: steering, drive, equalizing; suns tied together; equalizing ring held.
- ==Motor doesn't turn = machine won't turn. Motor/ring won't hold = won't track straight.==
- Checks: ==turn diameter== (360° left and right, compare) and ==sprocket speed difference== (tracks off, count sprocket revs in one minute at full steer).

## 303h · Undercarriage {#303h}

### Design (Part A)
- ==Narrow pads = more traction and less undercarriage wear.== ==Wide pads = more load carrying (flotation)== but they bend and wear the chain. Use the narrowest pad that works.
- ==Stability== matters most on excavators and cranes. ==Tracked cranes lift best with loads close to the machine.==
- ==**Fixed** track frames: bolted front and rear, more stable.== ==**Oscillating** (swing frame): one central pivot, frames move up and down.==
- ==**Equalizer bar** (with pivot shaft): supports the front of the machine and lets the frames oscillate.==
- Track links: ==bottom is a wear surface (rail)==. ==Bushing pressed into the big bore, pin into the small bore.== Sprocket picks up the bushing end first.
- ==One-piece links==; ==split master link (bolted through the pad)==; ==master pin (removable)==: ==slightly recessed and smaller diameter==; needs a press.
- Conventional track: seals/spacers (low-travel machines like excavators). ==Lubricated track (SALT) reduces wear.==
- ==Flush link type: master pin only.== ==Interlocking: bushing extends into the next link (less dirt).==
- Pads: bolts with anti-seize, self-locking nuts. ==**Grouser** = raised bar for traction.== Standard (single grouser, best traction). ==**Open centre**: for soils that pack between sprocket and chain.== Multi-grouser: better flotation, less traction, less surface damage. Rubber: paved and ag. Extreme service: heat-treated, thicker.
- ==Sprocket/final drive = last reduction.== ==**Low drive**: sprocket in line with the front idler; more stability, low centre of gravity.== ==**High drive**: reduces shock loads on sprocket and final drive==; needs a rear idler; more pin/bushing wear.
- Change sprockets with the track, both sides together. ==**Segmented** sprocket: replace without removing the track== (change all segments).
- ==**Carrier (pedestal) rollers**: top, support the chain.== ==**Track rollers**: bottom, support the machine's weight.== Bogie rollers spread weight.
- ==Roller flanges keep the chain aligned== (cornering and slopes). Double vs single flange (single next to the sprocket).
- ==Roller shaft is fixed to the frame; the shell turns around it.==
- ==**Duo-cone seal** = two metal rings; install with an **alcohol-based** lubricant, never oil.== Rollers are lubed for life at manufacture.
- ==Idlers: centre flange; part of the tension and recoil system==; replace in pairs.
- ==Tension: loosen in packing soils; tighten to make up for chain wear== (too tight wears everything; too loose throws track). ==Hydraulic adjuster: add grease = tighter== (nitrogen systems are opposite). Threaded rod on small/old machines.
- ==Recoil spring absorbs shock and is **always under tension**==; large machines may use nitrogen.

### Service (Part B)
- Undercarriage can be ~50% of a machine's maintenance cost. Causes: speed, wrong components, misalignment, poor maintenance.
- ==Sag check: drive toward the front idler and coast to a stop==; string or straightedge; ==measure between the front idler and the next direction change== (carrier roller, or sprocket on high drive).
- Leaking rollers/idlers: grease/oil as a stop-gap; ==will need replacement==.
- Pin and bushing wear: stretch the track tight, ==measure pin centre to pin centre over several links== (avoid the master).
- ==Sprockets, pins and bushings wear faster in **reverse**== (bushing scrubbing).
- ==Track pitch (pin to pin) **increases** with wear; measure across several pins.==
- Link height, grouser height (straightedge), roller/idler diameters, ==sprocket: tooth side to opposite side across teeth==.
- Alignment: diagonal measurements must match. ==Idler must line up with sprocket and rollers== (guide plates). Idler high for pulling, low for pushing.
- ==Lifting gear rated for the load==; stands or hardwood blocking. Grade 8+ fasteners, anti-seize, ==mating surfaces clean of rust, dirt, paint==, torque and retorque.
- ==Remanufacture only if enough material remains== (pull before total failure). Weld up links, ==turn pins and bushings==, replace grousers. ==Ice lugs (cleats) welded on grousers add traction== (1-2-1 pattern). Some idlers need holes cut before welding.
- ==Recoil springs must be **caged**== (a broken retaining bolt releases huge force). Never fully remove nitrogen valves; release grease slowly.

## 303i · Final drives and electric drive {#303i}

- ==Final drive = last reduction (multiplies torque)==; takes shock loads.
- Types: spur (single/double), planetary (single, double, triple), combination, chain.
- ==Inboard planetary: driveshaft between it and the wheel; needs a very thick shaft.== ==Outboard: wheel/sprocket mounts directly; carrier often acts as cover and mount; small axles; much easier to service.==
- ==Typical path: sun = input, carrier = output, ring = held.== Double: first set drives the second; total = ratio 1 × ratio 2.
- Mechanically driven on wheeled machines, hydraulically on tracked (motor may spin opposite the output).
- ==Chain final drives: skid steers and motor graders.== ==Grader tandem housing works like a walking beam== (ground clearance). Chain pros: one input, several outputs, no slip over distance, cheap, compact; housing often holds brakes.
- Spur: bevel set turns 90°. ==Small spur = drive pinion (bull pinion); large = driven (bull gear).== Big gears, radial loads, big housing.
- Maintenance: splash lube, right oil, clean. ==Oil level: level ground, level line parallel to ground, remove plug and check.== ==Small centre cover gives access to the sun gear and axle; not vented, so pressure builds when warm.== Pressed-on sprockets: caution with presses.

### Electric drive
- ==Needs specialized training.== Usually AC motors (longer life, more efficient than DC; DC brushes can arc).
- Pros: long life, easy service, ==retards well downhill==, fuel efficient, less oil.
- ==**Power flow**: engine → generator/alternator (AC) → main rectifier (AC to DC) → filtering capacitors → **DC bus (stores DC)** → inverters (DC back to AC) → traction motors.==
- Generator: mechanical → electrical; ==stator = fixed field connected to a power supply==, rotor turns.
- ==**Dynamic braking**: traction motors become generators== (dynamic brake pedal); inverter phase module → DC → ==retarding grid== ("giant toaster"); ==braking choppers switch the grid==; ==grid blower cools it==. Supplements the mechanical brakes.
- Self-load test holds the engine under load while stationary.
- ==DC bus capacitors are a serious hazard; normally discharged by firing the choppers; **verify discharged before work (>50 V)**.== Systems can be in kilovolts.
- ==PPE: face shield, glasses, high-voltage rubber gloves under leather protectors.== ==Safe distance: 12 in with PPE, 2.5 ft without.==

## 303j · Drive axles and carriers {#303j}

### Basics (Part A)
- Axles carry weight, ==turn power 90°==, and reduce speed. ==**GAWR** = weight an axle can safely carry== (housing is the main factor).
- ==**Full-floating**: shaft carries no load; can be pulled with weight on the tires.== ==**Semi-floating**: shaft carries load; wheels must be raised to pull the shaft.==
- ==Carrier holds the gear components== (may be integral). ==Pinion depth set with **shims** at the pinion cage.==
- ==Drive pinion delivers torque to the bevel gear== (from the input yoke). ==**Overhung**: no support at the pinion end. **Straddle**: bearing on the pinion nose== (high torque; short stub).
- ==Bevel (ring) gear delivers torque to the differential case==; ==bolted to the **flanged** case half==. Heel = outer edge, toe = inside.
- ==**Thrust screw** (opposite the pinion, behind the bevel gear) prevents bevel gear deflection under heavy load.==
- Adjusting rings both sides set side bearing preload/position. ==Cross shaft (spider) sits between the case halves and carries the differential pinions.== ==Side gears pass torque to the axle shafts.== Thrust washers throughout. Output shaft for tandem axles.
- ==Path of power: yoke → pinion → bevel gear → case → cross shaft → diff pinions → side gears → axle shafts → wheels.==
- ==Differential lets driven wheels turn at different speeds== (==essential cornering==; outer wheel faster). In a straight line the diff pinions don't spin on the cross shaft.
- ==Most carriers are single speed, single reduction; ratio = pinion to bevel gear.==
- ==Torque is equal at each wheel regardless of RPM; the good wheel only gets as much as the slipping wheel.== ==Wheel torque = bevel gear torque ÷ 2.==
- ==RPM can't be lost: total wheel RPM = bevel gear RPM × 2.==
- ==Transfer case (drop box): splits power front/rear and drops it to driveline height.== ==Inter-axle differential (optional) splits torque front/rear at varying amounts.==
- ==Traction devices send more torque to the wheel with the most traction== (0 traction one side = 100% to the other). ==Lock = wheels at the same RPM; locks one axle shaft to the case.==
- ==Locking diffs eliminate differential action== (operator controlled). ==Jaw/dog style: engage at low engine speed, travelling straight.== Disc style: electric-hydraulic, more forgiving with wheel spin.
- Limited slip: friction discs, automatic; normal diff in corners. ==No-spin: replaces the cross shaft, pinions and side gears==; acts locked but allows cornering (ratchets).

### Service (Part B)
- ==Oil level: level with the filler opening.== Wrong viscosity or low level = premature wear. Splash or ==pressure lube (internal pump, often overdriven for low-speed lube)==.
- Leaks: seals, ==housing joints (O-ring or RTV)==, breathers, housing fatigue. ==Check endplay on input and output shafts.==
- Diagnose: suspension, driveline, wheels/tires/hubs, ==road test only when it won't cause more damage==.

| Noise | Likely cause |
|---|---|
| On drive | Pinion issues |
| On coast | Pinion/ring too tight (heard decelerating) |
| Intermittent | Warped ring gear, loose case bolts |
| Constant | Flat spot on pinion, ring or bearings |
| ==Turns only== | ==Side gears, diff pinions, spider, thrust washers, axle splines== |

- Overheating: low oil, high oil (foaming), dirty housing, wrong oil.
- If axles share oil with final drives, check them too.
- ==Before teardown: backlash (dial indicator 90° to tooth, 4 places)==, runout, rolling torque, tooth pattern.
- Mark side caps and ==all matched parts==. ==No-spin case halves are spring loaded.== Keep pinion shims. Don't spin bearings with air.
- ==Bevel gear and pinion are replaced as a matched set.==

| Failure | Cause |
|---|---|
| Ring teeth broken at toe | Shock load, ==too little backlash== |
| Pitted pinion | Severe service, poor lube |
| Scored thrust washers | Bad, wrong or dirty lube |
| Bent housing | Overload, accident, shock |
| Axle broken at flange | Loose wheel bearing, bent housing, loose hub bolts |

### Assembly
- ==Pinion bearing preload: shims between the two pinion bearings== (more shim = less preload). Press the bearings, ==measure rolling torque while turning, not breakaway==. Torque = spring scale pull × radius. ==Final preload comes from yoke nut torque.==
- ==**Nominal dimension**: pinion end to bevel gear centreline; etched on the pinion end.== ==0 or blank = standard. **+** = move pinion **away** from the bevel gear. **−** = move it **closer**.==
- ==Shims at the bearing cage==: thicker = pinion further away. ==Shims between inner bearing and pinion gear==: thicker = closer. Old gear set = old shims; new set = adjust to the etched number.
- ==Side bearing preload and backlash: adjusting rings.== Remove endplay, add a few notches for preload.
- ==Backlash: turn both rings the same amount== (keeps preload). Reusing old gears = keep the old backlash. ==More backlash: move the gear **away** from the pinion (loosen flanged side, tighten plain side).== ==Less: move **toward** the pinion.==
- ==Runout: radial (side) and back face.==
- ==Tooth pattern: paint the convex (drive) side; keep drag on the pinion.==

| Pattern | Cause | Fix |
|---|---|---|
| ==Heavy face== | ==Pinion too far out== | ==Move pinion in==, reset backlash |
| ==Heavy flank== | ==Pinion too far in== | ==Move pinion out==, reset backlash |
| ==Heavy heel== | ==Ring gear too far out== | ==Move ring toward pinion (less backlash)== |
| ==Heavy toe== | ==Ring gear too far in== | ==Move ring away from pinion (more backlash)== |

> **Memory hook:** pinion **depth** fixes face/flank (face = pinion in, flank = pinion out). **Ring gear position** (backlash) fixes heel/toe (heel = toward pinion, toe = away).

## 303k · Clutches {#303k}

- ==**Overcentre clutch** couples a drive and driven unit; intermittent use, not for shifting gears.== ==Doesn't use spring force to apply== (the linkage locks overcentre); may be hydraulic or air operated. Slips if overloaded. Stationary uses (pumps, generators). ==On/off only; doesn't control speed.==
- Parts: flywheel, ==drive ring (internal teeth, drives the disc)==, ==clutch disc (driven by the drive ring)==, ==pressure plate assembly== (back plate and hub near the flywheel, floating plate clamps toward the flywheel).
- ==Flywheel, drive ring and disc always turn at engine speed (drive members).== ==Plates, hub and output shaft turn at flywheel speed only when engaged (driven members).==
- ==Overcentre linkage: no springs; lever "snaps" the clutch in; forks.== ==Adjusting ring: **toward** the pressure plates = **more** force; away = less.== Release pin must be pulled to adjust. Linkage is under 90° when engaged.
- ==Path: engine → drive ring → clutch disc → pressure plate assembly → output shaft.==
- ==Bearings need regular greasing.== Heat spots (blue/dark). ==Pull-in force (checked with a pull scale) sets clamping force and torque capacity.==
- ==Engine seal leak glazes the disc → slipping; discs must be replaced.== Disengaging at high RPM can damage the engine.
- Removal checks: ==crankshaft endplay before and after== (dial indicator), ==flywheel face runout (push crank fully one way to remove endplay; add all readings ignoring + and −)==, bore runout, housing concentricity and face runout.

### Special clutches
- ==**Overrunning**: drives one way, freewheels the other; output can turn faster than input.== Roller (spring and roller in a ramped race), sprag, dog/jaw (ratchet-like).
- Cone and bevel: cone into a bevel; slips under overload (transmissions, rear axles).
- ==Electromagnetic: current applied = clutch applied== (A/C compressors, fan hubs, mowers; easy remote control).
- Wet (oil) clutches: hydraulic piston clamps discs and plates; ==oil cools and cleans==.
