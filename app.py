import streamlit as st

st.set_page_config(page_title="🤖 Machine Learning Quiz", page_icon="🎓", layout="centered")

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

st.title("Machine Learning Assessment")
st.subheader("Test your understanding of Machine Learning concepts with this quiz! From statistics to algorithms — let's see how well you know your ML fundamentals. Good luck! 🍀")
st.markdown("<p style='color: #64748b; font-size: 15px; font-weight: 500;'>Last Updated : Aug 31, 2026</p>", unsafe_allow_html=True)
st.write("---")

prefixes = ["Ⓐ", "Ⓑ", "Ⓒ", "Ⓓ"]

# ──────────────────────────────────────────────────────────────
# PYTHON QUIZ (COMMENTED OUT)
# ──────────────────────────────────────────────────────────────

# practical_mcqs = [
#     {
#         "q": "What is the output of the following code?\n<pre><code>dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}\nupdate_dict = {'age': 31, 'city': 'Los Angeles', 'country': 'USA'}\nm = dict | update_dict\nprint(m.get('age'))</code></pre>",
#         "opts": ["30", "31", "None", "Raises KeyError"],
#         "ans": "31"
#     },
#     {
#         "q": "What is the data type of <code>dict['phone_numbers']</code> in the following dictionary?\n<pre><code>dict = {\n    'name': 'Alice',\n    'phone_numbers': ('123-456-7890', '987-654-3210')\n}</code></pre>",
#         "opts": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'str'>"],
#         "ans": "<class 'tuple'>"
#     },
#     {
#         "q": "What is the value of <code>dict[2][1]</code> for the dictionary below?\n<pre><code>dict = {\n    2: ['reading', 'traveling', 'cooking']\n}</code></pre>",
#         "opts": ["'reading'", "'traveling'", "'cooking'", "Raises KeyError"],
#         "ans": "'traveling'"
#     },
#     {
#         "q": "What is the length of the list <code>L</code> generated by the following list comprehension?\n<pre><code>L = [i for i in range(-20, 20) if i % 2 == 0]</code></pre>",
#         "opts": ["20", "40", "19", "21"],
#         "ans": "20"
#     },
#     {
#         "q": "What is the value of <code>l[0]</code> after executing these list operations?\n<pre><code>l = [10, 20, 30, 'p', 98.7, 'apple', True, 67.5]\nl.append(40)\nl.insert(0, 90)</code></pre>",
#         "opts": ["10", "90", "40", "67.5"],
#         "ans": "90"
#     },
#     {
#         "q": "What is the output of <code>print(j.count(60))</code> for the list <code>j</code> below?\n<pre><code>j = [50, 60, 70, 80, 50, 60, 60, 60, 20]</code></pre>",
#         "opts": ["2", "3", "4", "5"],
#         "ans": "4"
#     },
#     {
#         "q": "What is the value of <code>t</code> after running this sequence?\n<pre><code>t = ('10', 20, True, 'Hello', 3.14)\nk = list(t)\nk.append(40)\nt = tuple(k)</code></pre>",
#         "opts": ["('10', 20, True, 'Hello', 3.14, 40)", "('10', 20, True, 'Hello', 3.14)", "(40, '10', 20, True, 'Hello', 3.14)", "Raises TypeError"],
#         "ans": "('10', 20, True, 'Hello', 3.14, 40)"
#     },
#     {
#         "q": "What is the output of <code>print(t.index(3.14))</code> for the tuple <code>t</code> below?\n<pre><code>t = ('10', 20, True, 'Hello', 3.14)</code></pre>",
#         "opts": ["3", "4", "5", "Raises ValueError"],
#         "ans": "4"
#     },
#     {
#         "q": "What is the return value of <code>aot(5, 6)</code> for the function defined below?\n<pre><code>def aot(b, h):\n    return 0.5 * b * h</code></pre>",
#         "opts": ["15.0", "30.0", "15", "30"],
#         "ans": "15.0"
#     },
#     {
#         "q": "What is the return value of <code>aoc(2)</code> for the function defined below?\n<pre><code>def aoc(r):\n    return 3.14 * r * r</code></pre>",
#         "opts": ["6.28", "12.56", "12.0", "3.14"],
#         "ans": "12.56"
#     },
#     {
#         "q": "What is printed when calling <code>greatestO4(23, 453, 54, 76)</code> with the definition below?\n<pre><code>def greatestO4(n1, n2, n3, n4):\n    if n1 > n2:\n        f1 = n1\n    else:\n        f1 = n2\n    if n3 > n4:\n        f2 = n3\n    else:\n        f2 = n4\n    if f1 > f2:\n        print(f'{f1} is greatest')\n    else:\n        print(f'{f2} is greatest')</code></pre>",
#         "opts": ["23 is greatest", "453 is greatest", "54 is greatest", "76 is greatest"],
#         "ans": "453 is greatest"
#     },
#     {
#         "q": "What is printed when the following nested condition is executed with values: <code>n1 = 10, n2 = 20, n3 = 60</code>?\n<pre><code>if n1 > n2:\n    if n1 > n3:\n        print(f'{n1} is the greatest number')\n    else:\n        print(f'{n3} is the greatest number')\nelse:\n    if n2 > n3:\n        print(f'{n2} is the greatest number')\n    else:\n        print(f'{n3} is the greatest number')</code></pre>",
#         "opts": ["10 is the greatest number", "20 is the greatest number", "60 is the greatest number", "No output"],
#         "ans": "60 is the greatest number"
#     },
#     {
#         "q": "What is printed when the code below is executed with <code>marks = 34</code>?\n<pre><code>if marks < 34:\n    print('fail')\nelif marks > 34 and marks < 65:\n    print('distinction')\nelse:\n    print('invalid')</code></pre>",
#         "opts": ["fail", "distinction", "invalid", "No output"],
#         "ans": "invalid"
#     },
#     {
#         "q": "What is the return value of <code>sum_list([1, 2, 3, 4, 5])</code> for this recursive function?\n<pre><code>def sum_list(numbers):\n    if len(numbers) == 0:\n        return 0\n    else:\n        return numbers[0] + sum_list(numbers[1:])</code></pre>",
#         "opts": ["15", "10", "5", "0"],
#         "ans": "15"
#     },
#     {
#         "q": "What is the output of <code>print(s)</code> after creating the set <code>s</code> below?\n<pre><code>s = {1, 2, 3, 3, 3, 3, 4, 54, 6, 7, 2, 1, 1, 12}</code></pre>",
#         "opts": ["{1, 2, 3, 4, 6, 7, 12, 54}", "{1, 2, 3, 3, 3, 3, 4, 54, 6, 7, 2, 1, 1, 12}", "{1, 2, 3, 4, 6, 7, 12}", "Raises SyntaxError"],
#         "ans": "{1, 2, 3, 4, 6, 7, 12, 54}"
#     },
#     {
#         "q": "What does <code>s.difference(t)</code> return for the following sets?\n<pre><code>s = {1, 2, 3, 4, 6, 7, 12, 54}\nt = {1, 2, 3, 4, 5, 6, 7, 8, 9}</code></pre>",
#         "opts": ["{12, 54}", "{5, 8, 9}", "{1, 2, 3, 4, 6, 7}", "set()"],
#         "ans": "{12, 54}"
#     },
#     {
#         "q": "What is the value of <code>x</code> after running the code below?\n<pre><code>a = '2345.6'\nx = a.isdecimal()</code></pre>",
#         "opts": ["True", "False", "None", "Raises AttributeError"],
#         "ans": "False"
#     },
#     {
#         "q": "What does <code>c.capitalize()</code> return if <code>c</code> is defined as follows?\n<pre><code>c = 'a well-structured paragraph typically ranges from 4 to 7 sentences'</code></pre>",
#         "opts": ["'A well-structured...'", "'A Well-Structured...'", "'a well-structured...'", "'A WELL-STRUCTURED...'"],
#         "ans": "'A well-structured...'"
#     },
#     {
#         "q": "What does the sliced string <code>y</code> contain after executing this code?\n<pre><code>s = 'I love eating toasted cheese and tuna sandwiches'\ny = s[::-1]</code></pre>",
#         "opts": ["The reversed string s", "The original string s", "A list of characters in reverse order", "Raises ValueError"],
#         "ans": "The reversed string s"
#     },
#     {
#         "q": "What is the final value of <code>total</code> after executing the loop below?\n<pre><code>n = 5\ntotal = 0\nwhile n > 0:\n    total += n\n    n -= 1</code></pre>",
#         "opts": ["15", "10", "5", "0"],
#         "ans": "15"
#     }
# ]
#
# theoretical_mcqs = [
#     {"q": "Which of these is not a core data type?", "opts": ["Lists", "Dictionary", "Tuples", "Class"], "ans": "Class"},
#     {"q": "Which of the following is an immutable data type?", "opts": ["List", "Dictionary", "Set", "Tuple"], "ans": "Tuple"},
#     {"q": "What is the primary difference between a list and a tuple?", "opts": ["Lists are mutable, tuples are immutable", "Tuples are mutable, lists are immutable", "Lists can store different data types", "Tuples can store different data types"], "ans": "Lists are mutable, tuples are immutable"},
#     {"q": "Which keyword is used to define a custom function?", "opts": ["func", "define", "def", "lambda"], "ans": "def"},
#     {"q": "What best describes a Python dictionary?", "opts": ["An ordered sequence of items", "A collection of key-value pairs", "An immutable list", "A set of unique numbers"], "ans": "A collection of key-value pairs"},
#     {"q": "What is the purpose of the `continue` statement?", "opts": ["Exit a loop immediately", "Skip rest of iteration and move next", "Restart the loop from beginning", "Return a value from function"], "ans": "Skip rest of iteration and move next"},
#     {"q": "How do you start a single-line comment in Python?", "opts": ["//", "/*", "<!--", "#"], "ans": "#"},
#     {"q": "What is 'Type Casting'?", "opts": ["Checking variable type", "Converting between data types", "Assigning strict types", "Deleting data type"], "ans": "Converting between data types"},
#     {"q": "What is the scope of a variable defined inside a function?", "opts": ["Global", "Local", "Nonlocal", "Module"], "ans": "Local"},
#     {"q": "What is the default return value of a function missing a return?", "opts": ["0", "False", "None", "Error"], "ans": "None"}
# ]

