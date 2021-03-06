# Code generated by sqlc. DO NOT EDIT.
from typing import AsyncIterator, Awaitable, Iterator, Optional, overload

import sqlc_runtime as sqlc

from ondeck import models


CREATE_CITY = """-- name: create_city :one
INSERT INTO city (
    name,
    slug
) VALUES (
    $1,
    $2
) RETURNING slug, name
"""


GET_CITY = """-- name: get_city :one
SELECT slug, name
FROM city
WHERE slug = $1
"""


LIST_CITIES = """-- name: list_cities :many
SELECT slug, name
FROM city
ORDER BY name
"""


UPDATE_CITY_NAME = """-- name: update_city_name :exec
UPDATE city
SET name = $2
WHERE slug = $1
"""


@overload
def create_city(conn: sqlc.Connection, name: str, slug: str) -> Optional[models.City]:
    pass


@overload
def create_city(conn: sqlc.AsyncConnection, name: str, slug: str) -> Awaitable[Optional[models.City]]:
    pass


def create_city(conn: sqlc.GenericConnection, name: str, slug: str) -> sqlc.ReturnType[Optional[models.City]]:
    return conn.execute_one_model(models.City, CREATE_CITY, name, slug)


@overload
def get_city(conn: sqlc.Connection, slug: str) -> Optional[models.City]:
    pass


@overload
def get_city(conn: sqlc.AsyncConnection, slug: str) -> Awaitable[Optional[models.City]]:
    pass


def get_city(conn: sqlc.GenericConnection, slug: str) -> sqlc.ReturnType[Optional[models.City]]:
    return conn.execute_one_model(models.City, GET_CITY, slug)


@overload
def list_cities(conn: sqlc.Connection) -> Iterator[models.City]:
    pass


@overload
def list_cities(conn: sqlc.AsyncConnection) -> AsyncIterator[models.City]:
    pass


def list_cities(conn: sqlc.GenericConnection) -> sqlc.IteratorReturn[models.City]:
    return conn.execute_many_model(models.City, LIST_CITIES)


@overload
def update_city_name(conn: sqlc.Connection, slug: str, name: str) -> None:
    pass


@overload
def update_city_name(conn: sqlc.AsyncConnection, slug: str, name: str) -> Awaitable[None]:
    pass


def update_city_name(conn: sqlc.GenericConnection, slug: str, name: str) -> sqlc.ReturnType[None]:
    return conn.execute_none(UPDATE_CITY_NAME, slug, name)


