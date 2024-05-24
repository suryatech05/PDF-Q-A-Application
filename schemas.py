from pydantic import BaseModel

class PDFDocumentBase(BaseModel):
    filename: str
    content: str

class PDFDocumentCreate(PDFDocumentBase):
    pass

class PDFDocument(PDFDocumentBase):
    id: int

    class Config:
        orm_mode = True
