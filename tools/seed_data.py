"""Seed dataset (first batch, researched 23-Oct-2026). The daily update task edits data/prices.json directly."""
import json, datetime

S = {
 'cbs':   ('Central Bank of Syria bulletin (via Verify-Sy)', 'https://www.verify-sy.com/ar/topic/economy/newsroom/exchange-rates-in-syria-22OCT'),
 'aks':   ('Aksalser – parallel market rates', 'https://www.aksalser.com/news/2026/10/22/%D8%B3%D8%B9%D8%B1-%D8%B5%D8%B1%D9%81-%D8%A7%D9%84%D8%AF%D9%88%D9%84%D8%A7%D8%B1-%D9%88-%D8%A7%D9%84%D9%8A%D9%88%D8%B1%D9%88-%D9%88-%D8%A7%D9%84%D8%B0%D9%87%D8%A8-%D9%85%D9%82%D8%A7%D8%A8%D9%84-2225/'),
 'spc':   ('Syrian Petroleum Company price list (via Syfatora)', 'https://syfatora.com/fuel'),
 'drama': ('Council of Ministers fuel announcement (report)', 'https://www.drama-s7.com/2026/10/blog-post_924.html'),
 'alsifr':('Al-Sifr – fuel vs minimum wage', 'https://alsifr.org/gasoline-syria'),
 'shofey':('Shofey – Damascus building material prices', 'https://shofey.com/blog/%D8%A3%D8%B3%D8%B9%D8%A7%D8%B1-%D9%85%D9%88%D8%A7%D8%AF-%D8%A7%D9%84%D8%A8%D9%86%D8%A7%D8%A1-%D9%81%D9%8A-%D8%AF%D9%85%D8%B4%D9%82'),
 'cip':   ('CIP Syria – building cost guide 2026', 'https://cip.sy/ar/%D8%AA%D9%83%D9%84%D9%81%D8%A9-%D8%A7%D9%84%D8%A8%D9%86%D8%A7%D8%A1/'),
 'imt':   ('Imtilak – construction costs in Syria', 'https://www.imtilak.sy/ar/articles/construction-costs-in-syria'),
 'yahya': ('Yahya Construction – cost per m² 2026', 'https://yahyaconstruction.com/ar/%D8%AA%D9%83%D9%84%D9%81%D8%A9-%D9%85%D8%AA%D8%B1-%D8%A7%D9%84%D8%A8%D9%86%D8%A7%D8%A1-%D9%81%D9%8A-%D8%B3%D9%88%D8%B1%D9%8A%D8%A7/'),
 'arab':  ('Al Arabiya – Omran cement price', 'https://www.alarabiya.net/aswaq/economy/2026/04/19/%D8%AA%D8%B1%D8%A7%D8%AC%D8%B9-%D9%83%D8%A8%D9%8A%D8%B1-%D8%A8%D8%A7%D8%B3%D8%B9%D8%A7%D8%B1-%D8%A7%D9%84%D8%A7%D8%B3%D9%85%D9%86%D8%AA-%D9%81%D9%8A-%D8%B3%D9%88%D8%B1%D9%8A%D8%A7-%D9%88%D8%AE%D8%B7%D8%B7-%D9%84%D8%A7%D8%B9%D8%A7%D8%AF%D8%A9-%D8%AA%D8%B7%D9%88%D9%8A%D8%B1-%D8%A7%D9%84%D9%82%D8%B7%D8%A7%D8%B9'),
 'qsand': ('Qiwaa – sand and gravel prices 2026', 'https://qiwaa.com/%D8%B3%D8%B9%D8%B1-%D8%A7%D9%84%D8%B1%D9%85%D9%84-%D9%88%D8%A7%D9%84%D8%A8%D8%AD%D8%B5-%D9%81%D9%8A-%D8%B3%D9%88%D8%B1%D9%8A%D8%A7-2026/'),
 'qcer':  ('Qiwaa – ceramic prices 2026', 'https://qiwaa.com/%D8%B3%D8%B9%D8%B1-%D8%A7%D9%84%D8%B3%D9%8A%D8%B1%D8%A7%D9%85%D9%8A%D9%83-%D9%81%D9%8A-%D8%B3%D9%88%D8%B1%D9%8A%D8%A7-2026/'),
 'kulfa': ('Kulfa – Syria price index', 'https://kulfa.app/prices.php?c=sy'),
 'gamb':  ('Gambini Designs – finishing cost 2026', 'https://gambinidesigns.com/blog/interior-finishing-cost-syria-2026.html'),
 'cms':   ('CMS Levant – Damascus construction cost', 'https://www.cmslevant.com/blog/construction-cost-syria-2026.html'),
 'dama':  ('Dama Post – daily worker wage', 'https://damapost.com/15/08/2026/%D8%A7%D9%84%D8%B9%D8%A7%D9%85%D9%84-%D8%A7%D9%84%D9%85%D9%8A%D8%A7%D9%88%D9%85-%D9%81%D9%8A-%D8%B3%D9%88%D8%B1%D9%8A%D8%A7-%D8%A3%D8%AC%D8%B1-%D9%84%D8%A7-%D9%8A%D9%84%D8%AD%D9%82-%D8%A8%D9%83%D9%84/123683/'),
 'waz':   ('Wazaif Syria – salary guide 2026', 'https://wazaifsyria.com/salary'),
}

