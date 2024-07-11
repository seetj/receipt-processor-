from fastapi import FastAPI, Body , HTTPException, status
from components.schemas.schemas import Receipt
from pydantic import ValidationError
from scores.scores import total_score
import uuid 

app = FastAPI()

receipts = {}

@app.post("/receipts/process",status_code=status.HTTP_200_OK)
async def post_receipt(receipt: Receipt=Body(...)):
    '''
    This function sends a post request to /receipts/process. It takes a receipt in the form of JSON and creates an uuid to assign to the
    receipt. The score of the receipt will be determined and returned to the user in the form of JSON as well.

    Arguments: The function takes the body of the request as receipt data. It should be in JSON format as well align with the Pydantic model "Receipt"

    Return: The function returns an JSON response that contains status code of 200 or 400 depending on the result of the response. If successful,
    the function will return a JSON object that contains the id assigned to the receipt.
    '''

    
    try: 
        receipt_id = str(uuid.uuid4())
        points = total_score(receipt) 
        receipts[receipt_id] = points
        print(receipts)
        return {
            "id" : receipt_id,
        }
    
    except ValidationError:
        raise HTTPException(status_code=400,detail="The receipt is invalid")



@app.get("/receipts/{id}/points")
def get_points(id: str):
    try:
        points = receipts.get(id)
        return {
            "points" : points 
        }
    except ValidationError as e:
        raise HTTPException(status_code=404,detail="No receipt found for that id")
