import requests

def download_openapi_json(url: str, filename: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, 'w') as file:
            file.write(response.text)
        print(f"Successfully downloaded the OpenAPI JSON and saved it to {filename}.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = "http://localhost:8000/openapi.json"
    filename = "openapi.json"
    download_openapi_json(url, filename)
