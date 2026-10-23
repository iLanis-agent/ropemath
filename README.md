# Rope Math

Rope piece, spool, cost and time arithmetic. The 100 meters at 6 meters a piece cut 16 full pieces with 4 meters left over.

## Named constants

None. Every number is the owner's own entry.

## What it computes

- **The pieces truth** - the meters (1 to 100000) divided by the meters a piece (1 to 10000), rounded down, with the meters left over.
- **The spools truth** - the pieces (1 to 1000000) divided by the pieces a spool (1 to 10000), rounded up, with what the last spool gives.
- **The cost truth** - the spools (1 to 100000) times the spool price ($0.01 to $999.99) to the cent, and spread over the pieces, half rounded up.
- **The time truth** - the cuts (1 to 1000000) times the seconds a cut (1 to 1000), in seconds and in minutes and seconds.

## Boundary

Arithmetic only. Counting applied as written. It has not seen any rope, knife or knot and does not know whether a rope will really measure out, the ends will fray or a price will hold, and it gives no verdict that a spool is worth its price or a rope is right for a load. Every number is the owner's own entry.

## Files

- `index.html` - landing page with the boundary and starting examples.
- `app.html` - the calculator; every box recomputes on each keystroke.
- `engine.js` - the four truths, shared by the page and the tests.
- `oracle.py` - an independent Python re-implementation; writes `expected.json`.
- `test.js` - runs the engine against `expected.json` (99 cases, 20 error cases).

## Tests

```
python3 oracle.py
node test.js
```
