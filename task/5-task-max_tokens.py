from task.app.main import run

#  Try `max_tokens` parameter. It sets the maximum length of the AI's response. The AI will stop generating text once it hits this limit.
#  User message: What is token when we are working with LLM?

QUESTION = "What is token when we are working with LLM?"

run(user_input=QUESTION,
    deployment_name='gpt-4o',
    print_request=False,
    print_only_content=False,
    max_tokens=25,
    #  Use `max_tokens` parameter with value 10
)

# Previously, we have seen that the `finish_reason` in choice was `stop`, but now it is `length`, and if you check the
# `content,` it is clearly unfinished.