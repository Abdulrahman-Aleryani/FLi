import frappe

sitemap = 1

def get_context(context):
    try:
        context.doc = frappe.get_cached_doc("About Us Settings")
        if context.doc.is_disabled:
            frappe.local.flags.redirect_location = "/404"
            raise frappe.Redirect
    except frappe.DoesNotExistError:
        context.doc = frappe._dict({
            "page_title": "About Us",
            "company_introduction": None,
            "is_disabled": False
        })
    return context
