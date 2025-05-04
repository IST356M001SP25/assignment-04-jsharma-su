# Reflection

Student Name:  Jiya Sharma
Sudent Email:  jsharma@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`
This assignment helped solidify my undestanding of how to use Pandas for loading, filtering, and summarizing dataset, and how to integrate thsoe capabilities into a user-friendly web interface using Streamlit. The task of building the UniBrow application gave me hands-on practice working with real-wrold data file types such as csv, excel, and json, and applying operations like read_csv(), read_excel(), and DataFrame.dexcribe(). One area I struggled with initially was understanding how to dynamically update Streamlit components based on the contents of the uploaded file - particularly in enabling the user to filter a DataFrame based on a selected text column and its unique values. I wasn't sure how to make the dropdown for values update after a column was selected. After reviewing the Streamlit documentation and experiementing with the st.selectbox() and df[column].unique() approach, I was able to get it working. Another challeenge was making sure the tests for pandaslib.py passed. Writing functions with proper type hints and docstrings helped clarify what each function was supposed to return. I had to debug a few logical errors - for example, I initially forgot to return only the selected columns when building the column filter, which caused the output DataFrame to include all columns. Running pytest and writing additional test cases under if __name__ == "main__" hel;ped me catch and fix these issues early. One concept I want to revisit is how Streamlit reruns scripts from the top down every time a widget changes. Understanding this behavior more deeply will help me avoid unnecessary reproccessing in future apps. I also need more practice with composing Stremlit layouts, such as using columns to make the UI more user-friendly. Overall this assignment helped bridge the gap between data manipulation and user interface design, and I feel much more confident now is building interactive Python tools with Streamlit. In the future I will practice more Streamlit apps that involve dynamic widget updating based on user input. I will also practice writing more Pandas functions involving grouping and aggregation, as those are still a bit confusing to me.

