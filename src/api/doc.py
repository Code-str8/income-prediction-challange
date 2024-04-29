from fastapi import APIRouter, Response
from typing import List
from pydantic import BaseModel

router = APIRouter()


@router.get("/", summary="Welcome", tags=["Documentation"])
async def root():
    """
    Hello! Try it out!
    """
    return Response(
        content="Welcome to Income Predict API! Visit /docs to see the documentation on how to use this API.",
        media_type="text/plain"
    )


@router.get("/docs", summary=" API Documentation", tags=["Documentation"])
async def get_docs():
    """
    Documentation for the Income Predict API.

    This API is designed to predict the income over limit or below based on various input features.
    
    To use the API, send a POST request to the '/predict' endpoint with the required input data in the request body.
    The API will process the input and return a prediction indicating the income level for the given person.
    
    """
    return 

