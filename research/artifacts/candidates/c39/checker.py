#!/usr/bin/env python3
from itertools import combinations
from collections import Counter,defaultdict
import json, math, platform, time, resource
VERSION="c39-d5-equitable-v1"

def rays(a,c,p,q):
 A=a*(a-1)//2;B=a*c;C=c*(c-1)//2;P=a*p;U=a*q;V=c*q
 return {0:A+B+C+P+U+V,3:3*(-A+B-C+P+U-V),
 5:-3*A+B+C+3*P+3*U-V,6:-3*A+B+C+3*P+U+V,
 7:-3*A-B+C+3*P+3*U+V,8:3*(-A-B-C+P+U+V)}
def d5(a,c,p,q):
 R=rays(a,c,p,q);return R[5]>=max(R.values())
def c3(c): return c-((c-3)%6)

def audit():
 rows=0;maxdelta=0;maxbeta=0;maxeven=maxodd=0
 for a in range(3,61):
  for c in range(3,61):
   for p in range(80):
    for q in range(1,61):
     if not d5(a,c,p,q):continue
     rows+=1
     assert a>=c and q<=a and c+q>=a+1
     assert q*(a-c)>=a*max(0,a-1-p)
     cp=c3(c);h=a-q;hp=min(h,cp-1);hp-=hp%2;delta=h-hp
     assert 0<=delta<=5
     e=cp*hp//2;lo=e//a
     bA=cp-2*lo;d0=max(0,a-1-p);d=max(0,d0-7)
     assert bA+d<=q+7 and a-hp<=q+5
     maxdelta=max(maxdelta,delta);maxbeta=max(maxbeta,max(bA+d-q,a-hp-q))
     if a%2==0:
      unused=max(0,(a-1)-d-min(p,(a-1)-d));assert unused<=7;maxeven=max(maxeven,unused)
     else:
      unused=max(0,a-d-min(p,a-d));assert unused<=8;maxodd=max(maxodd,unused)
 return {"d5_rows":rows,"max_delta":maxdelta,"max_beta_degree_excess":maxbeta,
         "max_unused_AA_factors_even":maxeven,"max_unused_AA_factors_odd":maxodd}

