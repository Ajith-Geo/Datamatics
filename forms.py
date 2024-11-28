import requests

def submit_form(customer_name, order_id, feedback_category, sentiment_score):
    form_url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfBuzFvWRlVVm9bVrxB-R5ZovEoSAw-Qq_CR7KdX_2Ua_6-jA/formResponse"
    form_data = {
        "entry.665770853": customer_name,
        "entry.430623167": order_id,
        "entry.1815337387": feedback_category,
        "entry.831206065": sentiment_score
    }
    response = requests.post(form_url, data=form_data)
    if response.status_code == 200:
        return "Form submitted successfully."
    else:
        return f"Failed to submit form. Status code: {response.status_code}, Response: {response.text}"
