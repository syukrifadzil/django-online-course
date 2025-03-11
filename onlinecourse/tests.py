from django.test import TestCase
import json

# Define course data
course_data = {
    "name": "Learning Django",
    "image": "Download from here",
    "description": "Django is an extremely popular and fully featured server-side web framework, written in Python",
    "pub_date": "Today",
    "instructors": ["admin"],
    "lessons": [
        {
            "title": "What is Django",
            "order": 0,
            "content": (
                "Django is a high-level Python web framework that encourages rapid development and "
                "clean, pragmatic design. Built by experienced developers, it takes care of much of "
                "the hassle of web development, so you can focus on writing your app without needing "
                "to reinvent the wheel. It’s secure."
            )
        }
    ]
}

# Define test question data
test_question_data = {
    "course": "Learning Django",
    "content": "Is Django a Python framework",
    "grade": 100,
    "choices": [
        {
            "content": "Yes",
            "is_correct": True
        },
        {
            "content": "No",
            "is_correct": False
        }
    ]
}

# Combine into a single dataset
test_data = {
    "course": course_data,
    "test_question": test_question_data
}

# Save to a JSON file
with open("test_data.json", "w") as f:
    json.dump(test_data, f, indent=4)

print("Test data has been saved to test_data.json")
