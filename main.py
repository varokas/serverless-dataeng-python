from pydantic import BaseModel
from enum import Enum

from botocore.config import Config

from params_aws import params_aws
from params_aws import model

### Initialize 
print("Start Loading model...")
model = "model" # s3
## mlflow (s3)
print("Finish Loading model...")


class RequestType(Enum):
    hello = "hello"
    params = "params"

REGION="ap-southeast-1"

class Request(BaseModel):
    type: RequestType

class HelloRequest(Request):
    echo: str

class HelloResponse(BaseModel):
    echo: str

def handler(event:str, context):
    try:
        type = event["type"]
        if not type:
            return {"status": "error", "message": "request with no type"}

        if type == "hello":
            return hello(HelloRequest.parse_obj(event))
        else:
            return {"status": "error", "message": f"unknown type: {type}"}
    except Exception as e:
        print(e)
        return {"status": "error", "message": f"{e}"}
    
def hello(request: HelloRequest):
    res = HelloResponse(echo= request.echo)
    return res.dict()