# ──────────────────────────────────────────────────────────────
# MACHINE LEARNING QUIZ — 30 Marks (20 Practical + 10 Theory)
# Level: Easy to Moderate
# ──────────────────────────────────────────────────────────────

practical_mcqs = [
    # Q1 — Statistics: Mean
    {
        "q": "What is the output of the following code?\n<pre><code>import numpy as np\nscores = np.array([56, 78, 92, 88, 45, 78, 90, 65, 78, 100])\nprint(np.mean(scores))</code></pre>",
        "opts": ["77.0", "78.0", "76.0", "80.0"],
        "ans": "77.0"
    },
    # Q2 — Statistics: Median
    {
        "q": "What is the output of <code>np.median(scores)</code> for the array below?\n<pre><code>import numpy as np\nscores = np.array([56, 78, 92, 88, 45, 78, 90, 65, 78, 100])</code></pre>",
        "opts": ["77.0", "78.0", "79.0", "80.0"],
        "ans": "78.0"
    },
    # Q3 — Statistics: Mode
    {
        "q": "What is the output of the following code?\n<pre><code>import pandas as pd\nscores = [56, 78, 92, 88, 45, 78, 90, 65, 78, 100]\nprint(pd.Series(scores).mode()[0])</code></pre>",
        "opts": ["56", "78", "92", "100"],
        "ans": "78"
    },
    # Q4 — Statistics: Standard Deviation
    {
        "q": "Two classes have the same mean score of 72.5. Class A has scores <code>[70, 72, 75, 74, 73, 71]</code> and Class B has <code>[50, 90, 60, 95, 55, 85]</code>. Which class has a <strong>higher</strong> standard deviation?",
        "opts": ["Class A", "Class B", "Both are equal", "Cannot be determined"],
        "ans": "Class B"
    },
    # Q5 — Correlation
    {
        "q": "What is the approximate output of the code below?\n<pre><code>import pandas as pd\ndf = pd.DataFrame({\n    'study_hours': [1, 2, 3, 4, 5, 6, 7, 8],\n    'exam_score':  [50, 55, 60, 62, 70, 75, 85, 90]\n})\nprint(round(df['study_hours'].corr(df['exam_score']), 2))</code></pre>",
        "opts": ["0.99", "0.50", "-0.99", "0.00"],
        "ans": "0.99"
    },
    # Q6 — Bayes' Theorem
    {
        "q": "A disease affects 1% of a population. A test has 99% sensitivity and 5% false positive rate. If a person tests positive, what is the approximate probability they actually have the disease?\n<pre><code>P(Disease) = 0.01\nP(Pos|Disease) = 0.99\nP(Pos|No Disease) = 0.05</code></pre>",
        "opts": ["~16.7%", "~95%", "~99%", "~50%"],
        "ans": "~16.7%"
    },
    # Q7 — train_test_split
    {
        "q": "What does the following code do?\n<pre><code>from sklearn.model_selection import train_test_split\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)</code></pre>",
        "opts": [
            "Splits data into 80% training and 20% testing",
            "Splits data into 20% training and 80% testing",
            "Creates 5 folds for cross-validation",
            "Normalizes the features"
        ],
        "ans": "Splits data into 80% training and 20% testing"
    },
    # Q8 — Linear Regression: Prediction
    {
        "q": "A simple linear regression model is trained with <code>y = 500 * x + 1000</code>. What is the predicted value when <code>x = 5</code>?\n<pre><code>predicted = 500 * 5 + 1000</code></pre>",
        "opts": ["3500", "2500", "4000", "1500"],
        "ans": "3500"
    },
    # Q9 — Linear Regression: Coefficient
    {
        "q": "After training a linear regression model, you run:\n<pre><code>from sklearn.linear_model import LinearRegression\nreg = LinearRegression()\nreg.fit(X_train, y_train)\nprint(reg.coef_)\n# Output: [828.46]</code></pre>\nWhat does <code>828.46</code> represent?",
        "opts": [
            "The slope — for each unit increase in X, y increases by 828.46",
            "The y-intercept of the regression line",
            "The R² score of the model",
            "The mean squared error"
        ],
        "ans": "The slope — for each unit increase in X, y increases by 828.46"
    },
    # Q10 — Linear Regression: Intercept
    {
        "q": "After fitting a linear regression, <code>reg.intercept_</code> returns <code>-1632534.0</code>. What does this value represent?",
        "opts": [
            "The predicted y value when all features are zero",
            "The maximum error of the model",
            "The slope of the regression line",
            "The total number of training samples"
        ],
        "ans": "The predicted y value when all features are zero"
    },
    # Q11 — Logistic Regression: Output
    {
        "q": "What type of output does a Logistic Regression model produce?\n<pre><code>from sklearn.linear_model import LogisticRegression\nmodel = LogisticRegression()\nmodel.fit(X_train, y_train)\nprint(model.predict([[30, 50000]]))</code></pre>",
        "opts": [
            "A class label (e.g., 0 or 1)",
            "A continuous numeric value",
            "A probability between -1 and 1",
            "A list of feature importances"
        ],
        "ans": "A class label (e.g., 0 or 1)"
    },
    # Q12 — Confusion Matrix
    {
        "q": "Given the confusion matrix below, how many samples were <strong>correctly predicted</strong>?\n<pre><code>from sklearn.metrics import confusion_matrix\n# Result:\n# [[50,  5],\n#  [10, 35]]</code></pre>",
        "opts": ["85", "15", "50", "35"],
        "ans": "85"
    },
    # Q13 — Accuracy Score
    {
        "q": "What is the accuracy of a model with the following confusion matrix?\n<pre><code># [[50,  5],\n#  [10, 35]]\n# Total = 100</code></pre>",
        "opts": ["85%", "50%", "35%", "90%"],
        "ans": "85%"
    },
    # Q14 — Decision Tree: max_depth
    {
        "q": "What happens when you set <code>max_depth=1</code> in a Decision Tree?\n<pre><code>from sklearn.tree import DecisionTreeClassifier\ndt = DecisionTreeClassifier(max_depth=1)\ndt.fit(X_train, y_train)</code></pre>",
        "opts": [
            "The tree makes only one split (a decision stump)",
            "The tree has unlimited depth",
            "The tree uses only one feature",
            "The model becomes a linear regression"
        ],
        "ans": "The tree makes only one split (a decision stump)"
    },
    # Q15 — Random Forest: n_estimators
    {
        "q": "What does <code>n_estimators=100</code> mean in a Random Forest model?\n<pre><code>from sklearn.ensemble import RandomForestClassifier\nrf = RandomForestClassifier(n_estimators=100)\nrf.fit(X_train, y_train)</code></pre>",
        "opts": [
            "The forest contains 100 decision trees",
            "The model uses 100 features",
            "The maximum depth of each tree is 100",
            "The model trains for 100 epochs"
        ],
        "ans": "The forest contains 100 decision trees"
    },
    # Q16 — KNN: Prediction Logic
    {
        "q": "In KNN classification with <code>n_neighbors=5</code>, if 3 nearest neighbors belong to class A and 2 to class B, what will the model predict?\n<pre><code>from sklearn.neighbors import KNeighborsClassifier\nknn = KNeighborsClassifier(n_neighbors=5)</code></pre>",
        "opts": ["Class A", "Class B", "The average of A and B", "It raises an error"],
        "ans": "Class A"
    },
    # Q17 — Feature Scaling
    {
        "q": "What does <code>StandardScaler</code> do to the data?\n<pre><code>from sklearn.preprocessing import StandardScaler\nscaler = StandardScaler()\nX_scaled = scaler.fit_transform(X)</code></pre>",
        "opts": [
            "Transforms features to have mean=0 and std=1",
            "Scales all values to the range [0, 1]",
            "Removes outliers from the dataset",
            "Converts categorical data to numerical"
        ],
        "ans": "Transforms features to have mean=0 and std=1"
    },
    # Q18 — K-Fold Cross Validation
    {
        "q": "In 5-fold cross-validation, how many times is the model trained and evaluated?\n<pre><code>from sklearn.model_selection import cross_val_score\nscores = cross_val_score(model, X, y, cv=5)</code></pre>",
        "opts": ["5 times", "1 time", "10 times", "It depends on the dataset size"],
        "ans": "5 times"
    },
    # Q19 — K-Means Clustering
    {
        "q": "What does <code>n_clusters=3</code> specify in K-Means?\n<pre><code>from sklearn.cluster import KMeans\nkm = KMeans(n_clusters=3)\nkm.fit(X)</code></pre>",
        "opts": [
            "The algorithm will group data into 3 clusters",
            "The algorithm runs 3 iterations",
            "The algorithm uses 3 features",
            "The algorithm removes 3 outliers"
        ],
        "ans": "The algorithm will group data into 3 clusters"
    },
    # Q20 — PCA
    {
        "q": "What does PCA with <code>n_components=2</code> do to a dataset with 10 features?\n<pre><code>from sklearn.decomposition import PCA\npca = PCA(n_components=2)\nX_reduced = pca.fit_transform(X)</code></pre>",
        "opts": [
            "Reduces the dataset from 10 features to 2 principal components",
            "Selects the 2 best features and removes the rest",
            "Doubles the number of features",
            "Splits data into 2 clusters"
        ],
        "ans": "Reduces the dataset from 10 features to 2 principal components"
    }
]

