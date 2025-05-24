# 📦 Importing required libraries
import os  # For checking and creating folders
from fpdf import FPDF  # For creating PDF files
import matplotlib.pyplot as plt  # For drawing charts
import pandas as pd  # For working with tabular data
from datetime import datetime  # For working with dates and times

# 📄 Step 1: Reading and processing data from a text file
def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        data = [line.strip().split(', ') for line in lines]  # Splitting each line into parts
    df = pd.DataFrame(data, columns=["Employee", "Project", "Hours"])  # Making a table with column names
    df["Hours"] = pd.to_numeric(df["Hours"])  # Converting hours from text to numbers
    return df

# 🔢 Creating a summary table showing total hours for each employee and project
def create_summary(df):
    pivot = df.pivot_table(index="Employee", columns="Project", values="Hours", aggfunc="sum", fill_value=0)
    pivot["Total"] = pivot.sum(axis=1)  # Adding a column to show total hours per employee
    return pivot

# 📊 Step 2: Drawing charts to visualize the data
def generate_charts(df):
    os.makedirs("charts", exist_ok=True)  # Making a folder to save charts if it doesn't exist

    # 📊 Drawing a bar chart: Hours per employee per project
    summary = df.pivot_table(index="Employee", columns="Project", values="Hours", aggfunc="sum", fill_value=0)
    ax = summary.plot(kind="bar", color=["#AEC6CF", "#FFB347", "#77DD77"], figsize=(8,4))
    ax.set_ylabel("Hours")
    ax.set_title("Hours Worked by Each Employee per Project")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("charts/bar_chart.png", bbox_inches='tight')  # Saving the bar chart as an image
    plt.close()

    # 🥧 Drawing a pie chart: Total hours by employee
    total = df.groupby("Employee")["Hours"].sum()
    plt.figure(figsize=(6,6))
    colors = ["#FFB347", "#AEC6CF", "#77DD77"]
    plt.pie(total, labels=total.index, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.title("Total Hours Contribution by Employee")
    plt.tight_layout()
    plt.savefig("charts/pie_chart.png", bbox_inches='tight')  # Saving the pie chart as an image
    plt.close()

# 📄 Step 3: Creating the PDF report
class PDF(FPDF):
    # 🖨️ Adding page numbers at the bottom of each page
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, 'C')

# 🧾 Creating the final PDF with charts and summary table
def create_pdf(summary):
    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=True, margin=15)

    # 📄 Page 1: Adding title and summary table
    pdf.add_page()
    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 10, "Guru Design & Drafting Services", ln=True, align='C')
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Project Time Tracking Summary", ln=True, align='C')
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')
    pdf.ln(6)

    # 🧮 Adding summary table to PDF
    pdf.set_font("Arial", "B", 9)
    col_width = pdf.w / (len(summary.columns) + 1.5)
    pdf.cell(col_width, 8, "Employee", 1, align='C')
    for col in summary.columns:
        pdf.cell(col_width, 8, col, 1, align='C')
    pdf.ln()
    pdf.set_font("Arial", "", 9)
    for idx, row in summary.iterrows():
        pdf.cell(col_width, 8, idx, 1, align='C')
        for val in row:
            pdf.cell(col_width, 8, str(val), 1, align='C')
        pdf.ln()

    # 🖼️ Adding bar chart image on the first page
    chart_height = pdf.h / 3
    y_position = pdf.h / 2
    pdf.set_y(y_position - 12)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Hours Worked by Each Employee per Project (Bar Chart)", ln=True, align='C')
    pdf.image("charts/bar_chart.png", x=20, y=y_position, w=pdf.w - 40, h=chart_height)

    # 📄 Page 2: Adding pie chart
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Total Hours Contribution by Employee (Pie Chart)", ln=True, align='C')
    pdf.image("charts/pie_chart.png", x=pdf.w * 0.2, w=pdf.w * 0.6)

    # 💾 Saving the final PDF report
    pdf.output("Employee_Project_Summary_Report.pdf")

# 🚀 Running everything if the script is executed directly
if __name__ == "__main__":
    filename = "project_time_log.txt"
    if not os.path.exists(filename):
        print(f"❌ Data file '{filename}' not found. Please create the file with your data.")
    else:
        df = read_data(filename)          # Reading the data from the file
        summary = create_summary(df)      # Creating summary table
        generate_charts(df)               # Drawing charts
        create_pdf(summary)               # Making the PDF report
        print("\n✅ Report generated: Employee_Project_Summary_Report.pdf")