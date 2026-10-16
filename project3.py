# part 1: Ask the students for their info
name = input("Enter your name, Student: ")
book = input("Enter your favorite book: ")

# part 2: store the students info by different data types
student_number = 10
school_rating = 4
height_m = 1.45
is_present = True
Grade_level = 6

# part 3: Print each detail with its data type
print("Name:", name, "-> type:", type(name))
print("Book:", book,"-> type:", type(book))
print("student number", student_number, "-> type:", type(student_number))
print("school rating", school_rating, "-> type:", type(school_rating))
print("height (in meters)", height_m, "-> type:", type(height_m))
print("is present", is_present,"-> type:", type(is_present))
print("Grade", Grade_level, "-> type:", type(Grade_level))

# part 4: Typecast the numbers and the true/false value into strings
student_number_text = str(student_number)
school_rating_text = str(school_rating)
status_text = str(is_present)
Grade_level_text = str(Grade_level)

print("student number as text", student_number_text,"-> type", type(student_number_text))
print("school rating as text", school_rating_text, "-> type", type(school_rating_text))
print("status as text", status_text, "-> type", type(status_text))
print("grade level as text", Grade_level_text, "-> type", type(Grade_level_text))

# Part 5: Slice the name to make a nickname
first_three = name[0:3]
last_letter = name[-1:]
nickname = first_three + last_letter
print("First 3 letters of name:", first_three)
print("Last letter of name:", last_letter)
print("nickname:",nickname )

# part 6: Reverse the book name using slicing
reversed_book = book[::-1]
print("reversed book name:", reversed_book)

# Part 7: Join everything together to build the final badge message
badge_line_1 = "STUDENT " + nickname.upper()
badge_line_2 = "ID:" + student_number_text + " | STUDENT NUMBER" + student_number_text
badge_line_3 = "SCHOOL RATING:" + school_rating_text + " | STATUS" + status_text
badge_line_4 = "Reverse book code" + reversed_book.upper()

# Part 8: print the complete ID
print("")
print("=====STUDENT ID=====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("====================")