theoretical_mcqs = [
    # Q21
    {
        "q": "Which of the following best describes Machine Learning?",
        "opts": [
            "Explicitly programming rules for every scenario",
            "A system that learns patterns from data to make predictions",
            "A database management technique",
            "A hardware optimization process"
        ],
        "ans": "A system that learns patterns from data to make predictions"
    },
    # Q22
    {
        "q": "Which type of Machine Learning uses labeled data for training?",
        "opts": ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Semi-supervised Learning"],
        "ans": "Supervised Learning"
    },
    # Q23
    {
        "q": "In Machine Learning, what is a 'feature'?",
        "opts": [
            "An input variable used for prediction",
            "The output the model predicts",
            "The accuracy of the model",
            "The size of the training dataset"
        ],
        "ans": "An input variable used for prediction"
    },
    # Q24
    {
        "q": "Why is the median sometimes preferred over the mean as a measure of central tendency?",
        "opts": [
            "The median is not affected by outliers",
            "The median is always larger than the mean",
            "The median works only with categorical data",
            "The median requires more computation"
        ],
        "ans": "The median is not affected by outliers"
    },
    # Q25
    {
        "q": "What does 'correlation does not imply causation' mean?",
        "opts": [
            "Two variables moving together doesn't mean one causes the other",
            "Correlated variables are always independent",
            "Causation always implies correlation",
            "Correlation values are always positive"
        ],
        "ans": "Two variables moving together doesn't mean one causes the other"
    },
    # Q26
    {
        "q": "What is the primary goal of Linear Regression?",
        "opts": [
            "To predict a continuous numeric value",
            "To classify data into categories",
            "To cluster data into groups",
            "To reduce dimensionality"
        ],
        "ans": "To predict a continuous numeric value"
    },
    # Q27
    {
        "q": "What is 'overfitting' in Machine Learning?",
        "opts": [
            "The model performs well on training data but poorly on unseen data",
            "The model performs poorly on both training and test data",
            "The model has too few features",
            "The model trains too slowly"
        ],
        "ans": "The model performs well on training data but poorly on unseen data"
    },
    # Q28
    {
        "q": "Which algorithm is based on Bayes' Theorem and assumes features are independent?",
        "opts": ["Naive Bayes", "Decision Tree", "KNN", "SVM"],
        "ans": "Naive Bayes"
    },
    # Q29
    {
        "q": "What does SVM (Support Vector Machine) try to find?",
        "opts": [
            "The optimal hyperplane that best separates different classes",
            "The mean of all data points",
            "The nearest neighbors of each data point",
            "The principal components of the dataset"
        ],
        "ans": "The optimal hyperplane that best separates different classes"
    },
    # Q30
    {
        "q": "Which of the following is an Unsupervised Learning algorithm?",
        "opts": ["K-Means Clustering", "Linear Regression", "Logistic Regression", "Naive Bayes"],
        "ans": "K-Means Clustering"
    }
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
                # remove prefix logic (first 4 chars: "Ⓐ    ")
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