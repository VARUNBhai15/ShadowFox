import pandas as pd

# Read CSV with encoding fix
df = pd.read_csv("IPL sample data.csv", skiprows=4, encoding="latin1")

# Clean column names
df.columns = df.columns.str.strip()

print("Columns detected:\n", df.columns)

# Keep rows with player names
df = df.dropna(subset=["Player Name"])

# Convert Y/N → 1/0
df = df.replace({"Y": 1, "N": 0, "n": 0})

# Fill blanks
df = df.fillna(0)

# Convert numeric columns
for col in ["Pick", "Throw", "Runs"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

# Performance Score
df["PS"] = (
    df.get("Pick", 0) +
    df.get("Throw", 0) +
    df.get("Runs", 0)
)

# Show results
print("\n🏏 Player Performance:\n")
print(df[["Player Name", "PS"]])

# Best fielder
best = df.loc[df["PS"].idxmax()]
print("\n🏆 Best Fielder:", best["Player Name"])
print("Score:", best["PS"])
