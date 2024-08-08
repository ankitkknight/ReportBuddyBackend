from fastapi import APIRouter 
from app.api.api_v1.handlers import user
# from app.api.api_v1.handlers import ml
from app.api.api_v1.handlers import report as user_report
router = APIRouter()


router.include_router(user.user_router, tags=["user"]) 
router.include_router(user_report.report_router, prefix='/report',tags=["report"]) 
