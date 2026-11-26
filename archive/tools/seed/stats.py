import re, sys, glob, os
root = sys.argv[1]
pats = {
 'MP_narrates': r'Marco Polo (starts by )?narrat',
 'Polo_narrates': r'\bPolo narrates\b',
 'he_says': r'\b[Hh]e says\b',
 'acc_book': r'[Aa]ccording to the [Bb]ook',
 'anyway_next': r'Anyway, next',
 'anyway_any': r'\bAnyway\b',
 'next_he_mentions': r'next he mentions',
 'then_describes': r'Then (Polo|he) describes',
 'tradition_has': r'Tradition has it',
 'quick_note': r'A quick (note|aside)',
 'soft': r'\bSoft\b',
 'soft_close': r'Soft close',
 'thus_closer': r'^Thus ',
 'one_breath': r'(Venetian|one|coastal) breath',
 'enough_that': r'it is enough that',
 'asides_honest': r'asides? (has|have) to be honest',
}
fp = r'\b(I will tell|I tell you|I assure you|I can tell you|I can assure|I have been telling|I am going to|I will relate|What more shall I say|I should have told|And why should I|I will quit|Now I will)\b'
for f in sorted(glob.glob(os.path.join(root,'*.md'))):
    t = open(f).read()
    narr = t.split('\n## Notes')[0]
    notes = t.split('\n## Notes')[1] if '\n## Notes' in t else ''
    # drop title/epigraph lines starting with # or >
    body = '\n'.join(l for l in narr.split('\n') if not l.startswith('#') and not l.startswith('>'))
    words = len(re.findall(r"[\w’'-]+", body))
    body_cites = re.findall(r'\[(\d+)\]', body)
    note_ids = re.findall(r'^\[(\d+)\]', notes, re.M)
    counts = {k: len(re.findall(v, body, re.M)) for k,v in pats.items()}
    fpc = len(re.findall(fp, body))
    bc = [int(x) for x in body_cites]; ni=[int(x) for x in note_ids]
    seq_ok = bc == list(range(1,len(bc)+1))
    print(os.path.basename(f), 'words=',words, 'cites=',len(bc), 'notes=',len(ni), 'seq_ok=',seq_ok, 'missing_note=',sorted(set(bc)-set(ni)), 'orphan_note=',sorted(set(ni)-set(bc)), 'dupe_body=',sorted({x for x in bc if bc.count(x)>1}))
    print('   ', {k:v for k,v in counts.items() if v}, 'firstperson=',fpc)
