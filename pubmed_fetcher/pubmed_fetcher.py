import os
import requests
import pandas as pd
import argparse
from dotenv import load_dotenv

# ✅ Load API Key securely
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ API Key is missing! Set GEMINI_API_KEY in a .env file.")

# ✅ Keywords for non-academic affiliations
NON_ACADEMIC_KEYWORDS = [
    "Inc.", "Ltd.", "Pharmaceutical", "Biotech", "Corp.", "LLC",
    "Pfizer", "Moderna", "Novartis", "AstraZeneca", "Bayer",
    "Merck", "Johnson & Johnson", "Roche", "Sanofi", "GSK"
]

# ✅ Known company email domains for filtering
COMPANY_EMAIL_DOMAINS = ["pfizer.com", "moderna.com", "novartis.com", "bayer.com", "gsk.com"]

# ✅ Function to Fetch Papers from PubMed API
def fetch_pubmed_articles(query: str, max_results: int = 5) -> list:
    """Fetches research papers from PubMed based on a search query."""
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={query}&retmode=json&retmax={max_results}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get("esearchresult", {}).get("idlist", [])
    else:
        print("❌ Error fetching data from PubMed")
        return []

# ✅ Function to Fetch Paper Details, Authors & Emails
def fetch_paper_details(pubmed_ids: list) -> list:
    """Fetches metadata, authors, and corresponding author emails."""
    papers = []
    for pubmed_id in pubmed_ids:
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pubmed_id}&retmode=json"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            result = data.get("result", {}).get(pubmed_id, {})

            # Extract metadata
            title = result.get("title", "N/A")
            pub_date = result.get("pubdate", "N/A")
            authors = result.get("authors", [])
            doi_link = next((item["value"] for item in result.get("articleids", []) if item["idtype"] == "doi"), "N/A")

            # ✅ Extract author names safely
            author_names = [author.get("name", "Unknown") for author in authors]

            # ✅ Extract affiliations
            affiliations = [author.get("affiliation", "N/A") for author in authors]

            # ✅ Identify non-academic authors
            non_academic_authors = [
                author_names[i] for i, aff in enumerate(affiliations)
                if any(keyword.lower() in aff.lower() for keyword in NON_ACADEMIC_KEYWORDS)
            ]

            # ✅ Determine if non-academic based on affiliation or email domain
            is_non_academic = "Yes" if non_academic_authors else "No"

            papers.append({
                "PubmedID": pubmed_id,
                "Title": title,
                "Publication Date": pub_date,
                "Authors": ", ".join(author_names),
                "DOI Link": f"https://doi.org/{doi_link}" if doi_link != "N/A" else "N/A",
                "Non-Academic Authors": ", ".join(non_academic_authors) if non_academic_authors else "N/A",
                "Company Affiliation": ", ".join(affiliations) if affiliations else "N/A",
                "Non-Academic Detected": is_non_academic,
            })
        else:
            print(f"❌ Error fetching details for PubMed ID {pubmed_id}")

    return papers

# ✅ Function to Save Results to CSV
def save_to_csv(data: list, filename: str):
    """Saves the fetched research papers into a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"✅ Results saved to {filename}")

# ✅ Command-line Interface (CLI)
def main():
    parser = argparse.ArgumentParser(description="Fetch and filter research papers from PubMed")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results (default: print to console)")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()
    
    # Fetch papers
    pubmed_ids = fetch_pubmed_articles(args.query)

    if pubmed_ids:
        papers = fetch_paper_details(pubmed_ids)

        if args.debug:
            print("🔍 DEBUG: Full response from API:", papers)

        if args.file:
            save_to_csv(papers, args.file)
        else:
            print(papers)
    else:
        print("❌ No papers found.")

if __name__ == "__main__":
    main()
