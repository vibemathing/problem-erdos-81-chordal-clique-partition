"""Reconstruct the frozen C26 run output. No mathematical program is executed."""
import argparse,csv,hashlib,json
from pathlib import Path
EXPECTED="315153ef1c73a16cebaa7b9819bc32eba000b93095e4a64220c8a62e3614ac12"
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    here=Path(__file__).resolve().parent
    report=json.loads((here/'repacking-report.json').read_text())
    with (here/'repacking-table.csv').open(newline='') as handle:
        reader=csv.reader(handle);header=next(reader)
        if header!=['r','a','b','p','q','nu_star','Q','J','leaf_only_M','rho','number_of_core_masks']:
            raise ValueError('table header mismatch')
        rows=[]
        for row in reader:
            if len(row)!=11:raise ValueError('table dimensions')
            rows.append([int(v) if i in (0,1,2,3,4,7,10) else v for i,v in enumerate(row)])
    report['exact']['rows']=rows
    report['repairs']['large_repair_certificates']=[json.loads((here/f'repair-r{n}.json').read_text()) for n in (200,220,241,400)]
    report['repairs']['proper_two_prefix_fractional_certificate']=json.loads((here/'proper-two-prefix.json').read_text())
    raw=(json.dumps(report,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
    if len(raw)!=22183 or hashlib.sha256(raw).hexdigest()!=EXPECTED:raise ValueError('frozen result digest mismatch')
    with args.out.open('xb') as handle:handle.write(raw)
    print(json.dumps({'verdict':'candidate_only','bytes':len(raw),'sha256':EXPECTED,'mathematical_code_executed':False}))
if __name__=='__main__':main()
