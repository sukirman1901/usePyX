from pyx.ui import UI, PyxElement
from components.layout import docs_layout
from components.ui_helpers import make_code_block

def feedback_page():
    content = UI.div()
    
    # Breadcrumb
    content.add(UI.div().flex().gap(2).mb(4).add(UI.a("UI", "/docs/ui/overview").text("sm").text("gray-400")).add(UI.span("›").text("gray-400")).add(UI.span("Feedback").text("sm").font("medium").text("gray-900")))
    
    content.add(UI.h1("Feedback").text("3xl").font("extrabold").text("gray-900").mb(6))
    content.add(UI.p("Communicate status and feedback to your users.").text("lg").text("gray-600").mb(8))

    # Alert Example
    content.add(UI.h3("Alerts").text("xl").font("bold").mb(2))
    
    alert_info = UI.div().cls("bg-blue-50 border-l-4 border-blue-500 p-4 mb-4 text-blue-700")
    alert_info.add(PyxElement("p").add("Info: This is an informational alert.").font("medium"))
    content.add(alert_info)
    
    alert_error = UI.div().cls("bg-red-50 border-l-4 border-red-500 p-4 mb-6 text-red-700")
    alert_error.add(PyxElement("p").add("Error: Something went wrong!").font("medium"))
    content.add(alert_error)

    content.add(make_code_block('ui.div().cls("bg-blue-50 border-l-4 border-blue-500 p-4")'))

    # Spinner (CSS mock)
    content.add(UI.h3("Spinners").text("xl").cls("font-bold").mt(8).mb(2))
    spinner = UI.div().cls("animate-spin h-8 w-8 border-4 border-blue-500 rounded-full border-t-transparent mb-6")
    content.add(spinner)
    content.add(make_code_block('ui.div().cls("animate-spin h-8 w-8 border-4 border-blue-500 rounded-full border-t-transparent")'))


    # Toast
    content.add(UI.h3("Toast").text("xl").cls("font-bold").mt(8).mb(2))
    content.add(UI.p("Transient notifications that appear temporarily.").text("gray-600").mb(4))
    
    toast = UI.div().cls("flex items-center w-full max-w-xs p-4 space-x-4 text-gray-500 bg-white divide-x divide-gray-200 rounded-lg shadow space-x mb-4")
    toast.add(PyxElement("i").attr("data-lucide", "check-circle").cls("text-green-500 w-5 h-5"))
    toast.add(UI.div("Item moved successfully.").cls("ps-4 text-sm font-normal"))
    content.add(toast)
    
    content.add(make_code_block('ui.toast("Success!")'))
    
    return docs_layout(content, active_nav_item="Feedback")
