print("HELLO WORLD!!!")
# import os
# import json
# import math
# import requests
# import pandas as pd
# import msal
# import smtplib
# from datetime import datetime
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
 
# # ============================
# # CONFIGURATION
# # ============================
 
# # --- OneDrive (Graph API) ---
# client_id = "681200d3-f67d-4299-bd1c-58063d07ca24"
# client_secret = ""
# tenant_id = "3e98a0c9-6f90-4346-81c7-1e70a5d7f21b"
# user_email= "medrpa_prod@medicodio.com"  # Shared drive ID
# folder_path = "Daily Import"  # Path in OneDrive to scan
 
# authority = f"https://login.microsoftonline.com/{tenant_id}"
# scope = ["https://graph.microsoft.com/.default"]
 
# app = msal.ConfidentialClientApplication(
#     client_id, authority=authority, client_credential=client_secret
# )
 
# # --- API CONFIG ---
# auth_url = "https://api-dev.medicodio.com/rpa/auth/get-access-token"
# create_url = "https://api-dev.medicodio.com/rpa/chart/create"
# auth_payload = {
#     "client_id": "4e7b4b19b6cec02bd8714672385b8627",
#     "client_secret": "c3090d00-d82b-418f-9fa6-324a6a8739a3"
# }
# chunk_size = 50
 
# # --- Email Alerts ---
# sender_email = "dsalerts@medicodioinc.com"
# receiver_email = "shaheen.k@medicodio.ai"
# gmail_app_password = "ylgi emgx bsdv usro"
 
# # ============================
# # HELPERS
# # ============================
 
# def log(message):
#     print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")
 
# def get_onedrive_token():
#     token = app.acquire_token_for_client(scopes=scope)
#     if "access_token" in token:
#         return token["access_token"]
#     raise Exception(f"Unable to get access token: {token}")
 
# def list_onedrive_files():
#     access_token = get_onedrive_token()
#     headers = {"Authorization": f"Bearer {access_token}"}
#     url = f"https://graph.microsoft.com/v1.0/users/{user_email}/drive/root:/{folder_path}:/children"
#     resp = requests.get(url, headers=headers)
#     resp.raise_for_status()
#     return resp.json().get("value", [])
 
# def download_file(file_id, file_name, local_folder="temp_downloads"):
#     os.makedirs(local_folder, exist_ok=True)
#     access_token = get_onedrive_token()
#     headers = {"Authorization": f"Bearer {access_token}"}
#     url = f"https://graph.microsoft.com/v1.0/users/{user_email}/drive/items/{file_id}/content"
#     resp = requests.get(url, headers=headers, stream=True)
#     resp.raise_for_status()
#     local_path = os.path.join(local_folder, file_name)
#     with open(local_path, "wb") as f:
#         for chunk in resp.iter_content(chunk_size=8192):
#             f.write(chunk)
#     return local_path
 
# def send_email(subject, body):
#     msg = MIMEMultipart()
#     msg["From"] = sender_email
#     msg["To"] = receiver_email
#     msg["Subject"] = subject
#     msg.attach(MIMEText(body, "plain"))
#     try:
#         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#             server.login(sender_email, gmail_app_password)
#             server.send_message(msg)
#         log("📧 Email alert sent successfully")
#     except Exception as e:
#         log(f"❌ Failed to send email: {e}")
 
# def safe_get(row, col):
#     if col in row and pd.notna(row[col]):
#         val = row[col]
#         if isinstance(val, (pd.Timestamp, datetime)):
#             return val.strftime("%Y-%m-%d")
#         return str(val)
#     return "no information found"
 
# # ============================
# # SCHEMAS (all 4 header formats)
# # ============================
 
