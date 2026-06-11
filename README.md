# Marry-Here
Website that helps you to organize the most important day of your life

![Couple-support](https://github.com/user-attachments/assets/2b8b44b8-5ccd-42c2-93f1-f53cedc72d05)


### Wedding Gift Registry System

A Django web application for managing wedding gifts and guest lists. Couples build a gift registry and manage guests in one place. Each guest gets a tokenized invitation link where they can confirm attendance and reserve a gift.

## What it does (10-second version)

- The couple adds gifts (name, photo, price, significance 1 to 5) at `/groom/` and registers guests at `/groom/guests_list`.
- Each guest receives a unique link, `/guests/?token=...`, where they confirm or refuse attendance and reserve one of the available gifts.
- The home page shows a Chart.js pie of reserved vs. available gifts, and gifts are color-coded by significance.

## Important Note
This is an MVP (Minimum Viable Product), built as part of the "4 Days 4 Projects" initiative by [Pythonando](https://pythonando.com.br) on YouTube. The token in the invitation link is the only access control, so treat the URLs as shareable secrets and do not put real personal data in a public deployment.

### Pending Features
The following are intentionally not implemented yet:
- WhatsApp integration (the WhatsApp field is currently stored and shown as plain text only).
- Guest companion management (the "Add your companions" form on the guest page has no backing logic yet; the companion list is a static placeholder).
- Login and password authentication.
- Access control for the couple's admin pages beyond Django admin.
- Gift-guest relationship validation and confirmation authorization.

## Features

### Gift Registry
- Create and manage gift wishlists
- Upload gift photos
- Set gift prices and significance levels
- Track reserved and available gifts
- Visual representation of gift reservation status through charts
- Color-coded significance indicators for gifts

### Guest Management
- Register and track wedding guests
- Generate a unique tokenized invitation link for each guest
- Track guest confirmation status
- Store a WhatsApp number per guest (displayed as text)
- Status tracking (Waiting for confirmation, Confirmed, Refused)

## Technology Stack

- **Backend Framework:** Django
- **Frontend:** HTML, Tailwind CSS
- **JavaScript Libraries:** Chart.js
- **Database:** Django ORM (Default: SQLite)
- **Image Handling:** Django's ImageField

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Caio-Felice-Cunha/Marry-Here.git
cd Marry-Here
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. (Optional) Load demo data: 10 sample gifts and 10 sample guests.
```bash
python manage.py loaddata demo
```

6. Create an admin account to use Django admin at `/admin/`:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

### Configuration

The app runs with safe development defaults and needs no `.env` file locally. For any non-local deployment, copy `.env.example` to `.env` and set the values (`DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`, `DJANGO_ALLOWED_HOSTS`, `SITE_URL`). These are read in `core/settings.py`. `SITE_URL` is the base used to build the absolute invitation links shown on the guest list.

### URLs

| Path | Purpose |
| --- | --- |
| `/` | Redirects to `/groom/` |
| `/groom/` | Add gifts, view the reservation chart |
| `/groom/guests_list` | Register guests, see invitation links and statuses |
| `/guests/?token=<token>` | Guest page: confirm/refuse attendance, reserve a gift |
| `/admin/` | Django admin (requires a superuser) |

## Project Structure

### Models

#### Guests
- `guest_name`: Guest's full name
- `whatsapp`: WhatsApp contact number
- `maximum_companions`: Number of allowed companions
- `token`: Unique token for invitation link
- `status`: Guest confirmation status (WFC/C/R)

#### Gifts
- `gift_name`: Name of the gift
- `photo`: Gift image
- `price`: Estimated price
- `significance`: Importance level (1-5)
- `reserved`: Reservation status
- `reserved_by`: Link to guest who reserved the gift

## Usage

### Adding Gifts
1. Go to `/groom/` (the root URL redirects there)
2. Fill in the gift details form:
   - Gift name
   - Upload a photo
   - Set estimated price
   - Set significance level (1-5)
3. Submit the form to add the gift to the registry

### Managing Guests
1. Go to `/groom/guests_list`
2. Add new guests with their details:
   - Guest name
   - WhatsApp number
   - Maximum number of companions
3. Track guest responses through the status indicators

## Frontend Features

### Gift Display
- Grid layout for gifts
- Visual significance indicators:
  - Green: Not very important (≤ 2)
  - Orange: Important (3)
  - Red: Very Important (≥ 4)
- Pie chart showing reserved vs available gifts

### Guest List
- Clean list view of all guests
- Status indicators for guest responses
- Unique invitation link for each guest
- Profile picture placeholder

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Testing

Run the test suite (15 tests covering the views, models, and the invitation flow):
```bash
python manage.py test
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Credits

This project was developed as part of the "4 Days 4 Projects" initiative by [Pythonando](https://pythonando.com.br) on YouTube. Special thanks to the Pythonando team for providing the project structure and guidance.

## Acknowledgments

- Built with Django web framework
- Styled with Tailwind CSS
- Charts powered by Chart.js