def P(region, low, high, cur, date, src, note=''):
    n, u = S[src]
    d = {'region': region, 'low': low, 'high': high, 'currency': cur, 'date': date, 'source': n, 'url': u}
    if note: d['note'] = note
    return d

I = []
def item(id, cat, sub, name, unit, prices, spec='', kind='market', tags=''):
    I.append({'id': id, 'category': cat, 'subcategory': sub, 'name': name, 'spec': spec, 'unit': unit,
              'kind': kind, 'tags': tags, 'prices': prices, 'history': []})

G = 'Syria (general)'; D = 'Damascus'
# ---------------- Materials
item('rebar', 'Materials', 'Steel', 'Reinforcing Steel Bar (Rebar)', 'ton', [
    P(D, 125000, 140000, 'SYP', '2026-09-24', 'shofey', '12 mm and 14 mm bars, market price'),
    P(G, 600, 670, 'USD', '2026-10-04', 'cip', '12 mm, linked to global steel price'),
    P(G, 850, 950, 'USD', '2026-06-01', 'yahya', 'Retail estimate')], spec='Deformed bar 8–25 mm', tags='iron steel hadid حديد')
item('cement-bag', 'Materials', 'Cement', 'Portland Cement – Bagged', 'ton', [
    P(D, 19500, 24000, 'SYP', '2026-09-24', 'shofey', '20 bags of 50 kg; ≈ 975–1,200 SYP per bag'),
    P(G, 110, 150, 'USD', '2026-10-04', 'cip')], spec='OPC 42.5, 50 kg bags', tags='cement asmant اسمنت')
item('cement-factory', 'Materials', 'Cement', 'Cement – Ex-Factory (Omran)', 'ton', [
    P(G, 100, 120, 'USD', '2026-04-19', 'arab', 'State company Omran ex-factory; transport extra')], tags='cement omran عمران')
item('sand', 'Materials', 'Aggregates', 'Building Sand', 'm³', [
    P(D, 3500, 5000, 'SYP', '2026-09-24', 'shofey', 'Clean black/silt sand delivered to site'),
    P(G, 18, 29, 'USD', '2026-10-01', 'qsand', 'Washed or building sand')], tags='sand raml رمل')
item('gravel', 'Materials', 'Aggregates', 'Gravel (Concrete Aggregate)', 'm³', [
    P(D, 3000, 4500, 'SYP', '2026-09-24', 'shofey', 'Fine concrete gravel'),
    P(G, 18, 34, 'USD', '2026-10-01', 'qsand', 'Fine to coarse, by grading')], tags='gravel bahs بحص')
