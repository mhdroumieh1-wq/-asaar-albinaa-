# Daily price update – procedure

This file tells the daily update task how to refresh `data/prices.json`, which the Android app reads from
`https://raw.githubusercontent.com/mhdroumieh1-wq/-asaar-albinaa-/main/data/prices.json`.

## Rules
- Currency: Syria uses the **new Syrian pound** (two zeros removed in 2026). Record SYP prices in new pounds.
  If a source quotes old pounds (e.g. 14,000 per USD, 1,950,000 per ton of cement), divide by 100.
- Record each price exactly as published: `low`, `high` (equal if a single value), `currency` (`SYP` or `USD`),
  `date` (publication date of the source, not today), `source` (site / page name), `url`, optional `note`.
- `region`: one of `data.regions`. Use `Syria (general)` when the source does not name a city.
- Never invent or estimate a price. If no new source is found, leave the item unchanged.
- Keep at most 4 price entries per item: when adding a newer entry from the same source, replace the older one;
  otherwise drop the oldest entry.
- Facebook / Telegram: use only public posts that appear in web search results, with the post URL.
- Plausibility check before saving (at the market rate): rebar 500–1,200 USD/t, cement 80–250 USD/t,
  sand/gravel 10–45 USD/m³, block 0.2–0.8 USD/piece, ready-mix 60–160 USD/m³, diesel 0.6–2 USD/l.
  Reject values outside these bands unless the source explicitly explains a big change.

## Daily steps
1. **Exchange rate**: update `fx.official` (Central Bank of Syria bulletin) and `fx.market` (parallel market) with date and URL.
2. **Fuel** (official SPC / Ministry of Energy prices): gasoline 95 and 90, diesel, household and industrial gas, fuel oil.
3. **Materials**: rebar, cement (bagged and ex-factory), sand, gravel, block, ready-mix concrete, building stone.
4. **Finishes**: plaster, paint, ceramic, porcelain, marble, gypsum board, facade cladding, aluminium, doors.
5. **Equipment rental**: excavator, loader, backhoe, dump truck, mixer, concrete pump, crane, water tanker,
   compactor, generator (many have no published price yet – keep searching).
6. **Labour & salaries**: labourer, skilled trades, electrician/plumber, foreman, engineers, PM, admin, driver, minimum wage.
7. **Building cost per m²**: structure only, turnkey, finishing.
8. Search in Arabic and English, for example: `سعر طن الحديد سوريا اليوم`, `أسعار مواد البناء دمشق`,
   `سعر متر الباطون الجاهز سوريا`, `أجرة ساعة البوكلين سوريا`, `يومية عامل البناء سوريا`, `أسعار المحروقات سوريا اليوم`,
   `site:facebook.com أسعار مواد البناء دمشق`, plus city names (حلب، حمص، حماة، اللاذقية، طرطوس، ريف دمشق).
   Prefer sources published in the last 30 days.
9. You may add a new item (unique `id`, `category` from `data.categories`, `subcategory`, `name`, `unit`, `kind`
   = `market` or `official`, `tags` with English + Arabic search words, `prices`, `history: []`).
10. Run `python3 tools/update_history.py` (validates, stamps `updated`, appends today's trend point).
11. Commit with message `Daily prices YYYY-MM-DD` and push to `main`.
12. Report: number of items updated, notable price changes (> 5%), items still without data.
