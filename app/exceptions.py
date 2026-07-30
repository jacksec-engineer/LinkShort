"""Custom exception classes for the Cube-Link application."""


class CubeLinkError(Exception):
    """Base exception for all Cube-Link application errors."""


class LinkNotFoundError(CubeLinkError):
    """Raised when a link lookup returns no matching row."""


class DuplicateHashError(CubeLinkError):
    """Raised when an insert fails due to a UNIQUE constraint on hashsum."""


class DatabaseError(CubeLinkError):
    """Raised when a database operation fails for non-uniqueness reasons."""


class EncryptionError(CubeLinkError):
    """Raised when URL encryption fails."""


class DecryptionError(CubeLinkError):
    """Raised when URL decryption fails."""


class UrlValidationError(CubeLinkError):
    """Raised when URL validation fails.

    Attributes:
        code: Machine-readable error code identifying the failure type.
    """

    def __init__(self, message: str, code: str) -> None:
        super().__init__(message)
        self.code = code
