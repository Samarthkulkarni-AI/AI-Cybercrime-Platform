# AI-Enhanced Cybercrime Reporting and Investigation Platform

## 📖 About The Project

This project is an AI-integrated, multi-role web platform designed to bridge the gap between victims of cybercrime and law enforcement investigators. It provides a secure and user-friendly portal for victims to file reports and a powerful, data-driven dashboard for investigators to analyze, prioritize, and manage cases efficiently.

The platform leverages **Google Gemini AI** to provide intelligent features such as case type prediction, automated report refinement, and actionable insights for investigators.

---

## 🛠️ Tech Stack

This project is built with the following technologies:

*   **Backend:** Python, Django
*   **Database:** SQLite (for development)
*   **Frontend:** HTML, CSS, JavaScript
*   **AI/ML:** Google Gemini AI (Generative AI)
*   **Geocoding:** OpenStreetMap (Nominatim)
*   **Data Visualization:** Chart.js, Leaflet.js (for Heatmaps)

---

## ✅ Key Features

### 🛡️ For Victims (Users)
*   **Secure Reporting:** File detailed cybercrime reports with automatic case type and department prediction.
*   **AI Assistance:**
    *   **CyberShield AI Chatbot:** A compassionate AI assistant to guide victims and answer queries.
    *   **Report Refinement:** Converts rough incident descriptions into formal, professional incident reports.
*   **User Dashboard:** Track case status, view safety tips, and manage profile information.
*   **Secure Messaging:** Two-way, WhatsApp-style chat with investigators for each case.
*   **Evidence Upload:** Securely upload files/evidence related to the case.

### 🕵️‍♂️ For Investigators (Superusers)
*   **Investigator Dashboard:** A comprehensive view of all cases with status filtering and priority management.
*   **AI Insights:** Dynamic, AI-generated actionable insights based on current crime statistics.
*   **Crime Heatmap:** Visual representation of crime hotspots based on victim locations.
*   **Analytics:** Real-time charts and statistics (Total Cases, Success Rate, Case Type Breakdown).
*   **Case Management:** Update case status, review evidence, and communicate with victims.
*   **Export Data:** Export complaint data to CSV for offline analysis.

---

## 🚀 Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

*   Python 3.x
*   pip
*   A Google Cloud API Key (for Gemini AI)

### Installation

1.  **Clone the repo**
    ```sh
    git clone <repository-url>
    cd <repository-folder>
    ```

2.  **Create and activate a virtual environment**
    ```sh
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables**
    *   Create a `.env` file in the project root (or export variables in your shell).
    *   Add your Google API Key:
        ```
        GOOGLE_API_KEY=your_api_key_here
        ```

5.  **Apply database migrations**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Create a superuser (for the Investigator role)**
    ```sh
    python manage.py createsuperuser
    ```

7.  **Run the development server**
    ```sh
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

---

## 🔮 Future Roadmap

*   [ ] **Advanced Analytics:** Deeper integration with ML libraries for trend forecasting.
*   [ ] **Multi-language Support:** Expand the platform to support regional languages.
*   [ ] **Mobile App:** Develop a dedicated mobile application for easier reporting.
*   [ ] **Blockchain Integration:** For immutable evidence logging.