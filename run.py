import random
import pandas as pd
import time
import google.generativeai as genai


products = {
    "smartphone_1": {
        "name": "Advanced Smartphone",
        "description": "Experience the future with our latest smartphone!",
        "price": 799.99,
        "features": ["6.8-inch AMOLED display", "Quad-camera system", "5G connectivity"]
    },
    "laptop_1": {
        "name": "Ultimate Laptop",
        "description": "Unleash your productivity with our high-performance laptop!",
        "price": 1499.99,
        "features": ["15.6-inch 4K display", "Intel Core i9 processor", "32GB RAM"]
    },
}

# Configure the API key
genai.configure(api_key='AIzaSyD1xziAoEZCpyWkX-9bHUO9Nc01mEOolYY')

# Function to start a chat session and generate a response
def generate_response(prompt):
    response = genai.chat(prompt=prompt)
    print(response)  # Debug: print the response structure
    return response.candidates[0]['content']

# Function to generate a conversation
def generate_conversation():
    product = get_random_product()
    user_interest_level = random.randint(1, 3)  # 1: Low, 2: Medium, 3: High

    conversation = []

    # Salesperson greeting (tailored to user's interest level)
    prompt = "You are a salesperson at a company. Greet a potential customer who is browsing products."
    greeting = generate_response(prompt)
    conversation.append(["Salesman", greeting, str(time.time())])

    # Customer response
    prompt = f"The salesperson says: '{greeting}'. Respond as a customer showing {user_interest_level} interest in the product."
    customer_response = generate_response(prompt)
    conversation.append(["User", customer_response, str(time.time())])

    # Salesperson pitch (tailored to user's response and product details)
    prompt = (
        f"The customer says: '{customer_response}'. Craft a sales pitch for the {product['name']} "
        f"highlighting its benefits based on the customer's interest level."
    )
    pitch = generate_response(prompt)
    conversation.append(["Salesman", pitch, str(time.time())])

    # Customer response (based on pitch and potential sale)
    prompt = f"The salesperson says: '{pitch}'. Respond as a customer considering the product."
    customer_response = generate_response(prompt)
    conversation.append(["User", customer_response, str(time.time())])

    # Salesperson closing (tailored to user's response)
    prompt = (
        f"The customer says: '{customer_response}'. Craft a closing statement for the salesperson "
        f"based on the customer's interest level."
    )
    closing = generate_response(prompt)
    conversation.append(["Salesman", closing, str(time.time())])

    return conversation

# Function to get a random product
def get_random_product():
    product_id = random.choice(list(products.keys()))
    return products[product_id]

# Function to save conversations to CSV
def save_conversations(conversations, filename):
    df = pd.DataFrame(conversations, columns=["Speaker", "Dialogue", "Timestamp"])
    df.to_csv(filename, index=False)
    
# Generate conversations
num_conversations = 100  
conversations = []

start_time = time.time()  # Start time for calculating duration

try:
    for i in range(num_conversations):
        conversation = generate_conversation()
        conversations.extend(conversation)

        # Save progress every conversation
        save_conversations(conversations, "sales_conversations_proper.csv")
        print(f"Saved progress after {i + 1} conversations.")

except KeyboardInterrupt:
    print("Process interrupted. Saving progress...")

# Save final progress
save_conversations(conversations, "sales_conversations_proper.csv")
print("Final progress saved.")

# Calculate and print time taken to generate conversations
end_time = time.time()
print("Time taken to generate conversations:", end_time - start_time, "seconds")
