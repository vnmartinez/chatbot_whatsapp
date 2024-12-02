from fastapi import APIRouter, HTTPException, Request
import json

router = APIRouter()

@router.post("/messages-upsert")
async def webhook(request: Request):
    try:
        # Tenta obter o JSON primeiro
        body = await request.json()
        return {"status": "ok", "data": body}
    except json.JSONDecodeError:
        # Se não for JSON, tenta obter o form data
        try:
            form = await request.form()
            return {"status": "ok", "data": dict(form)}
        except Exception as e:
            raise HTTPException(status_code=400, detail="Invalid request format")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
