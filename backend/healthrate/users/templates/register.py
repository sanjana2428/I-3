<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register for HealthRate</title>
    <style>
        /* Add your CSS styling here */
        .container {
            max-width: 400px;
            margin: 50px auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
        .form-footer {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Register for HealthRate</h2>
        <form method="POST">
            {% csrf_token %}
            {{ form.as_p }}
            <div class="form-group">
                <button type="submit">Register</button>
            </div>
        </form>
        <div class="form-footer">
            <p>Already have an account? <a href="{% url 'login' %}">Login here</a></p>
        </div>
    </div>
</body>
</html>