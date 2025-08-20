app_name = "expense_erpgulf"
app_title = "expense_erpgulf"
app_publisher = "ERPGulf"
app_description = "Expense entry with tax calculations"
app_email = "support@erpgulf.com"
app_license = "mit"


fixtures = [
    {"dt": "Workspace", "filters": {"module": "expense_erpgulf"}},
    {"dt": "Custom Field", "filters": {"module": "expense_erpgulf"}},
    {
        "dt": "Client Script",
        "filters": {"module": "expense_erpgulf"},
    },
]