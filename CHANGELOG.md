# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2024-XX-XX

### Added
- Initial release of Flyway-Python, a database migration tool inspired by Flyway
- Support for SQLite and MySQL databases
- Migration file naming convention: `V<version>__<description>.sql` (e.g., `V1_0__Create_users_table.sql`)
- Automatic schema history tracking via `flyway_schema_history` table
- Migration locking mechanism to prevent concurrent migrations
- CRC32 checksum validation for migration scripts
- Support for default migration directory (`db/migration/`) and custom paths via `migrate_from_path()`
- Migration execution time tracking
- Type hints support with `py.typed` marker file
- `Migrator` class for managing database migrations
- `MigratorConfig` dataclass for configuration
- `Schema` dataclass for representing migration schemas
- `DbType` enum for supported database types
- Database adapter pattern with `Database`, `SQLiteDatabase`, and `MySQLDatabase` classes
- Support for multiple SQL statements in migration files (requires `CLIENT.MULTI_STATEMENTS` for MySQL)
