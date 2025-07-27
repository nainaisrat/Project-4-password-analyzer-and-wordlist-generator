from zxcvbn import zxcvbn

def analyze_password(password):
    results = zxcvbn(password)
    score = results['score']
    suggestions = results['feedback']['suggestions']
    return score, suggestions

if __name__ == "__main__":
    password = input("Enter a password to analyze: ")
    score, feedback = analyze_password(password)
    print(f"Strength Score (0–4): {score}")
    print("Suggestions:", feedback)
