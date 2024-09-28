import pdfplumber
import dateparser
import datetime

def extract_all_tables(pdf_path):
  """Extracts all tables from a PDF.

  Args:
    pdf_path: Path to the PDF file.

  Returns:
    A list of lists of lists, where each inner list represents a table.
  """

  with pdfplumber.open(pdf_path) as pdf:
    all_tables = []
    for page_num, page in enumerate(pdf.pages):
      tables = page.extract_tables()
      if tables:
        all_tables.extend(tables)
      else:
        print(f"No tables found on page {page_num + 1}")

    return all_tables

def flatten(matrix):
    """Single Layer Flatten"""
    return [item for row in matrix for item in row]

def fixup_tables(table):
  """Fixes The table count and format
  
    Required because region is split to another page
    We don't need region so we remove it, and we also remove the header
  """
  return table[1:1594] # 1594 is when region starts

def filter_tarlac(table):
  """Filters for Tarlac-based Poultry Farms"""
  new_list = []
  
  for row in table:
    business_addr = row[3]

    business_addr_list = business_addr.split(",")
    business_addr_city = business_addr_list[-1].strip().lower()

    if business_addr_city == "tarlac":
      new_list.append(row)

  return new_list

def filter_valid(table):
  """Filters for valid poultry farms as of `now`"""
  new_list = []

  for row in table:
    valid_date = row[6]
    date = dateparser.parse(valid_date)
    today = datetime.datetime.now()

    if date > today:
      new_list.append(row)

  return new_list


if __name__ == "__main__":
  print("Reading and Parsing...")
  tables_per_page = extract_all_tables("../data/data.pdf")

  print("Flattening...")
  tables_whole = flatten(tables_per_page)

  print("List Fixup...")
  tables_fixed = fixup_tables(tables_whole)
  print("Total Farms: " + str(len(tables_fixed)))

  tables_tarlac = filter_tarlac(tables_fixed)
  print("Tarlac Farms: " + str(len(tables_tarlac)))

  tables_valid = filter_valid(tables_tarlac)
  print("Valid Tarlac Farms as of " + str(datetime.datetime.now()) + " : "  + str(len(tables_valid)))