item('block', 'Materials', 'Masonry', 'Concrete Block 15 / 20 cm', 'piece', [
    P(D, 38, 55, 'SYP', '2026-09-24', 'shofey', '38 SYP for 15 cm, 55 SYP for 20 cm'),
    P(G, 0.30, 0.45, 'USD', '2026-10-04', 'cip', 'Grade 15 block')], tags='block blok بلوك')
item('readymix', 'Materials', 'Concrete', 'Ready-Mix Concrete C30', 'm³', [
    P(G, 90, 115, 'USD', '2026-10-04', 'cip', 'Includes mixing and delivery')], tags='concrete ready mix beton باطون')
item('slab-concrete', 'Materials', 'Concrete', 'Slab Concrete + Rebar (supply & place)', 'm² of slab', [
    P(G, 35, 50, 'USD', '2026-05-29', 'kulfa')], tags='slab concrete')
item('block-wall', 'Materials', 'Masonry', '20 cm Block Wall with Mortar (supply & build)', 'm²', [
    P(G, 14, 20, 'USD', '2026-05-29', 'kulfa')], tags='block wall')
item('building-stone', 'Materials', 'Stone', 'Building Stone (natural)', 'm²', [], spec='Awaiting a published price', tags='stone hajar حجر')

# ---------------- Finishes
item('plaster-int', 'Finishes', 'Plaster / Render', 'Interior Plaster – Rough + Smooth (Tayneh)', 'm²', [
    P(G, 2.5, 5, 'USD', '2026-06-15', 'kulfa', 'Materials and labour')], tags='plaster lbakh tayneh لبخ طينة')
item('plaster-ext', 'Finishes', 'Plaster / Render', 'Exterior Rough Render', 'm²', [
    P(G, 4, 6, 'USD', '2026-06-15', 'kulfa')], tags='render plaster')
item('plaster-labour', 'Finishes', 'Plaster / Render', 'Plastering – Labour Only', 'm²', [
    P(G, 2.5, 2.5, 'USD', '2026-09-01', 'gamb', 'Surface ≈ 3.5–4.5 × floor area')], tags='plaster labour')
item('gypsum-plaster', 'Finishes', 'Plaster / Render', 'Gypsum Plaster Smoothing', 'm²', [
    P(G, 7, 11, 'USD', '2026-05-29', 'kulfa')], tags='gypsum jibsin')
item('paint-full', 'Finishes', 'Paint', 'Painting – Full Job (putty, primer, finish), local paint', 'm²', [
    P(G, 3, 6, 'USD', '2026-06-15', 'kulfa')], tags='paint dihan دهان')
item('paint-int', 'Finishes', 'Paint', 'Interior Paint – Jotun / Caparol', 'm²', [
    P(G, 4, 6, 'USD', '2026-05-29', 'kulfa')], tags='paint jotun caparol')
item('paint-ext', 'Finishes', 'Paint', 'Exterior Paint – Jotun / Caparol', 'm²', [
    P(G, 6, 10, 'USD', '2026-05-29', 'kulfa')], tags='paint exterior')
item('ceramic-floor', 'Finishes', 'Ceramic & Porcelain', 'Floor Ceramic – Local', 'm²', [
    P(G, 6, 11, 'USD', '2026-10-01', 'qcer'), P(G, 8, 20, 'USD', '2026-10-04', 'cip', 'Medium grade')], tags='ceramic seramik سيراميك')
item('ceramic-wall', 'Finishes', 'Ceramic & Porcelain', 'Wall Ceramic 30×60 – Local', 'm²', [
    P(G, 5, 6, 'USD', '2026-10-01', 'qcer')], tags='ceramic wall')
item('porcelain-local', 'Finishes', 'Ceramic & Porcelain', 'Porcelain – Local', 'm²', [
    P(G, 8, 13, 'USD', '2026-10-01', 'qcer')], tags='porcelain tiles blat بلاط بورسلان')