# SCHEMAS = {
#     "schema1": {
#         "subcriber_name": "Subcriber_ID",
#         "emr_name": "EMR_ID",
#         "report_type": "Report_type",
#         "mapping": {
#             "patient_id": "Patient_ID",
#             "patient_last_name": "Patient_L_Name",
#             "patient_middle_name": "Patient_M_Name",
#             "patient_first_name": "Patient_F_Name",
#             "patient_gender": "Patient_Gender",
#             "dob": "Date_of_Birth",
#             "insurance_category": "Ins_Cat",
#             "insurance_company": "INS_Comp",
#             "chart_record_id": "Chart Record_ID",
#             "doctor_first_name": "Dr_FName",
#             "doctor_last_name": "Dr_LName",
#             "hospital_name": "Hosp_Name",
#             "date_of_service": "Date_Of_Service",
#             "time_in": "Time_In",
#             "time_out": "Time_Out",
#             "pre_op_diagnosis": "Pre_Op_Diagnosis",
#             "post_op_diagnosis": "Post_Op_Diagnosis",
#             "operative_procedure": "Op_n_Procedures",
#             "description_of_condition": "DESCRIPTION_OF_Condition",
#             "description_of_procedure": "DESCRIPTION_OF_Procedure",
#             "post_of_impression": "Post_Op_Impression",
#             "plan_and_prognosis": "Plan_and_Prognosis",
#             "chief_complient_hpi": "Chief_Complient_HPI",
#             "history": "History",
#             "health_concerns": "Health_Concerns",
#             "active_condition_problems": "Active_Condition_Problems",
#             "assessment": "Assessment",
#             "clinical_impression": "Clinical_Impression",
#             "diagnosis": "Diagnosis",
#             "ros": "ROS",
#             "physical_exam": "Physical_Exam",
#             "test_and_orders": "test_and_orders",
#             "summary_recommendations": "summary_recommendations",
#             "procedure": "procedure",
#             "plan": "plan",
#             "claim_id": "Claim_ID",
#             "fpt_place_of_service_code": "fpt_placeofservicecode",
#             "fpt_type_of_service": "fpt_typeofservice",
#             "fpt_type_of_visit": "fpt_typeofvisit",
#             "pdf_file_url": "File_name"
#         }
#     },
#     "schema2": {
#         "subcriber_name": "subscriber_name",
#         "emr_name": "emr_name",
#         "report_type": "report_type_name",
#         "mapping": {
#             "patient_id": "patient_id",
#             "patient_first_name": "patient_first_name",
#             "patient_middle_name": "patient_middle_name",
#             "patient_last_name": "patient_last_name",
#             "patient_gender": "patient_gender",
#             "dob": "dob",
#             "insurance_category": "insurance_category",
#             "insurance_company": "insurance_company",
#             "chart_record_id": "chart_record_id",
#             "doctor_first_name": "doctor_first_name",
#             "doctor_last_name": "doctor_last_name",
#             "hospital_name": "hospital_name",
#             "date_of_service": "date_of_service",
#             "time_in": "time_in",
#             "time_out": "time_out",
#             "pre_op_diagnosis": "pre_op_diagnosis",
#             "post_op_diagnosis": "post_op_diagnosis",
#             "operative_procedure": "operative_procedure",
#             "description_of_condition": "description_of_condition",
#             "description_of_procedure": "description_of_procedure",
#             "post_of_impression": "post_of_impression",
#             "plan_and_prognosis": "plan_and_prognosis",
#             "chief_complient_hpi": "chief_complient_hpi",
#             "history": "history",
#             "health_concerns": "health_concerns",
#             "active_condition_problems": "active_condition_problems",
#             "assessment": "assessment",
#             "clinical_impression": "clinical_impression",
#             "diagnosis": "diagnosis",
#             "ros": "ros",
#             "physical_exam": "physical_exam",
#             "test_and_orders": "test_and_orders",
#             "summary_recommendations": "summary_recommendations",
#             "procedure": "procedure",
#             "plan": "plan",
#             "claim_id": "claim_id",
#             "fpt_place_of_service_code": "fpt_place_of_service_code",
#             "fpt_type_of_service": "fpt_type_of_service",
#             "fpt_type_of_visit": "fpt_type_of_visit",
#             "pdf_file_url": "pdf_file_url"
#         }
#     },
#     "schema3": {
#         "subcriber_name": "Subcriber_ID",
#         "emr_name": "EMR_ID",
#         "report_type": "Report_type",
#         "mapping": {
#             "patient_id": "Patient_ID",
#             "patient_last_name": "Patient_L_Name",
#             "patient_first_name": "Patient_F_Name",
#             "patient_gender": "Patient_Gender",
#             "dob": "Date_of_Birth",
#             "date_of_service": "Date_Of_Service",
#             "doctor_first_name": "Dr_FName",
#             "doctor_last_name": "Dr_LName",
#             "hospital_name": "Hosp_Name",
#             "insurance_category": "Ins_Cat",
#             "insurance_company": "INS_Comp",
#             "fpt_place_of_service_code": "fpt_placeofservicecode",
#             "fpt_type_of_service": "fpt_typeofservice",
#             "fpt_type_of_visit": "fpt_typeofvisit",
#             "chief_complient_hpi": "cc",
#             "history": "HPI",
#             "past_medical_history": "Past Medical History",
#             "assessment": "Assessment",
#             "ros": "ros",
#             "plan": "Plan",
#             "procedure": "Treatment",
#             "pdf_file_url": "File_name"
 
