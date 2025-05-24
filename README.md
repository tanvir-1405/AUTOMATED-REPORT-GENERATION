# AUTOMATED-REPORT-GENERATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: TANVIR KAUR KHOKHAR

*INTERN ID*: CT04DM1447

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

The second project I developed is an Automated Report Generation Tool that reads structured data from a plain text file, analyzes it, and converts it into a clean, well-formatted PDF report with visual graphs. This system is particularly helpful in environments where routine reports are needed based on simple data logs — for example, employee time tracking across multiple projects.

The core objective of this tool is to automate the reporting process. Instead of manually copying data, analyzing it, and formatting it into a report, the program reads a text file with time-tracking data, calculates project-wise hours, and generates a visual summary in a PDF. It streamlines repetitive tasks and helps organizations maintain consistency and accuracy in their reports.

The input file used is a normal text file, where each line contains information in the format: employee_name,project_name,hours

This format is easy to create, edit, and share, making it ideal for small teams, startups, or scenarios where spreadsheet software isn’t used.

The entire application is written in Python, focusing on accessibility and simplicity. Since the system doesn’t rely on heavy libraries like pandas, it can run on machines with minimal dependencies. Instead, Python’s built-in file handling and data structures like lists and dictionaries are used to parse and store the data from the text file.

For generating visuals, the project uses Matplotlib, one of the most popular charting libraries in Python. It is used to create bar charts or pie charts showing how much time each employee has spent on different projects. These graphs provide a quick visual understanding of workload distribution and help identify focus areas or imbalances in time spent.

The reporting aspect is handled using the FPDF library, which allows the creation of custom PDF documents. The program generates a full report that includes a title, summaries, total hours, individual charts, and even a timestamp. The design is kept clean and professional, with customizable fonts, spacing, and layouts. The report is automatically saved as a .pdf file, named after the current date or project context.

User interaction is minimal: the user simply places the text file in the working directory and runs the script. The program processes the text file line by line, validates the format, accumulates the data, creates visuals, and then writes the entire report into a PDF. If the file is missing or contains invalid lines, the program alerts the user with a message and continues gracefully.

This system is highly applicable in real-life scenarios. For instance:

Managers can use it to track and report how much time each team member is spending on ongoing projects.

Freelancers can use it to log and summarize time spent on various client jobs.

Educational institutions or training programs can track student or intern hours across assignments.

One of the key strengths of this project is that it requires no manual formatting or spreadsheet software, making it accessible to users in non-technical roles or teams with minimal digital tools. The ability to generate consistent, visual reports with just a text file and a script adds enormous value to time-tracking and documentation processes.

Overall, this project demonstrates how basic file handling, simple data logic, and visual storytelling can come together to automate a real-world task effectively. It reflects Python’s flexibility and the power of combining traditional text-based input with modern reporting tools to create smart, usable solutions.

#OUTPUT

![Image](https://github.com/user-attachments/assets/6576cffd-8ad3-45d8-857d-e2a88ba212f4)

![Image](https://github.com/user-attachments/assets/6457d0e7-6e06-46c0-b68f-2b82bf647e64)

![Image](https://github.com/user-attachments/assets/b3cc6fae-6fea-452d-978b-2ff2b6077121)
