from fastapi import APIRouter, Depends,HTTPException
from app.services.report_service import ReportService
from uuid import UUID



report_router = APIRouter()

@report_router.post('/process', summary="Process a report")
async def process_report(data: str, user_id:UUID):
    try:
        await ReportService.process_report(data, user_id)
        return {"message": "Report uploaded successfully"}
    except:
        raise HTTPException(status_code=400, detail="An error occurred while uploading report")
