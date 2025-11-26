from db_functions_manga import DB_Functions

test_class:DB_Functions = DB_Functions(db_file_name="template.db")

test_class.INIT_table_manga()

# for i in range(0, 12):
#     test_class.CREATE_manga_log(
#         manga_id = f"{i}",
#         manga_title = f"mti {i+1}",
#         manga_site = f"msi {i+2}",
#         chapter_title = f"cti {i+3}",
#         chapter_link_latest = f"cli {i+4}"
#     )

# print("\n\n\n\n\n\n\n\n\n\n=========================")
# rows = test_class.GET_manga_log_all()
# for row in rows:
#     print(row)

print("\n\n\n\n\n\n\n\n\n\n=========================")
# breakpoint()
print(test_class.UPDATE_manga_log(manga_id="2", chapter_link_latest="kill yoursef"))
rows = test_class.GET_manga_log_all()
for row in rows:
    print(row)

print()