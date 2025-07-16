import os
import os
import uuid

def save_uploaded_files(uploaded_files, folder="uploaded_resumes"):
    os.makedirs(folder, exist_ok=True)
    file_paths = []

    for file in uploaded_files:
        file_id = uuid.uuid4().hex
        file_path = os.path.join(folder, f"{file_id}_{file.name}")
        with open(file_path, "wb") as f:
            f.write(file.read())
        file_paths.append(file_path)

    return file_paths
