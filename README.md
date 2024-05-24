# PDF-Q-A-Application
This full-stack application allows users to upload PDF documents and ask questions about their content. The backend uses FastAPI and LangChain/LLamaIndex for NLP processing, while the frontend is built with React.js. Documents are stored in SQLite or PostgreSQL, and PDFs are saved locally or on AWS S3.

# Features
. Upload PDF documents.
. Extract text content from uploaded PDFs.
. Ask questions about the content of the uploaded PDFs.
. Get answers to questions using NLP processing.
# Tools and Technologies
. Backend: FastAPI
. NLP Processing: LangChain/LLamaIndex
. Frontend: React.js
. Database: SQLite or PostgreSQL
. File Storage: Local filesystem or AWS S3
# Application Architecture
. Frontend: Built with React.js, it provides an interface for users to upload PDFs and ask questions.
. Backend: Developed with FastAPI, it handles file uploads, stores metadata, processes PDF content, and responds to queries using NLP.
. Database: Stores metadata of the uploaded PDFs. SQLite is used for local development, with PostgreSQL as an option for production.
. File Storage: Uploaded PDFs are stored in the local filesystem.
. NLP Service: Uses LangChain/LLamaIndex to extract text from PDFs and process natural language queries.
# Directory Structure
	pdf-qa-app/
	├── app/
	│   ├── main.py
	│   ├── models.py
	│   ├── schemas.py
	│   ├── database.py
	│   ├── crud.py
	│   ├── routers/
	│   │   ├── __init__.py
	│   │   ├── pdf.py
	│   ├── services/
	│   │   ├── __init__.py
	│   │   ├── nlp.py
	├── requirements.txt
	├── env/
	├── alembic.ini
	├── alembic/
	│   ├── env.py
	│   ├── versions/
	├── storage/
	│   ├── uploads/
	├── .env
	├── Dockerfile
	├── docker-compose.yml
	pdf-qa-frontend/
	├── public/
	├── src/
	│   ├── App.js
	│   ├── index.js
	├── package.json
# Setup Instructions

## Backend Setup
### 1. Clone the repository:

	git clone (https://github.com/suryatech05/PDF-Q-A-Application)
	cd PDF-Q-A-Application
### 2. Set up the virtual environment:

	python3 -m venv env
	source env/bin/activate
### 3. Install the dependencies:

	pip install -r requirements.txt
### 4. Configure the database:

#### . Create a .env file with the following content:

	DATABASE_URL=sqlite:///./sql_app.db
### 5. Run Alembic migrations:

	alembic upgrade head
### 6. Start the FastAPI server:

	uvicorn app.main:app --reload
## Frontend Setup
### 1. Navigate to the frontend directory:

	cd pdf-qa-frontend
### 2. Install the dependencies:

	npm install
### 3. Start the React development server:

	npm start
## Running with Docker
### 1. Build and start the application with Docker Compose:

	docker-compose up --build
# API Documentation
## 1. Upload PDF
### . Endpoint: /upload/
### . Method: POST
### . Request:
#### . Content-Type: multipart/form-data
#### . Body: file (PDF file)
### . Response:
#### . 200 OK
#### . JSON:

	{
	  "id": 1,
	  "filename": "example.pdf",
	  "content": "Extracted text content"
	}
## 2. Ask Question
### . Endpoint: /ask/
### . Method: POST
### . Request:
#### . Content-Type: application/json
	{
	  "document_id": 1,
	  "question": "What is the main topic of the document?"
	}
### . Response:
#### . 200 OK
#### . JSON: Answer to the question
# Contributing
Contributions are welcome! Please submit a pull request or open an issue for any improvements or bugs.

# License
This project is licensed under the MIT License.

By following the instructions in this README file, you should be able to set up, run, and deploy the PDF Q&A application. Make sure to replace placeholder links and values with your actual information.
