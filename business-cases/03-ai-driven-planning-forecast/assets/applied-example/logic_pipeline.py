import pandas as pd
from datetime import datetime

# -------------------------
# 1. Load backlog snapshot
# -------------------------

df = pd.read_csv("backlog_synthetic.csv")

# Keep a raw copy for traceability
raw_df = df.copy()


# -------------------------
# 2. Parse dates (best effort)
# -------------------------

DATE_COLUMNS = ["recorded_date", "resolved_date", "last_updated_date"]

for col in DATE_COLUMNS:
    df[col] = pd.to_datetime(df[col], errors="coerce", dayfirst=True)


# -------------------------
# 3. Basic ageing indicators
# -------------------------

today = pd.Timestamp(datetime.today().date())

df["is_resolved"] = df["status"].isin(["Closed", "Discarded"])

df["ageing_days"] = (
    df["resolved_date"].fillna(today) - df["recorded_date"]
).dt.days


# -------------------------
# 4. Data quality signals
# -------------------------

df["missing_dates"] = df[DATE_COLUMNS].isna().sum(axis=1)

df["owner_ambiguity"] = df["process_owner"].str.contains(
    "Head|Team", case=False, na=False
)

df["description_length"] = df["incident_description"].str.len()


# -------------------------
# 5. Duplicate suspicion (lightweight)
# -------------------------

df["normalized_description"] = (
    df["incident_description"]
    .str.lower()
    .str.replace(r"[^a-zA-Z0-9 ]", "", regex=True)
    .str.slice(0, 80)
)

duplicate_groups = (
    df.groupby("normalized_description")
    .filter(lambda x: len(x) > 1)
    .groupby("normalized_description")["incident_id"]
    .apply(list)
)

# -------------------------
# 6. Scenario signals
# -------------------------

open_backlog = df[~df["is_resolved"]]

scenario_signals = {
    "total_open_incidents": len(open_backlog),
    "high_priority_open": len(open_backlog[open_backlog["priority"] == "High"]),
    "avg_ageing_days": round(open_backlog["ageing_days"].mean(), 1),
    "multi_geo_share": round(
        (open_backlog["multi_geography"] == "Y").mean(), 2
    ),
    "suspected_duplicates": len(duplicate_groups),
}


# -------------------------
# 7. Outputs for interpretation
# -------------------------

signals_df = pd.DataFrame(
    scenario_signals.items(),
    columns=["signal", "value"]
)

signals_df.to_csv("signals_summary.csv", index=False)

duplicate_groups.to_csv("suspected_duplicates.csv")


# -------------------------
# 8. Console snapshot (for transparency)
# -------------------------

print("=== Decision Intelligence Signals ===")
print(signals_df)

print("\n=== Suspected Duplicate Incidents ===")
print(duplicate_groups)
