from django.shortcuts import render


def fruit_student_view(request):

    context = {
        "fruits": [
            "Apple",
            "Banana",
            "Mango",
            "Pineapple",
            "Grapes"
        ],

        "selected_students": [
            "Aarav Mehta",
            "Diya Kapoor",
            "Kabir Singh",
            "Meera Nair",
            "Rohan Iyer"
        ],

        "event_name": "Annual Sports Day 2026"
    }

    return render(request, "fruits_students.html", context)