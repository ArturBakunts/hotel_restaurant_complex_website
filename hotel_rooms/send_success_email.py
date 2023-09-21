from django.core.mail import EmailMessage
from django.template.loader import get_template


def send_confirmation_email(email, name, check_in, check_out, room_type, options_for_room, price):
    subject = "BakArt Hotel Reservation Confirmation"

    email_template = get_template('hotel_rooms/send_conf_email.html')

    context = {
        'user_name': name,
        'check_in_date': check_in,
        'check_out_date': check_out,
        'room_type': room_type,
        'options_for_room': options_for_room,
        'price': price,
    }

    email_body = email_template.render(context)

    email = EmailMessage(subject, email_body, to=[email])
    email.content_subtype = 'html'

    try:
        email.send()
        return "The message was sent successfully!"
    except Exception as ex:
        print(f"Error sending email: {ex}")
        return "Failed to send email."
