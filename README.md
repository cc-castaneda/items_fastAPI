# items_fastAPI

Description: Technical test of two services implemented with fastAPI, sqlalchemy and docker

# Documentación

### Proyecto de Gestión de Items

Este proyecto implementa dos endponts para la gestión de items utilizando fastAPI, SQLAlchemy y postgreSQL, siguiendo los principios de diseño de software moderno, incluyendo la separación y organización de funcionalidades, inyección de dependencias y el patrón repositorio.

El requerimiento no se adjunta, ya que es una prueba técnica y por respeto al responsable de diseñarla.

### Arquitectura

#### **Capa de Presentación (API)**

- Implementada con FastAPI
- Maneja las solicitudes HTTP y las respuestas
- Define los endpoints de la API

#### **Capa de Servicio**

- Contiene la lógica
- Intermediario entre la API y el repositorio

#### **Capa de Repositorio**

- Maneja las operaciones de base de datos
- Abstrae la lógica de persistencia

#### **Capa de Modelo de Datos**

- Estructuras de datos y los modelos ORM

#### **Capa de Esquemas (Pydantic)**

- Modelos de datos para la serialización y la deserialización
- Proporciona validación de datos

## Implementación

Las instrucciones a continuación asumen que tienes [pyenv](https://github.com/pyenv/pyenv) instalado.
Si no lo tiene, utilice cualquier otro método para crear un entorno virtual

- Instalar Python 3.10.0 (Es parte de los requerimientos)

```shell
pyenv install 3.10.0
```

- Crear un entorno virtual

```shell
pyenv virtualenv 3.10.0 items-fastAPI
```

- Activar el entorno virtual

```shell
pyenv local items-fastAPI
```

### Docker

- Inicio y ejecución de contenedores para cada servicio definido en el archivo `docker-compose.yml`

```shell
docker-compose up --build
```

- Bajar los servicios

```shell
docker-compose down
```

- Para acceder al contenedor de backend

```shell
docker-compose exec web bash
```

- Para acceder al contenedor del db

```shell
docker-compose exec db psql -U postgres -d items_db
```

- En caso de levantar el back sin docker:

```shell
uvicorn app.main:app --reload
```

- Revisión de logs

```shell
docker-compose logs -f
```

### Alembic

- Inicializa la configuración del db

```shell
alembic init alembic
```

- Inicializar (Realizar) una migración

```shell
alembic revision --autogenerate -m "Create items table"
```

- Aplicar la migración

```shell
alembic upgrade head
```

Tener en cuenta que lo puedes ejecutar dentro del contenedor del backend

### Pruebas de endpoints

- Crea un nuevo item

```shell
curl -X POST "http://localhost:8000/api/v1/items/" -H "Content-Type: application/json" -d '{"name": "Item 1", "price": 99.98}'
```

- Lista los items previamente comiteados

```shell
curl "http://localhost:8000/api/v1/items/"
```

## Consideraciones adicionales

### Optimización para las migraciones

- Otimizar alembic con docker compose (en el contenedor backend - web):

```shell
command: sh -c "alembic upgrade head --host 0.0.0.0 --port 8000"
```

- En caso de implementar el CRUD completo, esto solo es una base para su implementación y modificación según necesidad

```shell
@router.put("/items/{item_id}", response_model=items_schemas.Item)
def update_item(item_id: int, item: items_schemas.ItemUpdate, db: Session = Depends(get_db)):
    service = ItemsService(db)
    updated_item = service.update_item(item_id, item)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/items/{item_id}", response_model=bool)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    service = ItemsService(db)
    result = service.delete_item(item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Item not found")
    return result
```

### Se pueden desatacar las siguientes prácticas implementadas:

- Arquitectura en capas (routers, servicios, repositorios)
- Uso de Pydantic para validación de datos
- Implementación de ORM con SQLAlchemy
- Uso de variables de entorno para configuración
- Dockerización de la aplicación y la base de datos
- Uso de Alembic para migraciones de base de datos
- Middleware para obtener orígines permitidos en CORS
