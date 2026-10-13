# MLB Playoffs 2026: Structure, Rules and Bracket

*Snapshot updated Monday, Oct. 5, 2026. Results are complete through Sunday, Oct. 4. Games dated Oct. 5 or later are shown as scheduled, even if they have since started or finished.*

## How MLB is organized

Major League Baseball has 30 teams split into two leagues, the **American League (AL)** and the **National League (NL)**. Each league has three divisions (East, Central and West) of five teams each. Teams are scheduled to play 162 regular-season games; a final record can total 161 if a postponed game is not made up. The 2026 final standings below list every team by division.

## Making the playoffs

Each league sends six teams to the postseason, 12 in total.

**Division winners (seeds 1–3).** The team with the best record in each division wins it. The three division winners are seeded 1 through 3 by regular-season winning percentage, with tiebreakers where needed.

**Wild cards (seeds 4–6).** The wild cards are the three teams with the best records among everyone else in the league, regardless of division. They are seeded 4 through 6 by regular-season winning percentage, with tiebreakers where needed.

Division winners always outrank wild cards. A division winner with a worse record than a wild card still gets the higher seed. In 2026 the Astros won the AL West at 81-81 and were seeded third, ahead of the 93-68 Yankees.

**Tiebreakers.** Since 2022, ties that affect a postseason berth or seed are settled by regular-season results, starting with head-to-head record, rather than by a one-game playoff.

## The rounds

1. **Wild Card Series (best of 3).** Seed 3 hosts seed 6, and seed 4 hosts seed 5. The higher seed hosts every game. Seeds 1 and 2 get a bye.
1. **Division Series (best of 5).** Seed 1 plays the 4/5 winner, and seed 2 plays the 3/6 winner. The bracket is fixed, so MLB does not reseed after the first round. The higher seed hosts Games 1, 2 and 5 (a 2-2-1 format).
1. **League Championship Series (best of 7).** The two Division Series winners in each league play for the pennant: the ALCS decides the AL champion and the NLCS decides the NL champion. The higher seed hosts Games 1, 2, 6 and 7 (a 2-3-2 format).
1. **World Series (best of 7).** The AL champion plays the NL champion. The team with the better regular-season record hosts Games 1, 2, 6 and 7, regardless of league seed. If their records match, MLB applies its tiebreaker rules.

## Why it matters

Winning a division guarantees a playoff spot and a top-three seed. The top two division winners in each league advance directly to the Division Series, avoiding elimination in the best-of-three opener and gaining rest. Wild-card teams can still win the pennant and World Series.

## The bracket at a glance

This is the format for one league. The AL and NL each run an identical bracket, and their champions meet in the World Series.

