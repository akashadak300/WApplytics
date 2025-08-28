# WApplytics - WhatsApp Chat Analysis

## 📱 Project Overview

WApplytics is a Streamlit-based web app that lets you upload and analyze your exported WhatsApp chat files. It provides interactive visualizations and statistics about your group or personal chats, including message counts, word clouds, emoji usage, timelines, and more. This project is ideal for anyone curious about their chat activity, group dynamics, or communication patterns.

---

## ✨ Features

- **Message Statistics:** Total messages, words, media, and links shared.
- **User Activity:** Most active users and their contribution percentages.
- **Word Cloud:** Visual representation of the most common words (with emoji support).
- **Emoji Analysis:** Pie chart of the most used emojis.
- **Timelines:** Monthly and daily message activity trends.
- **Activity Maps:** Weekly and monthly activity heatmaps.
- **Stop Words Filtering:** Removes common stop words for accurate word clouds.
- **Media & Notification Filtering:** Ignores media and group notification messages.

---

## 🚀 How to Run

### 1. Clone the Repository

```sh
git clone https://github.com/akashadak300/WApplytics.git
cd WApplytics
```

### 2. Install Dependencies

Make sure you have Python 3.7+ installed.  
Install required packages using pip:

```sh
pip install -r requirements.txt
```

### 3. Run the App

```sh
streamlit run app.py
```

### 4. Use the App

- Export your WhatsApp chat as a `.txt` file (from WhatsApp > More > Export Chat).
- Open the app in your browser (Streamlit will provide a local URL).
- Upload your chat file using the sidebar.
- Select a user or view overall stats.
- Click "Show Analysis" to see interactive charts and stats.

---

## 🗂️ File Structure

- `app.py` — Main Streamlit app.
- `helper.py` — Core analysis and visualization functions.
- `preprocessor.py` — Chat file parsing and preprocessing.
- `requirements.txt` — Python dependencies.
- `stop_hinglish.txt` — Stop words list for filtering.

---

## 🛠️ Customization

- **Stop Words:** Edit `stop_hinglish.txt` to change stop words filtering.
- **Fonts:** The app uses `Segoe UI Emoji` for emoji support in charts (Windows). For other OS, set an emoji-compatible font in `app.py`.

---

## 💡 Example Insights

- Who sends the most messages?
- What are the most common words and emojis?
- When is the group most active?
- How does activity change over time?

---

## 📦 Requirements

- Python 3.7+
- Streamlit
- URLExtract
- matplotlib
- wordcloud
- emoji
- seaborn

(See `requirements.txt` for details.)


---

Demo Link: https://wca-campusx.herokuapp.com/
