# 2config.py

TEAM_COLUMN = 'Team'
CSV_PATH = 'Report/OUTPUT_BAI1/results.csv'
NA_VALUES = [
    'N/a', 'n/a', 'NA', 'na', 'NaN', 'nan', '', '#N/A', 'null', 'NULL'
]
GOOD_STATS = [
    'Performance: goals',
    'Performance: assists',
    'Expected: expected goals (xG)',
    'Expected: expedted Assist Goals (xAG)',
    'Progression: PrgC',
    'Progression: PrgP',
    'Progression: PrgR',
    'Per 90 minutes: Gls',
    'Per 90 minutes: Ast',
    'Per 90 minutes: xG',
    'Per 90 minutes: xGA',
    'Performance: Save%',
    'Performance: CS%',
    'Penalty Kicks: penalty kicks Save%',
    'Standard: shoots on target percentage (SoT%)',
    'Standard: Shoot on Target per 90min (SoT/90)',
    'Standard: goals/shot (G/sh)',
    'Total: passes completed (Cmp)',
    'Total: Pass completion (Cmp%)',
    'Total: progressive passing distance (TotDist)',
    'Short: Pass completion (Cmp%)',
    'Medium: Pass completion (Cmp%)',
    'Long: Pass completion (Cmp%)',
    'Expected: key passes (KP)',
    'Expected: pass into final third (1/3)',
    'Expected: pass into penalty area (PPA)',
    'Expected: CrsPA',
    'Expected: PrgP',
    'SCA: SCA',
    'SCA: SCA90',
    'GCA: GCA',
    'GCA: GCA90',
    'Tackles: TklW',
    'Blocks: Blocks',
    'Blocks: Sh',
    'Blocks: Pass',
    'Blocks: Int',
    'Touches: Att 3rd',
    'Touches: Att Pen',
    'Take-Ons: Succ%',
    'Carries: ProDist',
    'Carries: ProgC',
    'Carries: 1/3',
    'Carries: CPA',
    'Receiving: PrgR',
    'Performance: Fld',
    'Performance: Recov',
    'Aerial Duels: Won',
    'Aerial Duels: Won%'
]
BAD_STATS = [
    'Performance: yellow cards',
    'Performance: red cards',
    'Performance: goals against per 90mins (GA90)',
    'Challenges: Lost',
    'Take-Ons: Tkld%',
    'Carries: Mis',
    'Carries: Dis',
    'Performance: Fls',
    'Performance: Off',
    'Aerial Duels: Lost'
]
IGNORE_STATS = [
    'Name', 'Nation', 'Team', 'Position', 'Age',
    'Playing Time: matches played', 'Playing Time: starts', 'Playing Time: minutes',
    'Standard: average shoot distance (Dist)', 'Tackles: Tkl', 'Challenges: Att',
    'Touches: Touches', 'Touches: Def Pen', 'Touches: Def 3rd', 'Touches: Mid 3rd',
    'Take-Ons: Att', 'Carries: Carries', 'Receiving: Rec', 'Performance: Crs'
]