```mermaid
%% One-league overview. Theme, dagre layout, and light canvas
%% keep the diagram legible in light and dark viewers.
%%{init: {
  "theme": "base",
  "layout": "dagre",
  "themeVariables": {
    "background": "#ffffff",
    "primaryColor": "#ffffff",
    "primaryTextColor": "#000000",
    "primaryBorderColor": "#c0c0c0",
    "textColor": "#2f4f4f",
    "titleColor": "#2f4f4f",
    "lineColor": "#696969",
    "edgeLabelBackground": "#ffffff",
    "clusterBkg": "#ffffff",
    "clusterBorder": "#c0c0c0"
  },
  "flowchart": {
    "curve": "monotoneX",
    "nodeSpacing": 50,
    "rankSpacing": 50,
    "htmlLabels": true
  }
}}%%
flowchart LR

  %% SG_BRACKET: invisible white wrapper around the whole
  %% bracket. Its label is a single space so no title shows.
  %% The white fill keeps the space between groups (and the
  %% gray connecting lines) readable on a dark page.
  subgraph SG_BRACKET[" "]
    direction LR

    %% Seeds: purple = division winners, teal = wild cards.
    %% Order is chosen so each seed sits next to its opponent.
    subgraph SG_SEEDS["Seeds"]
      SEED_01["Seed 1<br/>Division winner"]:::nodeDivisionWinner
      SEED_04["Seed 4<br/>Wild card"]:::nodeWildCard
      SEED_05["Seed 5<br/>Wild card"]:::nodeWildCard
      SEED_02["Seed 2<br/>Division winner"]:::nodeDivisionWinner
      SEED_03["Seed 3<br/>Division winner"]:::nodeDivisionWinner
      SEED_06["Seed 6<br/>Wild card"]:::nodeWildCard
    end

    %% Round 1: seeds 3-6 play; seeds 1 and 2 have a bye.
    %% Each bye is a dashed pass-through node in this round's
    %% column, listed in bracket order, so every Division
    %% Series line arrives from the same column without
    %% crossing another line.
    subgraph SG_WILD_CARD_SERIES["Wild Card Series"]
      BYE_01["bye"]:::nodeBye
      WILD_CARD_04_05["4 hosts 5<br/>Best of 3"]:::nodeWildCardSeries
      BYE_02["bye"]:::nodeBye
      WILD_CARD_03_06["3 hosts 6<br/>Best of 3"]:::nodeWildCardSeries
    end

    %% Round 2: fixed bracket, no reseeding.
    subgraph SG_DIVISION_SERIES["Division Series"]
      DIVISION_SERIES_01["1 vs 4/5 winner<br/>Best of 5"]:::nodeDivisionSeries
      DIVISION_SERIES_02["2 vs 3/6 winner<br/>Best of 5"]:::nodeDivisionSeries
    end

    %% Round 3: the pennant.
    LEAGUE_CHAMPIONSHIP["League Championship<br/>Best of 7"]:::nodeLeagueChampionship

    %% Round 4: against the other league's champion.
    WORLD_SERIES["World Series<br/>Best of 7<br/>vs other league's champ"]:::nodeWorldSeries

    %% Seeds 1 and 2 pass through their bye to the Division
    %% Series ("---" draws a line without an arrowhead).
    SEED_04 & SEED_05 --> WILD_CARD_04_05
    SEED_03 & SEED_06 --> WILD_CARD_03_06
    SEED_01 --- BYE_01 --> DIVISION_SERIES_01
    WILD_CARD_04_05 --> DIVISION_SERIES_01
    SEED_02 --- BYE_02 --> DIVISION_SERIES_02
    WILD_CARD_03_06 --> DIVISION_SERIES_02
    DIVISION_SERIES_01 & DIVISION_SERIES_02 --> LEAGUE_CHAMPIONSHIP
    LEAGUE_CHAMPIONSHIP --> WORLD_SERIES
  end

  %% Styles (named CSS colors, same palette as the full diagram).
  classDef nodeDivisionWinner fill:lavender,stroke:slateblue,stroke-width:0.5px,color:darkslateblue
  classDef nodeWildCard fill:honeydew,stroke:teal,stroke-width:0.5px,color:darkslategray
  classDef nodeWildCardSeries fill:lavenderblush,stroke:palevioletred,stroke-width:0.5px,color:mediumvioletred
  classDef nodeDivisionSeries fill:whitesmoke,stroke:dimgray,stroke-width:0.5px,color:black
  classDef nodeLeagueChampionship fill:aliceblue,stroke:steelblue,stroke-width:0.5px,color:midnightblue
  classDef nodeWorldSeries fill:cornsilk,stroke:darkgoldenrod,stroke-width:0.5px,color:saddlebrown
  classDef nodeBye fill:white,stroke:silver,stroke-width:0.5px,stroke-dasharray:3 3,color:dimgray
  classDef groupStage fill:white,stroke:silver,stroke-width:0.5px
  class SG_SEEDS,SG_WILD_CARD_SERIES,SG_DIVISION_SERIES groupStage
  %% Invisible SG_BRACKET wrapper: white fill, no border.
  classDef groupWrapper fill:white,stroke:none
  class SG_BRACKET groupWrapper
```

## 2026 final division standings

Teams are listed in finishing order. Bold marks a division winner; WC marks a wild card.

