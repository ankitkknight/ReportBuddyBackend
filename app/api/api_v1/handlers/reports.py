from fastapi import APIRouter, Depends,HTTPException
from app.services.report_service import ReportService
from uuid import UUID



report_router = APIRouter()

@report_router.post('/upload-report', summary="Upload a report")
async def upload_report(data: str, user_id:UUID):
    return {"message": "Report uploaded successfully"}