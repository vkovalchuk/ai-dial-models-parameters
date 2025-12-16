from task.app.main import run

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

# TODO:
#  Try different models (`deployment_name`) with such user request:
#  User message: What LLMs can do?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro
QUESTION = "What LLMs can do?"

# WHY  "content_filter_result": {"error": {"code": "content_filter_error", "message": "The contents are not filtered"}},
run(user_input=QUESTION,
    deployment_name='gpt-4o',
    print_request=False, # Switch to False if you do not want to see the request in console
    print_only_content=False, # Switch to True if you want to see only content from response
)
run(user_input=QUESTION,
    deployment_name='gemini-2.5-pro',
    print_request=False, # Switch to False if you do not want to see the request in console
    print_only_content=False, # Switch to True if you want to see only content from response
)

# claude-3-7-sonnet@20250219 FAILS
# {"error":{"message":"Access denied","display_message":"Access denied","code":"403"}}

run(user_input=QUESTION,
    deployment_name='claude-sonnet-4@20250514',
    print_request=False, # Switch to False if you do not want to see the request in console
    print_only_content=False, # Switch to True if you want to see only content from response
)

# The main goal of this task is to explore the functional capabilities of DIAL to be able to work with different
# LLMs through unified API
