# Fake News Detection System

## Project Overview

This is a web-based Fake News Detection System that classifies news headlines as **real** or **fake** using machine learning. The backend is built with **Python Flask**, and the frontend uses **HTML**, **CSS**, **Bootstrap**, and **Tailwind CSS** for a responsive and user-friendly interface.

The system employs a **TF-IDF Vectorizer** to convert news headlines into numerical features and a **PassiveAggressiveClassifier** model to predict the authenticity of the news.

---

## Features

- Real-time fake news prediction based on user input headlines  
- Clean and responsive web interface  
- Error handling for invalid or empty inputs  
- Model and vectorizer loading with pickle files for quick predictions  

---

## Technologies Used

- Python 3.x  
- Flask  
- Scikit-learn  
- Pandas  
- Bootstrap  
- Tailwind CSS  
- Pickle  

---

## Getting Started

### Prerequisites

- Python 3.x installed  
- Required Python packages:  
  ```bash
  pip install flask scikit-learn pandas
