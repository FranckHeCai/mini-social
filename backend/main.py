import os
import uvicorn
from dotenv import load_dotenv
load_dotenv()


if __name__ == "__main__":
    debug = os.getenv('MODE') == 'development'
    uvicorn.run(app="src.app:app", host="0.0.0.0", port=8000, reload=debug)
