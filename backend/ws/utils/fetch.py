import requests


def get_project(host, port, project):
    response = requests.get(f'http://{host}:{port}/projects/{project}')
    response.raise_for_status()
    return response.json()


def get_project_images(host, port, project):
    response = requests.get(f'http://{host}:{port}/projects/images/{project}')
    response.raise_for_status()
    return response.json()


def get_image_data(host, port, image_id):
    response = requests.get(f'http://{host}:{port}/projects/images/data/{image_id}')
    response.raise_for_status()
    return response.content