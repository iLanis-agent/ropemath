// Rope Math engine: the pieces a spool cuts, the spools a job takes, the cost a piece, and the seconds the cuts take. Exact integers, half-up on display only. No named constants; every number is the owner's own entry.
function _i(t, err, digits, lo, hi) {
  t = typeof t === "string" ? t.trim() : "";
  if (!new RegExp("^[0-9]{1," + digits + "}$").test(t)) throw new Error(err);
  var v = parseInt(t, 10);
  if (v < lo || v > hi) throw new Error(err);
  return v;
}
function _p(t, err, intDigits, places, lo, hi) {
  t = typeof t === "string" ? t.trim() : "";
  var m = new RegExp("^([0-9]{1," + intDigits + "})(?:\\.([0-9]{1," + places + "}))?$").exec(t);
  if (!m) throw new Error(err);
  var v = parseInt(m[1], 10) * Math.pow(10, places) + (m[2] ? parseInt(m[2].padEnd(places, "0"), 10) : 0);
  if (v < lo || v > hi) throw new Error(err);
  return v;
}
function _m(v) {
  var w = Math.floor(v / 100), f = String(v % 100).padStart(2, "0");
  return w + "." + f;
}
function _pl(n, one, many) { return n + (n === 1 ? one : many); }
function _v(n, one, many) { return n === 1 ? one : many; }
var _MT = "the meters must be from 1 to 100000 with no decimal places";
var _MP = "the meters a piece must be from 1 to 10000 with no decimal places";
var _PC = "the pieces must be from 1 to 1000000 with no decimal places";
var _PS = "the pieces a spool must be from 1 to 10000 with no decimal places";
var _SP = "the spools must be from 1 to 100000 with no decimal places";
var _PR = "the spool price must be from 0.01 to 999.99 with up to 2 decimal places";
var _CU = "the cuts must be from 1 to 1000000 with no decimal places";
var _SC = "the seconds a cut must be from 1 to 1000 with no decimal places";

function piecesTruth(meters, perPiece) {
  var n = _i(meters, _MT, 6, 1, 100000), p = _i(perPiece, _MP, 5, 1, 10000);
  var k = Math.floor(n / p), left = n - k * p;
  return "The " + _pl(n, " meter", " meters") + " at " + _pl(p, " meter", " meters") + " a piece " + _v(n, "cuts", "cut") + " " + _pl(k, " full piece", " full pieces") + " with " + _pl(left, " meter", " meters") + " left over.";
}
function spoolsTruth(pieces, perSpool) {
  var n = _i(pieces, _PC, 7, 1, 1000000), p = _i(perSpool, _PS, 5, 1, 10000);
  var k = Math.floor((n + p - 1) / p), last = n - (k - 1) * p;
  return "The " + _pl(n, " piece", " pieces") + " at " + _pl(p, " piece", " pieces") + " a spool " + _v(n, "takes", "take") + " " + _pl(k, " spool", " spools") + ", the last spool giving " + _pl(last, " piece", " pieces") + ".";
}
function costTruth(spools, price, pieces) {
  var s = _i(spools, _SP, 6, 1, 100000), p = _p(price, _PR, 3, 2, 1, 99999), n = _i(pieces, _PC, 7, 1, 1000000);
  var cc = s * p;
  var pp = Math.floor((2 * cc + n) / (2 * n));
  return "The " + _pl(s, " spool", " spools") + " at $" + _m(p) + " a spool " + _v(s, "comes", "come") + " to $" + _m(cc) + ", $" + _m(pp) + " a piece.";
}
function timeTruth(cuts, seconds) {
  var c = _i(cuts, _CU, 7, 1, 1000000), s = _i(seconds, _SC, 4, 1, 1000);
  var t = c * s, m = Math.floor(t / 60), r = t % 60;
  return "The " + _pl(c, " cut", " cuts") + " at " + _pl(s, " second", " seconds") + " a cut " + _v(c, "takes", "take") + " " + _pl(t, " second", " seconds") + ", " + _pl(m, " minute", " minutes") + " " + _pl(r, " second", " seconds") + ".";
}
