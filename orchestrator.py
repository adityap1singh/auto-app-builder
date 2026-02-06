import os
from codegen import generate_backend
from cicd import generate_ci


def generate_project(prompt: str):
    os.makedirs("output/backend", exist_ok=True)
    os.makedirs("output/.github/workflows", exist_ok=True)


    backend_files = generate_backend(prompt)
    ci_file = generate_ci()


    return {
        "message": "Project generated successfully",
        "backend": backend_files,
        "ci_pipeline": ci_file
}