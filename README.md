Your **README.md** file should provide an overview of your project, including its purpose, installation steps, and usage instructions. Here’s a structured README you can use:  

---

# **PubMed Research Paper Fetcher**  

## **📌 Overview**  
This project is a Python-based CLI tool to fetch research papers from PubMed, extract metadata (title, authors, DOI, affiliations), and save results to a CSV file. It helps identify non-academic authors and filter research based on affiliations.  

## **🛠 Features**  
✅ Fetch research papers from PubMed using queries.  
✅ Extract metadata like title, authors, publication date, DOI link.  
✅ Identify non-academic authors based on affiliations.  
✅ Save results in a structured CSV format.  

---

## **📂 Installation**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/YOUR_USERNAME/pubmed-fetcher.git
cd pubmed-fetcher
```

### **2️⃣ Install Dependencies**  
Make sure you have Python **3.9 or higher** installed. Then, install dependencies using Poetry:  
```bash
poetry install
```

### **3️⃣ Set Up API Key**  
Create a `.env` file in the project root and add your API key:  
```bash
GEMINI_API_KEY=your_api_key_here
```

---

## **🚀 Usage**  
Run the script with a search query to fetch papers:  
```bash
poetry run get-papers-list "cancer research" -f results.csv
```
- The results will be saved in `results.csv`.  
- To enable debugging, add the `-d` flag:  
  ```bash
  poetry run get-papers-list "AI in healthcare" -d
  ```

---

## **📊 Output Format**  
The fetched data is stored in a CSV file with columns:  
- **PubmedID** – Unique PubMed ID  
- **Title** – Paper title  
- **Publication Date** – When it was published  
- **Authors** – List of authors  
- **DOI Link** – Direct DOI link  
- **Non-Academic Authors** – If any author belongs to a company  
- **Company Affiliation** – Organization details (if applicable)  
- **Non-Academic Detected** – Whether the paper has non-academic affiliations  

---

## **📝 Example Output**
| PubmedID  | Title  | Authors  | DOI Link  | Non-Academic Detected  |
|-----------|--------|----------|-----------|------------------------|
| 40072452  | Evaluation of Cancer Treatments | Tur P, Oldenburger E  | [Link](https://doi.org/10.1097/SPC.0000000000000750) | No  |

---

## **📄 License**  
This project is **MIT licensed**.  

---

Let me know if you need modifications! 🚀"# Aganitha Project" 
