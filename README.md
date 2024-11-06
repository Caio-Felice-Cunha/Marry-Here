# Marry-Here
Website that helps you to organize the most important day of your life

![Couple-support](https://github.com/user-attachments/assets/2b8b44b8-5ccd-42c2-93f1-f53cedc72d05)


### Wedding Gift Registry System

A Django-based web application for managing wedding gifts and guest lists. This system allows couples to create a gift registry and manage their wedding guests in one place.

## Important Note
This is an MVP (Minimum Viable Product) version of the application, developed as part of the "4 Days 4 Projects" initiative by [Pythonando](https://pythonando.com.br) on YouTube.

### Pending Features
The following features are planned for future implementation:
- Token validation system
- Gift-guest relationship validation
- Gift confirmation authorization system
- Authentication system with login and password
- Access control for bride and groom pages
- Additional security measures

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
- Generate unique invitation links for each guest
- Track guest confirmation status
- Manage guest companions
- WhatsApp integration for guest communication
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
cd wedding-registry
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django
pip install Pillow  # For image handling
```

4. Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

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
1. Navigate to the home page
2. Fill in the gift details form:
   - Gift name
   - Upload a photo
   - Set estimated price
   - Set significance level (1-5)
3. Submit the form to add the gift to the registry

### Managing Guests
1. Access the guests section
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

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Credits

This project was developed as part of the "4 Days 4 Projects" initiative by [Pythonando](https://pythonando.com.br) on YouTube. Special thanks to the Pythonando team for providing the project structure and guidance.

## Acknowledgments

- Built with Django web framework
- Styled with Tailwind CSS
- Charts powered by Chart.js
