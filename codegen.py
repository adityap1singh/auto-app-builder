def generate_backend(prompt: str):
    main_code = f'''
from fastapi import FastAPI


app = FastAPI(title="Generated App")


@app.get("/")
def read_root():
    return {{"message": "App generated from prompt: {prompt}"}}
'''


    with open("output/backend/main.py", "w") as f:
        f.write(main_code)


    return ["output/backend/main.py"]