"""
Abstract interfaces for repository collectors.

Repository collectors are responsible for gathering repository artifacts from
supported platforms and returning them in ORI's internal data models.
"""

from abc import ABC, abstractmethod

from .types import RepositoryMetadata


class RepositoryCollector(ABC):
    """
    Base interface for all repository collectors.

    Every repository provider supported by ORI should implement this interface.
    """

    @abstractmethod
    def collect(self, repository_url: str) -> RepositoryMetadata:
        """
        Collect basic repository metadata.

        Args:
            repository_url:
                The URL of the repository to collect.

        Returns:
            RepositoryMetadata describing the repository.
        """
        raise NotImplementedError
