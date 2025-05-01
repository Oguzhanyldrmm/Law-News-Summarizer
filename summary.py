import google.generativeai as genai
#from scrapper import extract_full_text

genai.configure(api_key="AIzaSyBXSZjCFGl6BXuwiXDr-IsEjmYeNR17KTI")
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_summaries(article_text):
    prompt = f"""
Aşağıdaki haberi 3 seviyede özetle:

- Kısa özet: 1-2 cümle ile özeti yaz.
- Orta özet: 4-5 cümlelik genel bir özet ver.
- Uzun özet: Haberin tüm detaylarını açıklayan ayrıntılı bir özet oluştur.

Haber metni:
\"\"\"
{article_text}
\"\"\"
    """

    response = model.generate_content(prompt)
    return response.text


def split_summaries(model_output):
    
    short = ""
    medium = ""
    long_ = ""
    
    lines = model_output.split("\n")

    for line in lines:
        line = line.replace("*", "").strip()  #for deleting * character
        lowered = line.lower()

        if "kısa özet" in lowered and ":" in line:
            short = line.split(":", 1)[1].strip()

        elif "orta özet" in lowered and ":" in line:
            medium = line.split(":", 1)[1].strip()

        elif "uzun özet" in lowered and ":" in line:
            long_ = line.split(":", 1)[1].strip()

    return short, medium, long_


""" text = extract_full_text("https://www.hukukihaber.net/yargitay-1-ceza-dairesinin-20246057-e-2025420-k-sayili-karari")
summary_text = generate_summaries(text)

print(summary_text)

short, medium, long_ = split_summaries(summary_text)

print("Kısa özet: ", short)
print("Orta özet: ", medium)
print("Uzun özet: ", long_)
"""