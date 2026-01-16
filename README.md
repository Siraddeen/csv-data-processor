# CSV Data Processor

🔗 **Live Demo**: [https://csv-data-processor.onrender.com](https://csv-data-processor.onrender.com)

---

## 📌 Overview

**CSV Data Processor** is a web-based application built with **Flask** and **Pandas** that allows users to upload CSV files, automatically clean and analyze the data, preview large datasets efficiently, and download the cleaned data in multiple formats.

This project is designed to handle **real-world CSV files** (including large datasets) and focuses on usability, performance, and clean data handling.

---

## ✨ Features

* 📂 Upload CSV files via browser
* 🧹 Automatically removes duplicate rows
* 📊 Displays dataset summary:

  * Total rows
  * Total columns
  * Duplicate row count
* 👀 Preview large datasets with:

  * Pagination (20 rows per page)
  * Scrollable table
  * Sticky table headers
* ⬇️ Download cleaned data as:

  * CSV (`*_cleaned.csv`)
  * Excel (`*_cleaned.xlsx`)
* 🖥️ Responsive and clean UI
* 🌍 Deployed live using **Render**

---

## 🧰 Tech Stack

**Backend**

* Python
* Flask
* Pandas
* Gunicorn

**Frontend**

* HTML5
* CSS3
* Vanilla JavaScript

**Deployment**

* GitHub (source control)
* Render (hosting)

---

## 📸 Screenshots
<img width="1919" height="1079" alt="Screenshot 2026-01-16 110404" src="https://github.com/user-attachments/assets/8d8c9500-4693-4d2c-89c4-c11ab369f0ec" />

```


```

---

## 🚀 How It Works

1. User uploads a CSV file
2. Backend processes the file using Pandas:

   * Reads CSV
   * Removes duplicate rows
   * Detects missing values
3. Frontend displays:

   * Summary cards
   * Paginated preview table
4. User can download cleaned data as CSV or Excel

---

## 🛠️ Local Setup (Optional)

```bash
# Clone repository
git clone https://github.com/<your-username>/csv-data-processor.git
cd csv-data-processor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

Open browser at:

```
http://127.0.0.1:5000
```

---

## 📄 Project Structure

```
python_csv/
├── app.py
├── requirements.txt
├── logic/
│   └── csv_processor.py
├── web/
│   └── routes.py
├── templates/
│   └── index.html
├── static/
└── README.md
```

---

## 🧠 Key Learnings

* Handling large CSV files efficiently
* Separating backend logic from frontend rendering
* Avoiding JSON serialization issues with Pandas
* Implementing pagination without frontend frameworks
* File download handling in Flask
* Debugging and deploying Flask apps with Gunicorn

---

## 📌 Future Enhancements

* Column sorting
* Search & filter functionality
* Backend pagination for very large files
* Authentication & user history
* Support for additional file formats

---

## 👤 Author

**Siraddeen**
Aspiring Data / Backend Engineer

---

## ⭐ Acknowledgements

Built as a hands-on project to strengthen real-world Flask, Pandas, and deployment skills.

If you find this project useful, feel free to ⭐ the repository.
