from datetime import datetime
from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------
# Create MCP Server
# ---------------------------------------------------

mcp = FastMCP("IRS-Demo-MCP")

# ---------------------------------------------------
# Sample Database
# ---------------------------------------------------

TAXPAYERS = {
    "111223333": {
        "name": "John Smith",
        "filing_status": "Single",
        "balance_due": 2500.75,
        "account_status": "Active",
        "last_return_year": 2025
    },
    "222334444": {
        "name": "Alice Johnson",
        "filing_status": "Married Filing Jointly",
        "balance_due": 0,
        "account_status": "Compliant",
        "last_return_year": 2025
    },
    "333445555": {
        "name": "David Wilson",
        "filing_status": "Head of Household",
        "balance_due": 18500,
        "account_status": "Collections",
        "last_return_year": 2024
    }
}

NOTICES = {
    "111223333": [
        {
            "notice": "CP14",
            "date": "2025-04-15",
            "description": "Balance Due"
        },
        {
            "notice": "LT11",
            "date": "2025-06-10",
            "description": "Final Notice Before Levy"
        }
    ],
    "222334444": [],
    "333445555": [
        {
            "notice": "CP501",
            "date": "2025-02-20",
            "description": "Reminder Notice"
        },
        {
            "notice": "CP504",
            "date": "2025-05-01",
            "description": "Intent to Levy"
        }
    ]
}

# ---------------------------------------------------
# Tool 1
# ---------------------------------------------------

@mcp.tool()
def validate_tin(tin: str) -> dict:
    """
    Validate Taxpayer Identification Number.
    """

    if len(tin) != 9:
        return {
            "valid": False,
            "message": "TIN must contain exactly 9 digits."
        }

    if not tin.isdigit():
        return {
            "valid": False,
            "message": "TIN must contain digits only."
        }

    return {
        "valid": True,
        "message": "TIN format is valid."
    }

# ---------------------------------------------------
# Tool 2
# ---------------------------------------------------

@mcp.tool()
def get_taxpayer_account(tin: str) -> dict:
    """
    Retrieve taxpayer account information.
    """

    taxpayer = TAXPAYERS.get(tin)

    if taxpayer is None:
        return {
            "found": False,
            "message": "Taxpayer not found."
        }

    return {
        "found": True,
        "taxpayer": taxpayer
    }

# ---------------------------------------------------
# Tool 3
# ---------------------------------------------------

@mcp.tool()
def lookup_filing_status(tin: str) -> dict:
    """
    Return filing status.
    """

    taxpayer = TAXPAYERS.get(tin)

    if taxpayer is None:
        return {
            "found": False
        }

    return {
        "found": True,
        "filing_status": taxpayer["filing_status"]
    }

# ---------------------------------------------------
# Tool 4
# ---------------------------------------------------

@mcp.tool()
def calculate_penalty(balance_due: float, days_late: int) -> dict:
    """
    Calculate a simple late payment penalty.

    Demo Formula:
    0.5% per month (30 days)
    Maximum 25%
    """

    months = days_late / 30

    penalty_rate = months * 0.005

    if penalty_rate > 0.25:
        penalty_rate = 0.25

    penalty = round(balance_due * penalty_rate, 2)

    total = round(balance_due + penalty, 2)

    return {
        "balance_due": balance_due,
        "days_late": days_late,
        "penalty": penalty,
        "total_due": total
    }

# ---------------------------------------------------
# Tool 5
# ---------------------------------------------------

@mcp.tool()
def get_notice_history(tin: str) -> dict:
    """
    Retrieve IRS notice history.
    """

    notices = NOTICES.get(tin)

    if notices is None:
        return {
            "found": False,
            "message": "Taxpayer not found."
        }

    return {
        "found": True,
        "notice_count": len(notices),
        "notices": notices
    }

# ---------------------------------------------------
# Tool 6
# ---------------------------------------------------

@mcp.tool()
def generate_payment_plan(balance: float) -> dict:
    """
    Generate a suggested installment plan.
    """

    if balance <= 0:
        return {
            "eligible": False,
            "message": "No balance due."
        }

    if balance <= 5000:
        months = 12

    elif balance <= 25000:
        months = 36

    else:
        months = 72

    monthly_payment = round(balance / months, 2)

    return {
        "eligible": True,
        "balance": balance,
        "months": months,
        "monthly_payment": monthly_payment
    }

# ---------------------------------------------------
# Tool 7
# ---------------------------------------------------

@mcp.tool()
def account_summary(tin: str) -> dict:
    """
    Return a complete taxpayer summary.
    """

    taxpayer = TAXPAYERS.get(tin)

    if taxpayer is None:
        return {
            "found": False
        }

    notices = NOTICES.get(tin, [])

    payment_plan = generate_payment_plan(
        taxpayer["balance_due"]
    )

    return {
        "generated_at": datetime.now().isoformat(),
        "taxpayer": taxpayer,
        "notice_history": notices,
        "recommended_payment_plan": payment_plan
    }

# ---------------------------------------------------
# Main
# ---------------------------------------------------

if __name__ == "__main__":
    print("PythonDemoServer started successfully.")
    print("Waiting for an MCP client...")
    mcp.run()