| League | Division | Teams (regular-season record) |
| ------ | -------- | ----------------------------- |
| AL | East | **Rays 98-64**<br>Yankees 93-68 · WC<br>Red Sox 87-75 · WC<br>Orioles 79-82<br>Blue Jays 79-83 |
| AL | Central | **Guardians 85-77**<br>White Sox 84-78 · WC<br>Twins 77-85<br>Tigers 76-86<br>Royals 69-93 |
| AL | West | **Astros 81-81**<br>Rangers 80-82<br>Mariners 76-86<br>Athletics 64-98<br>Angels 62-100 |
| NL | East | **Braves 94-68**<br>Phillies 88-74 · WC<br>Marlins 80-82<br>Nationals 77-85<br>Mets 74-88 |
| NL | Central | **Brewers 103-59**<br>Cubs 89-73 · WC<br>Pirates 82-80<br>Cardinals 77-85<br>Reds 75-87 |
| NL | West | **Dodgers 100-62**<br>Padres 91-71 · WC<br>D-backs 86-76<br>Giants 65-97<br>Rockies 58-104 |

## The 2026 field

| Seed | American League   | National League  | Qualification        |
| ---- | ----------------- | ---------------- | -------------------- |
| 1    | Rays (98-64)      | Brewers (103-59) | Division winner; bye |
| 2    | Guardians (85-77) | Dodgers (100-62) | Division winner; bye |
| 3    | Astros (81-81)    | Braves (94-68)   | Division winner      |
| 4    | Yankees (93-68)   | Padres (91-71)   | First wild card      |
| 5    | Red Sox (87-75)   | Cubs (89-73)     | Second wild card     |
| 6    | White Sox (84-78) | Phillies (88-74) | Third wild card      |

The Astros' division title gave them the AL's third seed despite the Yankees' better record. The D-backs (86-76) missed the NL's last wild-card spot by two games.

## Key dates

| Round            | Dates (2026)      |
| ---------------- | ----------------- |
| Wild Card Series | Sept. 29 – Oct. 1 |
| Division Series  | Oct. 3 – Oct. 10  |
| NLCS             | Oct. 11 – Oct. 19 |
| ALCS             | Oct. 12 – Oct. 20 |
| World Series     | Oct. 23 – Oct. 31 |

Games marked with an asterisk in the brackets are played only if needed. A World Series Game 7 would fall on Halloween. All dates come from MLB's published schedule and are subject to change.

## 2026 postseason bracket

The diagrams show results through Oct. 4 and later games as scheduled. They are the only place in this document that lists individual game scores.

Each completed game line gives the **winner first**, then the score. For a scheduled game, `@TB` means Tampa Bay hosts. An asterisk marks a game played only if necessary. In the league brackets, `@Hi` and `@Lo` mean the higher and lower seed; in the World Series, they mean the teams with the better and worse regular-season records.

**Team codes:** AL: BOS = Red Sox, CLE = Guardians, CWS = White Sox, HOU = Astros, NYY = Yankees, TB = Rays. NL: ATL = Braves, CHC = Cubs, LAD = Dodgers, MIL = Brewers, PHI = Phillies, SD = Padres.

The diagrams use the same colors as the overview: purple for division winners, teal for wild cards, pink for Wild Card Series, gray for Division Series, blue for league championships, and gold for the World Series. The light canvas and dagre layout are set inside each Mermaid block.

### American League

