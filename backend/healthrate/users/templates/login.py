<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login to HealthRate</title>
  <style>
    /* Basic Reset */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Roboto', sans-serif;
      background-color: #f4f4f9;
    }

    .container {
      max-width: 600px;
      margin: 50px auto;
      background-color: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    h2 {
      text-align: center;
      margin-bottom: 20px;
      color: #007bff;
    }

    .form-group {
      margin-bottom: 20px;
    }

    .form-group label {
      display: block;
      font-size: 16px;
      color: #333;
      margin-bottom: 8px;
    }

    .form-group input {
      width: 100%;
      padding: 10px;
      font-size: 16px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }

    .form-group button {
      width: 100%;
      padding: 10px;
      background-color: #007bff;
      color: white;
      font-size: 16px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    .form-group button:hover {
      background-color: #0056b3;
    }

    .form-footer {
      text-align: center;
      margin-top: 20px;
    }

    .form-footer a {
      text-decoration: none;
      color: #007bff;
    }

    .form-footer a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>

  <div class="container">
    <h2>Login to HealthRate</h2>
    <form method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <!-- Submit Button -->
      <div class="form-group">
        <button type="submit">Login</button>
      </div>
    </form>

    <div class="form-footer">
      <p>Don't have an account? <a href="{% url 'register' %}">Register here</a></p>
      <p><a href="#">Forgot your password?</a></p>
    </div>
  </div>

</body>
</html>