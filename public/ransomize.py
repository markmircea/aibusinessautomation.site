import json
import random

def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def save_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    # Load the JSON files
    test2 = load_json('public/test2.json')
    test3 = load_json('public/test3.json')
    test4 = load_json('public/test4.json')
    test5 = load_json('public/test5.json')

    # Combine test3, test4, and test5
    combined = test3 + test4 + test5

    for i in range(10, 21):
        # Select random entries
        selected_test2 = random.sample(test2, 15)
        selected_combined = random.sample(combined, 35)

        # Combine the selections
        result = selected_test2 + selected_combined

        # Shuffle the combined list
        random.shuffle(result)

        # Reassign IDs to ensure they're unique and sequential
        for index, item in enumerate(result, start=1):
            item['id'] = index

        # Save the result
        save_json(result, f'test{i}.json')

    print("Files test10.json to test20.json have been created with randomly shuffled questions.")

if __name__ == "__main__":
    main()
