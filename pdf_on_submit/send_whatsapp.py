from frappe.utils import get_url
import requests
import frappe
def send_whatsapp(doc,method=None):
    customer=frappe.get_doc("Customer",doc.customer)
    whatsapp_settings=frappe.get_doc("Whatsapp Setting")
    if not whatsapp_settings.disable:
        document_url="https://business.tpf.deom.com.sa/files/{}.pdf".format(doc.name)
        url = "https://api.4whats.net/sendFile/"
        querystring = {"instanceid":whatsapp_settings.instance_id,"token":whatsapp_settings.token,"phone":customer.mobile_no,"body":document_url,"filename":doc.name,"caption":whatsapp_settings.caption}
        response = requests.request("GET", url, params=querystring)
        json_response=frappe.parse_json(response.content.decode())
        print("********************")
        print(response.text)
        doc_log = frappe.get_doc({
                'doctype': 'Whatsapp Log',
                "log":response.text,
                "doctype_name":doc.name,
                "status":json_response["sent"]})
        doc_log.insert()

