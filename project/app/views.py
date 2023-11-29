from django.shortcuts import render
from .models import (
    FrontTimesChallenge,
    NoTeenSumChallenge,
    XYZThereChallenge,
    CenteredAverageChallenge,
)
from .forms import FrontTimesForm, NoTeenSumForm, XYZThereForm, CenteredAverageForm


def front_times_view(request):
    # Handle form submission for the front_times challenge
    if request.method == "POST":
        form = FrontTimesForm(request.POST)
        if form.is_valid():
            # Extract input from the form
            input_string = form.cleaned_data["input_string"]
            n = form.cleaned_data["n"]

            # Implement the CodingBat logic for front_times
            front_len = 3 if len(input_string) >= 3 else len(input_string)
            front = input_string[:front_len]
            result = front * n

            # Render the result
            return render(request, "front_times_result.html", {"result": result})
    else:
        # Display the form for user input
        form = FrontTimesForm()

    return render(request, "front_times.html", {"form": form})


def no_teen_sum_view(request):
    # Handle form submission for the no_teen_sum challenge
    if request.method == "POST":
        form = NoTeenSumForm(request.POST)
        if form.is_valid():
            # Extract input from the form
            a = form.cleaned_data["a"]
            b = form.cleaned_data["b"]
            c = form.cleaned_data["c"]

            # Implement the CodingBat logic for no_teen_sum
            result = no_teen_sum(a, b, c)

            # Render the result
            return render(request, "no_teen_sum_result.html", {"result": result})
    else:
        # Display the form for user input
        form = NoTeenSumForm()

    return render(request, "no_teen_sum.html", {"form": form})


def no_teen_sum(a, b, c):
    # Helper function for fixing teens
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    # Helper function to fix teens based on the CodingBat logic
    if (13 <= n < 15) or (16 < n <= 19):
        return 0
    else:
        return n


def xyz_there_view(request):
    # Handle form submission for the xyz_there challenge
    if request.method == "POST":
        form = XYZThereForm(request.POST)
        if form.is_valid():
            # Extract input from the form
            input_string = form.cleaned_data["input_string"]

            # Implement the CodingBat logic for xyz_there
            result = xyz_there(input_string)

            # Render the result
            return render(request, "xyz_there_result.html", {"result": result})
    else:
        # Display the form for user input
        form = XYZThereForm()

    return render(request, "xyz_there.html", {"form": form})


def xyz_there(s):
    # Helper function for xyz_there challenge
    length = len(s)
    xyz = "xyz"
    match = False

    if length < 3:
        return False

    for i in range(length - 2):
        temp = s[i : i + 3]
        if temp == xyz and (i == 0 or s[i - 1] != "."):
            match = True

    return match


def centered_average_view(request):
    # Handle form submission for the centered_average challenge
    if request.method == "POST":
        form = CenteredAverageForm(request.POST)
        if form.is_valid():
            # Extract input from the form
            nums_str = form.cleaned_data["nums"]
            nums = [int(num) for num in nums_str.split(",")]

            # Implement the CodingBat logic for centered_average
            result = centered_average(nums)

            # Render the result
            return render(request, "centered_average_result.html", {"result": result})
    else:
        # Display the form for user input
        form = CenteredAverageForm()

    return render(request, "centered_average.html", {"form": form})


def centered_average(nums):
    # Helper function for calculating centered average
    return (sum(nums) - min(nums) - max(nums)) // (len(nums) - 2)
