from frappe.utils import get_url
import requests
import frappe
def send_whatsapp(doc,method=None):
    customer=frappe.get_doc("Customer",doc.customer)
    whatsapp_settings=frappe.get_doc("Whatsapp Setting")
    document_url="https://business.tpf.deom.com.sa/files/{}.pdf".format(doc.name)
    print("$$$$$$$$$$$document_url$$$$$$$$$$$")
    print(document_url)
    url = "https://api.4whats.net/sendFile/"
    querystring = {"instanceid":whatsapp_settings.instance_id,"token":whatsapp_settings.token,"phone":customer.mobile_no,"body":document_url,"filename":doc.name,"caption":whatsapp_settings.caption}
    response = requests.request("GET", url, params=querystring)
    print("********************")
    print(response.text)

