from pyscript import document, display

club_members = [
    "Juan Dela Cruz",
    "Maria Santos",
    "Jose Rizal",
    "Ana Reyes",
]

def check_membership():
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    full_name = f"{first_name} {last_name}".strip()

    if not first_name or not last_name:
        message = "Please enter both your first and last name."
    else:
        result = full_name in club_members
        message = (
            f"Congratulations {full_name}! You are now part of the ICT club."
            if result
            else f"Sorry {full_name}, your name is not on the list."
        )

    document.getElementById("result").innerText = message
