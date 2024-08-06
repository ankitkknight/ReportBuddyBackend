import statistics
from typing import List
from uuid import UUID
from datetime import datetime
from fastapi import HTTPException, status
import requests


class ReportService:
    @staticmethod
    async def upload_report(data: str, user_id: UUID):
        accessToken = ""
        url = "https://na-1-dev.api.opentext.com/tenants/c84e0d98-0b45-4225-87ff-ca09c02e7761/oauth2/token"
        headers = {
            "Content-Type": "application/jsons",
        }
        body = {
        'client_id': "",
        'client_secret': "",
        'grant_type': 'password',
        'username': "Ank@123456",
        'password': "ankitkumarknight@gmail.com"
        }
        try:
          response = requests.post(url, headers=headers, json=body)
          response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
          data = response.json()
          accessToken = data['access_token']
        except requests.exceptions.RequestException as error:
          print(f"Error: {error}")
        
        
        # Save report to database
        return report