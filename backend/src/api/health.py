from fastapi import APIRouter

router = APIRouter(
  prefix='/health',
  tags=['health']
)

@router.get('/')
def health():
  return {'message' : 'API WORKING CORRECTLY'}