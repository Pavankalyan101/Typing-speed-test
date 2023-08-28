import time

def calculate_typing_speed(start_time, end_time, input_text):
    time_taken = end_time - start_time
    words = input_text.split()
    num_words = len(words)
    typing_speed = num_words / (time_taken / 60)  # Words per minute
    return typing_speed

def main():
    passage = "The quick brown fox jumps over the lazy dog."
    
    print("Type the following passage:")
    print(passage)
    input("Press Enter when you're ready to start...")
    
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()
    
    typing_speed = calculate_typing_speed(start_time, end_time, user_input)
    
    correct_words = 0
    passage_words = passage.split()
    user_words = user_input.split()
    for i in range(len(user_words)):
        if i < len(passage_words) and user_words[i] == passage_words[i]:
            correct_words += 1
    
    accuracy = (correct_words / len(passage_words)) * 100
    
    print("\nTyping Speed: {:.2f} words per minute".format(typing_speed))
    print("Accuracy: {:.2f}%".format(accuracy))

if __name__ == "__main__":
    main()
