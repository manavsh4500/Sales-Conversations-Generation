# Sales Conversations Generator

This project generates sales conversations using Google Generative AI. It aims to create realistic and engaging dialogues between a salesperson and potential customers about various products. The generated conversations are saved in a CSV file and can be used for further analysis or training purposes.

## Minimum Data Size Requirement
Each submission should encompass a minimum of 100 sets of dialogues, with each response in the conversation comprising 50-75 words. This forms the foundational requirement for a successful submission.

## Data Quality
1. **Contextual Relevance and Understanding**: Conversations should be inherently relevant to the sales context, exhibiting a profound understanding of the product or service being proffered.
2. **Coherence, Fluency, and Readability**: Assess the fluency and coherence of the generated responses. They should maintain a seamless flow, exhibit grammatical accuracy, and adhere to principles of effective communication.
3. **Creativity and Engagement**: Judge the creativity and engagement quotient of the conversations. They should showcase ingenuity in capturing the interest of prospective clients and presenting the product in novel, captivating ways.
4. **Toxicity and Bias Mitigation**: Conversations must be devoid of toxic language, personal attacks, or any form of discriminatory content. Bias and stereotypes must be meticulously avoided. Participants will be incentivized for demonstrating an awareness of ethical implications and promoting inclusive language.
5. **Number of Products Sold**: As a pivotal metric in a sales context, participants should aim for a high number of products or services sold. Effective sales conversations that culminate in simulated 'sales' will be rewarded with higher scores.
6. **Accuracy and Completeness of Information**: The veracity of information conveyed in the sales pitch is critical. Inaccurate, misleading, or incomplete statements will incur penalties.
7. **Compute Time to Generate Data**: The time it took to generate data measured using system time difference for measuring. Lower time per dialogue means a higher score.

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- Google Generative AI Python SDK
- Pandas library

### Installation
1. **Clone the repository:**
   sales-conversations-generator
Install the required packages:

pip install google-generativeai pandas
Configure your API key:
Replace 'YOUR_API_KEY' in the script with your actual Google Generative AI API key.

Running the Script
To generate the conversations, run the following command:

python run.py
Output
The generated conversations will be saved in sales_conversations_proper.csv.
The script will display the time taken to generate the conversations. **Time taken to generate conversations: 4174.8430206775665 seconds**

Code Explanation
Products Data
Defines the details of the products being discussed in the conversations:

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
Generating Responses
Function to start a chat session and generate a response:

def generate_response(prompt):
    response = genai.chat(prompt=prompt)
    return response.candidates[0]['content']
Generating Conversations
Function to generate a conversation based on a given product and customer interest level:

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
Saving Conversations
Function to save conversations to a CSV file:


def save_conversations(conversations, filename):
    df = pd.DataFrame(conversations, columns=["Speaker", "Dialogue", "Timestamp"])
    df.to_csv(filename, index=False)
    
**Results**
Total time taken to generate conversations: 4174.8430206775665 seconds
Output file: sales_conversations_proper.csv
