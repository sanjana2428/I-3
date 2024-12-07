from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import RegistrationForm, LoginForm,ReviewForm, ProviderResponseForm
from django.contrib.auth.decorators import login_required
from .models import Review, ProviderResponse

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        # Authenticate user
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            if user.user_type == 'patient':
                return redirect('patient_dashboard')
            elif user.user_type == 'provider':
                return redirect('provider_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        # Handle GET request
        return render(request, 'login.html')

@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')


@login_required
def patient_verify(request):
    if request.method == "POST":
        username = request.POST.get("username")
        patient_id = request.POST.get("patient_id")
       #dob = request.POST.get("dob")

        user = CustomUser.objects.filter(username=username, id=patient_id).first()
        if user:
            return render(request, "patient_dashboard.html", {"verified": True})
        else:
            return render(request, "patient_dashboard.html", {"verified": False, "error": "Invalid credentials"})

@login_required
def submit_review(request):
    if request.method == "POST":
        provider_name = request.POST.get("provider")
        rating = request.POST.get("rating")
        review_content = request.POST.get("review_content")

        review = Review(
            patient=request.user,
            provider=CustomUser.objects.get(username=provider_name),
            rating=rating,
            content=review_content,
        )
        review.save()
        return redirect("patient_dashboard")
    return render(request, "patient_dashboard.html")

@login_required
def provider_dashboard(request):
    return render(request, 'provider_dashboard.html')

@login_required
def submit_response(request, review_id):
    if request.method == "POST":
        response_text = request.POST.get("response_text")
        review = Review.objects.get(id=review_id)

        if review.provider == request.user:
            ProviderResponse.objects.create(review=review, response_text=response_text)
            return redirect("provider_dashboard")
        else:
            return render(request, "provider_dashboard.html", {"error": "Unauthorized"})


@login_required
def write_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.patient = request.user
            review.save()
            return redirect('patient_dashboard')
    else:
        form = ReviewForm()
    return render(request, 'write_review.html', {'form': form})

@login_required
def provider_response(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        form = ProviderResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.review = review
            response.save()
            return redirect('provider_dashboard')
    else:
        form = ProviderResponseForm()
    return render(request, 'provider_response.html', {'form': form, 'review': review})
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout