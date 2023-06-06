
# # importing required package
# import linecache
  
# # extracting the 5th line

# filenumber=0
# start=2
# ##39325
# while(start<39325):
#     with open(f"./1/{filenumber}.json","a+") as file:
#         file.write("[")
#         filestart=start
#         fileend=0
#         i=filestart

#         while(fileend<5):
#             particular_line = linecache.getline('1.JSON', start)
#             for j in particular_line:
#                 if j=='}':
#                     fileend=fileend+1

#             if fileend==5:
#                 file.write("}")
#             else:
#                 file.write(particular_line)

#             start=start+1

#         file.write("]")
#         # start=fileend
#     filenumber=filenumber+1

  