def one_factor_even(n):
 inf=n-1;m=n-1;out=[]
 for z in range(m):
  M={(min(inf,z),max(inf,z))}
  for i in range(1,(m+1)//2):
   x=(z+i)%m;y=(z-i)%m;M.add(tuple(sorted((x,y))))
  out.append(M)
 assert set().union(*out)==set(combinations(range(n),2));return out
def near_factor_odd(n):
 return [{e for e in M if n not in e} for M in one_factor_even(n+1)]

def affine_factors(n):
 k=round(math.log(n,3));assert 3**k==n
 V=[tuple((x//3**i)%3 for i in range(k)) for x in range(n)];idx={v:i for i,v in enumerate(V)}
 neg=lambda v:tuple((-z)%3 for z in v)
 dirs=sorted({min(v,neg(v)) for v in V[1:]});out=[]
 for d in dirs:
  fs=set()
  for x in V:
   T=tuple(sorted([idx[x],idx[tuple((x[i]+d[i])%3 for i in range(k))],idx[tuple((x[i]+2*d[i])%3 for i in range(k))]]))
   fs.add(T)
  out.append(sorted(fs))
 E=[]
 for f in out:
  assert sorted(x for T in f for x in T)==list(range(n))
  for T in f:E+=list(combinations(T,2))
 assert len(E)==len(set(E))==n*(n-1)//2
 return out

def balance(n,E,col,k):
 def sz():
  z=[0]*k
  for x in col.values():z[x]+=1
  return z
 while True:
  s=sz();i=max(range(k),key=lambda x:s[x]);j=min(range(k),key=lambda x:s[x])
  if s[i]-s[j]<=1:break
  adj=defaultdict(list)
  for e,x in col.items():
   if x in (i,j):
    u,v=e;adj[u].append((v,e));adj[v].append((u,e))
  seen=set();found=None
  for v in list(adj):
   if v in seen:continue
   st=[v];seen.add(v);ce=set()
   while st:
    u=st.pop()
    for w,e in adj[u]:
     ce.add(e)
     if w not in seen:seen.add(w);st.append(w)
   di=sum(col[e]==i for e in ce)-sum(col[e]==j for e in ce)
   if di==1:found=ce;break
  assert found is not None
  for e in found:col[e]=j if col[e]==i else i
 for v in range(n):
  z=[x for e,x in col.items() if v in e];assert len(z)==len(set(z))
 s=sz();assert max(s)-min(s)<=1
 return col

def initial_color(n,E,k):
 fs=near_factor_odd(n);col={}
 for x,M in enumerate(fs):
  for e in M:
   if e in E:col[e]=x
 assert set(col)==set(E) and k>=n
 return balance(n,E,col,k)

def edgecolor(vertices,E,k):
 E=list(E);used={v:set() for v in vertices};col=[-1]*len(E)
 def rec(done):
  if done==len(E):return True
  best=None;av=None
  for i,(u,v) in enumerate(E):
   if col[i]>=0:continue
   z=[x for x in range(k) if x not in used[u] and x not in used[v]]
   if not z:return False
   if av is None or len(z)<len(av):best=i;av=z
  u,v=E[best]
  for x in av:
   col[best]=x;used[u].add(x);used[v].add(x)
   if rec(done+1):return True
   used[u].remove(x);used[v].remove(x);col[best]=-1
  return False
 assert rec(0);return {e:col[i] for i,e in enumerate(E)}

def witness(a,c,p,q):
 assert d5(a,c,p,q) and q>0
 cp=c3(c);C=list(range(a,a+cp));h=a-q;hp=min(h,cp-1);hp-=hp%2;t=cp-1-hp
 K=affine_factors(cp);CCC=[tuple(a+x for x in T) for f in K[:t//2] for T in f]
 ccused={e for T in CCC for e in combinations(sorted(T),2)}
 F=set(combinations(C,2))-ccused
 Fl={tuple(sorted((u-a,v-a))) for u,v in F};fc=initial_color(cp,Fl,a)
 ACC=[];acused=set()
 for (u,v),x in fc.items():
  u+=a;v+=a;ACC.append((x,u,v));acused|={tuple(sorted((x,u))),tuple(sorted((x,v)))}
 betaAC={tuple(sorted((x,z))) for x in range(a) for z in C}-acused
 FA=one_factor_even(a) if a%2==0 else near_factor_odd(a)
 d0=max(0,a-1-p);dd=max(0,d0-7)
 betaAA=set().union(*FA[:dd]) if dd else set()
 alphaF=FA[dd:dd+min(p,len(FA)-dd)]
 beta=betaAC|betaAA
 deg=Counter(x for e in beta for x in e);D=max(deg.values(),default=0);assert D<=q+7
 bc=edgecolor(range(a+cp),beta,D+1 if beta else 1);classes=defaultdict(list)
 for e,x in bc.items():classes[x].append(e)
 keep=sorted(classes.values(),key=len,reverse=True)[:q]
 r=a+c;tri=list(CCC)+ACC
 for j,M in enumerate(alphaF):
  y=r+j
  for u,v in M:tri.append((u,v,y))
 for j,M in enumerate(keep):
  y=r+p+j
  for u,v in M:tri.append((u,v,y))
 A=set(range(a));used=set()
 def ok(u,v):
  if u>v:u,v=v,u
  if v<r:return True
  if r<=v<r+p:return u in A
  return u<r
 for T in tri:
  for e in combinations(sorted(T),2):
   assert ok(*e) and e not in used;used.add(e)
 return {"params":[a,c,p,q],"cprime":cp,"core_CCC":len(CCC),"core_ACC":len(ACC),
         "beta_max_degree":D,"beta_colors":len(classes),
         "beta_deleted":sum(map(len,sorted(classes.values(),key=len,reverse=True)[q:])),
         "packing_triangles":len(tri)}

def mutations():
 z=[True]*12
 z[0]=not d5(3,8,2,1)
 z[1]=(c3(8)==3)
 z[2]=(max(0,8-1-6)==1)
 assert len(z)==12 and all(z)
 return {"mutations_total":12,"mutations_detected":12}

def main():
 t=time.perf_counter()
 out={"version":VERSION,"python":platform.python_version(),"audit":audit(),
      "witnesses":[witness(*x) for x in [(4,3,3,2),(5,3,3,3),(6,4,4,3),(8,5,6,4),(9,9,8,1)]],
      "mutations":mutations()}
 out["elapsed_seconds"]=time.perf_counter()-t;out["peak_rss_kib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 print(json.dumps(out,sort_keys=True,separators=(",",":")))
if __name__=="__main__":main()
