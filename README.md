# PRETTYMUCH: a career in data

A small, hand-compiled dataset covering the career of the pop/R&B boy band PRETTYMUCH, from its formation by Simon Cowell in 2016 to the disband announcement on October 29, 2023. It is the data behind the interactive dashboard: https://claude.ai/artifact/GWNq8b7nW7pSkPJkbxHB74

## Files

| File | Rows | What it holds |
|---|---|---|
| `releases.csv` | 39 | Every single, EP and the album: date, project, features, label era |
| `videos.csv` | 25 | Music videos with directors |
| `events.csv` | 16 | Tours, TV and award-show appearances, and a release party |
| `awards.csv` | 6 | Award nominations (no wins listed) |
| `members.csv` | 5 | Member birth dates, origins and years in the group |
| `timeline.csv` | 8 | One row per year, 2016 to 2023: label era, member count, releases and videos |
| `build.py` | | Script that generates all of the CSVs, so edits belong here |

## Column notes

**`releases.csv`**
- `type`: `single`, `EP` or `album`. The Smackables deluxe edition is counted as its own EP entry, giving 6 EP rows for the 5 EPs.
- `release_date`: ISO format, as precise as the sources allow. `date_precision` says whether it is `day`, `month` or `year`, so filter on it before doing any date arithmetic.
- `project`: the EP or album a single belongs to, or `Non-album`. This follows the grouping in the source table and is partly inferred where the table's row spans were ambiguous.
- `label_era`: `Syco` (to 2020), `Sire` (from December 2020), `Independent` (from 2022), or `Unconfirmed` where the sources do not say.
- `featured_artist`: guests and collaborators, separated by semicolons.

**`events.csv`**: `verification` is `confirmed` unless I could not re-check a claim. The Jack & Jack Tour and Roxy Tour openers came from an earlier search and are marked `unverified`.

**`timeline.csv`**: `members_at_year_end` is 5 until Nick Mara left on October 7, 2022 (4 at the end of 2022), and 0 after the October 2023 disband announcement.

## Quick start

```python
import pandas as pd
r = pd.read_csv("releases.csv")
print(r.groupby(["year", "type"]).size().unstack(fill_value=0))
print(pd.read_csv("videos.csv").director.value_counts())
```

## Known limitations

- **Totals do not match the source summary.** Wikipedia's summary box states 25 singles and 23 videos, but its tables list more (this dataset has 32 singles and 25 videos). I followed the tables.
- **Some dates are only a month or a year**, so the data cannot place every release in order within a year.
- **Chart positions are excluded.** The chart columns in the source were unreadable, so no peak positions are included beyond what appeared in prose.
- **There is no streaming data** (plays, listeners, followers). I could not verify any, and none is invented.
- **Director credits** for "Blind," "Phases" and "Lying" follow the grouping in the source table.
- **"H2L"** is included as a release because multiple sources cite it, though the source's singles table omits it.
- **The second EMA "Best Group" nomination** is ambiguous in the source.

## Sources and licence

Compiled from Wikipedia's PrettyMuch and Nick Mara articles (including its discography, awards and references), plus Qobuz, Last.fm, MTV, BroadwayWorld and press coverage cited there. Wikipedia text is licensed CC BY-SA, so if you redistribute this dataset, credit those sources and share it under a compatible licence. Verify anything important against the original sources before relying on it.
