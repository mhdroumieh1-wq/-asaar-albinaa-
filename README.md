# Syria Construction Prices (SY Build Prices)

English Android app showing daily-updated indicative construction and contracting prices in Syria:
building materials, finishing works, equipment rental, fuel, labour wages and salaries, and building cost per m².

- `data/prices.json` – the price database (updated daily, see `UPDATE_GUIDE.md`)
- `android/` – app source (WebView shell + offline HTML UI); build with `android/build.sh`
- `tools/` – data helpers

The app downloads `data/prices.json` from this repository, keeps the last copy for offline use, and lets the user
store private supplier prices on the phone. Prices are indicative only.
