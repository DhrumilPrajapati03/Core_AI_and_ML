import streamlit as st

st.set_page_config(page_title="🐍 Python Data Type Quiz", page_icon="🎓", layout="centered")

# Custom CSS to perfectly match the requested design aesthetic
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Vibrant Dark background */
    .stApp {
        background: radial-gradient(circle at top center, #1e1b4b 0%, #0f172a 100%);
        color: #f8fafc;
    }
    
    h1, h2, h3 {
        color: #f8fafc !important;
    }

    /* Container border matching a softer card style */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #1e293b !important;
        border: 2px solid #334155 !important;
        border-radius: 12px !important;
        box-shadow: 0 8px 16px -4px rgba(0, 0, 0, 0.5) !important;
    }

    /* Radio Group container layout */
    div.stRadio > div[role="radiogroup"] {
        display: flex;
        flex-direction: column;
        gap: 14px;
        margin-top: 15px;
    }
    
    /* Option Custom Selector Box */
    div.stRadio > div[role="radiogroup"] > label {
        background-color: #334155 !important;
        padding: 16px 20px;
        border-radius: 8px;
        border: 2px solid transparent !important;
        margin: 0;
        cursor: pointer;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        width: 100%;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }

    /* Hover effect */
    div.stRadio > div[role="radiogroup"] > label:hover {
        background-color: #2e264f !important;
        border-color: #a78bfa !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(167, 139, 250, 0.2) !important;
    }

    /* Selected state - A cheerful, bright green */
    div.stRadio > div[role="radiogroup"] > label:has(input:checked) {
        background-color: #064e3b !important;
        border: 2px solid #34d399 !important;
        box-shadow: 0 0 10px rgba(52, 211, 153, 0.4) !important;
        color: #ffffff;
    }

    /* Hide the default circular radio button */
    div.stRadio > div[role="radiogroup"] > label > div:first-child {
        display: none !important;
    }

    /* Adjust font inside the option wrapper */
    div.stRadio > div[role="radiogroup"] > label [data-testid="stMarkdownContainer"] p {
        font-size: 16px !important;
        font-weight: 600;
        margin: 0 !important;
        color: #f1f5f9 !important;
        letter-spacing: 0.3px;
    }

    /* Custom submit button */
    .stButton>button {
        background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%) !important;
        color: white !important;
        font-size: 16px !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        border: none !important;
        margin-top: 25px;
        width: 100%;
        box-shadow: 0 4px 15px rgba(236, 72, 153, 0.4) !important;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(236, 72, 153, 0.6) !important;
    }
    
    hr {
        margin: 15px 0 !important;
        border-top: 2px dashed #475569 !important;
    }
    
    .question-number {
        font-size: 14px;
        font-weight: 800;
        color: #ffffff;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        padding: 6px 14px;
        border-radius: 20px;
        display: inline-block;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .question-text {
        margin-bottom: 20px;
        font-size: 18px;
        font-weight: 600;
        color: #f8fafc;
    }
    
    pre {
        background-color: #0f172a !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        padding: 14px !important;
        margin: 12px 0 !important;
        overflow-x: auto !important;
    }
    
    code {
        font-family: 'Fira Code', 'Courier New', Courier, monospace !important;
        color: #38bdf8 !important;
        font-size: 15px !important;
        font-weight: 500 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Python Assessment")
st.subheader("Test your understanding of Python data types with this quiz! Answer the practical and theoretical questions to see how well you know your stuff. Good luck! 🍀")
st.markdown("<p style='color: #64748b; font-size: 15px; font-weight: 500;'>Last Updated : Jan 10, 2025</p>", unsafe_allow_html=True)
st.write("---")

prefixes = ["Ⓐ", "Ⓑ", "Ⓒ", "Ⓓ"]

practical_mcqs = [
    {
        "q": "What is the output of the following code?\n<pre><code>dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}\nupdate_dict = {'age': 31, 'city': 'Los Angeles', 'country': 'USA'}\nm = dict | update_dict\nprint(m.get('age'))</code></pre>",
        "opts": ["30", "31", "None", "Raises KeyError"],
        "ans": "31"
    },
    {
        "q": "What is the data type of <code>dict['phone_numbers']</code> in the following dictionary?\n<pre><code>dict = {\n    'name': 'Alice',\n    'phone_numbers': ('123-456-7890', '987-654-3210')\n}</code></pre>",
        "opts": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'str'>"],
        "ans": "<class 'tuple'>"
    },
    {
        "q": "What is the value of <code>dict[2][1]</code> for the dictionary below?\n<pre><code>dict = {\n    2: ['reading', 'traveling', 'cooking']\n}</code></pre>",
        "opts": ["'reading'", "'traveling'", "'cooking'", "Raises KeyError"],
        "ans": "'traveling'"
    },
    {
        "q": "What is the length of the list <code>L</code> generated by the following list comprehension?\n<pre><code>L = [i for i in range(-20, 20) if i % 2 == 0]</code></pre>",
        "opts": ["20", "40", "19", "21"],
        "ans": "20"
    },
    {
        "q": "What is the value of <code>l[0]</code> after executing these list operations?\n<pre><code>l = [10, 20, 30, 'p', 98.7, 'apple', True, 67.5]\nl.append(40)\nl.insert(0, 90)</code></pre>",
        "opts": ["10", "90", "40", "67.5"],
        "ans": "90"
    },
    {
        "q": "What is the output of <code>print(j.count(60))</code> for the list <code>j</code> below?\n<pre><code>j = [50, 60, 70, 80, 50, 60, 60, 60, 20]</code></pre>",
        "opts": ["2", "3", "4", "5"],
        "ans": "4"
    },
    {
        "q": "What is the value of <code>t</code> after running this sequence?\n<pre><code>t = ('10', 20, True, 'Hello', 3.14)\nk = list(t)\nk.append(40)\nt = tuple(k)</code></pre>",
        "opts": ["('10', 20, True, 'Hello', 3.14, 40)", "('10', 20, True, 'Hello', 3.14)", "(40, '10', 20, True, 'Hello', 3.14)", "Raises TypeError"],
        "ans": "('10', 20, True, 'Hello', 3.14, 40)"
    },
    {
        "q": "What is the output of <code>print(t.index(3.14))</code> for the tuple <code>t</code> below?\n<pre><code>t = ('10', 20, True, 'Hello', 3.14)</code></pre>",
        "opts": ["3", "4", "5", "Raises ValueError"],
        "ans": "4"
    },
    {
        "q": "What is the return value of <code>aot(5, 6)</code> for the function defined below?\n<pre><code>def aot(b, h):\n    return 0.5 * b * h</code></pre>",
        "opts": ["15.0", "30.0", "15", "30"],
        "ans": "15.0"
    },
    {
        "q": "What is the return value of <code>aoc(2)</code> for the function defined below?\n<pre><code>def aoc(r):\n    return 3.14 * r * r</code></pre>",
        "opts": ["6.28", "12.56", "12.0", "3.14"],
        "ans": "12.56"
    },
    {
        "q": "What is printed when calling <code>greatestO4(23, 453, 54, 76)</code> with the definition below?\n<pre><code>def greatestO4(n1, n2, n3, n4):\n    if n1 > n2:\n        f1 = n1\n    else:\n        f1 = n2\n    if n3 > n4:\n        f2 = n3\n    else:\n        f2 = n4\n    if f1 > f2:\n        print(f'{f1} is greatest')\n    else:\n        print(f'{f2} is greatest')</code></pre>",
        "opts": ["23 is greatest", "453 is greatest", "54 is greatest", "76 is greatest"],
        "ans": "453 is greatest"
    },
    {
        "q": "What is printed when the following nested condition is executed with values: <code>n1 = 10, n2 = 20, n3 = 60</code>?\n<pre><code>if n1 > n2:\n    if n1 > n3:\n        print(f'{n1} is the greatest number')\n    else:\n        print(f'{n3} is the greatest number')\nelse:\n    if n2 > n3:\n        print(f'{n2} is the greatest number')\n    else:\n        print(f'{n3} is the greatest number')</code></pre>",
        "opts": ["10 is the greatest number", "20 is the greatest number", "60 is the greatest number", "No output"],
        "ans": "60 is the greatest number"
    },
    {
        "q": "What is printed when the code below is executed with <code>marks = 34</code>?\n<pre><code>if marks < 34:\n    print('fail')\nelif marks > 34 and marks < 65:\n    print('distinction')\nelse:\n    print('invalid')</code></pre>",
        "opts": ["fail", "distinction", "invalid", "No output"],
        "ans": "invalid"
    },
    {
        "q": "What is the return value of <code>sum_list([1, 2, 3, 4, 5])</code> for this recursive function?\n<pre><code>def sum_list(numbers):\n    if len(numbers) == 0:\n        return 0\n    else:\n        return numbers[0] + sum_list(numbers[1:])</code></pre>",
        "opts": ["15", "10", "5", "0"],
        "ans": "15"
    },
    {
        "q": "What is the output of <code>print(s)</code> after creating the set <code>s</code> below?\n<pre><code>s = {1, 2, 3, 3, 3, 3, 4, 54, 6, 7, 2, 1, 1, 12}</code></pre>",
        "opts": ["{1, 2, 3, 4, 6, 7, 12, 54}", "{1, 2, 3, 3, 3, 3, 4, 54, 6, 7, 2, 1, 1, 12}", "{1, 2, 3, 4, 6, 7, 12}", "Raises SyntaxError"],
        "ans": "{1, 2, 3, 4, 6, 7, 12, 54}"
    },
    {
        "q": "What does <code>s.difference(t)</code> return for the following sets?\n<pre><code>s = {1, 2, 3, 4, 6, 7, 12, 54}\nt = {1, 2, 3, 4, 5, 6, 7, 8, 9}</code></pre>",
        "opts": ["{12, 54}", "{5, 8, 9}", "{1, 2, 3, 4, 6, 7}", "set()"],
        "ans": "{12, 54}"
    },
    {
        "q": "What is the value of <code>x</code> after running the code below?\n<pre><code>a = '2345.6'\nx = a.isdecimal()</code></pre>",
        "opts": ["True", "False", "None", "Raises AttributeError"],
        "ans": "False"
    },
    {
        "q": "What does <code>c.capitalize()</code> return if <code>c</code> is defined as follows?\n<pre><code>c = 'a well-structured paragraph typically ranges from 4 to 7 sentences'</code></pre>",
        "opts": ["'A well-structured...'", "'A Well-Structured...'", "'a well-structured...'", "'A WELL-STRUCTURED...'"],
        "ans": "'A well-structured...'"
    },
    {
        "q": "What does the sliced string <code>y</code> contain after executing this code?\n<pre><code>s = 'I love eating toasted cheese and tuna sandwiches'\ny = s[::-1]</code></pre>",
        "opts": ["The reversed string s", "The original string s", "A list of characters in reverse order", "Raises ValueError"],
        "ans": "The reversed string s"
    },
    {
        "q": "What is the final value of <code>total</code> after executing the loop below?\n<pre><code>n = 5\ntotal = 0\nwhile n > 0:\n    total += n\n    n -= 1</code></pre>",
        "opts": ["15", "10", "5", "0"],
        "ans": "15"
    }
]

theoretical_mcqs = [
    {"q": "Which of these is not a core data type?", "opts": ["Lists", "Dictionary", "Tuples", "Class"], "ans": "Class"},
    {"q": "Which of the following is an immutable data type?", "opts": ["List", "Dictionary", "Set", "Tuple"], "ans": "Tuple"},
    {"q": "What is the primary difference between a list and a tuple?", "opts": ["Lists are mutable, tuples are immutable", "Tuples are mutable, lists are immutable", "Lists can store different data types", "Tuples can store different data types"], "ans": "Lists are mutable, tuples are immutable"},
    {"q": "Which keyword is used to define a custom function?", "opts": ["func", "define", "def", "lambda"], "ans": "def"},
    {"q": "What best describes a Python dictionary?", "opts": ["An ordered sequence of items", "A collection of key-value pairs", "An immutable list", "A set of unique numbers"], "ans": "A collection of key-value pairs"},
    {"q": "What is the purpose of the `continue` statement?", "opts": ["Exit a loop immediately", "Skip rest of iteration and move next", "Restart the loop from beginning", "Return a value from function"], "ans": "Skip rest of iteration and move next"},
    {"q": "How do you start a single-line comment in Python?", "opts": ["//", "/*", "<!--", "#"], "ans": "#"},
    {"q": "What is 'Type Casting'?", "opts": ["Checking variable type", "Converting between data types", "Assigning strict types", "Deleting data type"], "ans": "Converting between data types"},
    {"q": "What is the scope of a variable defined inside a function?", "opts": ["Global", "Local", "Nonlocal", "Module"], "ans": "Local"},
    {"q": "What is the default return value of a function missing a return?", "opts": ["0", "False", "None", "Error"], "ans": "None"}
]

with st.form("quiz_form"):
    user_answers = {}
    
    st.subheader("💻 Practical Set")
    for i, mcq in enumerate(practical_mcqs):
        with st.container(border=True):
            st.markdown(f"<div class='question-number'>Question {i+1}</div>", unsafe_allow_html=True)
            st.markdown(f"<hr>", unsafe_allow_html=True)
            st.markdown(f"<div class='question-text'>{mcq['q']}</div>", unsafe_allow_html=True)
            
            # Prepend A, B, C, D visually
            formatted_opts = [f"{prefixes[idx]} \u00A0\u00A0 {opt}" for idx, opt in enumerate(mcq['opts'])]
            
            selection = st.radio(
                f"prac_{i}", 
                formatted_opts, 
                key=f"p_{i}", 
                label_visibility="collapsed", 
                index=None
            )
            
            # Map the selected string back to the original answer
            if selection:
                # remove prefix logic (first 4 chars: "Ⓐ    ")
                user_answers[f"prac_{i}"] = selection[4:].strip()
            else:
                user_answers[f"prac_{i}"] = None
                
    st.write("---")
    
    st.subheader("💭 Theoretical Set")
    for i, mcq in enumerate(theoretical_mcqs):
        with st.container(border=True):
            st.markdown(f"<div class='question-number'>Question {i+21}</div>", unsafe_allow_html=True)
            st.markdown(f"<hr>", unsafe_allow_html=True)
            st.markdown(f"<div class='question-text'>{mcq['q']}</div>", unsafe_allow_html=True)
            
            formatted_opts = [f"{prefixes[idx]} \u00A0\u00A0 {opt}" for idx, opt in enumerate(mcq['opts'])]
            
            selection = st.radio(
                f"theo_{i}", 
                formatted_opts, 
                key=f"t_{i}", 
                label_visibility="collapsed", 
                index=None
            )
            
            if selection:
                user_answers[f"theo_{i}"] = selection[4:].strip()
            else:
                user_answers[f"theo_{i}"] = None

    submitted = st.form_submit_button("🚀 Submit Quiz")

    if submitted:
        score = 0
        for i, mcq in enumerate(practical_mcqs):
            if user_answers.get(f"prac_{i}") == mcq['ans']:
                score += 1
        for i, mcq in enumerate(theoretical_mcqs):
            if user_answers.get(f"theo_{i}") == mcq['ans']:
                score += 1

        if score == 30:
            st.balloons()
            st.markdown(f"<div style='background-color:#064e3b; padding:20px; border-radius:10px; color:#34d399; font-weight:bold; font-size:20px; text-align:center;'>🎉 Perfect Score! You got {score} / 30 marks!</div>", unsafe_allow_html=True)
        elif score >= 20:
            st.markdown(f"<div style='background-color:#1e3a8a; padding:20px; border-radius:10px; color:#60a5fa; font-weight:bold; font-size:20px; text-align:center;'>🌟 Great job! You got {score} / 30 marks.</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='background-color:#7f1d1d; padding:20px; border-radius:10px; color:#f87171; font-weight:bold; font-size:20px; text-align:center;'>👍 Good effort. You got {score} / 30 marks. Keep reviewing the concepts!</div>", unsafe_allow_html=True)


print("done")