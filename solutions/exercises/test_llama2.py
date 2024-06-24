def test_get_prompt():
    # Test case 1: Basic instruction
    instruction = "Please provide the current time."
    expected_prompt = "<s>[INST] <<SYS>>\nYou are an AI assistant that gives helpful answers. You answer the question in a short and concise way.\n<</SYS>>\n\nPlease provide the current time. [/INST]"
    assert get_prompt(instruction) == expected_prompt

    # Test case 2: Instruction with special characters
    instruction = "What is the meaning of 'GitHub Copilot'?"
    expected_prompt = "<s>[INST] <<SYS>>\nYou are an AI assistant that gives helpful answers. You answer the question in a short and concise way.\n<</SYS>>\n\nWhat is the meaning of 'GitHub Copilot'? [/INST]"
    assert get_prompt(instruction) == expected_prompt

    # Test case 3: Empty instruction
    instruction = ""
    expected_prompt = "<s>[INST] <<SYS>>\nYou are an AI assistant that gives helpful answers. You answer the question in a short and concise way.\n<</SYS>>\n\n [/INST]"
    assert get_prompt(instruction) == expected_prompt

    # Test case 4: Instruction with line breaks
    instruction = "Please\nprovide\nthe\ncurrent\ntime."
    expected_prompt = "<s>[INST] <<SYS>>\nYou are an AI assistant that gives helpful answers. You answer the question in a short and concise way.\n<</SYS>>\n\nPlease\nprovide\nthe\ncurrent\ntime. [/INST]"
    assert get_prompt(instruction) == expected_prompt

    print("All test cases passed!")

test_get_prompt()