#         },
#         "derived": {
#             "pre_op_diagnosis": ["cc", "HPI", "Assessment", "Treatment", "Plan"]
#         }
#     },
#     "schema4": {
#         "subcriber_name": "subscriber_name",
#         "emr_name": "emr_name",
#         "report_type": "report_type_name",
#         "mapping": {
#             "claim_id": "claim_id",
#             "chart_record_id": "chart_record_id",
#             "patient_id": "patient_id",
#             "patient_first_name": "patient_first_name",
#             "patient_middle_name": "patient_middle_name",
#             "patient_last_name": "patient_last_name",
#             "patient_gender": "patient_gender",
#             "dob": "dob",
#             "insurance_category": "insurance_category",
#             "insurance_company": "insurance_company",
#             "doctor_first_name": "doctor_first_name",
#             "doctor_last_name": "doctor_last_name",
#             "hospital_name": "hospital_name",
#             "date_of_service": "date_of_service",
#             "time_in": "time_in",
#             "time_out": "time_out",
#             "chief_complient_hpi": "chief_complient_hpi",
#             "history": "history",
#             "health_concerns": "health_concerns",
#             "active_condition_problems": "active_condition_problems",
#             "assessment": "assessment",
#             "clinical_impression": "clinical_impression",
#             "diagnosis": "diagnosis",
#             "ros": "ros",
#             "physical_exam": "physical_exam",
#             "test_and_orders": "test_and_orders",
#             "summary_recommendations": "summary_recommendations",
#             "procedure": "procedure",
#             "plan": "plan",
#             "fpt_place_of_service_code": "fpt_place_of_service_code",
#             "fpt_type_of_service": "fpt_type_of_service",
#             "fpt_type_of_visit": "fpt_type_of_visit",
#             "pdf_file_url": "File_name"
 
#         }
#     }
# }
# def move_file_to_processed(file_id, file_name):
#     """Move processed file to 'Daily Import/processed' folder in OneDrive."""
#     access_token = get_onedrive_token()
#     headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
 
#     # First, ensure the 'processed' folder exists
#     processed_url = f"https://graph.microsoft.com/v1.0/users/{user_email}/drive/root:/{folder_path}/processed"
#     resp = requests.get(processed_url, headers=headers)
    
#     if resp.status_code == 404:  # Folder does not exist, create it
#         create_folder_url = f"https://graph.microsoft.com/v1.0/users/{user_email}/drive/root:/{folder_path}:/children"
#         folder_body = {"name": "processed", "folder": {}, "@microsoft.graph.conflictBehavior": "replace"}
#         requests.post(create_folder_url, headers=headers, json=folder_body)
 
#     # Move the file
#     move_url = f"https://graph.microsoft.com/v1.0/users/{user_email}/drive/items/{file_id}"
#     move_body = {
#         "parentReference": {
#             "path": f"/drive/root:/{folder_path}/processed"
#         },
#         "name": file_name
#     }
#     move_resp = requests.patch(move_url, headers=headers, json=move_body)
 
