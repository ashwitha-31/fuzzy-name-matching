# Fuzzy Name Matching System – Major Project

This project is a Flask-based web application designed for fuzzy matching of names written in Hindi (Devanagari script) and Roman (English) script. It is useful in police, legal, or public record systems where name spelling variations are common.

## Features

- Fuzzy name matching using RapidFuzz
- Supports both Hindi and English inputs
- Transliteration using `indic-transliteration`
- CSV upload to match multiple names at once
- Web interface and API endpoint for integration

## Technologies Used

- Python
- Flask
- Pandas
- RapidFuzz
- Indic Transliteration
- HTML (Jinja2 templating)

---

## How to Run the Project

### Step 1: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 2: Start the Application

```bash
python app.py
```

### Step 3: Open in Browser

Go to:
```
http://localhost:5000
```

---

## CSV Upload Format

Prepare a `.csv` file like this:

| ID  | Full Name | Remarks                   |
|-----|-----------|---------------------------|
| 101 | rajesh    | FIR entry                 |
| 102 | ramesh    | Alias used                |
| 103 | सुरेश     | Hindi script (original)   |

No headers needed if simple, but it works best with: **ID, Full Name, Remarks**

---

## API Endpoint

You can also use this endpoint for backend calls:

```
POST http://localhost:5000/api/match
```

Sample JSON body:

```json
{ "name": "rajesh" }
```

---

## Author

**Ashwitha Dasu**  
Final Year Major Project – Dept. of Computer Science  
Python • Flask • RapidFuzz • Hindi NLP
