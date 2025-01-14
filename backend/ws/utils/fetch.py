import requests


def get_project(host, port, project):
    return requests.get(f'http://{host}:{port}/project/{project}').json()


def get_project_images(host, port, project):
    return requests.get(f'http://{host}:{port}/project/images/{project}').json()


def get_image_data(host, port, image_id):
    image_data = requests.get(f'http://{host}:{port}/projects/images/data/{image_id}')
    return image_data.content