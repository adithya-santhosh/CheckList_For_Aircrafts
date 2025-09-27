# ✈️ Aviation Tool - Flight Deck

A full-stack web application designed for aviation enthusiasts and pilots to generate pre-flight checklists and browse airline fleet information. This project is built with Flask and demonstrates a range of web development skills, from backend data handling to creating a dynamic, interactive frontend with a video background.

***

## 📸 Screenshots

Here’s a look at the application in action.

*(**Note**: Replace these with your actual screenshots. It's recommended to create a `screenshots` folder in your project to store them.)*

| Login Page | Dashboard |
| :---: | :---: |
| ![Alt text](Screenshots\userlogin.png) | ![Alt text](Screenshots\dashboard.png) |
| **_Figure 1:_** _The secure login portal._ | **_Figure 2:_** _The dynamic video dashboard._ |

| Checklist Generator | Airline Browser |
| :---: | :---: |
| ![Alt text](Screenshots\cheecklist.png)  | ![Alt text](Screenshots\Airline_partner.png)  |
| **_Figure 3:_** _Interactive checklist selection._ | **_Figure 4:_** _Browsing airline fleets._ |


***

## ✨ Key Features

* **Secure Login System**: A simulated but functional user login and session management system.
* **Dynamic Video Dashboard**: A visually engaging dashboard with a fullscreen video background.
* **External Data Integration**: Checklists are loaded dynamically from an external Excel file using the Pandas library, making them easy to update.
* **Interactive Checklist Generator**: Users can select an aircraft to view its specific pre-flight checklist, complete with interactive checkboxes.
* **Airline Fleet Browser**: A section to view collaborated airlines and the types of aircraft they operate.
* **Responsive Design**: The UI is built with Bootstrap 5, ensuring it works seamlessly on both desktop and mobile devices.

***

## 🛠️ Technologies Used

* **Backend**:
    * Python 3
    * Flask (for the web server and routing)
    * Pandas (for reading data from the Excel file)
* **Frontend**:
    * HTML5
    * CSS3
    * Bootstrap 5 (for components and layout)
    * jQuery (for interactive elements)
* **Development**:
    * Git & GitHub (for version control)

***

## 🚀 Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/aviation-checklist.git](https://github.com/your-username/aviation-checklist.git)
    cd aviation-checklist
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Prepare the data and assets:**
    * Ensure you have a `checklists.xlsx` file in the root directory with the correct column headers (`Aircraft`, `Checklist Item`, `Action`, `ImageFile`).
    * Place all necessary images (logos, planes) in the `static/images/` folder.
    * Place your background video in the `static/videos/` folder and ensure it's named `background_video.mp4`.

5.  **Run the application:**
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:5000`.

***

## 📋 Demo Steps

1.  **Login**:
    * Navigate to the homepage. You will be redirected to the login page.
    * Enter the credentials:
        * **Username**: `admin`
        * **Password**: `password123`
    * Click "Login".

2.  **Explore the Dashboard**:
    * You will land on the main dashboard with a video background.
    * From here, you can choose to either "Open Checklists" or "Browse Airlines".

3.  **Generate a Checklist**:
    * Click on **"Open Checklists"**.
    * Select an aircraft (e.g., "Cessna 172") from the dropdown menu. An image of the selected plane will appear.
    * Click **"Generate Checklist"**.
    * On the results page, you can interact with the checklist by clicking the checkboxes to mark items as complete.

4.  **Browse Airlines**:
    * Navigate back to the dashboard or use the navbar to go to the "Airlines" page.
    * Here you will see a list of partner airlines.
    * Click on **"View Fleet"** for any airline to see a list of the aircraft they operate, along with images.
