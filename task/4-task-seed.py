from task.app.main import run

#  Try the `seed` parameter:
#       It allows us to reduce entropy by making the model's output more deterministic.
#       There's no universally "best" seed - any integer works fine. Common approaches:
#            - For testing: Use simple values like 42, 123, or 1000
#       Default: None or random unless specified on the LLM side
#  User message: Name a random animal

QUESTION = "Name a random animal"

run(user_input=QUESTION,
    # deployment_name='gemini-2.5-pro',
    deployment_name='gpt-4o',
    print_request=False,
    print_only_content=True,
    seed=42,
    n=5,
    #  1. Use `seed` parameter with value 42 (or whatever you want)
    #  2. Use `n` parameter with value 5
)

# Check the content in choices. The expected result is that in almost all choices the result will be the same.
# If you restart the app and retry, it should be mostly the same.
# Also, try it without `seed` parameter.
# For Anthropic and Gemini this parameter will be ignored