# Gestão de Images

## EndPoints

- `GET localhost:3002/images`: obter todas as imagens
- `GET localhost:3002/images/<image_id>`: obter a imagem *image_id*
- `GET localhost:3002/images/info/<image_id>`: obter as informações da imagem *image_id*
- `GET localhost:3002/images/data/<image_id>`: obter os *bytes* da imagem *image_id*
- `POST localhost:3002/images`: adicionar uma image
- `DELETE localhost:3002/images/<image_id>`: eliminar a imagem *image_id*