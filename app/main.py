from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_mcp import FastApiMCP

from app.exceptions import NotFoundException
from app.routers import project, asset, shot, task, user, upload

app = FastAPI(
    title="Shotgrid MCP Server",
    description="A Model Context Protocol (MCP) server for Shotgrid API integration.",
    version="1.0.0"
)

app.include_router(project.router)
app.include_router(asset.router)
app.include_router(shot.router)
app.include_router(task.router)
app.include_router(user.router)
app.include_router(upload.router)


@app.exception_handler(NotFoundException)
async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=404,
        content={"detail": f"{exc.entity} with id {exc.id} not found"},
    )


if __name__ == "__main__":
    mcp = FastApiMCP(
        app,
        name="Shotgrid MCP Server",
        description="MCP server for Shotgrid API integration",
    )
    mcp.mount()

    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
