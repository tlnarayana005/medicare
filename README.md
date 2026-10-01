# 🏥 Medicare - Medical Recommendation System

A smart healthcare assistant that provides **personalized medical guidance** based on user-reported symptoms. Built with **Flask** and **Machine Learning (Random Forest)**, the system predicts suitable medicines, offers dietary recommendations, and includes a nearby hospital locator — all in one place.

## ✨ Features

- **Symptom-Based Medicine Prediction** — Uses a trained Random Forest model to predict the most relevant medicines.
- **Dietary Suggestions** — Recommends recovery-friendly diet plans based on the predicted condition.
- **Nearby Hospital Locator** — Automatically finds healthcare facilities near the user using geolocation and OpenStreetMap.
- **User Authentication** — Register, login, and manage your profile with a secure account system.
- **Responsive UI** — Clean, Bootstrap-powered interface that works on all devices.

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Flask (Python) |
| ML Model | Scikit-learn (Random Forest) |
| Frontend | HTML, CSS, Bootstrap 5 |
| Database | SQLite (SQLAlchemy ORM) |
| Maps | Folium + OpenStreetMap / Overpass API |
| Auth | Flask-Login |

## 📁 Project Structure

```
Medicare/
├── app.py                  # Flask application entry point
├── exp.py                  # Standalone map generation utility
├── requirements.txt        # Python dependencies
├── model/
│   ├── Training.csv        # Training dataset
│   ├── training.py         # Model training script
│   ├── diseasepred.pkl     # Trained ML model
│   ├── medications.csv     # Medications dataset
│   ├── diets.csv           # Diet recommendations dataset
│   ├── req.py              # Symptom/disease dictionaries
│   └── run.py              # Model runner
├── project/
│   ├── __init__.py         # Flask app factory & config
│   ├── models.py           # SQLAlchemy database models
│   ├── data.sqlite         # SQLite database
│   ├── core/
│   │   └── views.py        # Home, About, Contact routes
│   ├── users/
│   │   ├── views.py        # Auth, prediction, hospital routes
│   │   ├── forms.py        # WTForms for registration/login
│   │   ├── map.py          # Hospital map generation
│   │   └── picture_handler.py
│   ├── templates/          # Jinja2 HTML templates
│   ├── static/             # CSS, images, generated maps
│   └── error_pages/        # Custom error handlers
```

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+ installed
- pip package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/tlnaraynaa/Medicare.git
   cd Medicare
   ```

2. **Create a virtual environment** *(recommended)*
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://127.0.0.1:5000/
   ```

## 🧠 How It Works

1. **User enters symptoms** — Describe symptoms in plain text.
2. **ML model predicts** — The Random Forest model identifies the most likely condition.
3. **Results displayed** — Predicted disease, recommended medicines, dietary advice, and medication descriptions.
4. **Hospital finder** — Nearby hospitals are plotted on an interactive Folium map.

## 🎯 Use Cases

- **Self-assessment** before visiting a doctor
- **Remote & rural healthcare** where access is limited
- **Medical decision support** for preliminary diagnosis

## 🌍 Impact

- Reduces dependency on immediate consultations for minor concerns
- Aids in early disease detection and management
- Bridges the gap between technology and healthcare
- Cost-effective and accessible solution

## 📜 License

This project is licensed under the **MIT License**.

## 🤝 Contributing

Contributions are welcome! Feel free to **fork** the repository and submit a **pull request**.

## 📬 Contact

- **Email**: tlnarayana005@gmail.com
- **GitHub**: [tlnaraynaa](https://github.com/tlnaraynaa)

---

🚀 *Empowering healthcare with technology!*
