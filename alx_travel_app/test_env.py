import environ

env = environ.Env()
environ.Env.read_env()  # Reads the .env file

# Print the secret key to check if it's loaded correctly
print(env('DJANGO_SECRET_KEY'))

