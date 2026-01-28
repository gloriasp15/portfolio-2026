import pandas as pd
from datetime import datetime

# -------------------------
# 1. Load logic outputs
# -------------------------

signals = pd.read_csv("signals_summary.csv")
duplicates = pd.read_csv("suspected_duplicates.csv")

# -------------------------
# 2. Build narrative context
# -------------------------

signals_context = "\n".join(
    f"- {row['signal']}: {row['value']} ({row['description']})"
    for _, row in signals.iterrows()
)

duplicates_context = "\n".join(
    f"- {row['normalized_description']}: {row['incident_ids']} ({row['comment']})"
    for _, row in duplicates.iterrows()
)

context_block = f"""
BACKLOG SIGNALS
{signals_context}

SUSPECTED DUPLICATES
{duplicates_context}
"""

# -------------------------
# 3. Prompt construction
# -------------------------

prompt = f"""
You are supporting an executive team reviewing an operational backlog
across Operations, IT and Business teams in Spain and Brazil.

Based ONLY on the signals and observations below:
- explain what is currently happening in the backlog
- highlight key tensions or risks
- surface coordination or duplication issues
- avoid recommendations or prioritisation decisions

Signals:
{context_block}

Produce a concise executive narrative (max 10 bullet points).
"""

# -------------------------
# 4. LLM call (conceptual)
# -------------------------
# NOTE:
# This is a conceptual call. In a real environment, this would use
# a secure internal GenAI platform or API-based LLM service.

def call_llm(prompt_text):
    """
    Placeholder for LLM call.
    Replace with actual OpenAI / internal GenAI client in production.
    """
    return (
        "- The backlog shows sustained pressure, with a high share of open and high-priority incidents.\n"
        "- Average ageing indicates that several issues remain unresolved beyond expected cycles.\n"
        "- A significant proportion of incidents affect multiple geographies, increasing coordination complexity.\n"
        "- Multiple incidents appear to describe the same underlying problems, suggesting duplicated effort across teams.\n"
        "- Ownership is fragmented across Operations, IT and Business, contributing to slower resolution.\n"
        "- Manual reporting alone is unlikely to surface these patterns consistently at executive level."
    )

narrative_output = call_llm(prompt)

# -------------------------
# 5. Write executive output
# -------------------------

output_file = "executive_summary.md"

with open(output_file, "w") as f:
    f.write("# Executive Intelligence Summary\n\n")
    f.write(f"_Generated on {datetime.today().strftime('%Y-%m-%d')}_\n\n")
    f.write(narrative_output)

print(f"Executive summary generated: {output_file}")