item('porcelain-iran', 'Finishes', 'Ceramic & Porcelain', 'Porcelain – Iranian', 'm²', [
    P(G, 10, 15, 'USD', '2026-10-01', 'qcer')], tags='porcelain tiles')
item('porcelain-ital', 'Finishes', 'Ceramic & Porcelain', 'Porcelain – Italian', 'm²', [
    P(G, 25, 40, 'USD', '2026-10-01', 'qcer')], tags='porcelain tiles')
item('porcelain-8080', 'Finishes', 'Ceramic & Porcelain', 'Porcelain 80×80 – Material Only', 'm²', [
    P(G, 8, 12.25, 'USD', '2026-06-15', 'kulfa')], tags='porcelain tiles')
item('tile-install', 'Finishes', 'Ceramic & Porcelain', 'Tile / Porcelain Installation – Labour Only', 'm²', [
    P(G, 2.5, 4, 'USD', '2026-06-15', 'kulfa')], tags='tiling labour blat')
item('marble-local', 'Finishes', 'Marble & Stone', 'Marble – Local Syrian', 'm²', [
    P(G, 25, 50, 'USD', '2026-05-29', 'kulfa')], tags='marble rukham رخام')
item('marble-import', 'Finishes', 'Marble & Stone', 'Marble – Turkish / Italian', 'm²', [
    P(G, 50, 100, 'USD', '2026-05-29', 'kulfa')], tags='marble')
item('gypsum-board', 'Finishes', 'Ceilings', 'Gypsum Board False Ceiling', 'm²', [
    P(G, 8.5, 12.5, 'USD', '2026-06-15', 'kulfa')], tags='gypsum board ceiling')
item('facade-stone', 'Finishes', 'Facade', 'Facade – Natural Stone Cladding', 'm²', [
    P(G, 40, 75, 'USD', '2026-05-29', 'kulfa')], tags='facade stone wajiha واجهة حجر')
item('facade-artstone', 'Finishes', 'Facade', 'Facade – Artificial Stone', 'm²', [
    P(G, 20, 38, 'USD', '2026-05-29', 'kulfa')], tags='facade')
item('facade-alu', 'Finishes', 'Facade', 'Facade – Aluminium Composite Cladding', 'm²', [
    P(G, 32, 55, 'USD', '2026-05-29', 'kulfa')], tags='facade alucobond')
item('facade-wpc', 'Finishes', 'Facade', 'Facade – WPC Wood Cladding', 'm²', [
    P(G, 28, 45, 'USD', '2026-05-29', 'kulfa')], tags='facade wpc')
item('window-local', 'Finishes', 'Aluminium & Doors', 'Aluminium Windows – Profile 60, Local / Iranian', 'm²', [
    P(G, 45, 72, 'USD', '2026-05-29', 'kulfa')], tags='aluminium windows')
item('window-tr', 'Finishes', 'Aluminium & Doors', 'Aluminium Windows – Profile 60, Turkish', 'm²', [
    P(G, 60, 95, 'USD', '2026-05-29', 'kulfa')], tags='aluminium windows')
item('window-tb', 'Finishes', 'Aluminium & Doors', 'Aluminium Windows – Thermal Break, Turkish', 'm²', [
    P(G, 100, 145, 'USD', '2026-05-29', 'kulfa')], tags='aluminium windows')
item('door-mdf', 'Finishes', 'Aluminium & Doors', 'Interior Door – Local MDF', 'piece', [
    P(G, 80, 140, 'USD', '2026-05-29', 'kulfa')], tags='door')
item('elec-install', 'Finishes', 'MEP', 'Electrical Installation – Local / Chinese Materials', 'm²', [
    P(G, 7, 12, 'USD', '2026-05-29', 'kulfa')], tags='electrical')

