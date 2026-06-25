from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def test_agents_file_documents_required_project_rules() -> None:
    content = read_text("AGENTS.md")

    assert "CSV files" in content
    assert "type hints" in content
    assert "50 lines" in content
    assert "Write the failing test before implementing behavior" in content
    assert "cyclomatic complexity at 10 or lower" in content
    assert "qa_engineer" in content
    assert "pytest" in content
    assert "radon cc ." in content
    assert "Commit after one complete feature" in content


def test_qa_engineer_subagent_defines_commit_gate() -> None:
    content = read_text(".agents/qa_engineer.md")

    assert "pytest" in content
    assert "radon cc ." in content
    assert "type hints" in content
    assert "50 lines" in content
    assert "cyclomatic complexity is 10 or lower" in content
    assert "Decision" in content
    assert "pass/block" in content


def test_budget_cli_tdd_skill_has_valid_frontmatter_and_workflow() -> None:
    content = read_text(".codex/skills/budget-cli-tdd/SKILL.md")

    assert content.startswith("---\n")
    assert "name: budget-cli-tdd" in content
    assert "description:" in content
    assert "Read `AGENTS.md` before making changes" in content
    assert "Write or update tests first" in content
    assert "pytest" in content
    assert "radon cc ." in content
    assert "qa_engineer" in content
