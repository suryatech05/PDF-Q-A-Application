from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database
from ..services import nlp
import os

router = APIRouter()

@router.post("/upload/", response_model=schemas.PDFDocument)
async def upload_pdf(file: UploadFile, db: Session = Depends(database.get_db)):
    content = await file.read()
    content_text = nlp.extract_text_from_pdf(content)
    document_data = schemas.PDFDocumentCreate(
        filename=file.filename,
        content=content_text
    )
    document = crud.create_document(db=db, document=document_data)
    save_path = os.path.join("storage", "uploads", file.filename)
    with open(save_path, "wb") as f:
        f.write(content)
    return document

@router.post("/ask/", response_model=str)
async def ask_question(document_id: int, question: str, db: Session = Depends(database.get_db)):
    document = crud.get_document(db, document_id=document_id)
    if document:
        answer = nlp.answer_question(document.content, question)
        return answer
    return "Document not found"
