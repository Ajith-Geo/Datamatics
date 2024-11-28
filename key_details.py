def geminis(email: str):

    import google.generativeai as genai
    genai.configure(api_key='')
    model = genai.GenerativeModel('gemini-1.5-flash')

    fields= {  'Customer Name': '<Name>',  'Order ID': '<Order ID or N/A>',  'Feedback Category': '<Category>',  'Sentiment Score': '<Score>'}
    response = model.generate_content(f'only return json. Extract the following details from customer email: Customer Name: Identify the name from the salutation, signature, or email body. Order ID: Extract if mentioned, otherwise mark as N/A. Feedback Category: Classify as Product, Service, or Delivery based on the content. Sentiment Score: Determine tone as Positive (+1), Neutral (0), or Negative (-1). Return the output in this format: {fields}  email: {email}')
    formatted_output = f'{response.text}\n'
    formatted_output = formatted_output.replace('json','').replace('','')
    return str(formatted_output)
