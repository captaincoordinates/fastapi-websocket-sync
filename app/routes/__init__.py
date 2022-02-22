from fastapi import APIRouter

from app.routes.root import PATH as path_root, ROUTER as router_root

router = APIRouter()
router.include_router(router_root, prefix=path_root)