# ---------------- Equipment rental
for eid, nm, unit in [('excavator', 'Excavator (Poclain) 20–30 t – with operator', 'hour'), ('loader', 'Wheel Loader (Trax) – with operator', 'hour'),
                      ('backhoe', 'Backhoe Loader (JCB) – with operator', 'hour'), ('dumptruck', 'Dump Truck (Qallab) – per trip', 'trip'),
                      ('mixer', 'Concrete Mixer Truck', 'day'), ('pump', 'Concrete Pump', 'pour'),
                      ('mobilecrane', 'Mobile Crane 25–50 t', 'day'), ('watertanker', 'Water Tanker', 'trip'),
                      ('compactor', 'Vibratory Roller / Compactor', 'day'), ('generator', 'Generator 100 kVA', 'day')]:
    item(eid, 'Equipment', 'Rental', nm, unit, [], spec='Awaiting a published price', tags='equipment rental ijar آليات')
item('crane-lift', 'Equipment', 'Rental', 'Crane Lift – Water Tank to Roof', 'lift', [P(G, 60, 90, 'USD', '2026-06-15', 'kulfa')], tags='crane')

# ---------------- Fuel (official)
item('gasoline95', 'Fuel', 'Gasoline', 'Gasoline Octane 95', 'litre', [
    P(G, 195, 195, 'SYP', '2026-09-16', 'spc'), P(G, 195, 195, 'SYP', '2026-10-05', 'drama')], kind='official', tags='benzine benzin بنزين')
item('gasoline90', 'Fuel', 'Gasoline', 'Gasoline Octane 90', 'litre', [
    P(G, 185, 185, 'SYP', '2026-09-16', 'spc'), P(G, 185, 185, 'SYP', '2026-10-05', 'drama')], kind='official', tags='benzine بنزين')
item('diesel', 'Fuel', 'Diesel', 'Diesel (Mazout)', 'litre', [
    P(G, 175, 175, 'SYP', '2026-09-16', 'spc'), P(G, 175, 175, 'SYP', '2026-10-05', 'drama')], kind='official', tags='diesel mazout مازوت')
item('lpg-home', 'Fuel', 'Gas', 'Household Gas Cylinder (10 kg)', 'cylinder', [
    P(G, 1600, 1600, 'SYP', '2026-09-16', 'spc')], kind='official', tags='gas ghaz غاز')
item('lpg-ind', 'Fuel', 'Gas', 'Industrial Gas Cylinder', 'cylinder', [
    P(G, 2400, 2400, 'SYP', '2026-09-16', 'spc'), P(G, 2560, 2560, 'SYP', '2026-10-05', 'drama')], kind='official', tags='gas industrial')
item('fueloil', 'Fuel', 'Fuel Oil', 'Fuel Oil (Fuel)', 'ton', [P(G, 52800, 52800, 'SYP', '2026-10-05', 'drama')], kind='official', tags='fuel oil fiol فيول')

# ---------------- Labour & salaries
item('worker', 'Labour', 'Daily Wages', 'Construction Labourer', 'day', [
    P(G, 15, 18, 'USD', '2026-10-04', 'cip')], tags='worker amil عامل labour')
item('skilled', 'Labour', 'Daily Wages', 'Skilled Tradesman (mason, tiler, carpenter, operator)', 'day', [
    P(G, 20, 35, 'USD', '2026-10-04', 'cip')], tags='craftsman sinaye صنايعي mason tiler carpenter')
item('elec-plumb', 'Labour', 'Daily Wages', 'Electrician / Plumber', 'day', [
    P(G, 25, 45, 'USD', '2026-10-04', 'cip')], tags='electrician plumber')
item('daily-avg', 'Labour', 'Daily Wages', 'Daily Worker – National Average (all sectors)', 'day', [
    P(G, 966, 966, 'SYP', '2026-08-15', 'dama', 'June 2026 average')], tags='daily worker')
item('foreman', 'Labour', 'Salaries', 'Site Foreman', 'month', [], spec='Awaiting a published price', tags='foreman formani فورمان')
item('site-eng', 'Labour', 'Salaries', 'Site Supervising Engineer', 'month', [
    P(G, 600, 1200, 'USD', '2026-10-04', 'cip')], tags='engineer muhandis مهندس')
