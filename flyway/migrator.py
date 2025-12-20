"""Migrator class for database migrations."""

from dataclasses import dataclass

from flyway.db_type import DbType


@dataclass
class MigratorConfig:
    """Configuration for the migrator."""

    db_type: DbType
    user: str
