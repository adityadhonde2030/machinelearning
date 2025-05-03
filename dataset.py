import requests

url = "https://test.vidalhealthtpa.com"  # Replace with actual endpoint

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Origin": "https://test.vidalhealthtpa.com",
    "Referer": "https://test.vidalhealthtpa.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "ocp-apim-subscription-key": "5938b657dd2e4401bbaf8bc21cc98ada",
    "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "vapdKey": "KCeL4dNhStFAQbZK5gT7fRPpvrsPM3O7Gjh9GJrLEWglSILYycBzgL086fH+z8LJvJjAuX7zVYgkNVg2P52DSzMbT5YmHM3tdGxN01RUIXd0Og0di6tiSbI3ekvBLaWOylyGdzYODO9t8laixVVJYDh7F9ojgUuPrN2vGho3s8KcVDTXGL989pwpz2t1IsYP9JYsUGAbIJk3UdW+nhzno2b6lphnJGgiJvKNWQtRffw="
}

# Form-data with text field
files = {
    "preauthDtls": (None, """{
        "enrollDtlSeqID": "4783063",
        "claimantDtls": {
            "memberSeqID": "39110807",
            "enrollmentID": "BLR-UI-T0939-002-0000001-A",
            "policyNbr": "000001/TD/POLICY/TEST",
            "policySeqID": "6277726",
            "insSeqID": "36696",
            "genderTypeID": "FEM",
            "name": "KRISHA",
            "age": "24",
            "dateOfInception": "01/01/2025",
            "dateOfExit": "31/12/2025",
            "totalSumInsured": "1000000",
            "categoryTypeID": "CVV",
            "policyTypeID": "COR",
            "policySubTypeID": "PFL",
            "availSumInsured": 990488,
            "phone": "9763666693",
            "emailID": "akshay.gangurde@bfhl.in"
        },
        "admissionTime": "24/03/2025 12:00 AM",
        "hospitalCategory": "Nat",
        "hospitalPhone": "9763666693",
        "requestAmount": 100000,
        "preAuthRecvTypeID": "OLN",
        "preauthSubTypeBenefit": "CSH",
        "admissionType": "Planned",
        "dischargeTime": "27/03/2025 08:00 PM"
    }""", "text/plain"),  # Text selection in form-data dropdown

    "exceptionFile": (None, "null", "text/plain")  # "null" as text field
}

response = requests.post(url, headers=headers, files=files)

print("Response Status:", response.status_code)
print("Response Data:", response)
