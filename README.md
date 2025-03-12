

---


### **1️⃣ Project Title**
```
# PubMed Fetcher
A Python CLI tool to fetch and filter research papers from PubMed based on keywords.
```

---

### **2️⃣ Project Description**
```
## Overview
PubMed Fetcher is a Python-based CLI tool that allows users to search for research papers on PubMed using a query, extract relevant details, and save them to a CSV file.

This tool is useful for researchers, students, and professionals who need to analyze scientific literature efficiently.
```

---

### **3️⃣ Features**
```
## Features
✔️ Fetches research papers from PubMed based on search queries  
✔️ Extracts metadata such as title, authors, publication date, and DOI  
✔️ Identifies non-academic authors using predefined keywords  
✔️ Saves results in a CSV file for further analysis  
✔️ Command-line interface (CLI) for easy use  
```

---

### **4️⃣ Installation**
```
## Installation
### Prerequisites
- Python 3.8 or later  
- Poetry (for dependency management)  

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/07Raunak/pubmed-fetcher.git
   cd pubmed-fetcher
   ```
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Set up the `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

---

### **5️⃣ Usage**
```
## Usage
To fetch research papers, run:
```bash
poetry run get-papers-list "cancer research" -f results.csv
```
This will search for papers related to **"cancer research"** and save them in `results.csv`.

For debugging mode:
```bash
poetry run get-papers-list "AI in medicine" -f results.csv -d
```

---

### **6️⃣ Example Output**
```csv
PubmedID, Title, Publication Date, Authors, DOI Link, Non-Academic Authors, Company Affiliation, Non-Academic Detected
40072452, "Evaluation of...", 2025 Mar 12, "Tur P, Oldenburger E", "https://doi.org/10.1097/SPC...", N/A, N/A, No
40072444, "Risk Prediction...", 2025 Mar 12, "Ma B, Gandhi M", "https://doi.org/10.1001/jamadermatol...", N/A, N/A, No
```

---

### **7️⃣ Contribution Guidelines**
```
## Contributing
1. Fork the repo and create a new branch.
2. Make your changes and commit them.
3. Push to your fork and create a Pull Request.
```

---

### **8️⃣ License**
```
## License
This project is licensed under the MIT License.
```

---

### **📌 Next Steps**
- Create a `README.md` file in your project.
- Copy and paste the above content into the file.
- Commit and push it to GitHub:
  ```bash
  git add README.md
  git commit -m "Added README file"
  git push origin main
  ```

