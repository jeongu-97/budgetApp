from budget.core import add_transaction


def make_transaction(
    amount: str,
    transaction_type: str,
    description: str,
) -> dict[str, str]:
    return {
        "date": "2026-01-05",
        "type": transaction_type,
        "category": "식비",
        "description": description,
        "amount": amount,
        "memo": "",
    }


def test_add_transaction_increases_length() -> None:
    transactions: list[dict[str, str]] = []
    transaction = make_transaction("-12000", "지출", "점심식사")

    updated_transactions = add_transaction(transactions, transaction)

    assert len(updated_transactions) == 1


def test_add_transaction_stores_negative_expense_amount() -> None:
    transactions: list[dict[str, str]] = []
    transaction = make_transaction("-12000", "지출", "점심식사")

    updated_transactions = add_transaction(transactions, transaction)

    assert updated_transactions[0]["amount"] == "-12000"
    assert updated_transactions[0]["type"] == "지출"


def test_add_transaction_stores_positive_income_amount() -> None:
    transactions: list[dict[str, str]] = []
    transaction = make_transaction("3500000", "수입", "월급")

    updated_transactions = add_transaction(transactions, transaction)

    assert updated_transactions[0]["amount"] == "3500000"
    assert updated_transactions[0]["type"] == "수입"


def test_add_transaction_accepts_empty_description() -> None:
    transactions: list[dict[str, str]] = []
    transaction = make_transaction("25000", "기타수입", "")

    updated_transactions = add_transaction(transactions, transaction)

    assert updated_transactions[0]["description"] == ""