```mermaid
%% 2026 AL bracket. Results through Oct. 4; later games scheduled.
%% Edit results, series status, conditional games, and next-round
%% placeholders in this block as the postseason progresses.
%%{init: {
  "theme": "base",
  "layout": "dagre",
  "themeVariables": {
    "background": "#ffffff",
    "textColor": "#2f4f4f",
    "lineColor": "#696969",
    "clusterBkg": "#ffffff",
    "clusterBorder": "#c0c0c0"
  },
  "flowchart": {
    "curve": "monotoneY",
    "nodeSpacing": 45,
    "rankSpacing": 55,
    "htmlLabels": true,
    "wrappingWidth": 400
  }
}}%%
flowchart TB
  subgraph SG_AL_SEEDING["2026 seeds"]
    direction LR
    AL_SEED_01["1 · Rays 98-64"]:::nodeDivisionWinner
    AL_SEED_04_05["4 · Yankees 93-68<br/>5 · Red Sox 87-75 · out"]:::nodeWildCard
    AL_SEED_02["2 · Guardians 85-77"]:::nodeDivisionWinner
    AL_SEED_03["3 · Astros 81-81 · out"]:::nodeDivisionWinner
    AL_SEED_06["6 · White Sox 84-78"]:::nodeWildCard
  end

  subgraph SG_AL_WILD_CARD["Wild Card Series · final"]
    direction LR
    AL_BYE_01["bye"]:::nodeBye
    AL_WILD_CARD_04_05["Best of 3<br/><b>Yankees</b> def. Red Sox 2-0<br/>G1 · Tue 9/29 · NYY 9-0<br/>G2 · Wed 9/30 · NYY 9-2"]:::nodeWildCardSeries
    AL_BYE_02["bye"]:::nodeBye
    AL_WILD_CARD_03_06["Best of 3<br/><b>White Sox</b> def. Astros 2-0<br/>G1 · Tue 9/29 · CWS 6-3<br/>G2 · Wed 9/30 · CWS 7-3"]:::nodeWildCardSeries
  end

  subgraph SG_AL_DIVISION_SERIES["Division Series"]
    direction LR
    AL_DIVISION_SERIES_01["Best of 5<br/>Rays vs Yankees · TB leads 1-0<br/>G1 · Sat 10/3 · TB 1-0<br/>G2 · Mon 10/5 · @TB<br/>G3 · Wed 10/7 · @NYY<br/>G4* · Thu 10/8 · @NYY<br/>G5* · Sat 10/10 · @TB"]:::nodeDivisionSeries
    AL_DIVISION_SERIES_02["Best of 5<br/>Guardians vs White Sox · CWS leads 1-0<br/>G1 · Sat 10/3 · CWS 3-0<br/>G2 · Mon 10/5 · @CLE<br/>G3 · Wed 10/7 · @CWS<br/>G4* · Thu 10/8 · @CWS<br/>G5* · Sat 10/10 · @CLE"]:::nodeDivisionSeries
  end

  AL_CHAMPIONSHIP["ALCS · Best of 7<br/>TB/NYY vs CLE/CWS<br/>G1 · Mon 10/12 · @Hi<br/>G2 · Tue 10/13 · @Hi<br/>G3 · Thu 10/15 · @Lo<br/>G4 · Fri 10/16 · @Lo<br/>G5* · Sat 10/17 · @Lo<br/>G6* · Mon 10/19 · @Hi<br/>G7* · Tue 10/20 · @Hi"]:::nodeLeagueChampionship

  AL_SEED_01 --- AL_BYE_01
  AL_SEED_04_05 --> AL_WILD_CARD_04_05
  AL_SEED_02 --- AL_BYE_02
  AL_SEED_03 & AL_SEED_06 --> AL_WILD_CARD_03_06
  AL_BYE_01 & AL_WILD_CARD_04_05 --> AL_DIVISION_SERIES_01
  AL_BYE_02 & AL_WILD_CARD_03_06 --> AL_DIVISION_SERIES_02
  AL_DIVISION_SERIES_01 & AL_DIVISION_SERIES_02 --> AL_CHAMPIONSHIP

  classDef nodeDivisionWinner fill:lavender,stroke:slateblue,stroke-width:0.5px,color:darkslateblue
  classDef nodeWildCard fill:honeydew,stroke:teal,stroke-width:0.5px,color:darkslategray
  classDef nodeWildCardSeries fill:lavenderblush,stroke:palevioletred,stroke-width:0.5px,color:mediumvioletred
  classDef nodeDivisionSeries fill:whitesmoke,stroke:dimgray,stroke-width:0.5px,color:black
  classDef nodeLeagueChampionship fill:aliceblue,stroke:steelblue,stroke-width:0.5px,color:midnightblue
  classDef nodeBye fill:white,stroke:silver,stroke-width:0.5px,stroke-dasharray:3 3,color:dimgray
  classDef groupStage fill:white,stroke:silver,stroke-width:0.5px
  class SG_AL_SEEDING,SG_AL_WILD_CARD,SG_AL_DIVISION_SERIES groupStage
```

