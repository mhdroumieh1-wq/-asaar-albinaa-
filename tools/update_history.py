"""Run after editing data/prices.json: stamps 'updated', adds today's history point for every priced item
(mid value in USD at the market rate) and keeps the last 180 points. Also validates the file."""
import json, sys, datetime, os
P = os.path.join(os.path.dirname(__file__), '..', 'data', 'prices.json')
d = json.load(open(P, encoding='utf-8'))
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3)))
today = now.date().isoformat()
rate = float(d['fx']['market']['rate'])
errors = []
for it in d['items']:
    for p in it.get('prices', []):
        for k in ('region', 'low', 'high', 'currency', 'date', 'source', 'url'):
            if k not in p: errors.append(f"{it['id']}: price entry missing {k}")
        if p.get('currency') not in ('SYP', 'USD'): errors.append(f"{it['id']}: bad currency {p.get('currency')}")
        if p.get('low', 0) > p.get('high', 0): errors.append(f"{it['id']}: low > high")
    if it.get('prices'):
        vals = [((p['low'] + p['high']) / 2) / (1 if p['currency'] == 'USD' else rate) for p in it['prices']]
        pt = {'date': today, 'usd': round(sum(vals) / len(vals), 4)}
        h = [x for x in it.get('history', []) if x['date'] != today] + [pt]
        it['history'] = h[-180:]
if errors:
    print('\n'.join(errors)); sys.exit(1)
d['updated'] = now.replace(microsecond=0).isoformat()
json.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', d['updated'], sum(1 for i in d['items'] if i.get('prices')), 'priced items')
