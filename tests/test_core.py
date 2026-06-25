import csv
from pathlib import Path

from budget.core import add_transaction, filter_by_category, get_balance


ROOT = Path(__file__).resolve().parents[1]


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


def load_step2_transactions() -> list[dict[str, str]]:
    path = ROOT / "data" / "step2_transactions.csv"
    with path.open(encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


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


def test_get_balance_returns_zero_for_empty_transactions() -> None:
    assert get_balance([]) == 0.0


def test_get_balance_sums_income_and_expenses() -> None:
    transactions = [
        make_transaction("3500000", "수입", "월급"),
        make_transaction("-12000", "지출", "점심식사"),
        make_transaction("-1500", "지출", "지하철"),
        make_transaction("25000", "수입", "중고 판매"),
    ]

    assert get_balance(transactions) == 3511500.0


def test_get_balance_uses_step2_transactions_csv() -> None:
    transactions = load_step2_transactions()

    assert get_balance(transactions) == 24285027.0


def test_filter_by_category_matches_step2_category_case_insensitively() -> None:
    transactions = load_step2_transactions()

    filtered_transactions = filter_by_category(transactions, "여행")

    assert len(filtered_transactions) == 6
    assert all(
        transaction["category"].casefold() == "여행".casefold()
        for transaction in filtered_transactions
    )


def test_filter_by_category_ignores_ascii_case() -> None:
    transactions = [
        {**make_transaction("-12000", "지출", "점심식사"), "category": "Food"},
        {**make_transaction("-1500", "지출", "지하철"), "category": "food"},
        {**make_transaction("3500000", "수입", "월급"), "category": "급여"},
    ]

    filtered_transactions = filter_by_category(transactions, "FOOD")

    assert len(filtered_transactions) == 2
    assert {transaction["category"] for transaction in filtered_transactions} == {
        "Food",
        "food",
    }


def test_filter_by_category_returns_empty_list_for_missing_category() -> None:
    transactions = load_step2_transactions()

    assert filter_by_category(transactions, "없는카테고리") == []


def test_filter_by_category_returns_independent_results() -> None:
    transactions = load_step2_transactions()
    original_length = len(transactions)
    original_index = next(
        index
        for index, transaction in enumerate(transactions)
        if transaction["category"] == "의료"
    )
    original_description = transactions[original_index]["description"]

    filtered_transactions = filter_by_category(transactions, "의료")
    filtered_transactions.append(make_transaction("-12000", "지출", "점심식사"))
    filtered_transactions[0]["description"] = "수정된 설명"

    assert len(transactions) == original_length
    assert transactions[original_index]["description"] == original_description
