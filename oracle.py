import json, random
def dec(n, p=2):
    b = 10**p
    w, f = divmod(n, b)
    fs = str(f).zfill(p).rstrip("0")
    return str(w) + "." + fs if fs else str(w)
def m(n): return f"{n//100}.{str(n%100).zfill(2)}"
def pl(n, one, many): return f"{n}" + (one if n == 1 else many)
def v(n, one, many): return one if n == 1 else many
def pieces(n, p):
    k = n//p
    return f"The {pl(n,' meter',' meters')} at {pl(p,' meter',' meters')} a piece {v(n,'cuts','cut')} {pl(k,' full piece',' full pieces')} with {pl(n-k*p,' meter',' meters')} left over."
def spools(n, p):
    k = -(-n//p)
    return f"The {pl(n,' piece',' pieces')} at {pl(p,' piece',' pieces')} a spool {v(n,'takes','take')} {pl(k,' spool',' spools')}, the last spool giving {pl(n-(k-1)*p,' piece',' pieces')}."
def cost(s, pc, n):
    cc = s*pc
    pp = (2*cc + n)//(2*n)
    return f"The {pl(s,' spool',' spools')} at ${m(pc)} a spool {v(s,'comes','come')} to ${m(cc)}, ${m(pp)} a piece."
def time_(c, s):
    t = c*s; m_, r = t//60, t%60
    return f"The {pl(c,' cut',' cuts')} at {pl(s,' second',' seconds')} a cut {v(c,'takes','take')} {pl(t,' second',' seconds')}, {pl(m_,' minute',' minutes')} {pl(r,' second',' seconds')}."
random.seed(777)
R = random.randint
cases = [
 dict(fn="pieces", args=["100","6"], expect=pieces(100,6)),
 dict(fn="spools", args=["100","16"], expect=spools(100,16)),
 dict(fn="cost", args=["7","24.99","100"], expect=cost(7,2499,100)),
 dict(fn="time", args=["112","8"], expect=time_(112,8)),
 dict(fn="pieces", args=["1","1"], expect=pieces(1,1)),
 dict(fn="pieces", args=["96","6"], expect=pieces(96,6)),
 dict(fn="pieces", args=["100000","10000"], expect=pieces(100000,10000)),
 dict(fn="spools", args=["1","1"], expect=spools(1,1)),
 dict(fn="spools", args=["96","16"], expect=spools(96,16)),
 dict(fn="spools", args=["1000000","10000"], expect=spools(1000000,10000)),
 dict(fn="cost", args=["1","0.01","1"], expect=cost(1,1,1)),
 dict(fn="cost", args=["100000","999.99","1000000"], expect=cost(100000,99999,1000000)),
 dict(fn="time", args=["1","1"], expect=time_(1,1)),
 dict(fn="time", args=["60","60"], expect=time_(60,60)),
 dict(fn="time", args=["1000000","1000"], expect=time_(1000000,1000)),
]
for _ in range(20):
    n,p=R(1,100000),R(1,10000); cases.append(dict(fn="pieces", args=[str(n),str(p)], expect=pieces(n,p)))
for _ in range(20):
    n,p=R(1,1000000),R(1,10000); cases.append(dict(fn="spools", args=[str(n),str(p)], expect=spools(n,p)))
for _ in range(25):
    s,p,n=R(1,100000),R(1,99999),R(1,1000000); cases.append(dict(fn="cost", args=[str(s),dec(p),str(n)], expect=cost(s,p,n)))
for _ in range(19):
    c,s=R(1,1000000),R(1,1000); cases.append(dict(fn="time", args=[str(c),str(s)], expect=time_(c,s)))
errs=[["pieces",["0","6"]],["pieces",["100001","6"]],["pieces",["2.5","6"]],["pieces",["100","0"]],["pieces",["100","10001"]],
 ["spools",["0","16"]],["spools",["1000001","16"]],["spools",["100","0"]],["spools",["100","10001"]],["spools",["100","1.5"]],
 ["cost",["0","24.99","100"]],["cost",["100001","24.99","100"]],["cost",["7","0","100"]],["cost",["7","24.995","100"]],["cost",["7","24.99","0"]],
 ["time",["0","8"]],["time",["1000001","8"]],["time",["112","0"]],["time",["112","1001"]],["time",["112","8.5"]]]
json.dump(dict(cases=cases, errors=errs), open("expected.json","w"), indent=1)
print(len(cases),"cases,",len(errs),"errcases")