### National League

```mermaid
%% 2026 NL bracket. Results through Oct. 4; later games scheduled.
%% Game 4 of Dodgers-Braves is guaranteed after the 1-1 split.
%%{init: {
  "theme": "base",
  "layout": "dagre",
  "themeVariables": {
    "background": "#ffffff",
    "textColor": "#2f4f4f",
    "lineColor": "#696969",
    "clusterBkg": "#ffffff",
    "clusterBorder": "#c0c0c0"
  },
  "flowchart": {
    "curve": "monotoneY",
    "nodeSpacing": 45,
    "rankSpacing": 55,
    "htmlLabels": true,
    "wrappingWidth": 400
  }
}}%%
flowchart TB
  subgraph SG_NL_SEEDING["2026 seeds"]
    direction LR
    NL_SEED_01["1 · Brewers 103-59"]:::nodeDivisionWinner
    NL_SEED_04_05["4 · Padres 91-71<br/>5 · Cubs 89-73 · out"]:::nodeWildCard
    NL_SEED_02["2 · Dodgers 100-62"]:::nodeDivisionWinner
    NL_SEED_03["3 · Braves 94-68"]:::nodeDivisionWinner
    NL_SEED_06["6 · Phillies 88-74 · out"]:::nodeWildCard
  end

  subgraph SG_NL_WILD_CARD["Wild Card Series · final"]
    direction LR
    NL_BYE_01["bye"]:::nodeBye
    NL_WILD_CARD_04_05["Best of 3<br/><b>Padres</b> def. Cubs 2-0<br/>G1 · Tue 9/29 · SD 8-0<br/>G2 · Wed 9/30 · SD 4-1"]:::nodeWildCardSeries
    NL_BYE_02["bye"]:::nodeBye
    NL_WILD_CARD_03_06["Best of 3<br/><b>Braves</b> def. Phillies 2-1<br/>G1 · Tue 9/29 · ATL 5-3<br/>G2 · Wed 9/30 · PHI 4-3 (10)<br/>G3 · Thu 10/1 · ATL 6-2"]:::nodeWildCardSeries
  end

  subgraph SG_NL_DIVISION_SERIES["Division Series"]
    direction LR
    NL_DIVISION_SERIES_01["Best of 5<br/>Brewers vs Padres · MIL leads 2-0<br/>G1 · Sat 10/3 · MIL 3-2<br/>G2 · Sun 10/4 · MIL 4-3<br/>G3 · Tue 10/6 · @SD<br/>G4* · Wed 10/7 · @SD<br/>G5* · Fri 10/9 · @MIL"]:::nodeDivisionSeries
    NL_DIVISION_SERIES_02["Best of 5<br/>Dodgers vs Braves · tied 1-1<br/>G1 · Sat 10/3 · LAD 5-3<br/>G2 · Sun 10/4 · ATL 3-2<br/>G3 · Tue 10/6 · @ATL<br/>G4 · Wed 10/7 · @ATL<br/>G5* · Fri 10/9 · @LAD"]:::nodeDivisionSeries
  end

  NL_CHAMPIONSHIP["NLCS · Best of 7<br/>MIL/SD vs LAD/ATL<br/>G1 · Sun 10/11 · @Hi<br/>G2 · Mon 10/12 · @Hi<br/>G3 · Wed 10/14 · @Lo<br/>G4 · Thu 10/15 · @Lo<br/>G5* · Fri 10/16 · @Lo<br/>G6* · Sun 10/18 · @Hi<br/>G7* · Mon 10/19 · @Hi"]:::nodeLeagueChampionship

  NL_SEED_01 --- NL_BYE_01
  NL_SEED_04_05 --> NL_WILD_CARD_04_05
  NL_SEED_02 --- NL_BYE_02
  NL_SEED_03 & NL_SEED_06 --> NL_WILD_CARD_03_06
  NL_BYE_01 & NL_WILD_CARD_04_05 --> NL_DIVISION_SERIES_01
  NL_BYE_02 & NL_WILD_CARD_03_06 --> NL_DIVISION_SERIES_02
  NL_DIVISION_SERIES_01 & NL_DIVISION_SERIES_02 --> NL_CHAMPIONSHIP

  classDef nodeDivisionWinner fill:lavender,stroke:slateblue,stroke-width:0.5px,color:darkslateblue
  classDef nodeWildCard fill:honeydew,stroke:teal,stroke-width:0.5px,color:darkslategray
  classDef nodeWildCardSeries fill:lavenderblush,stroke:palevioletred,stroke-width:0.5px,color:mediumvioletred
  classDef nodeDivisionSeries fill:whitesmoke,stroke:dimgray,stroke-width:0.5px,color:black
  classDef nodeLeagueChampionship fill:aliceblue,stroke:steelblue,stroke-width:0.5px,color:midnightblue
  classDef nodeBye fill:white,stroke:silver,stroke-width:0.5px,stroke-dasharray:3 3,color:dimgray
  classDef groupStage fill:white,stroke:silver,stroke-width:0.5px
  class SG_NL_SEEDING,SG_NL_WILD_CARD,SG_NL_DIVISION_SERIES groupStage
```

