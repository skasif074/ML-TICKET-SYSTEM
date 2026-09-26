
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "qwen/qwen3.8-27b"

_client = None

FALLBACK_RESPONSES = {
    "Login Issue": "Please use the 'Forgot Password' option on the login page to reset your credentials. If the issue persists, contact our support team.",
    "Application Error": "We're sorry for the inconvenience. Please try refreshing the page or restarting the app. Our team has been notified and will investigate further.",
    "Report": "Your report request has been noted. Reports are typically generated within 24 hours and will be sent to your registered email.",
    "Account Update": "Your account update request has been received. Please verify your identity through the confirmation link sent to your registered email or phone.",
    "Performance": "We're aware of the slowdown and are working to resolve it. In the meantime, try clearing your cache or using a stable internet connection.",
}


def _get_client():
    global _client
    if _client is None:
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found in environment variables.")
        _client = Groq(api_key=GROQ_API_KEY)
    return _client


def generate_response(category: str, description: str) -> str:
    try:
        client = _get_client()

        prompt = (
            f"A customer support ticket was classified under the category '{category}'. "
            f"The customer wrote: \"{description}\". "
            "Write a short, polite, helpful support response in 2-3 sentences."
        )

        completion = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=150,
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        print(f"[generate_response] Falling back to rule-based response. Reason: {e}")
        return FALLBACK_RESPONSES.get(
            category, "Thank you for reaching out. Our support team will get back to you shortly."
        )


if __name__ == "__main__":
    test_category = "Login Issue"
    test_description = "I forgot my password and cannot login."
    reply = generate_response(test_category, test_description)
    print(f"Category: {test_category}")
    print(f"Suggested Response: {reply}")