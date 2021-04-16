import requests

def tests_prediction_for_Technology_Data_Analytics():
    url = "http://localhost:5000"

    payload={}
    files=[
    ('file',('sample-resumes_cfa1.pdf',open(r'C:\Users\khero\Desktop\CareerHelp\CareerHelp\textClassifier\test_resumes\sample-resumes_cfa1.pdf','rb'),'application/pdf'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    assert response.text == "Technology_Data_Analytics"

def tests_prediction_for_Communication_Entertainment_Arts():
    url = "http://localhost:5000"

    payload={}
    files=[
    ('file',('Marketing_Resume.pdf',open(r'C:\Users\khero\Desktop\CareerHelp\CareerHelp\textClassifier\test_resumes\Marketing_Resume.pdf','rb'),'application/pdf'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    assert response.text == "Communications_Entertainment_Arts"

def tests_prediction_for_NonProfit_Management():
    url = "http://localhost:5000"

    payload={}
    files=[
    ('file',('MusicTeacher_Resume.pdf',open(r'C:\Users\khero\Desktop\CareerHelp\CareerHelp\textClassifier\test_resumes\MusicTeacher_Resume.pdf','rb'),'application/pdf'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    assert response.text == "Non-Profit_Management_Education"

def tests_when_other_extension_sent():
    url = "http://localhost:5000"

    payload={}
    files=[
    ('file',('MusicTeacher_Resume.docx',open(r'C:\Users\khero\Desktop\CareerHelp\CareerHelp\textClassifier\test_resumes\MusicTeacher_Resume.docx','rb'),'application/vnd.openxmlformats-officedocument.wordprocessingml.document'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    assert response.text == "Only pdfs are allowed"
