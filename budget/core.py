"""Core budget ledger operations."""

from typing import Any


def add_transaction(
    transactions: list[dict[str, Any]],
    transaction: dict[str, Any],
) -> list[dict[str, Any]]:
    """Return transactions with transaction added to the ledger."""
    return [*transactions, transaction]
