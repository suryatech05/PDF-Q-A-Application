from sqlalchemy.orm import Session
from . import models, schemas

def get_document(db: Session, document_id: int):
    return db.query(models.PDFDocument).filter(models.PDFDocument.id == document_id).first()

def create_document(db: Session, document: schemas.PDFDocumentCreate):
    db_document = models.PDFDocument(**document.dict())
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document
