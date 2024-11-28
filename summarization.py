def gemini(email: str):

    import google.generativeai as genai
    genai.configure(api_key='')
    model = genai.GenerativeModel('gemini-1.5-flash')
    # email="Dear Team, I recently purchased a pair of headphones (Order #56789), and I'm quite disappointed with the experience. The product arrived late, and the packaging was damaged. Additionally, the headphones are not working as expected—they have a persistent static noise that ruins the sound quality. I was hoping for better service and a functional product, but this experience has been frustrating. Please let me know how this can be resolved quickly. Best regards,John Doe"
    response = model.generate_content("summarize the following email, only give the output of the summary with all the main insights being considered"+email)
    # print(response.text)
    return response.text
