# Health Prediction Application

## Overview

Health Prediction Application is a Python-based web application developed using Streamlit and SQLite. 
The application allows users to manage patient health records and generate health assessment remarks based on blood test values using AI-powered prediction.

## Features

* Create, Read, Update, and Delete (CRUD) patient records
* Store patient data in a SQLite database
* Input validation for:

  * Full Name
  * Email Address
  * Date of Birth
  * Blood Test Values
* AI-based health prediction remarks
* User-friendly Streamlit interface
* Persistent data storage

## Technologies Used

* Python
* Streamlit
* SQLite
* Gemini AI API
* Pandas

## Patient Information

The application stores the following details:

* Full Name
* Date of Birth
* Email Address
* Glucose
* Haemoglobin
* Cholesterol
* Remarks (AI Generated)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project folder:

```bash
cd healthpredictionapp
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure your Gemini API Key in `ai_prediction.py` or using environment variables.

5. Run the application:

```bash
streamlit run app.py
```

## Application Workflow

1. Enter patient details.
2. Validate user inputs.
3. Generate health remarks using AI prediction.
4. Store data in SQLite database.
5. View, update, and delete records as required.

## Challenges Faced

* Integrating external AI API services.
* Handling API rate limits and exceptions.
* Implementing data validation and database operations.

## Author
Khushboo Joshi