### World Series

The AL and NL champions advance to this final series. Home field belongs to the team with the better regular-season record, regardless of league seed.

```mermaid
%% The pennant winners feed the World Series. Replace the
%% placeholders and @Hi/@Lo hosts once the matchup is known.
%%{init: {
  "theme": "base",
  "layout": "dagre",
  "themeVariables": {
    "background": "#ffffff",
    "textColor": "#2f4f4f",
    "lineColor": "#696969"
  },
  "flowchart": {
    "curve": "monotoneY",
    "nodeSpacing": 45,
    "rankSpacing": 55,
    "htmlLabels": true,
    "wrappingWidth": 400
  }
}}%%
flowchart TB
  AL_PENNANT["AL champion"]:::nodeLeagueChampionship
  NL_PENNANT["NL champion"]:::nodeLeagueChampionship
  WORLD_SERIES["World Series · Best of 7<br/>AL champ vs NL champ<br/>G1 · Fri 10/23 · @Hi<br/>G2 · Sat 10/24 · @Hi<br/>G3 · Mon 10/26 · @Lo<br/>G4 · Tue 10/27 · @Lo<br/>G5* · Wed 10/28 · @Lo<br/>G6* · Fri 10/30 · @Hi<br/>G7* · Sat 10/31 · @Hi"]:::nodeWorldSeries
  AL_PENNANT & NL_PENNANT --> WORLD_SERIES

  classDef nodeLeagueChampionship fill:aliceblue,stroke:steelblue,stroke-width:0.5px,color:midnightblue
  classDef nodeWorldSeries fill:cornsilk,stroke:darkgoldenrod,stroke-width:0.5px,color:saddlebrown
```

## Updating this document

Game scores appear only in the three 2026 diagrams. After a game, replace its scheduled `@host` line with the winner and score, then update that series' lead. Remove an asterisk when a later game becomes guaranteed; remove unplayed conditional games when the series ends. Replace the next-round matchup placeholder with the advancing team, mark the loser `out` in its seed node, and replace `@Hi` and `@Lo` with hosts once those teams are known. Update the snapshot cutoff at the top, render all diagrams, and check MLB's schedule for date changes.

## Sources

- [MLB.com: 2026 postseason schedule and results](https://www.mlb.com/news/2026-mlb-playoff-and-world-series-schedule)
- [MLB.com: postseason bracket and latest games](https://www.mlb.com/postseason)
- [MLB.com: final 2026 standings](https://www.mlb.com/standings/2026)
- [MLB.com: postseason format](https://www.mlb.com/news/mlb-playoff-format-faq)
- [MLB.com: standings tiebreaker rules](https://www.mlb.com/news/mlb-playoff-tiebreaker-rules)