from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from xhtml2pdf import pisa
from django.core import mail
def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        email = EmailMessage('Hello', 'Body', 'moversandpackers230@gmail.com', [context_dict['email']])
        email.attach('Recipt.pdf', result.getvalue() , 'application/pdf')
        email.send()
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
