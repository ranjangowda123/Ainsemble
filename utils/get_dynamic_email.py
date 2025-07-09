# import os.path
#
#
# def get_email():
#     base_path = os.path.dirname(__file__)
#     file_path  = os.path.join(base_path,"counter.txt")
#     # count = None
#     try:
#         with open(file_path, "r") as f:    # It tries to open a file named counter.txt in read ("r") mode.
#             count = int(f.read().strip())     # reads the whole content of the file (which should be a number like "112").
#     except (FileNotFoundError , ValueError):                 #  removes any extra spaces or newline characters.
#         count = 199                          #  converts that string to an integer.
#                                               # If counter.txt doesn’t exist, Python throws a FileNotFoundError.                                       # In that case, you start count at 115.
#     count+=1
#     print("Current count:", count)
#
#     with open(file_path, "w") as f:
#         f.write(str(count))               # f.write() only accepts strings.
#
#     return count
