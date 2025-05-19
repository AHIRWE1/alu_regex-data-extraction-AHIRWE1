import re

# Load text from sample_text.txt
def load_text(filepath="sample_text.txt"):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

# Regex patterns by category
regex_patterns = {
    "Emails": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "URLs": r"https?://[^\s]+",
    "Phone Numbers": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "Currency Amounts": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?",
    "HTML Tags": r"</?[a-zA-Z][a-zA-Z0-9]*(\s+[^<>]*)?>",
}

# Main extraction logic
def extract_data(text, patterns):
    for label, pattern in patterns.items():
        matches = re.findall(pattern, text)
        print(f"\n{label} Found:")
        for match in matches:
            print(f"  {match.strip() if isinstance(match, str) else match[0]}")

# Entry point
if __name__ == "__main__":
    sample_text = load_text("sample_text.txt")
    extract_data(sample_text, regex_patterns)
