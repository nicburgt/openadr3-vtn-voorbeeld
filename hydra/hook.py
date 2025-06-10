from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response
import json
import uvicorn

app = FastAPI()

@app.post("/token-hook")
async def token_hook(request: dict):
    # "roles": [{"role": "AnyBusiness"}]
    # data_dict = {
    #     "session": {
    #         "access_token": {
    #             "roles": []
    #         }
    #     }
    # }

    data_dict = {
        "session": {
            "access_token": {
                "scope": "read_all write_programs",
                "roles": [{"role": "AnyBusiness"}]
            }
        }
    }

    # Return the updated token
    return JSONResponse(status_code=200, content=data_dict)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)