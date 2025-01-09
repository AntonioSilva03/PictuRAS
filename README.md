# Gestão de Ferramentas

## EndPoints

- `GET localhost:5000/tools`: obter todas as ferramentas
- `GET localhost:5000/tools/tool`: obter a ferramenta *tool*
- `POST localhost:5000/tools`: adicionar a ferramenta *tool*
- `PUT localhost:5000/tools/tool`: atualizar a ferramenta *tool*
- `DELETE localhost:5000/tools/<tool>`: eliminar a ferramenta *tool*

## Run

```
docker compose up -d
docker compose down
```