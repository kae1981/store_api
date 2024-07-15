class BaseException(Exception):
    message: str = "Internal Server Error"

    def __init__(self, message: str | None = None) -> None:
        if message:
            self.message = message

@app.exception_handler(sqlalchemy.exc.IntegrityError)
async def handle_integrity_error(request, exc):
    return JSONResponse({"status_code": 400, "detail": "Falha ao incluir o registro. Verifique os dados e tente novamente."})

class NotFoundException(BaseException):
    message = "Not Found"
