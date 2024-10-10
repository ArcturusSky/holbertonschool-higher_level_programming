# CSV Mini-Course

## 1. Introduction to CSV

**CSV (Comma-Separated Values)** is a simple file format used to store tabular data, such as a spreadsheet or database. Each line in a CSV file corresponds to a row in the table, and each value within that line is separated by a comma, representing a column.

### Why Use CSV?
- **Simplicity**: Easy to read and write, both for humans and machines.
- **Compatibility**: Supported by many applications, including Excel, Google Sheets, and various programming languages.
- **Lightweight**: Minimal overhead compared to other formats like JSON or XML.

---

## 2. CSV Structure

A typical CSV file looks like this:

```python
id,title,body
1,First Post,This is the body of the first post.
2,Second Post,This is the body of the second post.
3,Third Post,This is the body of the third post.
```

- **Header Row**: The first line often contains column names (`id`, `title`, `body`).
- **Data Rows**: Each subsequent line contains data corresponding to the headers.

**Important Points:**
- **Delimiter**: While commas are standard, other delimiters like semicolons or tabs can be used.
- **Quoting**: If a field contains a comma, it can be enclosed in quotes to avoid confusion.
- **Newlines**: Each row is separated by a newline character.

---

## 3. Working with CSV in Python

Python provides a built-in `csv` module to handle CSV files efficiently.

### a. Reading CSV Files

To read data from a CSV file, you can use `csv.reader` or `csv.DictReader`.

**Using `csv.reader`:**

```python
import csv

with open('posts.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Skip header row
    for row in reader:
        print(row)  # Each row is a list
```

**Using `csv.DictReader`:**

```python
import csv

with open('posts.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['title'])  # Access by column name
```

**Advantages of `DictReader`:**
- Access data by column names, making the code more readable.
- Automatically uses the first row as headers.

### b. Writing CSV Files

To write data to a CSV file, use `csv.writer` or `csv.DictWriter`.

**Using `csv.writer`:**

```python
import csv

posts = [
    [1, "First Post", "This is the body of the first post."],
    [2, "Second Post", "This is the body of the second post."],
    [3, "Third Post", "This is the body of the third post."]
]

with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "title", "body"])  # Write header
    writer.writerows(posts)  # Write multiple rows
```

**Using `csv.DictWriter`:**

```python
import csv

posts = [
    {"id": 1, "title": "First Post", "body": "This is the body of the first post."},
    {"id": 2, "title": "Second Post", "body": "This is the body of the second post."},
    {"id": 3, "title": "Third Post", "body": "This is the body of the third post."}
]

with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ["id", "title", "body"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Write header
    writer.writerows(posts)  # Write multiple rows
```

**Advantages of `DictWriter`:**
- Clear mapping between data and columns using dictionaries.
- Automatically handles the order of columns based on `fieldnames`.

### c. Handling Special Cases

- **Different Delimiters:**

```python
import csv

with open('posts.tsv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(["id", "title", "body"])
    writer.writerow([1, "First Post", "This is the body of the first post."])
```

- **Quoting Fields:**

```python
import csv

with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(["id", "title", "body"])
    writer.writerow([1, "First, Post", "This is the body of the first post."])
```

---

## 4. Example: Fetching API Data and Saving to CSV

Building on your project task, here’s a complete example that fetches posts from JSONPlaceholder and saves them to a CSV file.

```python
import requests
import csv

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        posts = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in data]

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts)
        print("Posts have been saved to posts.csv")
    else:
        print("Failed to retrieve posts.")

if __name__ == "__main__":
    fetch_and_save_posts()
```

**Explanation:**
1. **Fetch Data:** Use `requests.get()` to retrieve posts from the API.
2. **Check Response:** Ensure the request was successful by checking `status_code`.
3. **Parse JSON:** Convert the response to JSON using `.json()`.
4. **Prepare Data:** Create a list of dictionaries containing only the necessary fields (`id`, `title`, `body`).
5. **Write CSV:** Use `csv.DictWriter` to write the data to `posts.csv`.

---

## 5. Tips and Best Practices

- **Always Specify Encoding:** Use `encoding='utf-8'` to handle special characters.
- **Handle Exceptions:** Implement error handling to manage issues like network errors or file access problems.
  
```python
try:
    # Your code here
except Exception as e:
    print(f"An error occurred: {e}")
```
  
- **Use Context Managers:** Using `with open(...)` ensures files are properly closed after operations.
- **Validate Data:** Ensure the data you're writing matches the expected format to avoid CSV corruption.
- **Avoid Hardcoding:** Use variables or configurations for file paths and URLs to make your code more flexible.

---

## 6. Additional Resources

- **Python CSV Module Documentation:** [https://docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html)
- **Real Python CSV Tutorial:** [https://realpython.com/python-csv/](https://realpython.com/python-csv/)
- **CSVLint (Validate CSV Files):** [https://csvlint.io/](https://csvlint.io/)