item('engineer', 'Labour', 'Salaries', 'Engineer – General (all fields)', 'month', [
    P(G, 30000, 125000, 'SYP', '2026-10-01', 'waz', 'Estimated range; average 60,000')], tags='engineer')
item('pm', 'Labour', 'Salaries', 'Project Manager', 'month', [
    P(G, 120000, 210000, 'SYP', '2026-10-01', 'waz')], tags='project manager')
item('accountant', 'Labour', 'Salaries', 'Accountant', 'month', [
    P(G, 25000, 110000, 'SYP', '2026-10-01', 'waz', 'Average 50,000')], tags='admin accountant idari إداري')
item('hr', 'Labour', 'Salaries', 'HR Manager', 'month', [
    P(G, 122000, 195000, 'SYP', '2026-10-01', 'waz')], tags='admin hr')
item('driver', 'Labour', 'Salaries', 'Driver', 'month', [
    P(G, 15000, 35000, 'SYP', '2026-10-01', 'waz', 'Average 22,000')], tags='driver')
item('minwage', 'Labour', 'Salaries', 'National Minimum Wage', 'month', [
    P(G, 12560, 12560, 'SYP', '2026-09-15', 'alsifr')], kind='official', tags='minimum wage')
item('supervision', 'Labour', 'Engineering Fees', 'Engineering Supervision Fee', 'm²', [
    P(G, 3, 7, 'USD', '2026-06-18', 'imt')], tags='supervision engineer fee')

# ---------------- Building cost per m2
item('cost-structure', 'Building Cost', 'Cost per m²', 'Structure Only (skeleton)', 'm²', [
    P(D, 240, 350, 'USD', '2026-10-01', 'cms'), P(G, 120, 150, 'USD', '2026-10-04', 'cip')], tags='cost skeleton adhm عظم')
item('cost-turnkey', 'Building Cost', 'Cost per m²', 'Turnkey – Medium Finishing', 'm²', [
    P(D, 400, 650, 'USD', '2026-10-01', 'cms'), P(G, 255, 320, 'USD', '2026-10-04', 'cip')], tags='cost turnkey iksa إكساء')
item('cost-finish', 'Building Cost', 'Cost per m²', 'Finishing Only – Mid Range', 'm²', [
    P(D, 200, 320, 'USD', '2026-09-01', 'gamb'), P('Aleppo', 170, 300, 'USD', '2026-09-01', 'gamb'), P('Homs', 165, 285, 'USD', '2026-09-01', 'gamb'),
    P('Latakia', 185, 300, 'USD', '2026-09-01', 'gamb')], tags='finishing iksa')

data = {
  'app': 'Syria Construction Prices', 'schema': 1,
  'updated': '2026-10-23T17:00:00+03:00',
  'fx': {'official': {'rate': 122.0, 'date': '2026-10-22', 'source': S['cbs'][0], 'url': S['cbs'][1]},
         'market': {'rate': 139.25, 'date': '2026-10-22', 'source': S['aks'][0], 'url': S['aks'][1]},
         'note': 'New Syrian pound (2 zeros removed in 2026). Conversions use the market rate.'},
  'regions': ['Syria (general)', 'Damascus', 'Rif Dimashq', 'Aleppo', 'Homs', 'Hama', 'Latakia', 'Tartus'],
  'categories': ['Materials', 'Finishes', 'Equipment', 'Fuel', 'Labour', 'Building Cost'],
  'items': I,
}
today = '2026-10-23'
for it in I:
    if it['prices']:
        # history: one point per update day, mid value converted to USD at market rate
        lows = []
        for p in it['prices']:
            mid = (p['low'] + p['high']) / 2
            lows.append(mid if p['currency'] == 'USD' else mid / data['fx']['market']['rate'])
        it['history'] = [{'date': today, 'usd': round(sum(lows) / len(lows), 4)}]
json.dump(data, open('/home/claude/-asaar-albinaa-/data/prices.json', 'w'), ensure_ascii=False, indent=1)
print(len(I), 'items;', sum(1 for i in I if i['prices']), 'with prices')
