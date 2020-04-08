from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template

from .utils import render_to_pdf

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Copper",
            "amount": 1399.99,
            "today":"Today"
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html',context)

        if pdf:
            response = HttpResponse(pdf,content_type='application/pdf')
            filename = "Invoice_%s.pdf"%("12345123")
            content = "inline; filename=%s"%(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not Found")



# def generate_view(request, *args, **kwargs):
#     template = get_template('invoice.html')
#     context = {
#         "invoice_id": 123,
#         "customer_name": "John Copper",
#             "amount": 1399.99,
#         "today":"Today"
#         }
#     html = template.render(context)
#     return HttpResponse