from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

def generate_invoice_pdf(order):

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph(f"Invoice - {order.order_number}", styles['Title']))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(f"Name: {order.full_name}", styles['Normal']))
    elements.append(Paragraph(f"Email: {order.email}", styles['Normal']))
    elements.append(Paragraph(f"Address: {order.full_address}", styles['Normal']))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(f"Total: ₹{order.order_total}", styles['Normal']))

    doc.build(elements)

    pdf = buffer.getvalue()
    buffer.close()

    return pdf