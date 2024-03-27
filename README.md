<h1>PyWhatKit Message Scheduler</h1>

<p>This Python script utilizes the PyWhatKit library to schedule and send messages on WhatsApp. It prompts the user to input the time (in 24-hour format), the recipient's phone number with the country code, and the message to be sent. The message is then delivered to the specified recipient at the specified time.</p>

<h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li>PyWhatKit library (<code>pip install pywhatkit</code>)</li>
    </ul>

<h2>Usage</h2>
    <ol>
        <li>Run the script in a Python environment.</li>
        <li>Enter the required details:
            <ul>
                <li>Hours in 24-hour format.</li>
                <li>Minutes in 24-hour format.</li>
                <li>Phone number of the recipient with the country code.</li>
                <li>The message you want to send.</li>
            </ul>
        </li>
        <li>The message will be sent at the specified time.</li>
    </ol>

<h2>Code Explanation</h2>
    <ul>
        <li><code>import pywhatkit as pyw</code>: Imports the PyWhatKit library.</li>
        <li><code>hrs = input("Enter hours in 24 hours format: ")</code>: Prompts the user to enter the hours in 24-hour format.</li>
        <li><code>mins = input("Enter mins in 24 hours format: ")</code>: Prompts the user to enter the minutes in 24-hour format.</li>
        <li><code>phone_number = input("Enter the phone number with country code: ")</code>: Prompts the user to enter the recipient's phone number with the country code.</li>
        <li><code>msg = input("Type the message you want to send--- \n")</code>: Prompts the user to enter the message to be sent.</li>
        <li><code>pyw.sendwhatmsg(phone_no=phone_number, message=msg, time_hour=int(hrs), time_min=int(mins))</code>: Utilizes PyWhatKit to send the message. It takes the phone number, message, hours, and minutes as arguments to schedule the message.</li>
    </ul>

<h2>Note</h2>
    <ul>
        <li>Ensure the recipient's phone number is accurate and includes the country code.</li>
        <li>The script sends messages through WhatsApp, so make sure you have a working internet connection and WhatsApp installed on your device.</li>
        <li>It's recommended to run the script on a device where WhatsApp Web is already logged in for smooth execution.</li>
    </ul>
