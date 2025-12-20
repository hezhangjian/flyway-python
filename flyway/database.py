from abc import ABC, abstractmethod


class Database(ABC):
    """Abstract base class for database adapters."""

    @abstractmethod
    def create_schema_history_table(self) -> None:
        """Create the schema history table if it doesn't exist."""
        pass

    @abstractmethod
    def record_migration(
            self,
            installed_rank: int,
            version: str,
            description: str,
            script: str,
            checksum: int,
            user: str,
            execution_time: int,
    ) -> None:
        """Record a migration in the schema history table.

        Args:
            installed_rank: Rank of the installed migration
            version: Version string of the migration
            description: Description of the migration
            script: Script filename
            checksum: Checksum of the script
            user: User who installed the migration
            execution_time: Execution time in milliseconds
        """
        pass

    @abstractmethod
    def is_version_migrated(self, version: str) -> bool:
        """Check if a version has been migrated.

        Args:
            version: Version string to check

        Returns:
            True if version has been migrated, False otherwise.
        """
        pass

    @abstractmethod
    def acquire_lock(self) -> None:
        """Acquire a lock for migration operations.

        Raises:
            RuntimeError: If lock cannot be acquired.
        """
        pass

    @abstractmethod
    def release_lock(self) -> None:
        """Release the migration lock.

        Raises:
            RuntimeError: If lock cannot be released.
        """
        pass
