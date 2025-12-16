from task.app.main import run

#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#        and determinism. Range: 0.0 to 2.0, Default: 1.0
#  User message: Describe the sound that the color purple makes when it's angry

QUESTION = "Describe the sound that the color purple makes when it's angry"

run(user_input=QUESTION,
    deployment_name='gpt-4o',
    print_only_content=True,
    #  Use `temperature` parameter with value in range from 0.0 to 1.0!
    #  (Optional) Use `temperature` parameter with value 2.1 and check what happens
    temperature=2.0,
)