#     if move_resp.status_code in [200, 201]:
#         log(f"📂 File {file_name} moved to 'processed' folder.")
#     else:
#         log(f"❌ Failed to move {file_name}: {move_resp.status_code} - {move_resp.text}")
 
# # ============================
# # MAIN SCRIPT
# # ============================
 
# def main():
#     log("Authenticating with Medicodio...")
#     auth_response = requests.post(auth_url, json=auth_payload)
#     auth_json = auth_response.json()
#     try:
#         access_token = auth_json["data"]["access_token"]
#         headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
#         log("✅ Authentication successful")
#     except KeyError:
#         log("❌ Authentication failed")
#         send_email("Processing Failed", f"Auth error:\n{json.dumps(auth_json, indent=2)}")
#         return
 
#     files_info = list_onedrive_files()
#     excel_files = [f for f in files_info if f["name"].endswith(".xlsx")]
 
#     if not excel_files:
#         log("No Excel files found in OneDrive folder.")
#         return
 
#     for f in excel_files:
#         file_name = f["name"]
#         file_id = f["id"]
#         log(f"Downloading {file_name}...")
#         local_path = download_file(file_id, file_name)
 
#         try:
#             df = pd.read_excel(local_path)
#             schema = None
#             for s in SCHEMAS.values():
#                 if all(col in df.columns for col in s["mapping"].values()):
#                     schema = s
#                     break
#             if not schema:
#                 raise Exception("No matching schema found")
 
#             charts = []
#             for _, row in df.iterrows():
#                 chart = {
#                     "subcriber_name": safe_get(row, schema["subcriber_name"]),
#                     "emr_name": safe_get(row, schema["emr_name"]),
#                     "report_type": safe_get(row, schema["report_type"]),
#                     "time_in": "00:00",
#                     "time_out": "00:00",
#                     "main_chart": "true",
#                     "pdf_file_url": ""
#                 }
#                 for payload_field, excel_col in schema["mapping"].items():
#                     chart[payload_field] = safe_get(row, excel_col)
#                 for field, cols in schema.get("derived", {}).items():
#                     chart[field] = " | ".join(
#                         [safe_get(row, c) for c in cols if safe_get(row, c) != "no information found"]
#                     ) or "no information found"
#                 charts.append(chart)
 
#             num_chunks = math.ceil(len(charts) / chunk_size)
#             for i in range(num_chunks):
#                 chunk = charts[i*chunk_size:(i+1)*chunk_size]
#                 log(f"Sending chunk {i+1}/{num_chunks} with {len(chunk)} records...")
#                 resp = requests.post(create_url, headers=headers, json={"charts": chunk})
#                 if resp.status_code == 200:
#                     log(f"✅ Chunk {i+1} processed successfully")
#                 else:
#                     log(f"❌ Chunk {i+1} failed: {resp.status_code}")
#                     log(resp.text)
#                     send_email("API Processing Failed", f"File: {file_name}\nChunk {i+1} failed with status {resp.status_code}\nAPI Response:\n{resp.text}")
 
#             if resp.status_code == 200:
#                 send_email("Processing Completed", f"File {file_name} processed successfully with {len(charts)} records.")
#             move_file_to_processed(file_id, file_name)
 
 
#         except Exception as e:
#             log(f"❌ Error processing {file_name}: {e}")
#             send_email("Processing Failed", f"Error processing {file_name}:\n{e}")
 
# if __name__ == "__main__":
#     log("Starting OneDrive folder polling...")
#     import time
 
#     POLL_INTERVAL = 300  # seconds, i.e., 5 minutes
 
#     while True:
#         try:
#             main()  # Process any new files
#         except Exception as e:
#             log(f"❌ Unexpected error during polling: {e}")
#         log(f"Waiting {POLL_INTERVAL} seconds before next check...")
#         time.sleep(POLL_INTERVAL)
