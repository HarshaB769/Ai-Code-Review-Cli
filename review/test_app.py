
from app import Finding, Review, render_markdown


def test_review_without_findings():
    review = Review(
        summary="The code looks good.",
        findings=[],
    )

    report = render_markdown(review)

    assert "The code looks good." in report
    assert "No issues reported" in report


def test_review_with_security_finding():
    review = Review(
        summary="Security issue found.",
        findings=[
            Finding(
                severity="high",
                category="security",
                line=3,
                issue="Hardcoded password",
                recommendation="Read the secret securely.",
            )
        ],
    )

    report = render_markdown(review)

    assert "HIGH" in report
    assert "Hardcoded password" in report
    assert "line 3" in report


def test_invalid_severity_is_rejected():
    try:
        Finding(
            severity="urgent",
            category="security",
            issue="Test issue",
            recommendation="Fix it",
        )
    except ValueError:
        return

    raise AssertionError("Invalid severity was accepted")
