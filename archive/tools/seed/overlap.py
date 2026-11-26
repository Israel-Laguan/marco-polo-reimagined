import re,sys,glob,os
def norm(t):
    t=t.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    t=re.sub(r'\{\d+\}','',t)
    return re.findall(r"[a-z]+",t.lower())
yule=norm(open(sys.argv[1],encoding='utf-8').read())
N=7
S=set(tuple(yule[i:i+N]) for i in range(len(yule)-N))
for f in sorted(glob.glob(os.path.join(sys.argv[2],'ch-*.md'))):
    txt=open(f,encoding='utf-8').read().split('## Notes')[0]
    w=norm(txt)
    cov=[False]*len(w)
    for i in range(len(w)-N):
        if tuple(w[i:i+N]) in S:
            for j in range(i,i+N): cov[j]=True
    print(os.path.basename(f), len(w), f"{100*sum(cov)/max(1,len(w)):.0f}% words in verbatim 7-gram runs from Yule")
